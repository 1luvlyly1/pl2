---
id: IND-01
code: I01
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về lãi suất cho vay, tín dụng BĐS, luật đất đai, bảng giá đất, pháp lý dự án, trái phiếu chủ đầu tư, FDI vào khu công nghiệp, hạ tầng, du lịch nghỉ dưỡng
version: v3.4
updated: 2026-11-04
---

# I01 – Bất động sản (nhà ở, khu công nghiệp, nghỉ dưỡng)

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Ngành gồm ba mảng có chu kỳ khác nhau, nên không được đánh đồng. **Nhà ở** (căn hộ, nhà phố, đất nền) nhạy nhất với lãi suất và pháp lý dự án. **Khu công nghiệp** đi theo dòng vốn FDI và dịch chuyển chuỗi cung ứng. **Nghỉ dưỡng** (căn hộ khách sạn, biệt thự biển) phụ thuộc lượng khách du lịch và tâm lý đầu tư. Một tin có thể tốt cho khu công nghiệp trong khi nhà ở vẫn trầm lắng.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Chủ đầu tư dự án, chủ khu công nghiệp | Huy động vốn qua vay dự án, trái phiếu và tiền đặt cọc của người mua; pháp lý chậm làm vốn bị chôn nhiều năm |
| SME | Sàn môi giới, nhà thầu phụ, thiết kế, quản lý tòa nhà | Phụ thuộc thanh toán của chủ đầu tư; dự án dừng thì dòng tiền đứt ngay |
| KHCN – hộ kinh doanh | Môi giới tự do, chủ nhà trọ, cửa hàng nội thất | Thu nhập theo số giao dịch hoặc số người thuê, không có đệm khi thị trường đóng băng |
| KHCN – cá nhân | Người mua để ở, nhà đầu tư cá nhân, người cho thuê, người mua trái phiếu chủ đầu tư | Khoản vay mua nhà là khoản nợ lớn nhất của hộ gia đình; nhà đầu tư dùng đòn bẩy chịu lỗ khi thanh khoản đóng băng |

Nhà ở tập trung ở hai đô thị lớn và vùng ven; khu công nghiệp ở các tỉnh phía Bắc và Đông Nam Bộ; nghỉ dưỡng ở các tỉnh ven biển miền Trung và các đảo.

