---
id: EX-NW-04
used_by: [Propagation, Product-Impact, Inside-out Monitor, Critic]
steps: [1-6]
depends_on: [core/05_output_prose.md, outside_in/news/nw_03_gian_lan_an_ninh.md, core/06_ngan_hang.md]
load_when: Few-shot cho tin nhóm GL loại lừa đảo, gian lận xảy ra ở nước khác và có thể lan sang Việt Nam (kênh L14)
version: v3.0
updated: 2026-11-02
---

# Ví dụ tin GL – Làn sóng lừa đảo mới ở một nước trong khu vực

> Kịch bản giả định để minh họa cách suy luận, không phản ánh dữ liệu thực.

**Sự kiện được giao:** Cơ quan chức năng một nước trong khu vực cảnh báo làn sóng lừa đảo mới: kẻ gian mạo danh nhân viên giao hàng, gửi đường link để cài ứng dụng giả, chiếm quyền điều khiển điện thoại rồi chuyển tiền qua ứng dụng ngân hàng; tiền được chuyển tiếp qua nhiều tài khoản thuê mượn.

Một nước trong khu vực cảnh báo làn sóng lừa đảo mạo danh nhân viên giao hàng, dụ cài ứng dụng giả để chiếm quyền điều khiển điện thoại, rồi chuyển tiền qua nhiều tài khoản thuê mượn. Đây là tin nhóm gian lận và an ninh mạng (GL), gồm lừa đảo nhắm vào khách hàng (GL2) và rửa tiền qua tài khoản bị lợi dụng (GL1). Tin xảy ra ở nước khác và có thể truyền sang Việt Nam qua các kênh dùng chung (L14): chuyển khoản tức thời và ứng dụng ngân hàng trên điện thoại. Mẫu lan truyền là cá nhân trước (P2). Tâm lý chưa rõ, ô D. Khung thời gian là chuẩn bị trong tuần.

Đối tượng bị nhắm tới là khách hàng cá nhân hay mua sắm trực tuyến, đặc biệt người lớn tuổi ít quen công nghệ, và hộ kinh doanh bán hàng qua mạng thường xuyên nhận cuộc gọi giao hàng. Ở cấp ngân hàng, tài khoản do khách hàng mở có thể bị thuê, mượn để làm trung gian nhận tiền. Không thấy bên hưởng lợi.

Mua sắm trực tuyến, giao hàng tận nhà và chuyển khoản tức thời đều phổ biến ở Việt Nam, nên thủ đoạn có thể được áp dụng tại đây trong vài tuần đến vài tháng. Quy định xác thực sinh trắc học cho giao dịch giá trị lớn có thể làm phần chuyển tiền lớn khó hơn, nhưng kẻ gian thường chuyển sang dụ chính chủ thực hiện giao dịch; đây là giả thuyết cần theo dõi. Nếu thủ đoạn tới Việt Nam, tài khoản thuê mượn có khả năng cao là mắt xích của nó, nên rủi ro ngân hàng trở thành trung gian chuyển tiền lừa đảo là có thật.

Không thấy cơ hội.

Các sản phẩm và kênh có thể bị lợi dụng là ngân hàng số và tài khoản thanh toán cá nhân (CN-DIG-01, CN-ACC-01), tài khoản hộ kinh doanh (HKD-ACC-01); ở cấp ngân hàng là tài khoản bị lợi dụng (NH-FR-01), phòng chống rửa tiền (NH-CO-01) và danh tiếng (NH-RP-01).

Cần theo dõi đăng nhập kèm ứng dụng điều khiển từ xa hoặc thiết bị mới ngay trước giao dịch lớn (X03), tài khoản mới nhận tiền từ nhiều nguồn rồi chuyển đi nhanh (X01), báo lừa đảo theo cùng kịch bản "giao hàng" (X02), và khách phản ánh tin nhắn hoặc cuộc gọi mạo danh (X08). Cần đội an ninh thông tin và chống gian lận xác nhận: ứng dụng ngân hàng có nhận biết được ứng dụng điều khiển từ xa hoặc ứng dụng giả trên máy khách không, và quy trình tạm khóa tài khoản nhận tiền nghi vấn đang mất bao lâu.

Ngân hàng nên cảnh báo sớm qua kênh chính thức, mô tả dấu hiệu nhận biết ở mức đơn giản: không bấm đường link lạ, không cài ứng dụng ngoài kho ứng dụng chính thức. Đầu mối gợi ý: chống gian lận, phòng chống rửa tiền, truyền thông. Giả định yếu nhất là thủ đoạn sẽ tới Việt Nam; nếu ứng dụng ngân hàng đã chặn được ứng dụng điều khiển từ xa, nhánh chiếm quyền điện thoại sẽ yếu đi, nhưng nhánh tài khoản thuê mượn vẫn còn.

```
[FG] loai_tin=GL | o=D | tam_ly=chua_ro | huong=rui_ro | phan_khuc=KHCN,NH | muc=co_the
```
