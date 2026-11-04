---
id: NEWS-FRAUD-CYBER
used_by: [Propagation, Product-Impact, Inside-out Monitor, Critic]
steps: [1, 2, 3, 4, 5, 6]
depends_on: [outside_in/news/nw_00_router.md, core/06_ngan_hang.md]
load_when: Tin nhóm GL – thủ đoạn gian lận ở nước khác, làn sóng lừa đảo, rửa tiền, lỗ hổng CVE, ransomware, tấn công chuỗi cung ứng phần mềm, rò rỉ dữ liệu
version: v3.0
updated: 2026-11-02
---

# Tin gian lận, lừa đảo, an ninh mạng (GL)

## 1. Khác các nhóm khác ở đâu
- Không lan theo dòng tiền mà lan theo **bề mặt tấn công**: kênh thanh toán, thiết bị, phần mềm, con người có thể bị lợi dụng.
- Nhanh: vài giờ đến vài tuần.
- Thường **không có cơ hội**. Viết rõ "không thấy cơ hội" thay vì ép ra.
- Agent **không biết** ngân hàng đang dùng phần mềm, phiên bản, đối tác nào. Mọi kết luận về việc ngân hàng có bị ảnh hưởng hay không đều phải ghi là **cần đội an ninh thông tin xác nhận**.

## 2. Bốn loại
| Mã | Loại | Ví dụ |
|---|---|---|
| `GL1` | Gian lận tài chính, rửa tiền | Tài khoản bị thuê, mượn để nhận tiền lừa đảo; gian lận thẻ; gian lận chứng từ thương mại; rửa tiền qua thương mại |
| `GL2` | Lừa đảo nhắm vào khách hàng | Mạo danh ngân hàng, cơ quan nhà nước; lừa đầu tư, việc làm, tình cảm; ứng dụng giả chiếm quyền điều khiển điện thoại |
| `GL3` | Lỗ hổng, tấn công kỹ thuật | Lỗ hổng CVE trong hệ điều hành, thư viện, thiết bị thanh toán; ransomware; tấn công qua nhà cung cấp phần mềm; tấn công từ chối dịch vụ |
| `GL4` | Rò rỉ dữ liệu | Dữ liệu khách hàng lộ ở ngân hàng, đối tác hoặc doanh nghiệp khác, rồi bị dùng để lừa đảo có chủ đích |

## 3. Năm câu hỏi phạm vi áp dụng
Đây là bước thay cho "lan truyền" ở các nhóm khác.

1. **Thủ đoạn hoặc lỗ hổng dựa vào kênh, thành phần nào?** Chuyển khoản nhanh, QR, thẻ, ví điện tử, ứng dụng ngân hàng, mã OTP, xác thực sinh trắc học, chữ ký số, email doanh nghiệp, thiết bị POS, hệ điều hành điện thoại, một phần mềm hoặc thư viện cụ thể.
2. **Kênh, thành phần đó có xuất hiện ở đâu?** Hệ thống ngân hàng (`NH-OR-01` `NH-OR-02`), đối tác công nghệ (`NH-OR-03`, kênh `L13`), thiết bị của khách hàng, hay quy trình của doanh nghiệp khách hàng. Không biết thì ghi "cần xác nhận", **không giả định** có hay không.
3. **Điều kiện để thủ đoạn thành công có ở Việt Nam không?** Ví dụ quy định xác thực sinh trắc học cho giao dịch giá trị lớn có thể làm một số thủ đoạn khó hơn, nhưng kẻ gian thường chuyển sang lừa chính chủ thực hiện giao dịch.
4. **Mức độ nghiêm trọng theo nội dung tin:** đã bị khai thác thực tế chưa, đã có bản vá chưa, mức nghiêm trọng được công bố. Chỉ dùng thông tin có trong sự kiện.
5. **Độ trễ tới Việt Nam** (thủ đoạn ở nước khác, kênh `L14`): thường có độ trễ, mức chắc chắn mặc định "có thể". Kênh càng giống nhau (chuyển khoản tức thời, QR) thì độ trễ càng ngắn.

## 4. Bề mặt tiếp xúc theo phân khúc
| Đối tượng | Thủ đoạn thường gặp | Sản phẩm, kênh bị lợi dụng | Rủi ro |
|---|---|---|---|
| KHCN – cá nhân | Mạo danh, ứng dụng giả, lừa đầu tư, chiếm đoạt tài khoản | `CN-DIG-01` `CN-ACC-01` `CN-CARD-01` `CN-CARD-02` `CN-PAY-01` | `FR` `RP` |
| KHCN – hộ kinh doanh | Mã QR bị dán đè, mạo danh cơ quan thuế hoặc ngân hàng, gian lận thẻ tại điểm bán | `HKD-REV-01` `HKD-REV-02` `HKD-REV-03` `HKD-ACC-01` | `FR` `OR` |
| SME | Email giả đối tác đổi số tài khoản nhận tiền, chiếm đoạt chữ ký số, hóa đơn giả | `SME-DIG-01` `SME-PAY-01` `SME-PAY-07` | `FR` |
| DN lớn | Email giả giá trị lớn, gian lận chứng từ L/C, rửa tiền qua thương mại, ransomware tại DN làm gián đoạn chi lương | `CIB-DIG-01` `CIB-PAY-02` `CIB-TF-*` `CIB-PAY-06` | `FR` `CO` `OR` |
| Cấp ngân hàng | Lỗ hổng trong hệ thống hoặc đối tác, tài khoản bị lợi dụng, tấn công từ chối dịch vụ, rò rỉ dữ liệu | `NH-OR-01` `NH-OR-02` `NH-OR-03` `NH-FR-01` `NH-CO-02` | `OR` `FR` `CO` `RP` |

