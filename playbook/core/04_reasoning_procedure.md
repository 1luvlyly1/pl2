---
id: CORE-PROCEDURE
used_by: [Orchestrator, ALL]
steps: [1-6]
depends_on: [00_INDEX.md, fear_greed/fg_01_dual_lens.md]
load_when: Orchestrator luôn nạp; agent con nạp khi cần biết bước của mình nhận gì, làm gì và chuyển gì cho bước sau
version: v3.4
updated: 2026-11-04
---

# Quy trình suy luận 6 bước

## 1. Đầu vào và đầu ra
**Đầu vào** là nội dung một sự kiện **đã được người dùng sàng lọc**. Agent không đánh giá sự kiện có đáng xử lý không, không tự tìm thêm tin, không thêm tình tiết. Có thể kèm theo:
- chỉ số hành vi làm bối cảnh (áp dụng `fear_greed/fg_01_dual_lens.md` mục 7);
- dòng `[CUM]` và hồ sơ cụm nếu tin thuộc một cụm tín hiệu.

**Đầu ra** là một bài văn xuôi theo `core/05_output_prose.md`, có cả lăng kính rủi ro (Fear) và cơ hội (Greed), kết thúc bằng 1–3 dòng nhãn `[FG]`. Nếu cần đo định lượng, bài viết được chuyển tiếp cho agent What-if (mục 5).

## 2. Ba việc phải làm ngay ở bước 1
- **Xếp nhóm tin.** Tin outside-in được xếp vào `TT` (tác động trực tiếp), `GT` (gián tiếp, dài hạn) hoặc `GL` (gian lận, lừa đảo, an ninh mạng) theo `outside_in/news/nw_00_router.md`, rồi nạp file của nhóm đó. Nhóm tin quyết định cách đọc ở các bước 2–6. Sự kiện bắt nguồn từ bên trong ngân hàng là `IO`.
- **Tra ngành.** Liệt kê biến số trong tin (giá gì, chính sách gì, vùng nào) và tra `industry/ind_00_index.md` mục 3 để biết ngành nào thiệt, ngành nào lợi; nạp tối đa ba file ngành. Bước 2 dùng mục 3 và 6 của file ngành, bước 3 dùng mục 4, bước 4 dùng mục 5.
- **Chọn mẫu lan truyền** `P1`, `P2` hoặc `P3` theo `core/02_concepts_patterns.md` mục 2.

## 3. Sáu bước
| Bước | Câu hỏi phải trả lời | Agent | File dùng | Chuyển cho bước sau |
|---|---|---|---|---|
| 1 | Tin thuộc nhóm nào? Chạm ai đầu tiên (KHCN, SME, DN lớn hay cấp ngân hàng)? Mẫu lan truyền nào? Ai thiệt, ai lợi? Tâm lý khách hàng thế nào, mỗi nhánh nằm ở ô nào của ma trận A–D? | Propagation | `outside_in/news/nw_00_router.md` và file nhóm tin; `industry/ind_00_index.md` và tối đa 3 file ngành; `core/02_concepts_patterns.md`; `fear_greed/fg_01_dual_lens.md` | Danh sách nút bị chạm đầu tiên ở cả hai phía, mẫu lan truyền, ô của từng nhánh |
| 2 | Rủi ro và dòng tiền tăng lan sang ai, qua kênh nào (`L01`–`L14`), sau bao lâu? Có vòng phản hồi không? Với tin `GL`: thay bằng phạm vi áp dụng và bề mặt tấn công | Propagation | `core/03_linkage_graph.md`; mục (e) file phân khúc; mục 3 và 6 file ngành | Các nhánh lan truyền, mỗi nhánh có kênh, độ trễ, mức chắc chắn |
| 3 | Sản phẩm nào chịu rủi ro, loại rủi ro gì, mức ưu tiên nào? Sản phẩm nào có nhu cầu tăng (`O1`–`O6`), cơ hội có đủ điều kiện chưa? | Product-Impact | Bảng (c) file phân khúc; `core/06_ngan_hang.md` khi chạm cấp ngân hàng; `fear_greed/fg_03_opportunity_map.md`; `core/01_risk_codes.md` | Sản phẩm hai phía, mã rủi ro, mức ưu tiên **P1**–**P3** |
| 4 | Tín hiệu nội bộ nào sẽ xác nhận rủi ro, xác nhận cơ hội, hoặc cho thấy hành vi sợ (`F`) hay tham (`G`)? | Inside-out Monitor | `inside_out/signals.md`; `fear_greed/fg_02_behavior_signals.md`; với tin `GL` thêm `X01`–`X08`; cột "Hành vi khuyến nghị khi xảy ra" của bảng (c) | Danh sách tín hiệu cần kiểm tra và việc con người cần làm |
| 5 | Nếu ngân hàng phản ứng theo tâm lý sợ (siết) hoặc tham (nới, đẩy bán), có tạo rủi ro mới không? | Inside-out Monitor | `inside_out/bank_response_risks.md`; `fear_greed/fg_01_dual_lens.md` mục 6 | Rủi ro thứ cấp do phản ứng của ngân hàng |
| 6 | Hai lăng kính có cân bằng với tầm quan trọng thật không? Mỗi cơ hội có mặt trái và điểm đảo chiều chưa? Có suy diễn quá đà, số bịa, vi phạm ràng buộc nào không? Viết kết luận | Critic | `guardrails.md`; `core/05_output_prose.md` | Bài văn xuôi hoàn chỉnh và dòng nhãn `[FG]` |

