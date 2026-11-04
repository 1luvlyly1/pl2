---
id: IND-15
code: I15
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về dịch bệnh, bảo hiểm y tế, đấu thầu thuốc, giá dịch vụ y tế, quy định nhà thuốc, già hóa dân số, thuốc giả, tỷ giá (thuốc nhập), y tế tư nhân, du lịch chữa bệnh
version: v3.4
updated: 2026-11-04
---

# I15 – Y tế và dược phẩm

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
**Dịch vụ y tế:** bệnh viện công là chủ đạo; bệnh viện tư, phòng khám tư, nha khoa, thẩm mỹ, xét nghiệm tăng nhanh ở đô thị. **Dược phẩm:** DN sản xuất trong nước (chủ yếu thuốc generic) và DN FDI; nhiều thuốc chuyên khoa và nguyên liệu dược nhập khẩu; bán qua kênh bệnh viện (đấu thầu) và kênh nhà thuốc (chuỗi và nhà thuốc lẻ). **Thiết bị y tế:** chủ yếu nhập khẩu, phân phối qua DN thương mại.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Chuỗi bệnh viện tư, nhà sản xuất dược, chuỗi nhà thuốc | Đấu thầu giá thấp; nguyên liệu nhập; tuân thủ quy chuẩn sản xuất |
| SME | Nhà phân phối dược, thiết bị; phòng khám | Bị bệnh viện chậm thanh toán; cần bảo lãnh dự thầu |
| KHCN – hộ kinh doanh | Nhà thuốc lẻ, phòng khám tư nhỏ, nha khoa | Cạnh tranh với chuỗi; chi phí tuân thủ kê đơn, hóa đơn |
| KHCN – cá nhân | Y bác sĩ, dược sĩ (thu nhập ổn định); người bệnh | Chi phí y tế đột xuất làm cạn tiết kiệm |

**Đặc thù quan trọng với ngân hàng:** nhu cầu ít nhạy với chu kỳ kinh tế. Đấu thầu thuốc và thanh toán bảo hiểm y tế có thể chậm, gây áp lực vốn cho nhà cung cấp (`L12`). Già hóa dân số là động lực dài hạn. Phía cá nhân, chi phí y tế lớn là một nguyên nhân phổ biến của tất toán tiết kiệm trước hạn và vay tiêu dùng gấp.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Dịch bệnh | Cầu thuốc, xét nghiệm, thiết bị tăng; bệnh viện quá tải; dịch kéo dài làm dịch vụ không khẩn cấp giảm | Nhà thuốc, bệnh viện | Ngay | `I10` `I16` |
| Chính sách đấu thầu, thanh toán bảo hiểm y tế | Thanh toán chậm làm nhà cung cấp kẹt vốn | Nhà phân phối | Vài tháng | – |
| Giá dịch vụ y tế, tự chủ bệnh viện | Doanh thu bệnh viện thay đổi theo điều chỉnh giá | Bệnh viện | Theo quyết định | – |
| Quy định nhà thuốc, kê đơn, hóa đơn | Nhà thuốc lẻ chịu chi phí tuân thủ; chuỗi có lợi thế | Nhà thuốc lẻ | Theo hiệu lực | `I09` |
| USD mạnh | Thuốc nhập, nguyên liệu, thiết bị đắt hơn | Nhà nhập khẩu, người bệnh mãn tính | Vài tháng | – |
| Già hóa, bệnh mãn tính | Cầu dài hạn tăng | DN y tế (chiều lợi) | Dài | Tin `GT` |
| Thu nhập tăng, tầng lớp trung lưu | Cầu y tế tư, bảo hiểm sức khỏe tăng | DN y tế tư | Dài | – |
| Vụ việc thuốc giả, sai phạm đấu thầu | Mất niềm tin, điều tra; có thể chạm tuân thủ, danh tiếng của đối tác | DN liên quan | Nhanh | – |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Chi phí y tế lớn đột xuất làm cạn tiết kiệm, buộc vay tiêu dùng hoặc tất toán sớm. Người bệnh mãn tính chịu giá thuốc nhập tăng.