## 5. Tín hiệu nội bộ X01–X08
| ID | Tín hiệu | Báo trước điều gì |
|---|---|---|
| `X01` | Tài khoản mới mở nhận tiền từ nhiều nguồn rồi chuyển đi trong thời gian ngắn | Tài khoản bị lợi dụng làm trung gian (`NH-FR-01`) |
| `X02` | Báo lừa đảo, tra soát, yêu cầu hoàn tiền tăng đột biến theo cùng một kịch bản | Thủ đoạn mới đang lan |
| `X03` | Đăng nhập từ thiết bị đã bị can thiệp hệ thống, có ứng dụng điều khiển từ xa, hoặc thiết bị mới ngay trước giao dịch lớn | Chiếm đoạt tài khoản (`GL2`) |
| `X04` | DN đổi thông tin người thụ hưởng ngay trước kỳ thanh toán lớn | Email giả đối tác (`GL2`) |
| `X05` | Giao dịch thẻ bất thường theo cụm điểm bán hoặc cùng dải số thẻ | Gian lận thẻ, lộ dữ liệu thẻ |
| `X06` | Chứng từ thương mại bất thường hoặc nghi trùng lặp | Gian lận tài trợ thương mại (`GL1`) |
| `X07` | Lưu lượng truy cập bất thường, lỗi xác thực tăng trên kênh số | Dấu hiệu tấn công (`GL3`) |
| `X08` | Đối tác công nghệ thông báo sự cố, hoặc khách phản ánh tin nhắn mạo danh ngân hàng | Sự cố bên thứ ba, chiến dịch mạo danh |

Dùng kèm `S13` (đăng nhập lạ, người thụ hưởng mới), `S14` (khiếu nại theo chủ đề), `G07` (giao dịch tới ứng dụng đầu tư không phép).

## 6. Cơ hội
- Thường không có. Ghi "không thấy cơ hội".
- Có thể ghi: cảnh báo sớm và rõ ràng giúp **giữ niềm tin** của khách; đây là việc cần làm, không phải cơ hội bán hàng.
- Nhu cầu sản phẩm bảo vệ (ví dụ bảo hiểm rủi ro an ninh mạng) chưa có trong danh mục playbook → ghi "sản phẩm chưa có trong danh mục".
- **Không** coi sự cố của ngân hàng khác là cơ hội quảng bá (`guardrails.md` mục 13).

## 7. Quy tắc an toàn khi viết
- Chỉ mô tả ở **mức nhận diện**: loại thủ đoạn, kênh bị lợi dụng, đối tượng bị nhắm tới.
- **Không** mô tả cách khai thác lỗ hổng, các bước thực hiện thủ đoạn, mã khai thác, hay bất cứ chi tiết nào giúp kẻ gian làm theo.
- **Không** kết luận hệ thống ngân hàng "bị ảnh hưởng" hay "an toàn" khi chưa có xác nhận.
- Nêu **khung thời gian cần hành động** (trong vài giờ, trong ngày, trong tuần) và **đầu mối gợi ý**: an ninh thông tin, chống gian lận, phòng chống rửa tiền, truyền thông, pháp chế.

## 8. Bố cục bài viết cho tin GL
Giữ 7 đoạn của `core/05_output_prose.md`, nhưng:
- Đoạn 3 (Fear): bề mặt tấn công và đối tượng bị nhắm tới, thay cho chuỗi lan truyền dòng tiền.
- Đoạn 4 (Greed): thường một câu "không thấy cơ hội".
- Đoạn 5: sản phẩm, kênh bị lợi dụng.
- Đoạn 6: tín hiệu `X` cần theo dõi **và danh sách điều cần đội an ninh xác nhận**.
- Đoạn 7: phản ứng của ngân hàng (cảnh báo khách rõ ràng, không mơ hồ), khung thời gian hành động, giả định yếu nhất.
- Ô ma trận thường là `D`; là `C` khi sự kiện cho thấy khách hàng đang hoảng sợ hàng loạt.

Bài mẫu: `examples/ex_NW_03_lo_hong_cve.md`, `examples/ex_NW_04_lua_dao_nuoc_ngoai.md`.
