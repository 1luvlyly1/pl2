---
id: EX-FG-03
used_by: [Propagation, Product-Impact, Critic]
steps: [1-6]
depends_on: [core/05_output_prose.md, fear_greed/fg_01_dual_lens.md]
load_when: Few-shot khi sự kiện vĩ mô có lợi cho nhiều phân khúc, vừa có nhu cầu thật (ô A) vừa có phong trào đầu cơ (ô B)
version: v3.0
updated: 2026-11-02
---

# Ví dụ Fear & Greed – Ô A và B: lãi suất giảm, chứng khoán tăng nóng

> Kịch bản giả định để minh họa cách suy luận, không phản ánh dữ liệu thực.

**Sự kiện được giao:** Lãi suất cho vay giảm mạnh. Thị trường chứng khoán tăng nóng, số tài khoản chứng khoán mở mới lập kỷ lục.

Lãi suất cho vay giảm mạnh, cùng lúc thị trường chứng khoán tăng nóng và số tài khoản chứng khoán mở mới lập kỷ lục. Đây là sự kiện outside-in, tác động cùng lúc tới mọi phân khúc nên lan theo mẫu toàn hệ thống (P3). Tâm lý là tham lam, thể hiện qua cụm "tăng nóng" và "lập kỷ lục". Nhu cầu vay để mua nhà, mở rộng sản xuất nằm ở ô A; dòng tiền đổ vào chứng khoán theo phong trào nằm ở ô B.

Bên hưởng lợi đầu tiên là người đi vay và doanh nghiệp có kế hoạch đầu tư, vì chi phí vốn giảm, cùng nhà đầu tư cá nhân đang nắm cổ phiếu, chứng chỉ quỹ. Bên chịu thiệt là người gửi tiết kiệm, nếu lãi suất tiền gửi giảm theo, và phía ngân hàng là nguồn tiền gửi có thể chảy sang chứng khoán.

Về rủi ro, nhánh có khả năng cao nhất là tiền gửi thanh toán và tiết kiệm chuyển sang tài khoản chứng khoán trong vài tuần, làm giảm huy động. Nhánh thứ hai là vay sai mục đích: khoản vay tiêu dùng, thấu chi có thể được dùng để mua cổ phiếu, và nếu thị trường điều chỉnh, các khoản này có thể trễ hạn sau vài tháng. Nhánh thứ ba là lừa đảo đầu tư, có khả năng cao tăng theo làn sóng nhà đầu tư mới, qua các nhóm "phím hàng" và ứng dụng không được cấp phép.

Về cơ hội, nhu cầu vay mua nhà và mua ô tô có khả năng cao tăng khi lãi suất giảm; doanh nghiệp có thể đẩy nhanh vay trung dài hạn cho dự án. Khách có lãi từ chứng khoán có thể quan tâm tới chứng chỉ quỹ thay vì tự đầu tư, và hệ sinh thái chứng khoán, quản lý quỹ có thể tăng thu nhập dịch vụ (L11). Phần nhu cầu đến từ phong trào thuộc ô B: tăng nhanh nhưng dễ đảo chiều.

Ở phía rủi ro, sản phẩm cần chú ý là tiền gửi và Sinh lời tự động (CN-DEP-01, CN-ACC-03) với rủi ro thanh khoản; vay tiêu dùng tín chấp và MyCash (CN-LN-06, CN-LN-05) với rủi ro sai mục đích; ngân hàng số (CN-DIG-01) với lừa đảo; và quỹ cổ phiếu TCEF, TCFIN (CN-INV-02b, CN-INV-02c) với rủi ro khiếu nại nếu khách mua ở đỉnh. Ở phía cơ hội, nhu cầu có thể tăng ở vay mua nhà và ô tô (CN-LN-02, CN-LN-04; O1), với điều kiện tính khả năng trả nợ theo lãi suất sau ưu đãi; vay trung dài hạn theo dự án (CIB-LN-02, O1); và chứng chỉ quỹ (CN-INV-02, O4), với điều kiện đánh giá khẩu vị rủi ro.

Để xác nhận và theo dõi, cần xem dòng tiền từ tài khoản thanh toán và tiết kiệm sang công ty chứng khoán; tiền giải ngân vay tiêu dùng chuyển ngay sang tài khoản chứng khoán (G01); tất toán tiết kiệm để mua cổ phiếu (G02); mua dồn quỹ cổ phiếu một ngành (G03); và giao dịch tới ứng dụng đầu tư không phép (G07). Ở phía cơ hội, cần xem số hồ sơ vay mua nhà mới và tỷ lệ phê duyệt.

Ngân hàng dễ phản ứng theo hướng tham: ưu đãi lãi suất sâu để giành khách vay mua nhà và đẩy chỉ tiêu bán chứng chỉ quỹ cổ phiếu. Cả hai đều tạo rủi ro khi thị trường điều chỉnh. Cơ hội sẽ đảo thành rủi ro nếu lãi suất tăng trở lại hoặc thị trường chứng khoán giảm mạnh; khi đó các nhánh ở ô B chuyển thẳng sang ô C. Giả định yếu nhất là lãi suất tiền gửi giảm theo lãi suất cho vay; sự kiện không nêu rõ điều này.

```
[FG] loai_tin=TT | o=A | tam_ly=binh_thuong | huong=co_hoi | phan_khuc=KHCN,CIB | muc=co_kha_nang_cao
[FG] loai_tin=TT | o=B | tam_ly=tham | huong=ca_hai | phan_khuc=KHCN | muc=co_kha_nang_cao
```
