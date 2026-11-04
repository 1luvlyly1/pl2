---
id: IND-02
code: I02
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về đầu tư công, giá thép, quặng, than, xi măng, giá điện, chống bán phá giá thép, quy định carbon của EU, hàng Trung Quốc giá rẻ, thị trường BĐS, bão lũ
version: v3.4
updated: 2026-11-04
---

# I02 – Xây dựng và vật liệu xây dựng

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Ngành gồm hai nhóm gắn chặt với nhau. **Xây dựng** gồm tổng thầu hạ tầng, nhà thầu dân dụng và nhà thầu phụ. **Vật liệu** gồm thép, xi măng, kính, gạch ốp lát, đá, cát, sơn, ống nhựa. Đầu ra chủ yếu là thị trường trong nước – đầu tư công, BĐS và người dân tự xây – một phần thép, xi măng, clinker được xuất khẩu. Ngành thép phụ thuộc quặng sắt, than cốc, phế liệu nhập khẩu; xi măng dùng nhiều than và điện.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Nhà sản xuất thép, xi măng; tổng thầu hạ tầng | Cạnh tranh với hàng nhập giá rẻ; chi phí năng lượng lớn; tổng thầu ứng vốn lớn và thu tiền chậm |
| SME | Nhà thầu phụ, đại lý vật liệu cấp 1 | Bị tổng thầu, chủ đầu tư chậm trả; hợp đồng giá cố định bị ép khi giá vật liệu tăng; thiếu tài sản bảo đảm để xin bảo lãnh |
| KHCN – hộ kinh doanh | Cửa hàng vật liệu, đội thợ xây, xe chở vật liệu | Bán chịu cho thợ và nhà thầu nhỏ nên dễ bị nợ đọng; hàng tồn mất giá khi giá thép giảm |
| KHCN – cá nhân | Người tự xây nhà, lao động xây dựng | Nhiều lao động thời vụ, thu nhập không qua chi lương nên khó thẩm định và khó theo dõi |

**Đặc thù quan trọng với ngân hàng:** nhà thầu thường phải ứng vốn và bị thanh toán chậm, nên nhu cầu vốn lưu động và bảo lãnh lớn. Cùng một biến động giá vật liệu, nhà sản xuất có hàng tồn được lợi còn nhà thầu ký giá cố định chịu thiệt – luôn tách vai trò. Mùa khô là cao điểm thi công; cuối năm là cao điểm giải ngân đầu tư công.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Giải ngân đầu tư công | Giải ngân chậm làm tổng thầu, nhà sản xuất thép, xi măng, đá thiếu đơn; giải ngân nhanh thì ngược lại, nhưng tiền từ ngân sách có thể tới chậm (`L12`) | Tổng thầu, nhà thầu phụ | Vài tháng | `I01` |
| Thị trường BĐS | Thị trường trầm lắng làm nhà thầu dân dụng thiếu việc và bị chủ đầu tư nợ đọng | Nhà thầu dân dụng, cửa hàng vật liệu | Nhanh | `I01` |
| Giá quặng, than, phế liệu | Giá tăng làm nhà thầu ký giá cố định thiệt; nhà sản xuất có hàng tồn lợi ngắn hạn | Nhà thầu | Vài tuần | `I11` |
| Giá điện, giá khí | Chi phí sản xuất thép lò điện, xi măng tăng ngay | Nhà sản xuất | Ngay | `I12` |
| Việt Nam chống bán phá giá thép nhập | Bảo vệ nhà sản xuất trong nước; người dùng thép (nhà thầu) chịu giá cao hơn | Nhà thầu | Theo quyết định | – |
| Nước ngoài phòng vệ thương mại với thép Việt Nam | DN xuất khẩu thép mất thị trường, phải bán vào trong nước | DN thép xuất khẩu | Theo quyết định | – |
| Quy định carbon biên giới của EU | Thép, xi măng, nhôm xuất sang EU chịu thêm chi phí phát thải | DN xuất khẩu sang EU | Theo lộ trình | Tin `GT` hoặc `TT` tùy giai đoạn |
| Lãi suất | Chi phí vốn của nhà thầu phải ứng vốn tăng | Nhà thầu | Vài tháng | – |
| Bão lũ | Công trình gián đoạn ngay; sau đó nhu cầu sửa chữa tăng | Nhà thầu vùng bão; sau đó cửa hàng vật liệu lợi | Ngay rồi đảo chiều | `I07` |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Lao động xây dựng mất việc khi công trình dừng; vì thu nhập không ổn định và không qua chi lương, ngân hàng khó thấy dấu hiệu sớm. Người tự xây nhà chịu chi phí tăng khi giá vật liệu tăng, có thể phải vay thêm hoặc dừng giữa chừng.

**Cơ hội.** Đầu tư công mạnh tạo việc làm. Giá vật liệu giảm làm nhu cầu vay xây, sửa nhà tăng.

