---
id: FG-OPPORTUNITY-MAP
used_by: [Product-Impact, Critic]
steps: [3]
depends_on: [fear_greed/fg_01_dual_lens.md, segments/, core/06_ngan_hang.md]
load_when: Bước 3 – khi có phân khúc hưởng lợi; tra sản phẩm có nhu cầu tăng theo đúng phân khúc trên đường lan truyền
version: v3.0
updated: 2026-11-02
---

# Bản đồ cơ hội theo phân khúc

Ba phân khúc: KHCN (nhóm cá nhân và nhóm hộ kinh doanh), SME, doanh nghiệp lớn (CIB), cộng thêm cấp ngân hàng. Mã sản phẩm dùng lại từ bảng (c) của các file phân khúc. Mã loại cơ hội `O1`–`O6` xem `fear_greed/fg_01_dual_lens.md`. Mỗi dòng có **điều kiện đủ chuẩn**: chỉ coi là cơ hội khi điều kiện này thỏa. Cột **mặt trái** là rủi ro khi cơ hội chuyển sang ô B hoặc đảo chiều.

## KHCN – nhóm cá nhân
| Khi nào hưởng lợi | Sản phẩm | Cơ hội | Điều kiện đủ chuẩn | Mặt trái |
|---|---|---|---|---|
| Thu nhập tăng (ngành tăng trưởng, thêm ca, thưởng) – qua `L02` | `CN-ACC-01` `CN-ACC-03` `CN-DEP-02` `CN-CARD-01` | `O2` `O1` | Thu nhập tăng qua nhiều kỳ lương, không chỉ một khoản thưởng | Chi tiêu theo thu nhập đỉnh; dư nợ thẻ tăng |
| Giá tài sản đang nắm giữ tăng (BĐS, nông sản, cổ phiếu) | `CN-INV-01` `CN-INV-02*` `CN-INS-02` `CN-DEP-01` | `O4` `O2` | Có tiền nhàn rỗi thật; sản phẩm phù hợp khẩu vị rủi ro | Mua ở đỉnh; tư vấn sai đối tượng `RP` |
| Nhận khoản tiền lớn một lần (bán nông sản, đền bù, bán BĐS) | `CN-DEP-01` `CN-DEP-04` `CN-ACC-03` | `O2` `O4` | Nguồn tiền rõ ràng | AML nguồn tiền `CO`; đầu tư theo phong trào |
| Nhu cầu mua nhà, xe khi lãi suất giảm hoặc thu nhập tăng | `CN-LN-01` `CN-LN-02` `CN-LN-03` `CN-LN-04` `CN-LN-08` | `O1` | Khả năng trả nợ tính theo lãi suất **sau** thời gian ưu đãi | Hết ưu đãi lãi suất; định giá TSBĐ theo giá sốt (`G04`) |
| Đi lại, du học, kiều hối tăng | `CN-PAY-01` `CN-ACC-02` `CN-CARD-01` `CN-INS-03` | `O3` `O4` | Nhu cầu gắn với mục đích thật | Rủi ro tỷ giá; gian lận thẻ ở nước ngoài |
| Sau biến cố sức khỏe, thiên tai (nhu cầu bảo vệ tăng) | `CN-INS-01` `CN-INS-03` | `O4` | Tư vấn đúng nhu cầu, không bán lúc khách đang hoảng sợ | Khiếu nại tư vấn sai, hủy hợp đồng sớm `S09` |
| Tiền gửi tìm nơi an toàn (tin xấu ở tổ chức khác) | `CN-DEP-01` `CN-ACC-01` `CN-DEP-04` | `O2` `O6` | Ngân hàng chủ động đón, không lôi kéo bằng tin đồn | Tiền nóng, rút đi nhanh khi lãi suất nơi khác cao hơn |

## KHCN – nhóm hộ kinh doanh
| Khi nào hưởng lợi | Sản phẩm | Cơ hội | Điều kiện đủ chuẩn | Mặt trái |
|---|---|---|---|---|
| Sức mua địa phương tăng – qua `L06` | `HKD-REV-01` `HKD-REV-02` `HKD-REV-03` `HKD-ACC-01` | `O3` `O2` | Doanh thu QR và unique payers tăng ít nhất 2–3 tháng | Mùa vụ; doanh thu đỉnh không đại diện cả năm |
| Cần vốn nhập hàng, mở rộng cửa hàng | `HKD-LN-01` `HKD-LN-02` `HKD-LN-03` `HKD-CARD-01` | `O1` `O3` | Hạn mức theo doanh thu bình quân, không theo tháng đỉnh | `G05`: xin hạn mức theo giá đỉnh |
| Thuế, hóa đơn mới đẩy HKD minh bạch doanh thu hoặc chuyển lên DN – qua `L07` | `HKD-ACC-01` `HKD-REV-02` → `SME-ACC-01` `SME-PKG-01` `SME-DIG-01` | `O2` `O3` `O6` | HKD có doanh thu ổn định, muốn chuyển đổi | Chi phí tuân thủ tăng, một số hộ ngừng kinh doanh |
| Chủ hộ có lãi (nút lai với KHCN) | Sản phẩm KHCN: `CN-DEP-01` `CN-INV-*` `CN-INS-02` | `O2` `O4` | Tách bạch tiền kinh doanh và tiền cá nhân | Rút vốn kinh doanh để đầu tư theo phong trào |

