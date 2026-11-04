---
id: EX-NW-01
used_by: [Propagation, Product-Impact, Critic]
steps: [1-6]
depends_on: [core/05_output_prose.md, outside_in/news/nw_01_truc_tiep.md]
load_when: Few-shot cho tin nhóm TT gói nhiều kênh (xung đột quân sự, địa chính trị), có nhánh phụ GL
version: v3.0
updated: 2026-11-02
---

# Ví dụ tin TT – Xung đột quân sự tại Trung Đông: dầu, vàng, tỷ giá, vận tải

> Kịch bản giả định để minh họa cách suy luận, không phản ánh dữ liệu thực.

**Sự kiện được giao:** Xung đột quân sự leo thang tại Trung Đông liên quan Iran. Giá dầu và giá vàng thế giới tăng mạnh, USD mạnh lên; một số hãng tàu tạm tránh tuyến qua eo biển Hormuz.

Xung đột quân sự leo thang tại Trung Đông liên quan Iran, kéo giá dầu và giá vàng thế giới tăng mạnh, USD mạnh lên, và một số hãng tàu tạm tránh tuyến qua eo biển Hormuz. Đây là tin nhóm tác động trực tiếp (TT), có một nhánh phụ về an ninh mạng và lừa đảo (GL). Tin lan theo mẫu P3 vì chạm nhiều phân khúc cùng lúc qua giá thế giới. Sự kiện không mô tả hành vi đổ xô trong nước, nên tâm lý khách hàng chưa rõ: nhánh rủi ro nằm ở ô D, nhánh cơ hội ở ô A.

Bên thiệt đầu tiên là doanh nghiệp dùng nhiên liệu làm đầu vào (vận tải, hàng không, logistics, nhựa, thủy sản đánh bắt) và doanh nghiệp nhập khẩu thanh toán bằng USD. Bên lợi đầu tiên là doanh nghiệp khai thác, phân phối nhiên liệu và khách hàng cá nhân đang giữ vàng. Ở cấp ngân hàng, tác động đến ngay qua tỷ giá và dòng tiền gửi.

Về rủi ro, nhánh mạnh nhất là chi phí nhiên liệu: doanh nghiệp vận tải và hàng không có khả năng cao bị ép biên lợi nhuận trong vài tuần, kéo theo các đại lý bán vé trong chương trình tài trợ chuỗi (L03). Nhánh thứ hai là tỷ giá: doanh nghiệp nhập khẩu và doanh nghiệp có nợ USD có khả năng cao tăng chi phí, cần thêm vốn lưu động. Nhánh thứ ba là vận tải biển: nếu các hãng tàu tránh tuyến kéo dài, doanh nghiệp xuất nhập khẩu có thể bị chậm giao hàng và chậm thu tiền sau một đến hai tháng. Với khách hàng cá nhân, giá xăng và hàng hóa tăng có thể làm chi tiêu co lại, kéo doanh thu của hộ kinh doanh xuống (L06). Ở cấp ngân hàng, giá vàng tăng có thể kéo một phần tiền gửi sang vàng.

Về cơ hội, doanh nghiệp năng lượng có thể cần thêm vốn lưu động và tài trợ nhập khẩu; doanh nghiệp xuất khẩu có doanh thu quy đổi tăng khi USD mạnh. Biến động tỷ giá làm nhu cầu phòng ngừa tăng, nhưng chỉ là cơ hội khi gắn với hợp đồng thương mại thật.

Ở phía rủi ro, sản phẩm cần chú ý là vay vốn lưu động và tài trợ đại lý bán vé (CIB-LN-01, CIB-SCF-01), L/C nhập khẩu và giao dịch ngoại tệ (CIB-TF-01, CIB-FX-01, SME-PAY-04), vay của SME và hộ kinh doanh vận tải (SME-LN-01, HKD-LN-01); ở cấp ngân hàng là huy động (NH-LQ-01) và trạng thái ngoại tệ (NH-MR-01). Ở phía cơ hội, nhu cầu có thể tăng ở vốn lưu động cho doanh nghiệp năng lượng (CIB-LN-01, O1), phái sinh tỷ giá để phòng ngừa (CIB-CM-02, O3) và tiền gửi từ khách chốt lời vàng (CN-DEP-01, O2). Các giao dịch liên quan khu vực xung đột cần rà soát trừng phạt (NH-CO-01).

Cần kiểm tra nhu cầu mua USD và L/C nhập khẩu của doanh nghiệp, mức sử dụng hạn mức của doanh nghiệp vận tải và hàng không, tất toán tiết kiệm và rút tiền mặt tăng theo giá vàng (G02, S07), và giao dịch chuyển tiền đi khu vực xung đột. Với nhánh an ninh mạng, cần theo dõi tin nhắn mạo danh và lừa đảo quyên góp (X02, X08). Chưa có số liệu dư nợ theo ngành, cần truy vấn nội bộ.

Ngân hàng dễ phản ứng theo hướng sợ: siết đồng loạt ngành vận tải, kể cả khách đã phòng ngừa giá nhiên liệu. Cơ hội sẽ đảo thành rủi ro nếu xung đột hạ nhiệt và giá dầu, giá vàng quay đầu nhanh; khi đó khách mua vàng ở đỉnh bằng tiền vay chịu lỗ. Nhánh tấn công mạng đi kèm xung đột mới là giả thuyết. Giả định yếu nhất là độ dài của xung đột: sự kiện không nêu, nên mức độ nhánh vận tải biển cần cập nhật theo diễn biến.

```
[FG] loai_tin=TT | o=D | tam_ly=chua_ro | huong=rui_ro | phan_khuc=CIB,SME,KHCN,NH | muc=co_kha_nang_cao
[FG] loai_tin=TT | o=A | tam_ly=chua_ro | huong=co_hoi | phan_khuc=CIB,KHCN | muc=co_the
[FG] loai_tin=GL | o=D | tam_ly=chua_ro | huong=rui_ro | phan_khuc=KHCN,NH | muc=gia_thuyet
```