### KHCN – hộ kinh doanh
**Thách thức.** Cửa hàng vật liệu bán chịu cho thợ và nhà thầu nhỏ, nên khi nhà thầu bị nợ đọng, cửa hàng cũng bị nợ đọng theo. Hàng tồn mất giá khi giá thép giảm.

**Cơ hội.** Mùa xây dựng và pha sửa chữa sau bão làm doanh thu tăng nhanh và cần vốn nhập hàng.

### SME
**Thách thức.** Nhà thầu phụ bị tổng thầu hoặc chủ đầu tư chậm trả, trong khi vẫn phải trả lương và mua vật liệu. Hợp đồng giá cố định bị ép biên khi giá vật liệu tăng. Cần bảo lãnh để dự thầu nhưng thiếu tài sản bảo đảm.

**Cơ hội.** Gói thầu đầu tư công, sửa chữa hạ tầng sau thiên tai; nhu cầu bảo lãnh dự thầu và thực hiện hợp đồng.

### DN lớn
**Thách thức.** Nhà sản xuất thép, xi măng chịu cạnh tranh từ hàng nhập giá rẻ và chi phí năng lượng. Tổng thầu ứng vốn lớn nhưng thu tiền chậm.

**Cơ hội.** Đầu tư công và FDI xây nhà xưởng; phòng vệ thương mại bảo vệ thị trường trong nước; đầu tư công nghệ giảm phát thải mở ra nhu cầu vay xanh.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay xây sửa nhà `CN-LN-08` (chi phí vượt dự toán); vay tiêu dùng `CN-LN-06` của lao động thời vụ (thu nhập không ổn định) | Vay xây sửa nhà (`O1`) khi giá vật liệu giảm |
| HKD | ShopCash `HKD-LN-01`, ShopCredit `HKD-LN-02` của cửa hàng vật liệu (nợ đọng từ khách mua chịu) | Vốn nhập hàng mùa cao điểm (`O1`); nhận tiền QR, SoftPOS `HKD-REV-03` (`O3`) |
| SME | Vay `SME-LN-01` (chậm thanh toán từ tổng thầu); bảo lãnh mua sắm công `SME-GTE-01` (rủi ro thực hiện hợp đồng) | Bảo lãnh dự thầu, thực hiện hợp đồng (`O3`); vốn lưu động (`O1`) cho nhà thầu có hợp đồng rõ |
| DN lớn | Vốn lưu động `CIB-LN-01`; L/C nhập quặng, than `CIB-TF-01`; bảo lãnh `CIB-TF-04`; nộp ngân sách `CIB-PAY-03` | Vay trung dài hạn đổi công nghệ `CIB-LN-02`, tiền gửi xanh `CIB-DEP-01`, phòng ngừa tỷ giá `CIB-CM-02` (`O1` `O3`) |
| Cấp ngân hàng | Tập trung tín dụng chuỗi BĐS – xây dựng | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S10` hóa đơn điện, nộp ngân sách của nhà máy thép, xi măng giảm | Sản lượng giảm | Chưa có; thay thế bằng số ngày có giao dịch và dòng vào của DN |
| `S11` nhà thầu phụ cùng một tổng thầu chậm trả | Tổng thầu có vấn đề | Chưa có |
| `S04` cửa hàng vật liệu dùng hạn mức tăng nhanh | Bị nợ đọng, thiếu vốn | Có với thẻ, thấu chi cá nhân của chủ hộ |
| `S02` doanh thu QR cửa hàng vật liệu theo địa bàn | Nhu cầu xây dựng địa phương | Chưa có |
| `G05` xin tăng hạn mức theo giá thép đỉnh | Đầu cơ hàng tồn | Gần đúng: hạn mức so với dòng vào 12 tháng của DN |
| Thấu chi DN xây dựng gần chạm hạn mức | Ứng vốn kéo dài | Có: tỷ lệ dùng thấu chi DN |

Luôn ghi "cần truy vấn dư nợ ngành xây dựng và vật liệu, giá trị bảo lãnh đang phát hành".

## 6. Liên kết ngành
- **Thượng nguồn – `I12` năng lượng; quặng và than nhập khẩu qua `I11` vận tải biển:** giá năng lượng và cước truyền thẳng vào giá thép, xi măng.
- **Hạ nguồn – `I01` BĐS, hạ tầng đầu tư công:** quyết định khối lượng việc của cả ngành.
- **Song song – `I13` (ống nhựa, sơn), `I05` (nội thất hoàn thiện):** cùng chịu chu kỳ xây dựng.

## 7. Điểm đảo chiều và lưu ý
- Giá thép tăng là cơ hội cho nhà sản xuất có hàng tồn nhưng là rủi ro cho nhà thầu giá cố định; luôn nói rõ vai trò.
- Đầu tư công giải ngân mạnh không có nghĩa nhà thầu có tiền ngay; xét độ trễ thanh toán từ ngân sách.
- Sau thiên tai, pha thiệt (gián đoạn) chuyển sang pha lợi (sửa chữa) trong vài tuần đến vài tháng; viết hai pha tách nhau.
