---
id: OI-WI-00
used_by: [What-if]
steps: [whatif-1, whatif-3]
depends_on: [core/whatif_chung/wc_00_quy_tac.md, core/whatif_chung/wc_03_cong_thuc.md]
load_when: Agent What-if nhận bài playbook về một tin bên ngoài (TT, GT, GL) hoặc một cụm tín hiệu [CUM], và cần dựng kịch bản đo ảnh hưởng
version: v3.4
updated: 2026-11-04
---

# What-if cho rủi ro từ bên ngoài (outside-in)

File này bổ sung cho phần dùng chung ở `core/whatif_chung/`. Đọc `wc_00_quy_tac.md` trước; file này chỉ nói những gì riêng của rủi ro bắt nguồn từ tin bên ngoài.

## 1. Đầu vào
Agent nhận ba thứ: bài văn xuôi của playbook đã qua Critic, 1–3 dòng `[FG]`, và nếu tin nằm trong một cụm thì dòng `[CUM]` cùng hồ sơ cụm. Agent không đọc lại tin gốc để tìm thêm chi tiết; mọi con số dùng làm cú sốc phải có trong tin như playbook đã dẫn. Agent cũng không đưa kết quả what-if ngược vào bài playbook.

## 2. Chọn rủi ro nào để đo
- Ưu tiên nhánh ở mức "có khả năng cao" hoặc "có thể" có sản phẩm mức **P1** hoặc **P2** trong bảng (c) của file phân khúc.
- Với tin `TT` (trực tiếp), thường đo nhánh đầu tiên (nút bị chạm đầu tiên) và một nhánh lan sang phân khúc khác.
- Với tin `GT` (gián tiếp), kịch bản là dài hạn: tầm thời gian nhiều quý, chỉ đo quy mô phơi nhiễm của nhóm cấu trúc (ví dụ khách của ngành giáo dục khi tỷ lệ sinh giảm), không đặt cú sốc ngắn hạn.
- Với tin `GL` (gian lận, an ninh mạng), chỉ đo quy mô nhóm có thể bị chạm để lên kế hoạch cảnh báo; không mô phỏng thiệt hại (bài mẫu 06).
- Nhánh chiều cơ hội (`O1`–`O6`) có thể đo bằng mức "ngược" để biết quy mô nhu cầu, nhưng kết quả không phải chỉ thị bán hàng.

## 3. Lấy độ lớn cú sốc từ tin
- **Dùng con số trong tin khi có.** Ghi nguồn đúng dạng: "tin 18/06/2026: cước container 40 feet tăng 23% trong một tuần". Con số trong tin thường là mức vừa.
- **Đổi đơn vị bằng phép tính nêu rõ.** Tin thường nói về giá, lãi suất hoặc sản lượng, còn kịch bản cần phần trăm thay đổi của thu nhập, khoản trả hay dòng tiền. Ví dụ: lãi suất từ 9% lên 13% đổi thành khoản trả tăng khoảng 30% theo công thức niên kim với kỳ hạn còn lại giả định 20 năm (bài mẫu 02). Phép đổi là giả định và ghi như vậy.
- **Không đổi khi thiếu mắt xích.** Giá cà phê giảm 2.500 đồng/kg không đổi được thành phần trăm thu nhập nông hộ khi không có sản lượng, giá vốn, diện tích. Khi đó cú sốc là giả định có lý do, không phải số "suy ra từ tin" (bài mẫu 03).
- **Tin xác nhận dùng được làm độ lớn.** Tin xác nhận (ví dụ "xuất khẩu sang Mỹ 7 tháng giảm khoảng 6%") không được đếm là nguyên nhân mới của cụm, nhưng là nguồn tốt cho độ lớn cú sốc vì đã xảy ra.
- **Mức nặng:** cận trên trong tin, hoặc giả định có lý do (ví dụ thuế với một nhóm hàng tới mức làm mất hẳn đơn của nhóm đó).
- **Không dự báo.** Không đặt cú sốc dựa trên dự báo của agent về giá, lãi suất, tỷ giá trong tương lai.

## 4. Chuỗi nhiều bước
- Mỗi bước lan truyền trong bài playbook có dữ liệu tương ứng thì thành một khối CTE. Các bước nối với nhau bằng khóa có thật, chủ yếu `cus_payroll.company_code` nối DN với nhân viên (kênh `L02`).
- Bước không có dữ liệu (ví dụ doanh thu QR của HKD quanh KCN, chuỗi anchor–spoke) ghi `GAP` và chuỗi tính dừng ở bước trước đó. Không nhảy qua bước thiếu dữ liệu để tính bước sau.
- Mức chắc chắn của kịch bản không cao hơn mức của bước playbook tương ứng; bước 3 trở đi luôn là "giả thuyết".

## 5. Cụm tín hiệu (`[CUM]`)
- Quần thể theo khóa cụm (ví dụ `vung=tay_nguyen × vai_tro=nong_ho`), dùng bộ lọc gần nhất có trong dữ liệu và ghi rõ phần nào của khóa không lọc được.
- Mỗi nguyên nhân của cụm là **một tham số sốc riêng**. Kịch bản có một dòng cho từng nguyên nhân và một dòng gộp, để thấy **phần cộng dồn**: dư nợ chỉ lộ ra khi các nguyên nhân dồn lại. Cách gộp phải nói rõ, ví dụ đệm sau sốc `B·Π(1−draw_k)`.
- Tin ngược chiều trong hồ sơ cụm được nhắc trong phần tham số (thường kéo mức vừa xuống), không bị bỏ qua.
- Tin xác nhận không thành nguyên nhân mới.

## 6. Bài mẫu
Danh sách và cách chọn: `outside_in/whatif/examples/oi_wi_ex_00_index.md`. Nạp một bài gần nhất với rủi ro đang đo.
