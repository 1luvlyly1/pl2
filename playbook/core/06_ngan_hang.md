---
id: CORE-BANK-LEVEL
used_by: [Propagation, Product-Impact, Inside-out Monitor, Critic, What-if]
steps: [1, 2, 3, 4]
depends_on: [core/01_risk_codes.md, core/03_linkage_graph.md]
load_when: Sự kiện chạm thẳng hoạt động của ngân hàng (thanh khoản, tỷ giá, hệ thống, lỗ hổng phần mềm, gian lận, tuân thủ, danh tiếng, nhà đầu tư), hoặc rủi ro của nhiều khách hàng cộng dồn lên cấp ngân hàng qua kênh L10
version: v3.4
updated: 2026-11-04
---

# Cấp ngân hàng

Cấp ngân hàng **không phải một phân khúc khách hàng**. Đây là nơi ghi các tác động lên hoạt động của chính ngân hàng. Nhiều tin outside-in chạm ngân hàng trước khi chạm khách hàng, hoặc chạm cùng lúc: lỗ hổng phần mềm, làn sóng lừa đảo, cú sốc tỷ giá, giá vàng tăng nóng kéo tiền gửi đi. Sự kiện inside-out (sự cố hệ thống, quyết định chính sách) cũng thường bắt đầu từ đây.

Mã `NH-` là **năng lực, hệ thống hoặc chỉ tiêu** của ngân hàng, không phải sản phẩm bán cho khách. Mã `IR-` là quan hệ nhà đầu tư và xếp hạng tín nhiệm. Trong dòng nhãn `[FG]`, cấp ngân hàng ghi `NH`; chỉ số của cấp này tính riêng, không cộng vào chỉ số của từng phân khúc.

## (a) Sáu đường tác động trực tiếp
| Đường | Chạm vào gì | Loại tin thường gặp | Cơ chế |
|---|---|---|---|
| Thanh khoản và huy động | Tiền gửi, CASA, tiền mặt tại chi nhánh và CDM | Giá vàng, chứng khoán tăng nóng; tin đồn về ngân hàng; đối thủ tăng lãi suất huy động | Khách rút tiền để đầu tư nơi khác hoặc vì lo sợ; tiền gửi chuyển sang kỳ hạn ngắn, chi phí vốn tăng |
| Thị trường | Trạng thái ngoại tệ, lãi suất, danh mục đầu tư của ngân hàng | Xung đột, giá dầu, quyết định lãi suất của Fed, USD mạnh | Nhu cầu mua ngoại tệ của DN nhập khẩu tăng; giá trái phiếu ngân hàng nắm giữ giảm khi lãi suất tăng |
| Hệ thống và công nghệ | Ngân hàng số, core banking, thẻ, POS, đối tác công nghệ | Lỗ hổng phần mềm, mã độc tống tiền, sự cố nhà cung cấp, sự cố hạ tầng | Gián đoạn chạm mọi phân khúc cùng lúc; lỗ hổng bị khai thác dẫn tới gian lận |
| Gian lận và tuân thủ | Tài khoản bị lợi dụng, phòng chống rửa tiền, trừng phạt | Làn sóng lừa đảo, thủ đoạn mới ở nước khác, danh sách trừng phạt mới | Tài khoản của ngân hàng trở thành mắt xích chuyển tiền lừa đảo; giao dịch với đối tác bị trừng phạt bị chặn |
| Danh tiếng và nhà đầu tư | Niềm tin công chúng, giá cổ phiếu, xếp hạng | Sự cố lớn, khiếu nại tập thể, tin xấu toàn ngành | Tin lan trên mạng xã hội trong vài giờ; nhà đầu tư định giá lại rủi ro |
| Vận hành mạng lưới | Chi nhánh, nhân sự, tiền mặt | Thiên tai, dịch bệnh, mất điện diện rộng | Chi nhánh đóng cửa, thiếu tiền mặt cục bộ, nhu cầu rút tiền tăng ở vùng bị ảnh hưởng |

