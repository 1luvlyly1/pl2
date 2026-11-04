# Đặc tả chỉ số Fear & Greed khách hàng

Phiên bản v3.0 · 02/11/2026 · Dành cho đội dữ liệu và kỹ thuật. **Không đưa file này vào playbook của agent.**

## 1. Ba chỉ số

| Chỉ số | Đo gì | Nguồn | Dùng để |
|---|---|---|---|
| **Hành vi** | Tâm lý thực tế của khách hàng qua cách dùng tiền | Dữ liệu giao dịch nội bộ, 7 thành phần | Hiển thị; **được** truyền vào agent làm bối cảnh |
| **Dòng tiền thực** | Tác động cơ bản: dòng tiền thật tăng hay giảm | Dữ liệu giao dịch nội bộ, 4 thành phần | Trục dọc của ma trận; hiển thị |
| **Tin tức** | Áp lực từ sự kiện bên ngoài | Dòng nhãn `[FG]` trong output của agent | Chỉ hiển thị; **không** truyền vào agent |

Tất cả tính theo ngày, cho toàn ngân hàng và từng phân khúc: `KHCN` (gồm cá nhân và hộ kinh doanh), `SME`, `CIB` (doanh nghiệp lớn). Trong KHCN có thể tách thêm hai nhóm con cá nhân và hộ kinh doanh để theo dõi, nhưng nhãn `[FG]` chỉ ghi `KHCN`.

## 2. Chỉ số hành vi – 7 thành phần
Mã tín hiệu theo `playbook/fear_greed/fg_02_behavior_signals.md`. Chiều đã chuẩn hóa: **cao hơn = tham lam hơn**.

| # | Thành phần | Mã | Đo bằng (gợi ý) | Chiều |
|---|---|---|---|---|
| 1 | Đòn bẩy để đầu tư | `G01` | Tỷ lệ tiền giải ngân vay tiêu dùng, thấu chi chuyển sang tài khoản công ty chứng khoán hoặc thanh toán đặt cọc BĐS trong 7 ngày | Thuận |
| 2 | Mua ròng iFund, iBond | `G03` `S08` | Giá trị mua mới trừ bán lại, so với trung bình 125 ngày | Thuận |
| 3 | Rút tiền mặt | `S07` | Rút qua CDM và tại quầy so với trung bình 50 ngày | **Đảo** |
| 4 | Tiền gửi chuyển đi | `F01` | Tiền gửi chuyển sang ngân hàng khác so với trung bình 50 ngày | **Đảo** |
| 5 | Kỳ hạn tiền gửi | `F02` | Tỷ trọng tiền gửi mới kỳ hạn từ 6 tháng trên tổng tiền gửi mới | Thuận |
| 6 | Định giá tài sản bảo đảm | `G04` | Tốc độ tăng giá định giá so với giá giao dịch thực cùng khu vực | Thuận |
| 7 | Nhu cầu hạn mức doanh nghiệp | `G05` `F04` | Giá trị hồ sơ xin tăng hạn mức trừ hạn mức bỏ trống không giải ngân | Thuận |

Thành phần không áp dụng cho một phân khúc (ví dụ `G05` với KHCN) thì bỏ qua và chia trung bình cho số thành phần còn lại.

## 3. Chỉ số dòng tiền thực – 4 thành phần
| # | Thành phần | Mã | Đo bằng (gợi ý) |
|---|---|---|---|
| 1 | Thu nhập qua lương | `S01` | Tổng giá trị và số người trong các lô chi lương, so cùng kỳ năm trước |
| 2 | Doanh thu bán lẻ | `S02` | Doanh thu QR/Soundbox/POS của hộ kinh doanh (KHCN) và SME, so cùng kỳ |
| 3 | Hoạt động sản xuất | `S10` | Thanh toán hóa đơn điện, cảng, nộp ngân sách của DN, so cùng kỳ |
| 4 | Chuỗi cung ứng | `S11` | Doanh số và tỷ lệ trả đúng hạn trong các chương trình tài trợ chuỗi |

