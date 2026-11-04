---
id: CORE-LINKAGE-GRAPH
used_by: [Propagation, Inside-out Monitor, What-if]
steps: [2, 4]
depends_on: [core/02_concepts_patterns.md]
load_when: Bước 2 – duyệt đường lan truyền giữa các nhóm khách (kênh L01–L14), xác định độ trễ và mức chắc chắn của từng bước
version: v3.4
updated: 2026-11-04
---

# Đồ thị liên kết khách hàng: 14 kênh lan truyền

Đồ thị này là bản đồ đường đi để agent Propagation duyệt từ nút bị chạm đầu tiên sang các nút khác. Mỗi kênh mô tả: rủi ro (hoặc dòng tiền) đi từ ai sang ai, theo cơ chế nào, sau bao lâu, và dữ liệu nội bộ nào nối được hai đầu. Cột "Có trong danh mục what-if" cho biết kênh đó có đo được bằng danh mục feature hiện tại không (`core/whatif_chung/wc_02_signal_map.md`).

## 1. Các kênh

| Mã | Từ → tới | Cơ chế truyền dẫn | Độ trễ điển hình | Dữ liệu nối hai đầu | Có trong danh mục what-if |
|---|---|---|---|---|---|
| `L01` | DN ↔ chủ DN, cổ đông | Chủ DN bảo lãnh cá nhân cho khoản vay của DN, dùng BĐS cá nhân làm tài sản bảo đảm, rút tiết kiệm cá nhân để bù vốn DN; ngược lại, biến cố của chủ chạm ngay quyết định của DN | Gần bằng 0 – cùng một túi tiền | Mã khách của chủ sở hữu, người đại diện pháp luật; hợp đồng bảo lãnh; tài sản bảo đảm bên thứ ba | Chưa có: không có quan hệ chủ–DN |
| `L02` | DN → nhân viên | DN chi lương qua ngân hàng; giảm lương, giảm ca, cắt lao động làm thu nhập nhân viên giảm, rồi tới khả năng trả nợ cá nhân | Một đến ba tháng (chu kỳ lương) | Lô chi lương, mã DN trả lương trên tài khoản nhân viên | Có: `cus_payroll.company_code` |
| `L03` | DN lớn → nhà phân phối, đại lý (SME, hộ kinh doanh) | DN đầu chuỗi đổi chính sách công nợ, chiết khấu, đơn hàng; chương trình tài trợ chuỗi cung ứng (SCF) truyền khó khăn từ đầu chuỗi xuống | Vài tuần đến một quý | Chương trình SCF, mã DN đầu chuỗi (anchor) | Chưa có: không có quan hệ anchor–spoke |
| `L04` | Chủ đầu tư BĐS ↔ người mua nhà | Người mua vay mua nhà dự án; chủ đầu tư chậm tiến độ, vướng pháp lý thì người mua ngừng trả nợ hoặc tranh chấp; ngược lại người mua ngừng thanh toán làm chủ đầu tư thiếu dòng tiền | Ba đến mười hai tháng (tiến độ dự án) | Mã dự án, tài khoản giữ hộ, khoản vay gắn dự án | Chưa có: không có mã dự án |
| `L05` | Tổ chức phát hành → nhà đầu tư cá nhân | Trái phiếu phân phối qua iBond, chứng chỉ quỹ qua iFund; tổ chức phát hành gặp khó khăn thì nhà đầu tư bán lại, khiếu nại | Ba đến mười hai tháng (kỳ trả lãi, gốc); tâm lý có thể lan trong vài ngày | Mã trái phiếu, tổ chức phát hành, danh mục quỹ theo ngành | Một phần: số dư và giá trị bán lại, không có tổ chức phát hành |
| `L06` | Cá nhân ↔ hộ kinh doanh, SME bán lẻ | Chi tiêu thẻ, QR của cá nhân là doanh thu của hộ kinh doanh; thu nhập cá nhân giảm thì doanh thu địa bàn giảm | Một đến ba tháng (chu kỳ chi tiêu) | Giao dịch QR, POS, Soundbox nhận tiền; mã ngành điểm bán; địa bàn | Chưa có: không có doanh thu QR |
| `L07` | Hộ kinh doanh → SME | Hộ lớn lên thành DN (thường do chính sách thuế), chuyển rủi ro và nhu cầu sang phân khúc SME | Theo lộ trình chính sách, nhiều tháng | Cờ chuyển đổi; chủ hộ là người đại diện của DN mới | Chưa có |
| `L08` | Thị trường quốc tế → DN xuất nhập khẩu | Thuế quan, nhu cầu, tỷ giá, cước vận tải ở nước ngoài truyền vào DN qua L/C, nhờ thu, ngoại tệ | Vài tuần đến một quý | Hồ sơ L/C, đối tác, quốc gia, mã hàng | Một phần: tỷ lệ giao dịch ngoại tệ, không có thị trường |
| `L09` | Ngân hàng → mọi khách hàng | Lãi suất, phí, khẩu vị tín dụng, hệ thống số, danh tiếng của ngân hàng chạm cùng lúc nhiều khách | Ngay (sự cố) đến một kỳ trả nợ (lãi suất) | Biểu phí, lãi suất, nhật ký sự cố, khiếu nại | Một phần: đo được nhóm khách bị chạm, không có nhật ký sự cố |
| `L10` | Khách hàng → cấp ngân hàng | Rủi ro của nhiều khách cộng dồn thành chất lượng tài sản, thanh khoản, danh tiếng, rồi giá cổ phiếu và xếp hạng | Một quý trở lên (công bố số liệu); tin xấu có thể vài ngày | Nợ xấu, CASA, lợi nhuận, công bố thông tin | Một phần: cộng được số dư, dư nợ theo nhóm |
| `L11` | Hệ sinh thái tài chính ↔ khách hàng | Công ty con và đối tác (chứng khoán, quản lý quỹ, bảo hiểm) gặp sự cố thì lan danh tiếng về ngân hàng mẹ, và ngược lại | Vài ngày đến vài tuần | Mã sản phẩm phân phối, đối tác | Một phần: số dư quỹ, bảo hiểm |
| `L12` | Nhà nước → DN | Mua sắm công, bảo lãnh dự thầu, thanh toán chậm từ ngân sách, nộp thuế | Theo chu kỳ ngân sách, nhiều tháng | Bảo lãnh, giao dịch nộp ngân sách | Chưa có |
| `L13` | Đối tác công nghệ → ngân hàng và khách hàng | Lỗ hổng hoặc sự cố ở nhà cung cấp POS, phần mềm bán hàng, kế toán liên kết, chữ ký số, đối tác bảo hiểm đi vào qua tính năng liên kết | Vài giờ đến vài ngày | Danh sách đối tác, tính năng liên kết, khách đang dùng | Chưa có |
| `L14` | Nước khác → Việt Nam (thủ đoạn gian lận) | Thủ đoạn lừa đảo lan qua biên giới khi dùng cùng loại kênh (chuyển khoản tức thời, QR, ví, ứng dụng ngân hàng) | Vài tuần đến vài tháng; mức mặc định "có thể" | Kịch bản báo lừa đảo, tín hiệu `X01`–`X08` | Chưa có |