## (b) Bảng độ nhạy cấp ngân hàng
| Mã | Năng lực, hệ thống | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `NH-LQ-01` | Huy động và CASA toàn hàng | `LQ` | Kênh đầu tư khác hấp dẫn hơn (vàng, chứng khoán tăng nóng); tin đồn về thanh khoản; đối thủ tăng lãi suất huy động | Tiền gửi chảy ra trong vài ngày đến vài tuần, chi phí vốn tăng | **Con người:** ALM theo dõi dòng tiền gửi hằng ngày, chuẩn bị kịch bản trả lời tin đồn. **Dữ liệu, what-if:** dòng ra theo hạng khách và địa bàn (`outside_in/whatif/examples/oi_wi_ex_05_tin_don_rut_tien.md`) |
| `NH-LQ-02` | Tiền mặt tại chi nhánh, CDM | `LQ` `OR` | Hoảng loạn; thiên tai; cơn sốt mua vàng bằng tiền mặt | Thiếu tiền mặt cục bộ trong một đến hai ngày | **Con người:** tăng tiếp quỹ ở địa bàn bị ảnh hưởng. **Dữ liệu:** rút tiền CDM theo ngày chưa có trong danh mục (`GAP`) |
| `NH-MR-01` | Trạng thái ngoại tệ, tỷ giá | `MR` | Xung đột, giá dầu tăng, USD mạnh lên, nhập khẩu vàng | Áp lực mua ngoại tệ, lỗ trạng thái | **Con người:** Treasury rà trạng thái và nhu cầu ngoại tệ của DN nhập khẩu lớn. **Dữ liệu:** số dư, tỷ lệ giao dịch ngoại tệ của DN |
| `NH-MR-02` | Danh mục trái phiếu, đầu tư của ngân hàng | `MR` | Lãi suất trong nước và quốc tế tăng | Giá trị danh mục giảm | **Con người:** ALM chạy độ nhạy lãi suất. **Dữ liệu:** ngoài danh mục what-if |
| `NH-OR-01` | Ngân hàng số, core banking | `OR` `FR` | Lỗ hổng phần mềm, tấn công, sự cố hạ tầng | Gián đoạn mọi phân khúc cùng lúc, trong vài giờ | **Con người:** thông báo sớm và rõ; miễn phí trả chậm cho khoản đến hạn trong thời gian sự cố. **Dữ liệu, what-if:** quy mô khách bị chạm (`inside_out/whatif/examples/io_wi_ex_03_su_co_ky_chi_luong.md`) |
| `NH-OR-02` | Thẻ, POS, cổng thanh toán, kết nối liên ngân hàng | `OR` `FR` | Lỗ hổng trong thiết bị hay phần mềm thanh toán; gian lận thẻ | Gian lận giao dịch, tra soát tăng | **Con người:** đội an ninh xác nhận phạm vi; theo dõi `X05`. **Dữ liệu:** giao dịch thẻ bất thường chưa có trong danh mục |
| `NH-OR-03` | Đối tác công nghệ, phần mềm liên kết | `OR` `FR` | Sự cố hoặc lỗ hổng ở bên thứ ba | Rò rỉ dữ liệu, gián đoạn tính năng liên kết | **Con người:** rà danh sách đối tác và tính năng liên kết đang dùng (`L13`) |
| `NH-OR-04` | Mạng lưới chi nhánh, nhân sự | `OR` | Thiên tai, dịch bệnh | Gián đoạn phục vụ tại quầy | **Con người:** phương án làm việc dự phòng theo vùng |
| `NH-FR-01` | Tài khoản bị lợi dụng (thuê, mượn, mua bán tài khoản) | `FR` `CO` | Làn sóng lừa đảo, thủ đoạn mới | Ngân hàng thành mắt xích chuyển tiền lừa đảo | **Con người:** chống gian lận rà `X01`. **Dữ liệu:** `GAP` |
| `NH-CO-01` | Phòng chống rửa tiền, trừng phạt, báo cáo giao dịch đáng ngờ | `CO` | Trừng phạt quốc tế mới, xung đột, gian lận xuyên biên giới | Giao dịch bị chặn, nguy cơ bị phạt | **Con người:** cập nhật danh sách sàng lọc; rà đối tác ở quốc gia bị trừng phạt |
| `NH-CO-02` | Bảo vệ dữ liệu cá nhân | `CO` `RP` | Rò rỉ dữ liệu ở ngân hàng hoặc đối tác | Phạt, mất niềm tin | **Con người:** quy trình thông báo sự cố dữ liệu |
| `NH-RP-01` | Danh tiếng, niềm tin công chúng | `RP` | Sự cố, khiếu nại, tin xấu toàn ngành | Khách rút tiền, ngừng dùng dịch vụ | **Con người:** truyền thông chủ động, không phản ứng quá mức. **Dữ liệu:** khiếu nại (`S14`) chưa có trong danh mục |
| `IR-EQ-01` | Cổ phiếu TCB | `MR` `RP` | Kết quả kinh doanh, tin danh tiếng, dòng vốn ngoại | Giá giảm, khó tăng vốn | **Con người:** quan hệ nhà đầu tư chuẩn bị thông điệp |
| `IR-RT-01` | Xếp hạng tín nhiệm | `MR` `LQ` | Chất lượng tài sản, rủi ro tập trung | Hạ hạng làm chi phí vốn quốc tế tăng | **Dữ liệu, what-if:** rủi ro tập trung theo ngành (`inside_out/whatif/examples/io_wi_ex_04_canh_bao_som_dn.md`) |
| `IR-DIS-01` | Công bố thông tin | `CO` `RP` | Chậm hoặc sai công bố | Phạt, mất niềm tin | **Con người:** quy trình công bố |
| `IR-ECO-01` | Hệ sinh thái (chứng khoán, quản lý quỹ, bảo hiểm) | `RP` `MR` | Sự cố tại công ty con, đối tác | Lan danh tiếng về ngân hàng mẹ (`L11`) | **Con người:** phối hợp truyền thông với công ty con |

