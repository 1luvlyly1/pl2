---
id: EX-FG-01
used_by: [Propagation, Product-Impact, Critic]
steps: [1-6]
depends_on: [core/05_output_prose.md, fear_greed/fg_01_dual_lens.md]
load_when: Few-shot khi sự kiện có lợi cho một nhóm và hại cho nhóm khác, kèm hành vi tham lam (ô B)
version: v3.0
updated: 2026-11-02
---

# Ví dụ Fear & Greed – Ô B: giá cà phê lập đỉnh, người trồng đổ xô trữ hàng

> Kịch bản giả định để minh họa cách suy luận, không phản ánh dữ liệu thực.

**Sự kiện được giao:** Giá cà phê Robusta lập đỉnh mới. Tại nhiều vùng trồng, nông dân và đại lý đổ xô trữ hàng chờ giá lên thêm và mở rộng diện tích.

Giá cà phê Robusta lập đỉnh, và tại nhiều vùng trồng, nông dân và đại lý đổ xô trữ hàng, mở rộng diện tích. Đây là sự kiện outside-in, chạm cùng lúc doanh nghiệp xuất khẩu và người trồng, nên lan theo cả hai mẫu P1 và P2. Sự kiện mô tả rõ hành vi đổ xô, nên tâm lý ở phía người trồng là tham lam: nhánh hưởng lợi nằm ở ô B (cơ hội nóng), còn nhánh bị thiệt nằm ở ô D.

Bên hưởng lợi đầu tiên là doanh nghiệp xuất khẩu, đại lý thu mua và nông hộ, vì doanh thu và thu nhập vụ tăng. Bên thiệt đầu tiên là doanh nghiệp rang xay trong nước và các quán cà phê, vì giá đầu vào tăng nhanh hơn giá bán. Ngay trong nhóm xuất khẩu cũng có bên thiệt: doanh nghiệp đã ký bán kỳ hạn ở giá thấp nhưng nay phải thu mua ở giá cao.

Về rủi ro, nhánh đáng lo nhất là doanh nghiệp xuất khẩu kẹt hợp đồng giá cũ. Họ có khả năng cao thiếu vốn lưu động và có thể phải phá hợp đồng, kéo theo rủi ro với L/C xuất khẩu. Nhánh thứ hai là doanh nghiệp rang xay và hộ kinh doanh quán cà phê: biên lợi nhuận có thể giảm trong một đến ba tháng. Nhánh thứ ba nằm ẩn ngay trong phía hưởng lợi: các khoản vay để trữ hàng và mở rộng diện tích ở giá đỉnh là giả thuyết rủi ro cho một đến hai vụ sau, nếu giá quay đầu.

Về cơ hội, doanh nghiệp xuất khẩu đã có hợp đồng giá mới cần thêm vốn lưu động để thu mua, cần tài trợ xuất khẩu và bán ngoại tệ; nhu cầu này có khả năng cao tăng ngay trong vụ. Tiền về tay nông hộ và chủ đại lý có khả năng cao làm tiền gửi tăng (L01), và có thể lan sang hộ kinh doanh địa phương qua chi tiêu (L06) sau một đến ba tháng. Tuy vậy, một phần nhu cầu vay mới đến từ việc trữ hàng chờ giá, tức là đầu cơ chứ không phải nhu cầu sản xuất thật.

Ở phía rủi ro, sản phẩm cần chú ý là L/C xuất khẩu và vay vốn lưu động của doanh nghiệp kẹt giá cũ (CIB-TF-02, CIB-LN-01), ShopCash của quán cà phê (HKD-LN-01), và các khoản vay của đại lý, nông hộ dùng để trữ hàng (HKD-LN-02, CN-LN-08). Ở phía cơ hội, nhu cầu có thể tăng ở vốn lưu động, tài trợ xuất khẩu và ngoại tệ cho doanh nghiệp có hợp đồng giá mới (CIB-LN-01, CIB-TF-02, CIB-FX-01; O1, O3); tiền gửi và Sinh lời tự động cho nông hộ (CN-DEP-01, CN-ACC-03; O2); và ở mức có thể, chứng chỉ quỹ cho chủ đại lý có tiền nhàn rỗi (CN-INV-02, O4), với điều kiện tư vấn phù hợp khẩu vị rủi ro.

Để xác nhận cơ hội, cần xem L/C xuất khẩu và lượng USD bán cho ngân hàng của doanh nghiệp ngành cà phê, cùng tiền gửi mới tại các tỉnh trồng cà phê. Để biết cơ hội đã thành nóng, cần theo dõi hồ sơ xin tăng hạn mức gấp nhiều lần doanh thu bình quân (G05) và tiền vay chuyển sang mua đất, đặt cọc mở rộng diện tích (G01). Chưa có số liệu dư nợ theo ngành, cần truy vấn nội bộ.

Ngân hàng dễ phản ứng theo hướng tham: định hạn mức và giá trị hàng tồn kho làm tài sản bảo đảm theo giá đỉnh. Nên dùng giá bình quân nhiều vụ. Cơ hội sẽ đảo thành rủi ro nếu giá quay đầu khi nguồn cung từ các nước sản xuất khác phục hồi. Giả định yếu nhất là tỷ lệ doanh nghiệp kẹt hợp đồng giá cũ; sự kiện không nêu, nên mức độ của nhánh rủi ro này cần kiểm tra trực tiếp.

```
[FG] loai_tin=TT | o=B | tam_ly=tham | huong=co_hoi | phan_khuc=KHCN,CIB | muc=co_kha_nang_cao
[FG] loai_tin=TT | o=D | tam_ly=chua_ro | huong=rui_ro | phan_khuc=KHCN,SME,CIB | muc=co_the
```