## 2. Quy tắc duyệt
- **Số bước mặc định tối đa là ba.** Bước thứ tư trở đi chỉ khi có bằng chứng định lượng cho các bước trước (`guardrails.md` mục 6).
- **Mỗi bước giảm một mức chắc chắn.** Nút bị chạm đầu tiên và bước 1 có cơ chế rõ dùng "có khả năng cao"; bước 2 dùng "có thể"; bước 3 dùng "giả thuyết, cần kiểm chứng". Tín hiệu nội bộ đã xác nhận cho phép nâng một mức.
- **Độ trễ cộng dồn theo đường đi.** Một chuỗi `L08` → `L02` → `L06` thường mất từ một quý trở lên để tới hộ kinh doanh; viết rõ để người đọc biết khi nào cần kiểm tra tín hiệu.
- **Kênh có độ trễ gần bằng 0** (`L01`, quan hệ chủ hộ – hộ kinh doanh) không tính là một bước riêng khi xét mức chắc chắn.
- **Kênh hai chiều** (`L01`, `L04`, `L06`, `L11`): kiểm tra chiều ngược lại như một vòng phản hồi (`core/02_concepts_patterns.md` mục 5).
- **Kênh chưa có dữ liệu:** nhận định đi qua kênh đó không thể được what-if kiểm chứng; ghi tín hiệu cần bổ sung thay vì nâng mức chắc chắn.
