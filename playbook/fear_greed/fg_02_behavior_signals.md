---
id: FG-SIGNALS
used_by: [Inside-out Monitor, Critic]
steps: [4]
depends_on: [inside_out/signals.md, fear_greed/fg_01_dual_lens.md]
load_when: Bước 4 – đọc tín hiệu nội bộ theo hai chiều và nhận diện hành vi sợ hãi/tham lam của khách hàng
version: v2.0
updated: 2026-11-02
---

# Tín hiệu Fear & Greed

## 1. Đọc tín hiệu S01–S16 theo hai chiều
Cùng một tín hiệu có thể là sợ hãi hoặc tham lam. **Quy tắc then chốt: xem tiền đi đâu.** Tiền rút ra để trả nợ, chi tiêu thiết yếu hoặc cất giữ là Fear. Tiền rút ra để mua tài sản đang tăng nóng là Greed.

| ID | Tín hiệu gốc | Đọc chiều Fear | Đọc chiều Greed / cơ hội |
|---|---|---|---|
| `S01` | Lô chi lương | Trễ, giảm người, giảm quỹ lương | Tăng người, tăng quỹ lương, trả đúng hạn → `O2` tài khoản lương, thẻ |
| `S02` | Doanh thu QR/Soundbox/POS | Giảm theo địa bàn, MCC | Tăng đều nhiều tháng → `O1` `O3` cho HKD |
| `S03` | Unique payers | Giảm, mất khách | Tăng, có khách mới thật |
| `S04` | Dùng hạn mức tăng nhanh | Kèm thu nhập giảm → căng thẳng | Kèm chuyển tiền sang tài khoản chứng khoán, đặt cọc BĐS → vay để đầu cơ (xem `G01`) |
| `S05` | Hành vi trả nợ thẻ | Chuyển sang trả tối thiểu | Trả toàn bộ, trả trước hạn → `O5` |
| `S06` | Tất toán sớm, vay cầm cố tiền gửi | Cần tiền gấp | Rút ra để mua tài sản đang tăng nóng (xem `G02`) |
| `S07` | Rút tiền mặt tăng đột biến | Hoảng loạn, tin đồn | Mua vàng, đặt cọc đất bằng tiền mặt theo phong trào |
| `S08` | Giao dịch iBond/iFund | Bán lại theo một issuer, một ngành | Mua dồn một ngành vừa tăng mạnh (xem `G03`) |
| `S09` | Bảo hiểm | Hủy sớm, ngừng đóng phí | Mua tăng sau biến cố → `O4`, nhưng phải kiểm tra tư vấn phù hợp |
| `S10` | Hóa đơn điện, cảng, NSNN | Giảm, nộp trễ | Tăng → sản lượng, xuất khẩu tăng |
| `S11` | Chuỗi cung ứng (SCF) | Spoke đồng loạt chậm trả | Doanh số chuỗi tăng, spoke xin tăng hạn mức → `O1` |
| `S12` | Dòng tiền chủ DN ↔ DN | Chủ bơm tiền cứu DN | Chủ rút lợi nhuận về tài khoản cá nhân → `O2` `O4` |
| `S13` | Đăng nhập lạ, người thụ hưởng mới | Lừa đảo chiếm đoạt | Pha Greed thường kéo theo lừa đảo đầu tư (xem `G07`) – vẫn là Fear |
| `S14` | Khiếu nại theo chủ đề | Tăng ngay khi có sự cố | Ở pha Greed, khiếu nại tư vấn sai thường đến muộn vài tháng |
| `S15` | Vị thế FX/phái sinh của khách | Giá trị thị trường âm lớn | Vị thế tăng vượt nhu cầu phòng ngừa (xem `G06`) |
| `S16` | Doanh thu HKD về TK cá nhân | Né thuế, rủi ro AML | Chuyển ngược về TK HKD → minh bạch hóa, `O6` |