## 4. Quy về thang 0–100
1. Tính giá trị thô của từng thành phần theo ngày, theo phân khúc.
2. Khử mùa vụ: chia cho giá trị cùng kỳ năm trước (hoặc trừ đi), để Tết và mùa thu hoạch không bị đọc nhầm thành tâm lý.
3. Quy về **phân vị** so với lịch sử 12 tháng gần nhất của chính thành phần đó: điểm = phân vị × 100. Thành phần chiều đảo: điểm = 100 − phân vị × 100.
4. Chỉ số = trung bình cộng các thành phần (trọng số bằng nhau, như CNN). Làm tròn số nguyên.
5. **Chưa đủ 12 tháng lịch sử:** không hiển thị chỉ số, ghi "chưa đủ lịch sử". Không dùng giá trị ước lượng.

## 5. Chỉ số tin tức
Đầu vào: các dòng `[FG]` đã đọc theo `fg_tag_format.md`.

1. Điểm ô: `B` = +2, `A` = +1, `D` = −1, `C` = −2. Dòng có hai ô (`A,B`) lấy trung bình hai ô.
2. Trọng số mức chắc chắn: `co_kha_nang_cao` = 1,0 · `co_the` = 0,6 · `gia_thuyet` = 0,3.
3. Điểm dòng = điểm ô × trọng số. Một dòng có nhiều phân khúc thì tính cho từng phân khúc. Dòng có `NH` chỉ tính vào chỉ số toàn hàng, không tính cho phân khúc nào.
4. Điểm phân khúc = trung bình có trọng số của các dòng trong **30 ngày** gần nhất (chia cho tổng trọng số).
5. Chỉ số = 50 + 25 × điểm, giới hạn trong 0–100.
6. Dưới 3 sự kiện trong 30 ngày cho một phân khúc: hiển thị "ít dữ liệu" bên cạnh chỉ số.
7. Hiển thị thêm số nhánh theo nhóm tin `TT` / `GT` / `GL` trong 30 ngày, để biết chỉ số đang bị kéo bởi loại tin nào. Nhánh `GT` có tầm thời gian dài; có thể giảm trọng số còn một nửa nếu thấy chỉ số bị kéo lệch bởi tin dài hạn.

## 6. Dải và cách đọc
| Điểm | Dải |
|---|---|
| 0–24 | Sợ hãi cực độ |
| 25–44 | Sợ hãi |
| 45–54 | Trung lập |
| 55–74 | Tham lam |
| 75–100 | Tham lam cực độ |

**Ô ma trận** (x = chỉ số hành vi, y = chỉ số dòng tiền thực):

| | x < 25 | 25 ≤ x < 75 | x ≥ 75 |
|---|---|---|---|
| **y ≥ 50** | Bi quan quá mức | Ô A – Cơ hội lành mạnh | Ô B – Cơ hội nóng |
| **y < 50** | Ô C – Rủi ro khuếch đại | Ô D – Rủi ro cơ bản | Lạc quan sai chỗ |

**Cảnh báo lệch** (tin tức − hành vi): dưới 8 điểm là đồng pha; 8–14 là lệch vừa; từ 15 trở lên là lệch lớn, thường là dấu hiệu đảo chiều sớm.

## 7. Truyền vào agent
- Chỉ truyền **chỉ số hành vi** của phân khúc liên quan, dạng một dòng: `Bối cảnh: chỉ số hành vi KHCN = 78 (Tham lam cực độ)`. Agent xử lý theo `playbook/fear_greed/fg_01_dual_lens.md` mục 7.
- **Không** truyền chỉ số tin tức, chỉ số dòng tiền thực, hay điểm số khác.
- Chưa đủ lịch sử thì không truyền gì.

## 8. Quyền riêng tư
- Chỉ tính và hiển thị số liệu tổng hợp. Không có chỉ số cho từng khách hàng.
- Mỗi ô (phân khúc × địa bàn) cần đủ số khách tối thiểu (gợi ý ≥ 50) mới hiển thị, để tránh nhận diện ngược.

## 9. Kiểm tra trước khi dùng thật
- Chạy lại trên dữ liệu quá khứ, xem chỉ số có phản ánh đúng các giai đoạn biến động đã biết không (ví dụ những đợt rút tiền theo tin đồn, đợt thị trường tăng nóng).
- Kiểm tra từng thành phần có tương quan quá cao với nhau không; hai thành phần gần trùng nhau thì giữ một.
- So sánh chỉ số tin tức với nhận định của chuyên viên trên một mẫu sự kiện để đánh giá chất lượng dòng nhãn.
- Đây là chỉ số nội bộ để đọc tâm lý khách hàng, **không phải dự báo thị trường**.
