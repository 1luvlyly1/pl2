---
id: CORE-CONCEPTS
used_by: [Propagation, Critic]
steps: [1, 2]
depends_on: []
load_when: Bước 1 – xác định hướng sự kiện (outside-in hay inside-out), chọn mẫu lan truyền P1/P2/P3, xử lý hộ kinh doanh và cấp ngân hàng, kiểm tra vòng phản hồi
version: v3.4
updated: 2026-11-04
---

# Khung khái niệm: hai hướng phát hiện, ba mẫu lan truyền, vòng phản hồi

## 1. Hai hướng phát hiện rủi ro

### Outside-in – từ bên ngoài vào
Sự kiện xảy ra bên ngoài ngân hàng, chạm vào khách hàng trước, rồi qua khách hàng chạm vào danh mục sản phẩm của ngân hàng. Nguồn đầu vào là tin tức, chính sách (NHNN, Bộ Tài chính, thuế), biến động thị trường (lãi suất, tỷ giá, vàng, chứng khoán, BĐS), thiên tai, dịch bệnh, thương mại quốc tế, sự cố của DN hay đối tác. Câu hỏi agent phải trả lời: **sự kiện này chạm ai đầu tiên, lan sang ai tiếp theo, rơi vào sản phẩm nào**. Tin outside-in được xếp vào ba nhóm `TT`, `GT`, `GL` để chọn cách suy luận (`outside_in/news/nw_00_router.md`).

### Inside-out – từ bên trong ra
Tín hiệu hay biến cố phát sinh bên trong ngân hàng rồi lan ra khách hàng, thị trường và nhà đầu tư. Có ba dạng:
- **Tín hiệu trong dữ liệu:** quá hạn, dòng lương, doanh thu QR, tất toán tiết kiệm… thay đổi bất thường. Tín hiệu là triệu chứng; nguyên nhân thường ở bên ngoài và cần tìm lại qua playbook ngành.
- **Quyết định của ngân hàng:** đổi lãi suất, phí, hạn mức, khẩu vị tín dụng, quy trình. Quyết định có thể tạo rủi ro thứ cấp (`inside_out/bank_response_risks.md`).
- **Sự cố của ngân hàng:** hệ thống gián đoạn, lỗi xử lý, sự cố bảo mật. Thường lan theo mẫu toàn hệ thống (P3).

Câu hỏi agent phải trả lời: **tín hiệu này báo trước điều gì ở khách hàng, và hành động của ngân hàng có tạo rủi ro thứ cấp không**. Dòng nhãn của nhánh inside-out ghi `loai_tin=IO`.

### Một sự kiện có thể có cả hai chiều
Ngành BĐS suy yếu (outside-in) khiến ngân hàng siết cho vay mua nhà (inside-out); chủ đầu tư thiếu dòng tiền bán hàng, rủi ro quay lại danh mục doanh nghiệp lớn. Khi thấy chiều thứ hai, viết nó thành một nhánh riêng có dòng nhãn riêng.

## 2. Ba mẫu lan truyền
Mẫu lan truyền trả lời câu hỏi "ai bị chạm trước". Chọn đúng mẫu quyết định thứ tự đọc file phân khúc và kênh liên kết. Mẫu lan truyền viết `P1`–`P3` trong ngoặc mã; **khác với mức ưu tiên P1–P3 in đậm trong bảng (c) của file phân khúc** (mức ưu tiên nói về độ nhanh và độ nặng của tác động lên sản phẩm).

### `P1` – Doanh nghiệp trước
Sự kiện làm thay đổi doanh thu, chi phí hoặc pháp lý của một tổ chức trước. Từ DN, rủi ro lan ra bốn hướng:
- chủ DN và cổ đông (thường là KHCN hạng cao) qua bảo lãnh cá nhân, tài sản bảo đảm, tiền rút từ tiết kiệm cá nhân để bù vốn (`L01`);
- nhân viên qua chi lương (`L02`);
- nhà cung cấp, nhà phân phối là SME, hộ kinh doanh qua công nợ và tài trợ chuỗi cung ứng (`L03`);
- khách hàng của DN như người mua nhà dự án, trái chủ (`L04`, `L05`).

Ví dụ: Mỹ áp thuế lên đồ gỗ → DN gỗ xuất khẩu mất đơn → xưởng vệ tinh, công nhân, nông hộ trồng rừng.

### `P2` – Cá nhân trước
Sự kiện làm thay đổi thu nhập, sức khỏe, tài sản hoặc hành vi của con người trước. Từ cá nhân, rủi ro lan ra:
- chi tiêu giảm, làm doanh thu của hộ kinh doanh, SME bán lẻ, DN tiêu dùng giảm (`L06`);
- chủ DN gặp biến cố cá nhân, chạm DN mình sở hữu hoặc bảo lãnh (`L01`);
- hành vi tài chính đổi: rút tiền, bán lại sản phẩm đầu tư, ngừng đóng phí bảo hiểm.