**Đặc thù quan trọng với ngân hàng:** BĐS là tài sản bảo đảm phổ biến nhất của toàn hệ thống, nên giá BĐS biến động lan sang mọi phân khúc qua rủi ro tài sản bảo đảm (`CL`), kể cả khoản vay không dùng để mua nhà. Thị trường có tâm lý đầu cơ mạnh: dễ có pha tham (sốt đất theo tin quy hoạch) và pha sợ (đóng băng thanh khoản). Chu kỳ dài, độ trễ từ chính sách tới giao dịch thường nhiều tháng.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Lãi suất cho vay mua nhà | Cầu mua giảm; người đã vay thả nổi phải trả nhiều hơn mỗi tháng, nhất là khi hết thời gian ưu đãi | Người vay mua nhà, nhà đầu tư dùng đòn bẩy | Một đến vài kỳ trả nợ | – |
| Hạn mức tín dụng, siết tín dụng BĐS | Chủ đầu tư thiếu vốn hoàn thiện dự án; người mua khó vay, giao dịch chậm. Nới tín dụng thì ngược lại và dễ kéo pha tham | Chủ đầu tư, người mua | Nhanh, vài tuần | `I02` |
| Luật đất đai, bảng giá đất, thủ tục pháp lý | Pháp lý tắc làm dự án không mở bán được; bảng giá đất tăng làm tiền sử dụng đất và giá vốn tăng. Tháo gỡ pháp lý là điểm đảo chiều phổ biến | Chủ đầu tư | Nhiều tháng | – |
| Đáo hạn trái phiếu chủ đầu tư | Chủ đầu tư phải trả nợ, giãn nợ hoặc bán tài sản; người mua trái phiếu bị chậm trả, có thể bán tháo | Chủ đầu tư, nhà đầu tư cá nhân (`L05`) | Theo lịch đáo hạn | – |
| FDI, dịch chuyển chuỗi cung ứng | FDI chậm lại (ví dụ do thuế quan với hàng xuất khẩu) làm cầu thuê đất khu công nghiệp, nhà xưởng, nhà ở công nhân giảm | Chủ khu công nghiệp, chủ nhà trọ | Trung hạn | `I04` |
| Đầu tư công vào hạ tầng | Hạ tầng mới kéo giá đất ven tuyến tăng, thường đi trước tiến độ thật; tin đồn quy hoạch tạo sốt đất | Nhà đầu tư cá nhân | Kỳ vọng đi trước | `I02` |
| Khách du lịch | Khách giảm làm công suất căn hộ nghỉ dưỡng giảm, người mua theo cam kết lợi nhuận bị ảnh hưởng | Chủ đầu tư nghỉ dưỡng, người mua căn hộ khách sạn | Theo mùa | `I10` |
| Giá vật liệu xây dựng | Chi phí xây dựng tăng, dự án chậm tiến độ, nhà thầu ký giá cố định thua lỗ | Nhà thầu, chủ đầu tư | Vài tháng | `I02` |
| Thiên tai, ngập lụt | Giá trị tài sản bảo đảm ở vùng rủi ro giảm, có thể kéo dài | Người có nhà ở vùng ngập | Ngay đến dài hạn | Tin khí hậu là `GT` |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Người vay mua nhà chịu áp lực trả nợ khi lãi suất tăng hoặc hết ưu đãi; khoản trả tăng làm họ cắt chi tiêu khác (lan sang `I09`). Người mua nhà dự án chịu rủi ro chậm bàn giao, chậm cấp giấy chứng nhận, và có thể ngừng trả nợ khi tranh chấp với chủ đầu tư (`L04`). Nhà đầu tư dùng đòn bẩy lỗ khi thanh khoản đóng băng và phải bán gấp. Người mua trái phiếu chủ đầu tư có thể bị chậm trả lãi, gốc.

**Cơ hội.** Khi lãi suất giảm và pháp lý thông thoáng, nhu cầu vay mua nhà để ở tăng. Người có tiền nhàn rỗi mua được giá tốt ở pha sợ. Nhu cầu vay sửa chữa, xây nhà tăng khi người dân chọn cải tạo thay vì mua mới.

### KHCN – hộ kinh doanh
**Thách thức.** Môi giới tự do mất thu nhập gần như ngay khi giao dịch chậm lại. Chủ nhà trọ quanh khu công nghiệp mất người thuê khi công nhân bị cắt giảm (kênh ngược từ `I03`, `I04`).

**Cơ hội.** Pha giao dịch sôi động kéo doanh thu môi giới, nội thất, sửa chữa. Khu công nghiệp mở rộng kéo nhu cầu nhà trọ, ăn uống quanh khu.

### SME
**Thách thức.** Sàn môi giới, nhà thầu phụ bị chủ đầu tư chậm thanh toán; khi dự án dừng, dòng tiền của họ đứt trong khi vẫn phải trả lương, trả nợ.

**Cơ hội.** Dự án tái khởi động cần nhà thầu, bảo lãnh thực hiện hợp đồng và vốn lưu động.

### DN lớn
**Thách thức.** Chủ đầu tư phụ thuộc vốn vay và trái phiếu dễ gặp áp lực thanh khoản khi bán hàng chậm hoặc trái phiếu đến hạn. Pháp lý chậm làm vốn bị chôn. Giá đất tăng làm chi phí tiền sử dụng đất tăng, thu hẹp biên lợi nhuận.