## SME – Doanh nghiệp vừa và nhỏ
| Khi nào hưởng lợi | Sản phẩm | Cơ hội | Điều kiện đủ chuẩn | Mặt trái |
|---|---|---|---|---|
| Đơn hàng tăng từ DN đầu chuỗi hoặc xuất khẩu – qua `L03` `L08` | `SME-LN-01` `SME-LN-02` `SME-LN-03` `SME-PAY-04` | `O1` `O3` | Đơn hàng có hợp đồng, dòng tiền về tài khoản thật | Phụ thuộc một khách hàng lớn |
| Thắng thầu, đầu tư công giải ngân nhanh – qua `L12` | `SME-GTE-01` `SME-LN-*` | `O3` `O1` `O5` | Năng lực thi công tương xứng số gói thầu | Nhận vượt năng lực → bị gọi bảo lãnh |
| Bán lẻ tăng | `SME-PKG-02` `SME-REV-01` `SME-ACC-01` | `O3` `O2` | Doanh thu qua thiết bị tăng đều | Gian lận thẻ tại điểm bán |
| Tăng tuyển dụng | `SME-PAY-06` → tài khoản lương nhân viên `CN-ACC-01` | `O2` | Lô lương tăng người `S01` | – |
| Dư tiền tạm thời | `SME-DEP-01` `SME-DEP-02` | `O2` | – | Rút nhanh khi cần vốn lưu động |
| DN mới thành lập, HKD chuyển đổi | `SME-ACC-01` `SME-PKG-01` `SME-DIG-01` | `O6` | – | Lịch sử tín dụng ngắn; dữ liệu kế toán chưa đủ tin cậy |

## CIB – Doanh nghiệp lớn
| Khi nào hưởng lợi | Sản phẩm | Cơ hội | Điều kiện đủ chuẩn | Mặt trái |
|---|---|---|---|---|
| Giá hàng hóa xuất khẩu tăng, đơn hàng xuất khẩu tăng – qua `L08` | `CIB-TF-02` `CIB-FX-01` `CIB-LN-01` `CIB-CM-02` | `O1` `O3` | Hợp đồng bán đã ký giá mới; không kẹt hợp đồng kỳ hạn giá cũ | Hợp đồng bán kỳ hạn giá thấp; tập trung vào ngành đang nóng |
| Mở rộng đầu tư, FDI vào | `CIB-ACC-02` `CIB-TF-01` `CIB-LN-02` `CIB-PAY-06` | `O1` `O3` `O2` | Dự án có pháp lý, vốn đối ứng | Chậm tiến độ; rủi ro tỷ giá với nợ ngoại tệ |
| DN đầu chuỗi tăng trưởng – qua `L03` | `CIB-SCF-01` `CIB-COL-01` | `O1` cho cả chuỗi, `O3` | Anchor ổn định, chính sách đại lý không đổi | Cả chuỗi cùng chịu khi anchor đảo chiều |
| Lãi suất, tỷ giá biến động (khách cần phòng ngừa) | `CIB-CM-01` `CIB-CM-02` `CIB-FX-01` | `O3` | Gắn với nhu cầu phòng ngừa thực | `G06`: đầu cơ thay vì phòng ngừa |
| Dư tiền, nhu cầu tiền gửi xanh | `CIB-DEP-01` | `O2` | – | Tiền gửi lớn rút đột ngột |
| Thị trường vốn thuận lợi | `CIB-INV-01` | `O3` | Tổ chức phát hành đủ chuẩn | Phân phối lại cho KHCN qua iBond `L05` → `RP` nếu bán sai đối tượng |

## Cấp ngân hàng (không phải phân khúc)
Chi tiết cơ hội ở cấp ngân hàng xem `core/06_ngan_hang.md` mục (c). Thường ít và không ép.

| Khi nào hưởng lợi | Kênh | Cơ hội | Ghi chú | Mặt trái |
|---|---|---|---|---|
| Nhiều phân khúc cùng ở ô A, chất lượng tài sản cải thiện | `IR-EQ-01` `IR-RT-01` | Chi phí vốn giảm → lãi suất cạnh tranh hơn cho mọi phân khúc (inside-out tích cực) | Chỉ ghi nhận, không khuyến nghị đầu tư | Kỳ vọng tăng trưởng cao tạo áp lực chạy chỉ tiêu (ngân hàng tham) |
| Hệ sinh thái tăng trưởng (chứng khoán, quỹ, bảo hiểm) – qua `L11` | `IR-ECO-01` | Thu nhập dịch vụ tăng | – | Sự cố ở công ty con lan danh tiếng về ngân hàng mẹ |