**Cơ hội.** Nhu cầu bảo hiểm sức khỏe tăng sau dịch hoặc tin y tế; y bác sĩ là khách thu nhập ổn định (vay mua nhà, đầu tư); mở phòng khám riêng.

### KHCN – hộ kinh doanh
**Thách thức.** Nhà thuốc lẻ cạnh tranh với chuỗi và chịu chi phí tuân thủ; tồn kho thuốc sau mùa dịch.

**Cơ hội.** Mùa dịch làm doanh thu tăng; số hóa thanh toán, quản lý bán hàng.

### SME
**Thách thức.** Nhà phân phối thuốc, thiết bị bị bệnh viện chậm thanh toán; cần bảo lãnh dự thầu.

**Cơ hội.** Trúng thầu; phòng khám chuyên khoa, nha khoa mở rộng (vay đầu tư thiết bị).

### DN lớn
**Thách thức.** Đấu thầu giá thấp; chi phí nguyên liệu nhập; tuân thủ quy chuẩn sản xuất.

**Cơ hội.** Chuỗi bệnh viện tư, chuỗi nhà thuốc mở rộng; sản xuất trong nước thay thế nhập khẩu; già hóa dân số.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay tiêu dùng `CN-LN-06`; tất toán sớm tiền gửi `CN-DEP-01` (`S06`) do chi phí y tế | Bảo hiểm sức khỏe `CN-INS-01` (`O4`) đúng nhu cầu; vay mua nhà cho y bác sĩ (`O1`); tài khoản lương (`O2`) |
| HKD | ShopCash `HKD-LN-01` của nhà thuốc lẻ (cạnh tranh, tồn kho) | QR, SoftPOS `HKD-REV-03`, vốn nhập thuốc (`O3` `O1`) |
| SME | Vay `SME-LN-01` kẹt vốn do chậm thanh toán | Bảo lãnh mua sắm công `SME-GTE-01` (`O3`), vay thiết bị (`O1`) |
| DN lớn | L/C nhập nguyên liệu, thiết bị `CIB-TF-01`, ngoại tệ `CIB-FX-01` | Vay đầu tư bệnh viện `CIB-LN-02`, chi lương `CIB-PAY-06`, thu hộ viện phí `CIB-COL-01` (`O1` `O2` `O3`) |
| Cấp ngân hàng | Rủi ro danh tiếng (`RP`) khi bán bảo hiểm sức khỏe không phù hợp nhu cầu | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S06` tất toán sớm, vay cầm cố tiền gửi tăng trong mùa dịch | Hộ gia đình cần tiền cho y tế | Có (phần tất toán) |
| `S09` hủy bảo hiểm sớm, hoặc số hợp đồng bảo hiểm sức khỏe mới tăng | Áp lực tài chính hoặc nhu cầu bảo vệ tăng | Gần đúng: phí bảo hiểm, số dư hiện tại |
| `S02` doanh thu QR của nhà thuốc theo địa bàn | Chỉ báo sớm dịch bệnh cục bộ | Chưa có |
| Thời gian thu tiền từ bệnh viện của nhà phân phối | Áp lực vốn do chậm thanh toán | Chưa có |
| Dòng lương của bệnh viện tư | Quy mô, ổn định của cơ sở | Có |

Luôn ghi "cần truy vấn dư nợ ngành y tế, dược theo kênh (bệnh viện, nhà thuốc)".

## 6. Liên kết ngành
- **Thượng nguồn – nguyên liệu nhập khẩu qua `I11`, `I13` (hóa chất).**
- **Song song – `I17` (y tế số), `I10` (du lịch chữa bệnh, thẩm mỹ).**
- **Ngành bị tác động ngược khi có dịch – `I10`, `I16`, `I09` cửa hàng.**

## 7. Điểm đảo chiều và lưu ý
- Doanh thu tăng mạnh mùa dịch không phải xu hướng; nhà thuốc, nhà phân phối mở rộng ở đỉnh dịch dễ tồn kho.
- Bảo hiểm sức khỏe là cơ hội `O4` nhưng phải đúng nhu cầu, không bán theo nỗi sợ (`guardrails.md` mục 12).
- Không nêu tên cơ sở y tế; không suy đoán sai phạm khi tin không nêu.
