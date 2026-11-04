---
id: IND-12
code: I12
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về giá dầu, khí, than, điều hành giá xăng dầu, giá điện bán lẻ, quy hoạch điện, năng lượng tái tạo, thiếu điện, hạn hán (thủy điện), xung đột tại vùng dầu mỏ, chuyển đổi xanh, trung tâm dữ liệu
version: v3.4
updated: 2026-11-04
---

# I12 – Năng lượng: dầu khí, xăng dầu, điện, năng lượng tái tạo

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
**Dầu khí** gồm thượng nguồn (thăm dò, khai thác), trung nguồn (lọc hóa dầu, khí) và hạ nguồn (phân phối xăng dầu). Xăng dầu trong nước một phần từ nhà máy lọc dầu, phần còn lại nhập khẩu; giá bán lẻ được điều hành định kỳ theo giá thế giới, có quỹ bình ổn. **Điện** có nguồn từ thủy điện, nhiệt điện than, khí, điện mặt trời, điện gió; truyền tải và bán lẻ do Nhà nước chi phối, giá điện bán lẻ do Nhà nước điều chỉnh; có chủ trương mua bán điện trực tiếp và điện mặt trời mái nhà.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Khai thác, lọc dầu, phát điện, phân phối xăng dầu | Nhà máy điện chịu giá nhiên liệu và chậm thu tiền điện; dự án tái tạo kẹt giá mua điện; đầu mối xăng dầu chịu kỳ điều hành |
| SME | Đầu mối phân phối nhỏ, nhà thầu lắp đặt điện mặt trời, dịch vụ kỹ thuật | Bị chủ dự án chậm thanh toán khi chính sách không rõ; đầu mối nhỏ thiếu vốn khi giá tăng |
| KHCN – hộ kinh doanh | Cửa hàng xăng dầu tư nhân, đại lý gas | Bị đầu mối hạn chế nguồn hoặc chiết khấu thấp khi giá biến động; lỗ hàng tồn khi giá giảm nhanh |
| KHCN – cá nhân | Người dùng nhiên liệu và điện, hộ lắp điện mặt trời mái nhà | Giá xăng, điện tăng làm chi phí sinh hoạt tăng |

**Đặc thù quan trọng với ngân hàng:** dự án điện có vốn lớn, vay dài hạn, nhạy lãi suất và chính sách giá mua điện. Phân phối xăng dầu cần vốn lưu động lớn và chịu rủi ro giá hàng tồn giữa các kỳ điều hành. Giá dầu là biến số chạm nhiều ngành nhất; khi gặp tin giá dầu, file này thường chỉ là một trong ba file ngành, không phải file chính.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Giá dầu thế giới | Giá tăng: thượng nguồn lợi; phân phối lợi trên hàng tồn nhưng cần thêm vốn. Giá giảm nhanh: phân phối lỗ hàng tồn | Đầu mối, cửa hàng xăng dầu | Ngay | `I10` `I11` |
| Kỳ điều hành giá xăng dầu trong nước | Giá điều hành chậm theo giá thế giới thì đầu mối bị kẹp biên; từng có giai đoạn thiếu xăng cục bộ | Đầu mối, cửa hàng | Theo kỳ | – |
| Giá khí, than nhập khẩu | Chi phí phát điện tăng; nhà máy chịu nếu giá bán điện không điều chỉnh | Nhà máy điện | Nhanh | – |
| Giá điện bán lẻ | Bên bán lợi; ngành dùng nhiều điện thiệt | Ngành tiêu hao năng lượng | Theo quyết định | `I02` `I13` |
| Hạn hán, El Niño | Thủy điện giảm, nguy cơ thiếu điện; từng có giai đoạn cắt điện ở phía Bắc | Nhà máy sản xuất, khu công nghiệp | Theo mùa | `I04` |
| Chính sách giá mua điện tái tạo, quy hoạch | Chính sách không rõ làm dự án tái tạo kẹt dòng tiền | Chủ dự án, nhà thầu | Dài | – |
| USD mạnh | Nhập xăng dầu, thiết bị và nợ USD đắt hơn | DN nhập khẩu | Ngay | – |
| Lãi suất | Dự án đòn bẩy cao chịu áp lực | Chủ dự án điện | Vài tháng | – |
| Xu hướng xanh, trung tâm dữ liệu, xe điện | Cầu điện tăng, cần đầu tư nguồn mới | DN phát điện | Dài | Tin `GT` |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Giá xăng, điện tăng làm chi phí sinh hoạt tăng và chi tiêu khác co lại (`L06`).