## 4. Câu hỏi kiểm tra nhanh ở bước 1
- Sự kiện đổi **doanh thu, chi phí hoặc pháp lý của một tổ chức** trước → `P1`.
- Sự kiện đổi **thu nhập, sức khỏe, tài sản hoặc hành vi của con người** trước → `P2`.
- Sự kiện chạm **cùng lúc** mọi khách qua giá vĩ mô, quy định hay hạ tầng ngân hàng → `P3`.
- Sự kiện bắt nguồn từ **bên trong ngân hàng** → inside-out; còn lại → outside-in.
- Đối tượng là hộ kinh doanh → xét cả `P1` và `P2`, đọc cả hai file KHCN.
- **Ai lợi, ai thiệt?** Liệt kê cả hai, kể cả khi một bên rất nhỏ. Không có thì nói là không thấy.
- **Biến số nào chạm ngành nào?** Cùng một ngành có thể vừa lợi vừa thiệt tùy vai trò trong chuỗi giá trị (người trồng, người thu mua, người xuất khẩu…).
- **Sự kiện có mô tả hành vi đổ xô, sốt, bán tháo, rút tiền, tin đồn không?** Có thì tâm lý cực đoan (ô B hoặc C). Không thì "tâm lý chưa rõ".

## 5. Sau bước 6: chuyển sang what-if (khi cần)
Nếu bài viết có rủi ro mức **P1** hoặc **P2** và cột "Hành vi khuyến nghị" có hướng dẫn "Dữ liệu, what-if", Orchestrator chuyển bài viết và dòng `[FG]` cho agent What-if:
- rủi ro từ tin bên ngoài → `outside_in/whatif/oi_wi_00_index.md`;
- sự kiện bên trong ngân hàng → `inside_out/whatif/io_wi_00_index.md`;
- cả hai dùng phần chung ở `core/whatif_chung/`.

What-if không sửa bài playbook và không đưa con số kết quả ngược vào bài (`guardrails.md` mục 18).

## 6. Mức chắc chắn
Không dùng điểm số. Mỗi nhận định, ở cả hai lăng kính, gắn với một trong ba mức:
- **Có khả năng cao:** nút bị chạm đầu tiên hoặc bước 1, cơ chế rõ ràng và không phụ thuộc điều kiện nào khác.
- **Có thể:** bước 2; hoặc bước 1 nhưng cơ chế phụ thuộc điều kiện (ví dụ "nếu DN không tìm được đơn thay thế").
- **Giả thuyết, cần kiểm chứng:** bước 3 trở lên, hoặc phải dựa vào giả định vì sự kiện thiếu chi tiết.

Có tín hiệu nội bộ đã xác nhận thì được nâng một mức và phải nói rõ tín hiệu nào. Cơ hội chưa thỏa điều kiện đủ chuẩn (`fear_greed/fg_01_dual_lens.md`) không được ở mức "có khả năng cao".