Ví dụ: lãi suất thả nổi neo cao → người vay mua nhà cắt chi tiêu → hộ kinh doanh quanh khu dân cư giảm doanh thu.

### `P3` – Toàn hệ thống
Sự kiện chạm cùng lúc mọi phân khúc qua giá cả vĩ mô, quy định, hạ tầng ngân hàng hoặc thiên tai diện rộng, rồi cộng dồn lên cấp ngân hàng (thanh khoản, danh tiếng, nhà đầu tư). Ví dụ: NHNN đổi lãi suất điều hành, tỷ giá biến động mạnh, sự cố hệ thống ngân hàng số. Với mẫu này, không có "bước 1" duy nhất; viết theo từng phân khúc rồi gom lên cấp ngân hàng.

### Cách nhận ra mẫu ở bước 1
| Câu hỏi | Trả lời "có" thì |
|---|---|
| Sự kiện đổi doanh thu, chi phí hoặc pháp lý của một tổ chức trước? | `P1` |
| Sự kiện đổi thu nhập, sức khỏe, tài sản hoặc hành vi của con người trước? | `P2` |
| Sự kiện chạm cùng lúc mọi khách qua giá vĩ mô, quy định hay hạ tầng? | `P3` |
| Đối tượng là hộ kinh doanh? | Xét cả `P1` và `P2` (mục 3) |

## 3. Hộ kinh doanh là nút lai
Ba phân khúc khách hàng là KHCN (gồm nhóm cá nhân và nhóm hộ kinh doanh), SME và doanh nghiệp lớn (mã `CIB`). Hộ kinh doanh nằm trong KHCN vì pháp lý và tài chính của hộ **không tách bạch** với chủ hộ: tiền của cửa hàng và tiền của gia đình là một túi. Hệ quả:
- mọi sự kiện chạm chủ hộ là chạm hộ kinh doanh ở cùng bước, và ngược lại; độ trễ gần bằng 0;
- khi đối tượng là hộ kinh doanh, luôn đọc cả hai file `segments/seg_01a_KHCN_ca_nhan.md` và `seg_01b_KHCN_ho_kinh_doanh.md`;
- khoản vay sản xuất kinh doanh của hộ có thể được trả bằng thu nhập cá nhân của chủ hộ và ngược lại, nên không tách rủi ro hai khoản như hai khách khác nhau.

## 4. Cấp ngân hàng không phải phân khúc
Cấp ngân hàng (mã `NH` trong dòng nhãn) là nơi ghi tác động lên hoạt động của chính ngân hàng. Cấp ngân hàng nhận tác động theo hai đường:
- **gián tiếp**, khi rủi ro của nhiều khách cộng dồn (mẫu `P3`, hoặc `P1`, `P2` lan rộng) thành vấn đề thanh khoản, chất lượng tài sản, danh tiếng (kênh `L10`);
- **trực tiếp**, khi tin chạm thẳng ngân hàng: lỗ hổng phần mềm, làn sóng gian lận, cú sốc tỷ giá, dòng tiền gửi chạy theo vàng.

Nhà đầu tư và xếp hạng tín nhiệm nằm ở cấp này. Chi tiết ở `core/06_ngan_hang.md`. Chỉ số của cấp ngân hàng không cộng vào chỉ số của từng phân khúc.

## 5. Vòng phản hồi
Rủi ro không chỉ đi một chiều. Ở bước 2, agent kiểm tra ít nhất một vòng phản hồi và nêu ở cuối đoạn rủi ro. Hai vòng hay gặp:
- **Vòng thu nhập – chi tiêu:** DN cắt lao động → thu nhập nhân viên giảm → chi tiêu giảm → hộ kinh doanh, SME bán lẻ giảm doanh thu → hộ giảm nhập hàng → nhà phân phối chậm thanh toán cho DN đầu chuỗi → DN đầu chuỗi càng khó khăn.
- **Vòng tài sản – tín dụng:** giá BĐS giảm → tài sản bảo đảm giảm → ngân hàng siết tín dụng → người mua không vay được → chủ đầu tư bán chậm → chậm tiến độ, chậm trả trái phiếu → nhà đầu tư trái phiếu bán tháo → giá BĐS giảm thêm.

Vòng có bước do chính ngân hàng gây ra (siết tín dụng) thì đọc thêm `inside_out/bank_response_risks.md`.

## 6. Một tin và nhiều tin
Playbook xử lý từng tin một. Một tin nhỏ đứng riêng có thể không đáng chú ý, nhưng nhiều tin có nguyên nhân khác nhau cùng dồn vào một nhóm khách (cùng vùng, cùng ngành, cùng vai trò) trong thời gian ngắn là rủi ro tập trung. Việc gom các tin thành cụm do bộ gom cụm làm ngoài playbook; khi một tin thuộc cụm, agent nhận thêm dòng `[CUM]` và hồ sơ cụm. Agent không tự gom cụm và không tính điểm cụm (`guardrails.md` mục 19).
