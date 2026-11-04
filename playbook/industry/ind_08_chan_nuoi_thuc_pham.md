---
id: IND-08
code: I08
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về dịch tả lợn châu Phi, cúm gia cầm, giá lợn hơi, giá ngô, đậu tương, lúa mì, đường, sữa; tiêu dùng nội địa; thuế tiêu thụ đặc biệt đồ uống; an toàn thực phẩm; tỷ lệ sinh
version: v3.4
updated: 2026-11-04
---

# I08 – Chăn nuôi, thực phẩm, đồ uống, hàng tiêu dùng nhanh

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
**Chăn nuôi** đi theo chuỗi thức ăn chăn nuôi → con giống → trang trại → giết mổ, chế biến → chợ, siêu thị. Thức ăn chăn nuôi phụ thuộc lớn vào ngô, đậu tương, lúa mì nhập khẩu. Chăn nuôi nông hộ nhỏ lẻ đang giảm; trang trại quy mô lớn và mô hình liên kết tăng. **Thực phẩm, đồ uống, hàng tiêu dùng nhanh** do DN lớn sản xuất (sữa, bia, nước giải khát, mì gói, dầu ăn, bánh kẹo, gia vị) và phân phối qua nhà phân phối, đại lý, tạp hóa. Một số DN lớn có chương trình tài trợ nhà phân phối với ngân hàng (`L03`).

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Nhà sản xuất, phân phối; DN chăn nuôi khép kín | Chi phí nguyên liệu nhập và tỷ giá; thuế tiêu thụ đặc biệt; sự cố thương hiệu |
| SME | Nhà phân phối khu vực, cơ sở chế biến | Phụ thuộc chính sách công nợ của hãng; tồn kho cận hạn |
| KHCN – hộ kinh doanh | Đại lý cấp 2, tạp hóa, lò mổ, sạp chợ, đại lý thức ăn | Bán chịu cho trại nhỏ; mất nguồn hàng khi có dịch |
| KHCN – cá nhân | Trang trại hộ gia đình, công nhân, người tiêu dùng | Nông hộ mất đàn khi có dịch, thường không có bảo hiểm |

**Đặc thù quan trọng với ngân hàng:** hàng thiết yếu nên nhu cầu ít nhạy với chu kỳ, nhưng biên lợi nhuận vẫn bị ép khi nguyên liệu tăng. Đồ uống có cồn, nước ngọt nhạy với chính sách thuế. Dịch bệnh vật nuôi tạo cú sốc cung đột ngột theo vùng, chạm trực tiếp nông hộ chăn nuôi – nhóm có khoản vay sản xuất ở ngân hàng. Rủi ro tập trung có thể xuất hiện khi nhiều nhà phân phối cùng một DN đầu chuỗi.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Giá ngô, đậu tương, lúa mì thế giới; USD | Chi phí thức ăn tăng, biên lợi nhuận trang trại bị ép | Trang trại, DN thức ăn | Vài tuần | `I07` |
| Dịch tả lợn châu Phi, cúm gia cầm | Nông hộ mất đàn ngay; sau đó giá thịt tăng làm trang trại an toàn sinh học có lợi | Nông hộ chăn nuôi, đại lý thức ăn | Ngay rồi đảo chiều | – |
| Giá lợn hơi | Giá giảm làm trang trại lỗ; giá tăng thì trang trại lợi nhưng nhà hàng, chế biến dùng thịt thiệt | Trang trại | Nhanh | `I10` |
| Tiêu dùng nội địa, thu nhập | Người tiêu dùng chuyển sang hàng rẻ | Nhà phân phối, đại lý | Một đến hai quý | `I09` |
| Thuế tiêu thụ đặc biệt, quy định nồng độ cồn | Sản lượng đồ uống giảm, nhà hàng thiệt | DN đồ uống, nhà hàng | Theo hiệu lực | `I10` |
| Giá đường, sữa bột, dầu thực vật | Chi phí sản xuất tăng | DN chế biến | Vài tuần | – |
| Sự cố an toàn thực phẩm | Mất niềm tin thương hiệu, thu hồi sản phẩm; có thể kèm rủi ro danh tiếng cho đối tác | DN liên quan, nhà phân phối | Ngay | – |
| Tỷ lệ sinh giảm, già hóa | Sữa trẻ em giảm cầu, dinh dưỡng người già tăng | DN sữa | Dài | Tin `GT` |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Nông hộ chăn nuôi mất đàn do dịch và thường không có bảo hiểm, nên khoản vay sản xuất mất nguồn trả ngay. Giá thực phẩm tăng làm chi tiêu khác của hộ gia đình co lại.

