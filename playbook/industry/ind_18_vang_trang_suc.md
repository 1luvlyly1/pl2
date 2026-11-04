---
id: IND-18
code: I18
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về giá vàng thế giới và trong nước, chênh lệch giá vàng, chính sách quản lý vàng miếng, nhập khẩu vàng, xung đột địa chính trị, lạm phát, USD, ngày Vía Thần Tài, mùa cưới, quy định chống rửa tiền
version: v3.4
updated: 2026-11-04
---

# I18 – Vàng, bạc, trang sức

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Ngành gồm **vàng miếng** (sản xuất và nhập khẩu do Nhà nước quản lý chặt, chính sách đang được điều chỉnh), **vàng nhẫn, vàng trang sức** (nhiều DN và tiệm vàng), bạc và đá quý.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | DN kinh doanh vàng bạc đá quý có hệ thống cửa hàng | Chịu chính sách quản lý; tồn kho lớn khi giá giảm nhanh |
| SME | Xưởng chế tác, cửa hàng | Giá nguyên liệu biến động; trang sức tồn kho bán chậm |
| KHCN – hộ kinh doanh | Tiệm vàng ở mọi địa phương, vừa bán lẻ vừa thu mua, nhiều giao dịch tiền mặt | Cần vốn lớn cho hàng tồn khi giá tăng; rủi ro cướp, vàng giả; chi phí tuân thủ |
| KHCN – cá nhân | Người giữ vàng – kênh tích trữ truyền thống của hộ gia đình, nhất là ở nông thôn | Người mua ở đỉnh bằng tiền vay hoặc tất toán tiết kiệm chịu lỗ khi giá quay đầu |

**Đặc thù quan trọng với ngân hàng:** vàng là **đối thủ trực tiếp của tiền gửi**. Khi giá vàng tăng nóng, tiền gửi chảy ra mua vàng (`NH-LQ-01`), nhu cầu rút tiền mặt tăng (`NH-LQ-02`). Giá trong nước có thể chênh so với thế giới do quản lý nguồn cung. Tâm lý đám đông mạnh (xếp hàng mua khi giá tăng nóng) – pha tham điển hình. Giao dịch tiền mặt lớn là điểm nhạy về chống rửa tiền. Mùa vụ: ngày Vía Thần Tài, mùa cưới cuối năm, trước Tết.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Giá vàng thế giới | Giá tăng: người giữ vàng lợi, người mua đổ xô (pha tham), sức mua trang sức giảm; giá giảm nhanh: người mua ở đỉnh lỗ | Người giữ vàng, tiệm vàng, cấp ngân hàng (huy động) | Ngay | Xem `outside_in/news/nw_01_truc_tiep.md` mục 2.1 |
| Xung đột địa chính trị, lạm phát | Cầu vàng trú ẩn tăng | Người mua | Ngay | – |
| Chênh lệch giá trong nước và thế giới | Chênh rộng tạo áp lực buôn lậu và chính sách can thiệp; chênh thu hẹp đột ngột làm người mua giá cao lỗ | Người mua vàng miếng | Nhanh | – |
| Chính sách quản lý vàng miếng, nhập khẩu | Nới nguồn cung làm chênh lệch thu hẹp | DN vàng, người giữ vàng miếng | Theo quyết định | Không suy đoán chính sách khi tin không nêu |
| USD, lãi suất | USD mạnh, lãi suất cao thường kìm giá vàng, nhưng không phải luôn đúng | Người giữ vàng | Vài tuần | – |
| Lãi suất tiền gửi trong nước | Lãi suất thấp làm tiền chuyển sang vàng | Cấp ngân hàng | Vài tuần | `NH-LQ-01` |
| Quy định chống rửa tiền, hóa đơn bán vàng | Tiệm vàng chịu chi phí tuân thủ | Tiệm vàng | Theo hiệu lực | – |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Người mua ở đỉnh – nhất là bằng tiền vay hoặc tất toán tiết kiệm – chịu lỗ khi giá quay đầu. Lừa đảo đầu tư vàng online và sàn vàng không phép tăng khi giá nóng. Mua vàng không hóa đơn khó bán lại.

**Cơ hội.** Người giữ vàng chốt lời có tiền để gửi lại ngân hàng, đầu tư, mua nhà (`O2` `O4`).