**Cơ hội.** Lắp điện mặt trời mái nhà, mua xe điện (vay mua, bảo hiểm); lao động kỹ thuật năng lượng có thu nhập tốt.

### KHCN – hộ kinh doanh
**Thách thức.** Cửa hàng xăng dầu tư nhân bị đầu mối hạn chế nguồn hoặc giảm chiết khấu khi giá biến động; giá giảm nhanh thì lỗ hàng tồn.

**Cơ hội.** Doanh thu tăng theo giá; dịch vụ lắp đặt điện mặt trời, sạc xe điện.

### SME
**Thách thức.** Nhà thầu lắp đặt bị chủ dự án chậm thanh toán khi chính sách không rõ; đầu mối nhỏ thiếu vốn khi giá tăng.

**Cơ hội.** Điện mặt trời mái nhà cho nhà xưởng; dịch vụ bảo trì; mua bán điện trực tiếp.

### DN lớn
**Thách thức.** Nhà máy điện chịu giá nhiên liệu và chậm thu tiền điện; dự án tái tạo kẹt giá mua điện; đầu mối xăng dầu chịu kỳ điều hành.

**Cơ hội.** Giá dầu cao làm thượng nguồn lợi; đầu tư nguồn điện mới, lưới, khí hóa lỏng; tài trợ xanh.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Chi tiêu thẻ `CN-CARD-01` co lại khi giá tăng (`BR`) | Vay lắp điện mặt trời, xe điện (`CN-LN-08` `CN-LN-04`, `O1`); bảo hiểm (`O4`) |
| HKD | ShopCredit `HKD-LN-02` của cửa hàng xăng dầu (lỗ hàng tồn) | Vốn nhập hàng (`O1`), QR, POS (`O3`) |
| SME | Vay `SME-LN-01`, bảo lãnh `SME-GTE-01` | Vốn lưu động, bảo lãnh (`O1` `O3`) |
| DN lớn | Vay dự án điện `CIB-LN-02`, L/C nhập xăng dầu `CIB-TF-01`, ngoại tệ `CIB-FX-01` | Vốn lưu động `CIB-LN-01`, phòng ngừa tỷ giá và hàng hóa `CIB-CM-02`, tiền gửi xanh, trái phiếu xanh `CIB-INV-01` (`O1` `O3`) |
| Cấp ngân hàng | Nhu cầu USD của nhà nhập khẩu (`NH-MR-01`); lạm phát kéo lãi suất (`NH-MR-02`) | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| Nhu cầu mua USD, L/C nhập xăng dầu theo kỳ | Áp lực tỷ giá | Gần đúng: số dư và giao dịch ngoại tệ của DN |
| `S04` hạn mức của đầu mối, cửa hàng xăng dầu | Thiếu vốn khi giá tăng | Có với thấu chi DN và thẻ, thấu chi của chủ hộ |
| `S10` hóa đơn điện của khách sản xuất | Sản lượng | Chưa có |
| `S15` vị thế phái sinh hàng hóa của khách | Rủi ro đối tác | Chưa có |

Luôn ghi "cần truy vấn dư nợ dự án điện theo loại nguồn, dư nợ phân phối xăng dầu".

## 6. Liên kết ngành
- **Khách dùng năng lượng làm đầu vào – `I10` hàng không, `I11` vận tải, `I13` hóa chất, phân bón, nhựa, `I02` thép, xi măng, `I06` tàu cá:** giá năng lượng là chi phí lớn của họ.
- **Song song – `I14` xe điện, `I17` trung tâm dữ liệu, `I04` FDI cần điện ổn định.**

## 7. Điểm đảo chiều và lưu ý
- Giá dầu chạm nhiều ngành nhất; chỉ nạp file của ngành bị tác động mạnh nhất, không kể hết.
- Phân phối xăng dầu lợi khi giá tăng nhưng lỗ khi giá giảm nhanh – điểm đảo chiều thường gặp.
- Không suy đoán quyết định điều hành giá của cơ quan nhà nước; không dự báo giá dầu.
