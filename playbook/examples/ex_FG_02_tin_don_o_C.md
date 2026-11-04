---
id: EX-FG-02
used_by: [Propagation, Product-Impact, Critic]
steps: [1-6]
depends_on: [core/05_output_prose.md, fear_greed/fg_01_dual_lens.md]
load_when: Few-shot khi sự kiện gần như không có tác động cơ bản nhưng tâm lý sợ hãi lan rộng (ô C)
version: v3.0
updated: 2026-11-02
---

# Ví dụ Fear & Greed – Ô C: tin đồn thanh khoản ở một ngân hàng khác

> Kịch bản giả định để minh họa cách suy luận, không phản ánh dữ liệu thực.

**Sự kiện được giao:** Tin đồn về khả năng thanh khoản của một ngân hàng khác lan trên mạng xã hội. Tại một số tỉnh, người dân xếp hàng rút tiền ở các chi nhánh của ngân hàng đó.

Tin đồn về khả năng thanh khoản của một ngân hàng khác lan trên mạng xã hội, và tại một số tỉnh người dân xếp hàng rút tiền ở ngân hàng đó. Với Techcombank, đây là sự kiện outside-in, lan theo mẫu cá nhân trước (P2). Tác động cơ bản lên khách hàng của Techcombank gần như bằng không, nhưng tâm lý đã ở mức sợ hãi, nên đây là rủi ro do hành vi, nằm ở ô C.

Bên chịu tác động đầu tiên là người gửi tiền cá nhân tại các địa bàn có tin đồn: nỗi sợ có thể lan từ một ngân hàng sang cả hệ thống, kể cả với khách của Techcombank. Phía hưởng lợi, nếu có, là các ngân hàng được xem là an toàn hơn, vì một phần tiền rút ra sẽ tìm nơi gửi khác.

Nhánh rủi ro có khả năng cao là khách cá nhân ở cùng địa bàn rút tiền mặt hoặc tất toán sớm để phòng thân, ngay trong vài ngày đầu. Hộ kinh doanh có thể rút doanh thu về tiền mặt thay vì để trong tài khoản. Kẻ gian có khả năng cao lợi dụng nỗi sợ, gửi tin nhắn mạo danh ngân hàng mời "chuyển tiền sang tài khoản an toàn". Nếu hiện tượng rút tiền lan sang nhiều ngân hàng, nhà đầu tư có thể lo ngại cho toàn ngành (L10); đây mới là giả thuyết.

Về cơ hội, tiền rút ra từ ngân hàng bị đồn có thể chuyển sang tiền gửi tại các ngân hàng được xem là vững, trong đó có Techcombank (O2, O6). Đây là cơ hội có thật nhưng mang tính tiền nóng: khách chuyển đến vì sợ chứ không vì sản phẩm, nên dễ rời đi khi tâm lý ổn định lại hoặc khi nơi khác trả lãi cao hơn.

Ở phía rủi ro, sản phẩm cần chú ý là tiền gửi có kỳ hạn, chứng chỉ tiền gửi và tài khoản thanh toán (CN-DEP-01, CN-DEP-04, CN-ACC-01) với rủi ro thanh khoản; dịch vụ qua CDM (CN-PAY-02) với áp lực tiền mặt; và ngân hàng số (CN-DIG-01) với rủi ro lừa đảo. Ở phía cơ hội, nhu cầu có thể tăng ở chính các sản phẩm tiền gửi đó (O2), với điều kiện ngân hàng đón khách một cách chính đáng, không nhắc tới hay khai thác tin đồn về ngân hàng khác. Không nên đẩy bán sản phẩm đầu tư hay bảo hiểm cho khách đang hoảng sợ.

Để đánh giá, cần theo dõi rút tiền mặt qua CDM và tại quầy theo địa bàn (S07), chuyển tiền gửi hàng loạt sang ngân hàng khác (F01), chuyển từ kỳ hạn dài sang kỳ hạn ngắn (F02), và đăng nhập lạ, người thụ hưởng mới (S13). Ở phía cơ hội, cần xem tiền gửi mới có đến từ tài khoản ở ngân hàng bị đồn không và khách chọn kỳ hạn nào: kỳ hạn rất ngắn cho thấy đây là tiền nóng.

Ngân hàng dễ phản ứng theo hướng tham, như tăng lãi suất huy động để hút tiền; việc này có thể bị hiểu là chính mình cũng thiếu thanh khoản. Phản ứng hợp lý hơn là chuẩn bị tiền mặt ở các điểm giao dịch thuộc địa bàn có tin đồn và cảnh báo khách về lừa đảo mạo danh. Nhánh sợ hãi sẽ lan mạnh hơn nếu xuất hiện thêm tin đồn về một ngân hàng thứ hai. Giả định yếu nhất là khách của Techcombank ở địa bàn đó sẽ phản ứng giống khách của ngân hàng bị đồn; điều này cần kiểm tra bằng S07 ngay trong ngày đầu.

```
[FG] loai_tin=TT | o=C | tam_ly=so | huong=rui_ro | phan_khuc=KHCN | muc=co_kha_nang_cao
[FG] loai_tin=TT | o=C | tam_ly=so | huong=co_hoi | phan_khuc=KHCN | muc=co_the
```
