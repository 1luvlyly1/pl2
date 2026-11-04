---
id: IO-WI-00
used_by: [What-if, Inside-out Monitor]
steps: [whatif-1, whatif-3]
depends_on: [core/whatif_chung/wc_00_quy_tac.md, core/whatif_chung/wc_03_cong_thuc.md, inside_out/signals.md, inside_out/bank_response_risks.md]
load_when: Sự kiện bắt nguồn từ bên trong ngân hàng – tín hiệu nội bộ xấu đi, quyết định ngân hàng đang cân nhắc (lãi suất, hạn mức, phí, khẩu vị), sự cố hệ thống, rủi ro tập trung – và cần đo ảnh hưởng
version: v3.4
updated: 2026-11-04
---

# What-if cho rủi ro từ bên trong ngân hàng (inside-out)

File này bổ sung cho phần dùng chung ở `core/whatif_chung/`. Đọc `wc_00_quy_tac.md` trước; file này chỉ nói những gì riêng của sự kiện nội bộ.

## 1. Khác gì với outside-in
Với tin bên ngoài, ngân hàng không kiểm soát cú sốc; what-if hỏi "nếu tin này chạm khách của ta ở mức đó thì sao". Với sự kiện nội bộ, có hai khác biệt quan trọng:
- **Nhiều cú sốc do chính ngân hàng tạo ra hoặc kiểm soát được** (tăng lãi suất, cắt hạn mức, đổi quy trình). Câu hỏi what-if là câu hỏi ra quyết định: "nếu làm thế này thì ai bị ảnh hưởng, có tạo rủi ro thứ cấp không". Vì vậy kịch bản luôn đo **cả hai mặt**: phần rủi ro giảm được nhờ quyết định và phần rủi ro mới do quyết định sinh ra (`inside_out/bank_response_risks.md`).
- **Dữ liệu nội bộ có lịch sử nhiều tháng.** Khi sự kiện là một tín hiệu đang xấu đi, độ lớn cú sốc nên lấy từ **tỷ lệ chuyển trạng thái trong quá khứ** tính bằng chính dữ liệu, thay vì giả định.

## 2. Bốn loại sự kiện nội bộ và câu hỏi what-if
| Loại | Ví dụ | Câu hỏi what-if | Mẫu công thức chính | Bài mẫu |
|---|---|---|---|---|
| Tín hiệu nội bộ xấu đi | Số khách trả tối thiểu thẻ (`S05`) tăng; tỷ lệ dùng hạn mức (`S04`) tăng | Nếu xu hướng giữ nguyên thêm `h` tháng, bao nhiêu khách và dư nợ chuyển sang quá hạn | Tỷ lệ chuyển trạng thái lịch sử | `io_wi_ex_01` |
| Quyết định ngân hàng đang cân nhắc | Cắt hạn mức thẻ, thấu chi của nhóm dùng nhiều; tăng biên độ lãi suất | Quyết định giảm được bao nhiêu phơi nhiễm và đẩy bao nhiêu khách vào khó khăn | Hạn mức căng, DSR, so sánh hai mặt | `io_wi_ex_02` |
| Sự cố vận hành | Ngân hàng số gián đoạn đúng kỳ chi lương | Bao nhiêu người nhận lương và bao nhiêu khoản trả nợ bị chạm; ai không có tiền đệm | Quy mô phơi nhiễm, số tháng đệm | `io_wi_ex_03` |
| Rủi ro tập trung, cảnh báo sớm DN | Nhóm DN có dòng tiền vào giảm, OD căng, lương giảm | Nếu nhóm DN này ngừng hoặc chậm trả lương, rủi ro lan sang nhân viên bao nhiêu | Điểm cảnh báo, độ phủ lương, chuỗi DN → nhân viên | `io_wi_ex_04` |

## 3. Lấy độ lớn cú sốc
- **Thông số của quyết định:** lấy từ phương án ngân hàng đang cân nhắc (mức cắt hạn mức, mức tăng lãi suất, thời gian dự kiến khắc phục sự cố). Ghi nguồn là "thông số do [bộ phận] cung cấp"; khi chưa có thì là giả định và cho ít nhất hai mức.
- **Tỷ lệ chuyển trạng thái lịch sử:** chọn tháng gốc `t0 = :as_of_month − :horizon_months`, đánh dấu khách có trạng thái A ở `t0` (ví dụ trả tối thiểu thẻ từ 2 lần trong 3 tháng), đếm bao nhiêu người trong số đó có trạng thái B ở `:as_of_month` (ví dụ quá hạn). Tỷ lệ này áp lên nhóm đang có trạng thái A ở hiện tại để dự phóng `h` tháng tới. Hai giả định phải ghi: điều kiện kinh tế `h` tháng tới giống giai đoạn lịch sử, và chính sách xử lý nợ không đổi. Mức nặng có thể dùng tỷ lệ của tháng gốc xấu nhất trong vài tháng gần đây.
- **Kiểm tra cỡ mẫu:** tỷ lệ lịch sử tính trên nhóm nhỏ thì không ổn định; câu truy vấn báo cỡ nhóm gốc, nhóm dưới `:min_group_size` không dùng.
- **Không dùng kết quả what-if để tự xác nhận tín hiệu.** Tín hiệu nội bộ là đầu vào; kết quả what-if là phóng chiếu, không phải bằng chứng thêm cho chính tín hiệu đó.

## 4. Đo cả hai mặt của quyết định
Với mọi kịch bản loại "quyết định ngân hàng", phần kết quả có ít nhất hai nhóm chỉ số:
- **Mặt lợi:** phơi nhiễm giảm được (ví dụ phần hạn mức chưa dùng bị thu hẹp, dư nợ của khách rủi ro cao được giới hạn).
- **Mặt hại:** số khách bị đẩy vượt hạn mức hoặc vượt ngưỡng DSR, trong đó bao nhiêu người không có tiền đệm, bao nhiêu người đang trả nợ tốt (khách tốt bị chạm oan), và nhóm nào có khả năng chuyển sang ngân hàng khác.
Kết luận ở phần 7 của đầu ra nêu điều kiện để quyết định đáng làm (ví dụ chỉ áp dụng cho nhóm đã có quá hạn), không kết luận thay người ra quyết định.

## 5. Vòng phản hồi
Sự kiện nội bộ dễ tạo vòng lặp: siết hạn mức → khách mất đệm → quá hạn tăng → siết tiếp. Khi kịch bản có vòng phản hồi, agent mô tả vòng đó trong phần 7 và đề xuất chỉ số theo dõi sau khi quyết định có hiệu lực (thường là `S04`, `S05`, quá hạn của chính nhóm bị tác động). Không mô phỏng nhiều vòng trong một câu SQL.

## 6. Dòng nhãn
Dòng `[WI]` ghi `cua=IO`. Mã `rui_ro` có thể là mã năng lực ngân hàng (`NH-`) khi sự kiện chạm thẳng ngân hàng.

## 7. Bài mẫu
Danh sách và cách chọn: `inside_out/whatif/examples/io_wi_ex_00_index.md`.