## (c) Cơ hội ở cấp ngân hàng (ít, không ép)
| Khi nào | Cơ hội | Điều kiện |
|---|---|---|
| Tiền gửi tìm nơi an toàn khi tổ chức khác gặp sự cố | `O2` `O6` qua `NH-LQ-01` | Chỉ đón khách chủ động chuyển đến; không khai thác tin đồn (`guardrails.md` mục 13) |
| Khách bán vàng hoặc chứng khoán chốt lời | `O2` | Có kênh tiếp nhận tiền về (tiết kiệm, sinh lời tự động) |
| Biến động tỷ giá, lãi suất làm khách cần phòng ngừa | `O3` | Gắn với nhu cầu phòng ngừa thực của giao dịch thương mại (`segments/seg_03_DN_lon.md`) |
| Đối thủ gặp sự cố hệ thống | Không coi là cơ hội để quảng bá | Chỉ dùng làm bài học kiểm tra lỗ hổng tương tự ở mình |

## (d) Tín hiệu nội bộ ở cấp ngân hàng
- **Thanh khoản:** `S07` rút tiền mặt, `F01` chuyển tiền gửi đi, `F02` chuyển sang kỳ hạn ngắn, `G02` tất toán để mua tài sản đang nóng.
- **Hệ thống và gian lận:** `S13` đăng nhập lạ, `S14` khiếu nại theo chủ đề, tín hiệu `X01`–`X08` trong `outside_in/news/nw_03_gian_lan_an_ninh.md`.
- **Thị trường:** `S15` vị thế ngoại tệ, phái sinh của khách; nhu cầu mua ngoại tệ của DN nhập khẩu tăng.
- Tín hiệu nào đo được bằng danh mục feature: `core/whatif_chung/wc_02_signal_map.md`.

## (e) Liên hệ với các phân khúc
- **Ngân hàng → mọi phân khúc** (`L09`): sự cố hệ thống hoặc thay đổi chính sách chạm cùng lúc KHCN, SME, DN lớn (mẫu `P3`).
- **Phân khúc → ngân hàng** (`L10`): rủi ro của nhiều khách cộng dồn thành vấn đề thanh khoản, chất lượng tài sản, danh tiếng.
- **Đối tác công nghệ → ngân hàng và khách hàng** (`L13`): lỗ hổng ở bên thứ ba đi vào qua tính năng liên kết.
- **Thủ đoạn ở nước khác → Việt Nam** (`L14`): thủ đoạn gian lận lan qua biên giới khi dùng cùng loại kênh thanh toán.
