---
id: IO-WI-EX-00
used_by: [What-if]
load_when: Chọn 1 bài mẫu gần nhất trước khi dựng kịch bản what-if cho sự kiện bắt nguồn từ bên trong ngân hàng
version: v3.4
updated: 2026-11-04
---

# Bài mẫu what-if inside-out – danh sách và cách chọn

Sự kiện ở đây bắt nguồn từ bên trong ngân hàng: dữ liệu nội bộ cho thấy một tín hiệu xấu đi, ngân hàng đang cân nhắc một quyết định, hoặc hệ thống gặp sự cố. Mỗi bài theo khuôn `core/whatif_chung/wc_05_dau_ra.md` (8 phần), dòng nhãn ghi `cua=IO`. SQL đã qua `validate_whatif_sql.py` (0 lỗi) và chạy thử trên Spark với bảng dựng từ danh mục. Không bài nào chứa số liệu kết quả.

| Bài | Sự kiện nội bộ | Mẫu công thức | Điểm cần học |
|---|---|---|---|
| `io_wi_ex_01_tra_toi_thieu_the.md` | Số khách trả tối thiểu thẻ (`S05`) tăng | Tỷ lệ chuyển trạng thái lịch sử, có nhóm đối chứng | Lấy độ lớn cú sốc từ chính dữ liệu các tháng trước thay vì giả định; kiểm tra tín hiệu có giá trị báo trước không |
| `io_wi_ex_02_siet_han_muc_the.md` | Ngân hàng cân nhắc cắt hạn mức thẻ của nhóm dùng nhiều | Hạn mức căng, hai mặt của quyết định | Đặt phần phơi nhiễm giảm được cạnh số khách bị đẩy vượt hạn mức, tách khách tốt bị chạm oan |
| `io_wi_ex_03_su_co_ky_chi_luong.md` | Ngân hàng số gián đoạn đúng kỳ chi lương | Quy mô phơi nhiễm, đệm CASA | Kịch bản phục vụ quyết định vận hành (miễn phí trả chậm, thứ tự khôi phục); kết quả là cận trên khi thiếu ngày đến hạn |
| `io_wi_ex_04_canh_bao_som_dn.md` | Nhóm DN có nhiều tín hiệu dòng tiền xấu cùng lúc | Điểm cảnh báo, chuỗi DN → nhân viên | Điểm cảnh báo là công cụ sắp ưu tiên; nối sang nhân viên qua bảng lương; gợi ý quay lại playbook ngành tìm nguyên nhân bên ngoài |

## Chọn bài
| Sự kiện nội bộ mới | Bài |
|---|---|
| Một chỉ số hành vi khách (thẻ, thấu chi, tiết kiệm, quá hạn) đang xấu đi | 01 |
| Ngân hàng định siết hoặc nới: hạn mức, lãi suất, phí, khẩu vị tín dụng | 02 |
| Sự cố hệ thống, gián đoạn kênh, lỗi xử lý giao dịch | 03 |
| Rủi ro tập trung theo DN, ngành, chuỗi; cảnh báo sớm phía DN | 04 |
