---
id: NEWS-ROUTER
used_by: [Orchestrator, Propagation, Critic]
steps: [1]
depends_on: [core/02_concepts_patterns.md]
load_when: Luôn nạp ở bước 1 với mọi sự kiện outside-in – để xếp tin vào nhóm TT, GT hoặc GL và chọn cách suy luận
version: v3.0
updated: 2026-11-02
---

# Bộ định tuyến tin outside-in

Tin đã được người dùng sàng lọc. Việc xếp nhóm ở đây **chỉ để chọn cách suy luận**, không để loại tin. Mỗi nhóm lan theo một cơ chế khác nhau, nên dùng sai cách đọc sẽ ra kết luận sai.

## 1. Ba nhóm tin
| Nhóm | Mã | Ví dụ | Lan theo cơ chế | Tầm thời gian | File nạp thêm |
|---|---|---|---|---|---|
| **Tác động trực tiếp** | `TT` | Xung đột quân sự làm giá vàng, giá dầu tăng; giá nông sản, kim loại tăng giảm; tỷ giá, lãi suất, thuế quan, trừng phạt, chính sách trong nước | Dòng tiền thật của khách hàng và của ngân hàng thay đổi ngay | Vài ngày – 3 tháng | `outside_in/news/nw_01_truc_tiep.md` |
| **Tác động gián tiếp** | `GT` | Tỷ lệ sinh giảm, già hóa dân số, đại dịch kiểu COVID, biến đổi khí hậu, đô thị hóa, AI thay đổi việc làm | Cấu trúc nhu cầu, thu nhập và giá trị tài sản dịch chuyển chậm, cộng dồn | 6 tháng – nhiều năm | `outside_in/news/nw_02_gian_tiep.md` |
| **Gian lận, lừa đảo, an ninh mạng** | `GL` | Thủ đoạn gian lận ở nước khác, làn sóng lừa đảo mới, lỗ hổng CVE trong phần mềm phổ biến, ransomware, rò rỉ dữ liệu | Bề mặt tấn công: kênh, thiết bị, phần mềm, con người có thể bị lợi dụng | Vài giờ – vài tuần | `outside_in/news/nw_03_gian_lan_an_ninh.md` |

## 2. Ba câu hỏi để xếp nhóm
1. Tin có làm **giá, lãi suất, tỷ giá, dòng hàng hoặc quy định** thay đổi trong vòng 0–3 tháng không? → `TT`.
2. Tin mô tả **thay đổi cấu trúc** (dân số, sức khỏe cộng đồng, xã hội, khí hậu, công nghệ) có tác động từ 6 tháng trở lên? → `GT`.
3. Tin nói về **thủ đoạn gian lận, lừa đảo, rửa tiền, tấn công, lỗ hổng phần mềm, rò rỉ dữ liệu**? → `GL`.

Không khớp câu nào: xếp `TT` và ghi rõ "xếp nhóm theo mặc định".

## 3. Tin thuộc nhiều nhóm
Nhiều tin có một nhóm chính và một nhóm phụ. Suy luận đầy đủ theo nhóm chính; nhóm phụ viết thành **một nhánh riêng** trong bài, ngắn hơn.

| Loại tin | Nhóm chính | Nhóm phụ thường gặp |
|---|---|---|
| Chiến tranh, xung đột quân sự | `TT` (năng lượng, vàng, tỷ giá, vận tải) | `GL`: tấn công mạng đi kèm, trừng phạt mới, lừa đảo quyên góp giả |
| Đại dịch đang bùng phát, có phong tỏa | `TT` (doanh thu, thu nhập mất ngay) | `GT`: thay đổi hành vi lâu dài; `GL`: lừa đảo lợi dụng dịch |
| Đại dịch đã qua giai đoạn cấp tính | `GT` | – |
| Thiên tai lớn vừa xảy ra | `TT` | `GT` nếu là hiện tượng lặp lại theo khí hậu; `GL`: lừa đảo cứu trợ |
| Rò rỉ dữ liệu ở một doanh nghiệp lớn khác | `GL` | `TT` nếu doanh nghiệp đó là khách hàng của ngân hàng |
| Quy định mới về xác thực, phòng chống lừa đảo | `TT` (quy định) | `GL`: thủ đoạn sẽ chuyển hướng |

## 4. Tin xảy ra ở nước khác
Thêm một câu hỏi trước khi suy luận: **tin truyền tới Việt Nam qua đường nào?**
- Qua giá thế giới (vàng, dầu, nông sản, kim loại) → `TT`, thường nhanh.
- Qua thương mại và vận tải (đơn hàng, thuế quan, tuyến hàng hải) → `TT`.
- Qua dòng người và dòng tiền (lao động ở nước ngoài, kiều hối, du học, du lịch) → `TT` hoặc `GT`.
- Qua thủ đoạn dùng chung loại kênh (chuyển khoản nhanh, QR, ví điện tử, ứng dụng ngân hàng) → `GL`, kênh `L14`.
- Không thấy đường truyền rõ ràng → viết ngắn, mức "giả thuyết", không ép ra tác động.

## 5. Nhóm tin thay đổi các bước thế nào
| Bước (`core/04_reasoning_procedure.md`) | `TT` | `GT` | `GL` |
|---|---|---|---|
| 1. Ai bị chạm | Xếp khách theo **vai trò trong chuỗi giá trị** của mặt hàng hoặc biến số | Xếp khách theo **vòng đời và vùng địa lý** | Xếp khách và ngân hàng theo **bề mặt tấn công** |
| 2. Lan truyền | Kênh `L01`–`L14`, tối đa 3 hop | Ít hop, độ trễ dài, ghi rõ tầm thời gian | Không lan theo dòng tiền; lan theo kênh dùng chung và độ trễ của thủ đoạn |
| 3. Sản phẩm | Rủi ro và cơ hội gần như ngang nhau | Thiên về điều chỉnh khẩu vị và thiết kế sản phẩm | Sản phẩm, kênh bị lợi dụng; cơ hội thường không có |
| 4. Tín hiệu | `S`, `F`, `G` | Tín hiệu chậm, theo nhóm tuổi, vùng | `X01`–`X08` và `S13` `S14` |
| 6. Kết luận | Mức chắc chắn theo hop | Mặc định "có thể" hoặc "giả thuyết" | Nêu khung thời gian cần hành động; không kết luận hệ thống "bị ảnh hưởng" hay "an toàn" khi chưa xác nhận |

## 6. Ghi vào dòng nhãn
Thêm trường `loai_tin` vào mỗi dòng `[FG]` (xem `core/05_output_prose.md`): `TT`, `GT` hoặc `GL`. Tin nhiều nhóm thì ghi nhóm của **nhánh** đó, ví dụ nhánh tấn công mạng trong tin chiến tranh ghi `GL`.