### KHCN – hộ kinh doanh
**Thách thức.** Tiệm vàng cần vốn lớn cho hàng tồn khi giá tăng; rủi ro cướp, vàng giả; chi phí tuân thủ hóa đơn và chống rửa tiền; doanh thu trang sức giảm khi giá quá cao.

**Cơ hội.** Doanh thu mua bán tăng mạnh mùa sốt giá; nhận thanh toán số thay tiền mặt.

### SME
**Thách thức.** Xưởng chế tác chịu giá nguyên liệu biến động; tồn kho trang sức bán chậm.

**Cơ hội.** Trang sức thiết kế, giá trị gia tăng; xuất khẩu trang sức.

### DN lớn
**Thách thức.** Chịu chính sách quản lý; tồn kho lớn khi giá giảm nhanh.

**Cơ hội.** Nguồn cung vàng miếng mở rộng nếu chính sách nới; mở rộng chuỗi; thu hộ, thanh toán tiền mặt lớn.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Tất toán `CN-DEP-01` để mua vàng (`G02`); vay tiêu dùng `CN-LN-06` mua vàng (`G01`); rút tiền mặt qua CDM `CN-PAY-02`; gian lận (`FR`) qua sàn vàng không phép (`G07`) | Tiền gửi từ khách chốt lời (`O2`); đầu tư, bảo hiểm (`O4`) theo khẩu vị rủi ro |
| HKD | ShopCredit `HKD-LN-02` của tiệm vàng; giao dịch tiền mặt lớn | CDM `HKD-SVC-01`, QR, SoftPOS (`O3`); tiền gửi của hộ (`O2`) |
| SME | Vay `SME-LN-01` của xưởng chế tác | Thanh toán, thu hộ (`O3`) |
| DN lớn | Vốn lưu động `CIB-LN-01`; hàng tồn làm tài sản bảo đảm (`CL`); nhập khẩu vàng `CIB-TF-01` | Thu hộ tiền mặt `CIB-COL-01`, chi lương (`O3` `O2`) |
| Cấp ngân hàng | Huy động giảm (`NH-LQ-01`), tiền mặt (`NH-LQ-02`), tỷ giá (`NH-MR-01`), giao dịch tiền mặt lớn (`NH-CO-01`) | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `G02` tất toán tiết kiệm rồi rút tiền mặt hoặc chuyển cho tiệm vàng | Tiền gửi chảy sang vàng | Gần đúng: tất toán trước hạn và AUM giảm; không thấy đích chuyển |
| `S07` rút tiền mặt CDM tăng cùng lúc giá vàng tăng | Mua vàng bằng tiền mặt | Chưa có |
| `G01` tiền vay tiêu dùng chuyển cho bên bán vàng | Mua vàng bằng đòn bẩy | Chưa có |
| `S16` doanh thu tiệm vàng chảy về tài khoản cá nhân | Né thuế, rủi ro chống rửa tiền | Chưa có |
| `X01` tài khoản nhận tiền nhiều nguồn ghi nội dung đầu tư vàng | Lừa đảo đầu tư vàng | Chưa có |
| `F01` AUM, CASA theo hạng khách giảm | Dòng tiền rời ngân hàng | Gần đúng: độ dốc AUM, CASA tháng so với 3 tháng |

Luôn ghi "cần truy vấn dòng tiền chuyển đến tài khoản tiệm vàng, DN vàng theo tuần".

## 6. Liên kết ngành
- **Song song – `I07` (nông hộ giữ vàng sau vụ), `I10` (khách du lịch mua trang sức).**
- **Cấp ngân hàng – `core/06_ngan_hang.md` (huy động, tiền mặt, tỷ giá).**
- **Đối thủ của dòng tiền – chứng khoán, BĐS (`I01`) trong pha tham.**

## 7. Điểm đảo chiều và lưu ý
- Pha xếp hàng mua vàng là pha tham điển hình; điểm đảo chiều là khi giá quay đầu hoặc chênh lệch thu hẹp đột ngột do chính sách.
- Khi giá vàng giảm mạnh, dòng tiền có thể quay lại tiền gửi (cơ hội), nhưng người mua ở đỉnh bằng tiền vay gặp khó.
- Không đưa dự báo giá vàng; không khuyến nghị mua bán vàng (`guardrails.md` mục 10 và 20).