**Cơ hội.** Giá lợn hơi tăng làm thu nhập trang trại hộ tăng; tái đàn sau dịch cần vốn.

### KHCN – hộ kinh doanh
**Thách thức.** Đại lý thức ăn bán chịu cho trại nhỏ bị nợ đọng khi có dịch; sạp thịt, lò mổ mất nguồn hàng; tạp hóa chịu cạnh tranh từ chuỗi bán lẻ.

**Cơ hội.** Đại lý trong chuỗi của DN lớn có doanh thu ổn định; mùa Tết là cao điểm nhập hàng.

### SME
**Thách thức.** Nhà phân phối phụ thuộc chính sách công nợ của hãng; hàng tồn cận hạn sử dụng.

**Cơ hội.** Tài trợ nhà phân phối theo chương trình của DN lớn; chế biến thực phẩm tiện lợi.

### DN lớn
**Thách thức.** Chi phí nguyên liệu nhập và tỷ giá; thuế tiêu thụ đặc biệt; sự cố thương hiệu.

**Cơ hội.** Giá nguyên liệu giảm; mở rộng sang chăn nuôi khép kín; thị trường người cao tuổi; xuất khẩu thịt, thực phẩm chế biến.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay tiêu dùng `CN-LN-06` của hộ chăn nuôi (mất đàn) | Tiền gửi (`O2`), bảo hiểm (`O4`) theo nhu cầu thật |
| HKD | ShopCash `HKD-LN-01` của đại lý thức ăn, sạp thịt (nợ đọng, mất nguồn hàng) | Vốn nhập hàng mùa Tết (`O1`); QR, Soundbox `HKD-REV-01` (`O3`) |
| SME | Vay `SME-LN-01`, gói MerchantOne `SME-PKG-02` | Vốn lưu động nhà phân phối (`O1`), thanh toán (`O3`) |
| DN lớn | L/C nhập ngô, đậu tương `CIB-TF-01`, ngoại tệ `CIB-FX-01` | Tài trợ nhà phân phối `CIB-SCF-01`, phòng ngừa tỷ giá `CIB-CM-02`, thu hộ `CIB-COL-01`, chi lương (`O1` `O3` `O2`) |
| Cấp ngân hàng | Tập trung tài trợ chuỗi theo một DN đầu chuỗi | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S11` nhà phân phối cùng một DN lớn chậm trả đồng loạt | DN đầu chuỗi có vấn đề | Chưa có |
| `S02` doanh thu QR của sạp thịt, tạp hóa theo địa bàn | Mất nguồn hàng hoặc sức mua giảm | Chưa có |
| `S04` hạn mức của đại lý thức ăn tăng khi có dịch | Đại lý gánh nợ của trại | Có với thẻ, thấu chi cá nhân của chủ hộ |
| `S06` tất toán tiết kiệm theo tỉnh có dịch | Nông hộ cần tiền sau khi mất đàn | Có |
| Nhu cầu L/C nhập nguyên liệu thức ăn theo mùa | Chiều chi phí | Chưa có |

Luôn ghi "cần truy vấn dư nợ theo chuỗi DN đầu chuỗi hàng tiêu dùng nhanh, số nhà phân phối trong chương trình tài trợ".

## 6. Liên kết ngành
- **Thượng nguồn – `I07` (ngô, gạo, cà phê làm nguyên liệu), ngũ cốc nhập khẩu qua `I11`, `I13` (bao bì).**
- **Hạ nguồn – `I09` bán lẻ, `I10` ăn uống:** giá thịt và đồ uống truyền vào chi phí nhà hàng.
- **Song song – `I06` (thức ăn thủy sản dùng chung nguyên liệu).**

## 7. Điểm đảo chiều và lưu ý
- Sau dịch, giá thịt tăng kéo tái đàn ồ ạt; vài quý sau giá giảm.
- Hàng thiết yếu là nơi trú ẩn khi tiêu dùng yếu, nhưng biên lợi nhuận vẫn bị ép.
- Không nêu tên thương hiệu; với sự cố an toàn thực phẩm chỉ mô tả tác động lên chuỗi.
- Dịch vật nuôi ở một tỉnh không chạm đều cả nước; giới hạn ở vùng tin nêu.
