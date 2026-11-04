---
id: IND-03
code: I03
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về thuế quan Mỹ, EU, hiệp định thương mại, quy tắc xuất xứ, đơn hàng thời trang toàn cầu, giá bông, xơ sợi, cước vận tải biển, lương tối thiểu, dịch bệnh
version: v3.4
updated: 2026-11-04
---

# I03 – Dệt may, da giày

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Chuỗi giá trị đi từ sợi sang dệt, nhuộm rồi may; song song là da sang giày, túi xách. Việt Nam mạnh ở khâu may và gia công, yếu ở khâu vải và nguyên phụ liệu, nên vải, xơ sợi, phụ liệu nhập nhiều từ Trung Quốc và bông nhập khẩu. Nhiều DN làm gia công (chỉ nhận tiền công) hoặc mua nguyên liệu – bán thành phẩm, biên lợi nhuận mỏng. Đầu ra là Mỹ, EU, Nhật Bản, Hàn Quốc, theo mùa thời trang.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn và FDI | Nhà máy làm hàng xuất khẩu cho nhãn hàng quốc tế | Người mua ép giá, kéo dài kỳ thanh toán; quy tắc xuất xứ quyết định ưu đãi thuế |
| SME | Xưởng gia công, vệ tinh | Mất đơn đầu tiên khi DN lớn cắt giảm; biên mỏng nên ít đệm |
| KHCN – hộ kinh doanh | Xưởng may nhỏ, cửa hàng vải, chợ đầu mối; quán ăn, nhà trọ quanh nhà máy | Doanh thu phụ thuộc số giờ làm của công nhân |
| KHCN – cá nhân | Lực lượng công nhân rất đông, phần lớn là nữ, thu nhập qua chi lương; nhiều người gửi tiền về quê | Thu nhập theo giờ làm; giảm ca là giảm thu nhập ngay kỳ lương sau |

Vùng sản xuất chính: Đông Nam Bộ, đồng bằng sông Hồng, Bắc Trung Bộ; một số nhà máy dịch chuyển về tỉnh có lao động rẻ hơn.

**Đặc thù quan trọng với ngân hàng:** đây là ngành mẫu lan truyền "doanh nghiệp trước" điển hình – đơn hàng giảm ở DN, một đến hai tháng sau tới công nhân, rồi tới hộ kinh doanh quanh nhà máy. Lực lượng lao động đông nên tài khoản lương, thẻ, vay tiêu dùng của công nhân là phần phơi nhiễm KHCN lớn.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Thuế quan Mỹ, EU với hàng Việt Nam | Người mua chuyển đơn sang nước khác hoặc ép giá; trước hạn áp thuế có thể có pha đẩy hàng tạm thời | DN xuất khẩu, rồi xưởng vệ tinh | Đơn hàng mùa sau | `I11` |
| Quy tắc xuất xứ, chống lẩn tránh | DN dùng nhiều nguyên liệu nhập mất ưu đãi thuế, phải đổi nguồn nguyên liệu | DN xuất khẩu | Theo lộ trình | – |
| Tiêu dùng thời trang ở Mỹ, EU | Nhãn hàng tồn kho cao thì cắt đơn; tin về tồn kho nhãn hàng là tín hiệu sớm | DN xuất khẩu | Một đến hai quý | – |
| Giá bông, xơ sợi | Chi phí tăng; DN chỉ gia công ít bị ảnh hưởng | DN mua nguyên liệu | Vài tuần | `I13` |
| USD mạnh | Doanh thu quy đổi tăng nhưng đầu vào cũng nhập bằng USD, tác động ròng thường nhỏ | DN xuất khẩu | Ngay | – |
| Cước vận tải biển | Chi phí giao hàng tăng, giao chậm | DN bán theo giá đã gồm vận chuyển | Vài tuần | `I11` |
| Lương tối thiểu, cạnh tranh lao động | Chi phí tăng; nhà máy điện tử hút lao động | DN | Theo năm | `I04` |
| Dịch bệnh | Nhà máy đóng cửa, đơn bị hủy | Công nhân, DN | Ngay | – |
| Yêu cầu xanh, truy xuất nguồn gốc | Chi phí tuân thủ tăng | DN xuất khẩu | Dài | Tin `GT` |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Đơn hàng giảm dẫn tới cắt giờ làm, giãn việc, chậm lương. Công nhân đang có vay tiêu dùng, thẻ, thấu chi chịu áp lực trả nợ từ kỳ lương sau. Tác động lan sang gia đình ở quê vì khoản tiền gửi về giảm.