**Cơ hội.** Tháo gỡ pháp lý giúp mở bán; chủ khu công nghiệp hưởng lợi từ FDI; chính sách nhà ở xã hội, nhà ở công nhân mở ra phân khúc mới.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay mua nhà `CN-LN-01` `CN-LN-02` `CN-LN-03` (khoản trả tăng, tài sản bảo đảm giảm giá); vay xây sửa `CN-LN-08`; trái phiếu chủ đầu tư qua iBond `CN-INV-01` (chậm trả, khiếu nại) | Vay mua nhà để ở (`O1`) khi lãi suất giảm và dự án đủ pháp lý; bảo hiểm nhà `CN-INS-03` (`O4`) theo nhu cầu thật |
| HKD | Vay thế chấp kinh doanh `HKD-LN-02` dùng BĐS làm tài sản bảo đảm (giá trị tài sản giảm) | Tài khoản, thanh toán cho môi giới, nội thất (`O3`) khi giao dịch tăng |
| SME | Vốn lưu động `SME-LN-01`, bảo lãnh `SME-GTE-01` (chủ đầu tư chậm thanh toán); tài khoản giữ hộ BĐS `SME-ACC-04` | Bảo lãnh, vốn lưu động khi dự án khởi động lại (`O1` `O3`) |
| DN lớn | Vay dự án `CIB-LN-02`, trái phiếu `CIB-INV-01`, tài khoản giữ hộ `CIB-ACC-04`, bảo lãnh `CIB-TF-04` (thanh khoản chủ đầu tư) | Thu xếp vốn dự án đủ pháp lý, tài khoản giữ hộ, chi lương (`O1` `O3`) |
| Cấp ngân hàng | Rủi ro tài sản bảo đảm toàn danh mục, tập trung tín dụng BĐS, danh tiếng với sản phẩm trái phiếu | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `G04` hồ sơ vay mua BĐS thứ hai, thứ ba cùng khu vực | Đầu cơ đang tăng, pha tham | Có: đếm khoản vay có bảo đảm theo khách |
| `G01` tiền vay tiêu dùng chuyển sang đặt cọc BĐS | Đòn bẩy ẩn | Chưa có |
| `F03` bán gấp tài sản bảo đảm để trả nợ | Pha sợ, giá sắp giảm thêm | Gần đúng: tài sản biến mất giữa hai kỳ cùng dư nợ giảm |
| `S06` tất toán tiết kiệm trước hạn | Người vay cần tiền gấp để trả nợ | Có |
| `S08` bán lại trái phiếu của tổ chức phát hành BĐS | Mất niềm tin vào chủ đầu tư | Gần đúng: không có chiều tổ chức phát hành |
| `S12` chủ DN rút tiền cá nhân bơm cho DN | Chủ đầu tư đang thiếu vốn | Chưa có quan hệ chủ–DN |
| `S11` nhà thầu cùng một chủ đầu tư chậm trả đồng loạt | Chủ đầu tư có vấn đề | Chưa có |
| LTV khoản vay mua nhà theo khu vực | Đệm tài sản bảo đảm mỏng | Có: dư nợ và giá trị tài sản bảo đảm (cần xác nhận cột giá trị) |

Luôn ghi "cần truy vấn dư nợ BĐS theo khu vực và tỷ lệ tài sản bảo đảm là BĐS theo phân khúc".

## 6. Liên kết ngành
- **Thượng nguồn – `I02` xây dựng và vật liệu:** dự án dừng làm nhà thầu và cửa hàng vật liệu mất doanh thu; giá vật liệu tăng làm dự án chậm.
- **Hạ nguồn – `I05` nội thất nội địa, `I09` bán lẻ đồ gia dụng:** nhà bàn giao nhiều kéo nhu cầu nội thất, gia dụng sau vài tháng.
- **Song song – `I10` (nghỉ dưỡng theo khách du lịch), `I04` (khu công nghiệp theo FDI).**
- **Toàn hệ thống:** giá BĐS chạm mọi khoản vay có tài sản bảo đảm là BĐS, ở cả bốn phân khúc.

## 7. Điểm đảo chiều và lưu ý
- Pha tham (sốt đất theo tin quy hoạch, hạ tầng) đảo nhanh khi tín dụng bị siết hoặc tin đồn không thành sự thật.
- Pha sợ kéo dài khi pháp lý tắc; tháo gỡ pháp lý là điểm đảo chiều phổ biến nhất.
- Ba mảng có chu kỳ khác nhau: khu công nghiệp có thể tốt khi nhà ở trầm lắng.
- Với dự án cụ thể, không suy đoán tình trạng pháp lý hay khả năng trả nợ của chủ đầu tư khi tin không nêu.
