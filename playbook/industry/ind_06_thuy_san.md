---
id: IND-06
code: I06
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về giá tôm, cá tra, hải sản, thuế chống bán phá giá, thẻ vàng IUU, hạn mặn, dịch bệnh tôm, giá thức ăn thủy sản, giá dầu (tàu cá), nhu cầu Trung Quốc, Mỹ, EU
version: v3.4
updated: 2026-11-04
---

# I06 – Thủy sản

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Ngành có ba mảng: **nuôi trồng** (tôm, cá tra) tập trung ở đồng bằng sông Cửu Long; **đánh bắt** hải sản xa bờ ở các tỉnh ven biển miền Trung và Nam Bộ; **chế biến xuất khẩu** sang Mỹ, EU, Trung Quốc, Nhật Bản, Hàn Quốc. Đầu vào là thức ăn (phụ thuộc bột cá, đậu tương nhập khẩu), con giống, thuốc; dầu diesel là chi phí lớn nhất của tàu đánh bắt.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | DN vừa nuôi vừa chế biến xuất khẩu | Thuế chống bán phá giá, tồn kho, rủi ro kiểm dịch và trả hàng |
| SME | Cơ sở chế biến, đại lý thức ăn, thu mua | Bị loại khỏi chuỗi khi yêu cầu truy xuất tăng; thiếu vốn thu mua khi giá tăng |
| KHCN – hộ kinh doanh | Thương lái, nậu vựa, đại lý thuốc thú y thủy sản, chủ tàu nhỏ | Bán chịu cho nông hộ; kẹt hàng khi biên mậu đóng |
| KHCN – cá nhân | Nông hộ nuôi, ngư dân, công nhân chế biến | Mất vụ do dịch bệnh, hạn mặn; tàu nằm bờ khi dầu cao; thu nhập không qua chi lương |

**Đặc thù quan trọng với ngân hàng:** nông hộ thường mua thức ăn trả chậm qua đại lý – một dạng tín dụng không chính thức mà ngân hàng không thấy, nhưng khi mất vụ nợ này dồn lại và đẩy cả đại lý vào khó khăn. Rủi ro dịch bệnh và thời tiết lớn; mùa vụ theo vụ nuôi và mùa biển, hạn mặn vào mùa khô. Thẻ vàng IUU của EU với hải sản đánh bắt làm tăng chi phí truy xuất.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Giá tôm, cá tra xuất khẩu | Giá giảm dưới giá thành thì nông hộ treo ao, đại lý không thu được nợ thức ăn | Nông hộ, đại lý | Một vụ nuôi | – |
| Thuế chống bán phá giá, chống trợ cấp của Mỹ | Mất đơn sang Mỹ, DN ép giá thu mua; mức thuế khác nhau giữa các DN | DN chế biến, rồi nông hộ | Theo quyết định | – |
| Thẻ vàng IUU | Chi phí kiểm tra tăng, mất đơn EU; ngư dân và cảng cá bị siết thủ tục | Ngư dân, DN chế biến hải sản | Dài | – |
| Giá dầu | Tàu cá nằm bờ vì chi phí chuyến biển vượt giá trị đánh bắt | Ngư dân, chủ tàu | Ngay | `I12` |
| Giá thức ăn (đậu tương, bột cá), USD | Chi phí nuôi tăng | Nông hộ | Vài tuần | `I08` |
| Hạn mặn, nắng nóng, bão | Thiệt hại ao nuôi, tàu cá | Nông hộ, ngư dân vùng bị ảnh hưởng | Theo mùa | Tin thời tiết là `TT` nếu có vùng cụ thể |
| Dịch bệnh tôm | Mất vụ, nợ đại lý thức ăn dồn lại | Nông hộ nuôi tôm | Ngay | – |
| Nhu cầu Trung Quốc, biên mậu | Biên mậu đóng thì hàng ùn ở cửa khẩu; nhu cầu mạnh thì giá tăng | Thương lái | Nhanh | `I11` |
| Tỷ giá | USD mạnh làm doanh thu quy đổi tăng; lợi ròng vì đầu vào chủ yếu trong nước | DN xuất khẩu | Ngay | – |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Nông hộ nuôi mất vụ do dịch bệnh, hạn mặn, hoặc bán dưới giá thành. Ngư dân nằm bờ khi giá dầu cao. Nợ không chính thức với đại lý thức ăn bị dồn lại sau một vụ thất bại. Công nhân nhà máy chế biến giảm ca khi DN mất đơn.