**Cơ hội.** Đơn hàng tăng kéo tăng ca, thu nhập tăng; nhà máy mới mở tạo tài khoản lương mới.

### KHCN – hộ kinh doanh
**Thách thức.** Quán ăn, nhà trọ, tạp hóa quanh nhà máy mất doanh thu khi công nhân giảm giờ làm (`L06`).

**Cơ hội.** Nhà máy mới hoặc mùa tăng ca kéo doanh thu khu dân cư quanh nhà máy.

### SME
**Thách thức.** Xưởng gia công vệ tinh mất đơn đầu tiên khi DN lớn cắt giảm; bị chậm thanh toán; biên mỏng nên ít đệm.

**Cơ hội.** Đơn chuyển từ nước khác sang Việt Nam; nhu cầu vốn lưu động mùa cao điểm.

### DN lớn
**Thách thức.** Thuế quan và quy tắc xuất xứ; người mua ép giá, kéo dài kỳ thanh toán; chi phí lao động tăng.

**Cơ hội.** Đơn hàng dịch chuyển khỏi các nước khác; hiệp định thương mại; đầu tư vào khâu vải để đáp ứng quy tắc xuất xứ (vay trung dài hạn, vay xanh).

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay tiêu dùng `CN-LN-06`, thẻ `CN-CARD-01`, MyCash `CN-LN-05` của công nhân (thu nhập theo giờ làm giảm) | Tài khoản lương mới `CN-ACC-01` (`O2`) khi nhà máy tuyển dụng; bảo hiểm sức khỏe (`O4`) theo nhu cầu thật |
| HKD | ShopCash `HKD-LN-01` của hộ quanh nhà máy (doanh thu theo công nhân) | QR, Soundbox `HKD-REV-01` (`O3`) |
| SME | Vay `SME-LN-01` (mất đơn), thanh toán lương `SME-PAY-06` | Vốn lưu động mùa cao điểm (`O1`) khi có đơn rõ; ngoại tệ `SME-PAY-04` (`O3`) |
| DN lớn | L/C nhập nguyên liệu `CIB-TF-01`, vốn lưu động `CIB-LN-01`, tài trợ xuất khẩu `CIB-TF-02` | Tài trợ xuất khẩu, phòng ngừa tỷ giá `CIB-CM-02`, chi lương `CIB-PAY-06` (`O1` `O3` `O2`) |
| Cấp ngân hàng | CASA từ tài khoản lương giảm khi cắt giảm lao động | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S01` lô chi lương trễ, giảm số người hoặc tổng quỹ | Cắt ca, cắt lao động đã bắt đầu | Có: nhân viên theo DN trả lương, lương bình quân DN 3 và 6 tháng |
| `S10` hóa đơn điện, cảng giảm | Sản lượng giảm | Chưa có; thay thế bằng dòng vào và số ngày có giao dịch của DN |
| `S04` `S05` công nhân dùng thấu chi, thẻ tăng | Thu nhập công nhân đã giảm | Có |
| `S02` doanh thu QR quanh khu công nghiệp | Lan sang hộ kinh doanh | Chưa có |
| `X04` người mua nước ngoài đổi tài khoản nhận tiền | Lừa đảo email giả người mua | Chưa có |

Luôn ghi "cần truy vấn số tài khoản lương theo DN ngành dệt may, da giày".

## 6. Liên kết ngành
- **Thượng nguồn – `I13` (xơ sợi tổng hợp từ hóa dầu), bông nhập khẩu, `I11` vận tải:** chi phí nguyên liệu và giao hàng.
- **Hạ nguồn – `I09` bán lẻ thời trang trong nước:** hàng xuất khẩu không bán được có thể đổ vào thị trường nội địa.
- **Song song – `I04` (cạnh tranh lao động khu công nghiệp), `I01` (nhà trọ, khu công nghiệp).**

## 7. Điểm đảo chiều và lưu ý
- Pha đẩy hàng trước hạn áp thuế tạo đơn tăng tạm thời, sau đó đơn giảm; không coi là xu hướng.
- Tác động lên công nhân đến sau DN một đến hai tháng (qua `S01`); viết độ trễ rõ.
- Ví dụ mẫu lan truyền doanh nghiệp trước: `examples/ex_P1_doanh_nghiep_truoc.md`.