## 2. Hành vi sợ hãi bổ sung (F)
Các hành vi chưa có trong S01–S16. Dùng cùng với `S06` `S07` `S08` `S09` `S14`.

| ID | Hành vi | Nguồn dữ liệu | Báo trước điều gì |
|---|---|---|---|
| `F01` | Chuyển tiền gửi hàng loạt sang ngân hàng khác trong thời gian ngắn | Chuyển khoản đi theo địa bàn, phân khúc | Mất niềm tin; rủi ro thanh khoản `LQ` |
| `F02` | Đồng loạt chuyển từ tiền gửi kỳ hạn dài sang không kỳ hạn hoặc kỳ hạn ngắn | Core banking | Khách muốn giữ tiền sẵn sàng rút |
| `F03` | Bán gấp tài sản bảo đảm dưới giá để trả nợ trước hạn | Hồ sơ giải chấp, định giá | Giá TSBĐ cùng khu vực có thể giảm theo `CL` |
| `F04` | Hạn mức còn nhưng khách ngừng giải ngân, hoãn đầu tư | Hạn mức tín dụng DN | DN co lại; doanh thu ngân hàng giảm `BR` |

## 3. Hành vi tham lam (G)
Đây là các tín hiệu cho thấy cơ hội đang chuyển sang ô B của ma trận (`fear_greed/fg_01_dual_lens.md`).

| ID | Hành vi | Nguồn dữ liệu | Rủi ro tích tụ |
|---|---|---|---|
| `G01` | Tiền vay tiêu dùng hoặc thấu chi chuyển ngay sang tài khoản chứng khoán, sàn vàng, hoặc đặt cọc BĐS | Dòng tiền sau giải ngân | Sai mục đích vay; `CR` khi giá tài sản quay đầu |
| `G02` | Tất toán tiết kiệm hoặc vay cầm cố tiền gửi để mua sản phẩm đang tăng nóng | Core banking + dòng tiền ra | Giảm huy động `LQ`; khách chịu lỗ khi đảo chiều |
| `G03` | Mua dồn iBond/iFund của một ngành hoặc một tổ chức phát hành vừa tăng mạnh; tỷ trọng một sản phẩm trong tài sản khách tăng vọt | Hệ thống đầu tư | Rủi ro tập trung; khiếu nại `RP` khi giá giảm |
| `G04` | Nhiều hồ sơ vay mua BĐS thứ hai, thứ ba ở cùng một khu vực đang sốt; giá định giá TSBĐ tăng nhanh hơn giá giao dịch thực | Hồ sơ vay, định giá | `CL` `CR` khi giá đất quay về |
| `G05` | DN, HKD xin tăng hạn mức theo doanh thu ở giá đỉnh, gấp nhiều lần doanh thu bình quân | Hồ sơ tín dụng | Hạn mức vượt khả năng trả khi giá giảm |
| `G06` | Vị thế FX, phái sinh của khách vượt nhu cầu phòng ngừa thực (không gắn với hợp đồng thương mại) | Treasury | Đầu cơ thay vì phòng ngừa; rủi ro đối tác `CR` |
| `G07` | Giao dịch tới các sàn, ứng dụng đầu tư không được cấp phép tăng | Giao dịch chuyển khoản | Lừa đảo đầu tư `FR`, tuân thủ `CO` |

## 4. Cách dùng khi viết kết luận
- Nêu tín hiệu ở **cả hai chiều** cho các nhánh quan trọng: tín hiệu nào sẽ xác nhận cơ hội, tín hiệu nào cho thấy cơ hội đã thành nóng (G), tín hiệu nào cho thấy sợ hãi lan rộng (F).
- Nếu sự kiện nằm ở ô B, bắt buộc liệt kê ít nhất hai tín hiệu G để theo dõi.
- Nếu sự kiện nằm ở ô C, bắt buộc liệt kê `S07` và `F01`.