**Cơ hội.** Giá tăng làm thu nhập nông hộ tăng sau vụ, tạo tiền gửi mới; nâng cấp ao nuôi công nghệ cao cần vay sản xuất.

### KHCN – hộ kinh doanh
**Thách thức.** Đại lý thức ăn, thuốc bán chịu cho nông hộ dễ bị nợ đọng khi mất vụ. Thương lái bị kẹt hàng khi biên mậu đóng.

**Cơ hội.** Mùa giá tốt làm doanh thu đại lý tăng, cần vốn nhập hàng.

### SME
**Thách thức.** Cơ sở chế biến nhỏ bị loại khỏi chuỗi khi yêu cầu truy xuất tăng; thiếu vốn thu mua khi giá tăng.

**Cơ hội.** Đơn từ thị trường mới; chế biến sâu để tăng giá trị.

### DN lớn
**Thách thức.** Thuế chống bán phá giá; tồn kho khi nhu cầu giảm; rủi ro kiểm dịch, trả hàng.

**Cơ hội.** Giá xuất khẩu tăng, USD mạnh; mở rộng vùng nuôi đạt chuẩn quốc tế (vay trung dài hạn); tài trợ chuỗi cho nông hộ liên kết.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay tiêu dùng `CN-LN-06`, vay cầm cố `CN-LN-07` của nông hộ, ngư dân (mất vụ, nằm bờ) | Tiền gửi sau vụ `CN-DEP-01` (`O2`); bảo hiểm (`O4`) theo nhu cầu thật |
| HKD | ShopCash `HKD-LN-01`, ShopCredit `HKD-LN-02` của đại lý thức ăn, thương lái (nợ đọng từ nông hộ) | Vốn nhập hàng mùa vụ (`O1`); QR, nộp tiền mặt qua CDM `HKD-SVC-01` (`O3`) |
| SME | Vay `SME-LN-01` của cơ sở chế biến | Vốn thu mua (`O1`), ngoại tệ `SME-PAY-04` (`O3`) |
| DN lớn | Vốn lưu động `CIB-LN-01`, tài trợ xuất khẩu `CIB-TF-02`; hàng tồn làm tài sản bảo đảm (`CL`) | Tài trợ xuất khẩu, phòng ngừa tỷ giá `CIB-CM-02`, tài trợ chuỗi `CIB-TF-03` (`O1` `O3`) |
| Cấp ngân hàng | Tập trung theo vùng đồng bằng sông Cửu Long | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S02` doanh thu QR của đại lý thức ăn, thương lái theo tỉnh | Mất vụ hoặc giá thấp ở vùng | Chưa có |
| `S04` hạn mức của đại lý tăng nhanh mùa mất vụ | Đại lý đang gánh nợ của nông hộ | Có với thẻ, thấu chi cá nhân của chủ hộ |
| `S06` tất toán tiết kiệm của nông hộ | Cần tiền gấp sau vụ thất bại | Có, lọc theo tỉnh |
| `S10` hóa đơn điện nhà máy chế biến; `S01` chi lương giảm | DN chế biến giảm sản lượng | `S01` có; `S10` chưa có |
| `G05` xin tăng hạn mức thu mua ở giá đỉnh | Đầu cơ hàng tồn | Gần đúng |

Ngư dân và nông hộ thường không nhận lương qua ngân hàng; dùng tín hiệu tiền gửi, thẻ, thấu chi theo tỉnh thay thế. Luôn ghi "cần truy vấn dư nợ thủy sản theo tỉnh và theo mảng nuôi, đánh bắt, chế biến".

## 6. Liên kết ngành
- **Thượng nguồn – `I08` (thức ăn), `I13` (hóa chất, thuốc), `I12` (dầu diesel):** chi phí nuôi và chi phí chuyến biển.
- **Song song – `I11` (container lạnh), `I07` (cùng vùng đồng bằng sông Cửu Long, cùng chịu hạn mặn).**
- **Hạ nguồn – `I09` bán lẻ thực phẩm.**

## 7. Điểm đảo chiều và lưu ý
- Giá đỉnh kéo nông hộ thả nuôi ồ ạt, vụ sau dư cung và giá giảm – pha tham đảo chiều.
- Không suy ra mức thuế của DN cụ thể khi tin không nêu.
- Ngư dân và nông hộ không có chi lương; đừng dùng `S01` cho nhóm này.
