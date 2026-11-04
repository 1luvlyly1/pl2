---
id: CORE-OUTPUT-PROSE
used_by: [Critic, Orchestrator]
steps: [6]
depends_on: [core/04_reasoning_procedure.md, guardrails.md, fear_greed/fg_01_dual_lens.md]
load_when: Khi viết kết luận cuối cùng của một lượt suy luận
version: v3.4
updated: 2026-11-04
---

# Mẫu viết kết luận bằng văn xuôi (Fear & Greed)

Kết luận là một bài viết đọc liền mạch, **350–650 từ**. Không dùng bảng, không dùng JSON. Mã (`L..`, `CN-..`, `O..`, `S..`, `F..`, `G..`) chỉ đặt trong ngoặc sau cụm từ tiếng Việt để tra cứu; câu văn vẫn phải đọc hiểu được khi bỏ mã đi.

## Bố cục 7 đoạn
Mỗi đoạn có một nhiệm vụ riêng. Người đọc (trưởng phòng rủi ro, RM, ban điều hành) thường chỉ đọc đoạn 1, 2 và 7 trước; ba đoạn này phải tự đứng được.

| Đoạn | Nhiệm vụ | Phải có | Tránh |
|---|---|---|---|
| 1. Sự kiện và cách đọc | Cho người đọc biết đây là loại sự kiện gì và bài viết sẽ đi theo hướng nào | Tóm tắt sự kiện bằng lời của mình; outside-in hay inside-out; nhóm tin; mẫu lan truyền; tâm lý khách hàng (bình thường, sợ, tham, chưa rõ) và lý do; ô chính của ma trận | Chép lại nguyên văn tin; kết luận tâm lý không có căn cứ |
| 2. Ai thiệt, ai lợi đầu tiên | Xác định nút bị chạm đầu tiên ở cả hai phía | Tên nhóm khách cụ thể (không phải "khách hàng nói chung"), cơ chế thiệt hoặc lợi; phía nào không có thì nói là không thấy | Liệt kê sản phẩm ở đoạn này |
| 3. Fear – rủi ro lan đi thế nào | Kể đường đi của rủi ro theo từng nhánh | Từ ai sang ai, qua kênh nào (`L..`), sau bao lâu, mức chắc chắn; vòng phản hồi ở cuối đoạn | Đi quá ba bước; mọi bước đều "có khả năng cao" |
| 4. Greed – dòng tiền tăng lan đi thế nào | Kể đường đi của phía hưởng lợi | Như đoạn 3; với nhánh ở ô B, tách phần nhu cầu thật và phần đầu cơ | Ép ra cơ hội khi không có; viết thành lời chào bán |
| 5. Sản phẩm ở hai phía | Nối nhóm khách với sản phẩm | Sản phẩm chịu rủi ro, mã rủi ro, mức ưu tiên; sản phẩm có nhu cầu tăng, loại cơ hội (`O..`), điều kiện đủ chuẩn; theo thứ tự phân khúc như đoạn 3–4 | Liệt kê mọi sản phẩm của phân khúc |
| 6. Tín hiệu cần kiểm tra | Biến nhận định thành việc kiểm chứng được | Tín hiệu xác nhận rủi ro, tín hiệu xác nhận cơ hội, tín hiệu cơ hội đã thành nóng (`G`) hoặc sợ hãi lan rộng (`F`); chưa có số liệu thì nói thẳng | Đưa số liệu tín hiệu khi chưa truy vấn |
| 7. Phản ứng của ngân hàng, điểm đảo chiều, giả định yếu nhất | Giúp người ra quyết định tránh phản ứng sai | Ngân hàng dễ phản ứng sai theo hướng nào; điều kiện làm cơ hội đảo thành rủi ro; giả định yếu nhất của toàn bài | Khuyến nghị cắt hạn mức hay thu hồi nợ đồng loạt |

## Quy tắc viết
- Viết như chuyên viên rủi ro báo cáo cho trưởng phòng: rõ, cụ thể, không rào đón, không cổ vũ. Mỗi câu nói một ý có thể kiểm chứng.
- **Cân bằng theo tầm quan trọng thật.** Đoạn 3 và đoạn 4 dài tương xứng với mức độ của từng phía, không cố viết đều. Sự kiện gần như chỉ có một phía thì phía kia một câu là đủ.
- **Mức chắc chắn đi kèm mỗi nhận định** từ bước 2 trở đi ("có thể", "giả thuyết").
- **Cơ hội viết ở dạng "nhu cầu có thể tăng ở…"**, không viết thành chỉ thị bán hàng nhắm vào khách cụ thể.
- **Chỉ dùng thông tin có trong sự kiện và playbook.** Không viết số liệu không có cơ sở. Không nêu tên khách hàng cụ thể.
- **Ưu tiên chiều sâu** ở 2–3 nhánh quan trọng nhất của mỗi lăng kính thay vì liệt kê nhiều nhánh nông.
- **Mã chỉ để tra cứu.** Đặt mã trong ngoặc sau cụm từ tiếng Việt; bỏ mã đi câu vẫn đọc hiểu được. Sai: "`L02` → `CN-LN-06` P2." Đúng: "Công nhân mất ca có thể chậm trả khoản vay tiêu dùng sau một đến hai kỳ lương (`L02`, `CN-LN-06`)."

## Khung câu gợi ý
> [Sự kiện] là sự kiện [outside-in/inside-out], lan theo mẫu [P..]; tâm lý khách hàng [bình thường/sợ hãi/tham lam/chưa rõ], nên nhánh chính nằm ở ô [A/B/C/D]. Bên thiệt đầu tiên là [phân khúc] vì [cơ chế]; bên hưởng lợi đầu tiên là [phân khúc] vì [cơ chế]. Về rủi ro, [nhánh]… Về cơ hội, dòng tiền tăng có khả năng cao lan sang [phân khúc] qua [kênh] ([L..])… Ở phía sản phẩm, rủi ro tập trung ở [sản phẩm] ([mã]); nhu cầu có thể tăng ở [sản phẩm] ([mã], [O..]) nếu [điều kiện đủ chuẩn]… Để xác nhận, cần kiểm tra [tín hiệu]; nếu thấy [tín hiệu G] thì cơ hội đã chuyển sang nóng… Ngân hàng dễ [phản ứng sai]. Cơ hội sẽ đảo thành rủi ro nếu [điều kiện đảo chiều]. Giả định yếu nhất là […].

## Dòng nhãn [FG] (bắt buộc, đặt sau bài văn)
Sau bài văn xuôi, xuống dòng và ghi **1 đến 3 dòng nhãn**, mỗi dòng cho một nhánh chính (không tính vào số từ). Code dùng các dòng này để tính chỉ số tin tức; viết đúng định dạng, không thêm trường khác.

```
[FG] loai_tin=<nhóm tin> | o=<ô> | tam_ly=<tâm lý> | huong=<hướng> | phan_khuc=<phân khúc> | muc=<mức chắc chắn>
```

| Trường | Giá trị hợp lệ |
|---|---|
| `loai_tin` | `TT` (trực tiếp), `GT` (gián tiếp), `GL` (gian lận, lừa đảo, an ninh mạng), `IO` (sự kiện inside-out). Ghi nhóm của **nhánh** đó |
| `o` | `A`, `B`, `C`, `D`; hai ô thì ghi `A,B` |
| `tam_ly` | `so`, `binh_thuong`, `tham`, `chua_ro` |
| `huong` | `rui_ro`, `co_hoi`, `ca_hai` |
| `phan_khuc` | Một hoặc nhiều trong `KHCN` (gồm cả hộ kinh doanh), `SME`, `CIB` (doanh nghiệp lớn), `NH` (cấp ngân hàng), cách nhau bằng dấu phẩy, không dấu cách |
| `muc` | `co_kha_nang_cao`, `co_the`, `gia_thuyet` |

Ví dụ cho sự kiện giá cà phê lập đỉnh (hai nhánh ở hai ô khác nhau):
```
[FG] loai_tin=TT | o=B | tam_ly=tham | huong=co_hoi | phan_khuc=KHCN,CIB | muc=co_kha_nang_cao
[FG] loai_tin=TT | o=D | tam_ly=chua_ro | huong=rui_ro | phan_khuc=KHCN,SME | muc=co_the
```

## Biến thể theo nhóm tin
- **`GT`:** ghi tầm thời gian cho từng nhánh; đề xuất ở dạng theo dõi định kỳ hoặc xem lại khẩu vị, không cảnh báo khẩn (`outside_in/news/nw_02_gian_tiep.md` mục 5).
- **`GL`:** đoạn 3 viết về bề mặt tấn công thay cho chuỗi lan truyền; đoạn 4 thường là "không thấy cơ hội"; đoạn 6 có danh sách điều cần đội an ninh xác nhận; đoạn 7 nêu khung thời gian hành động (`outside_in/news/nw_03_gian_lan_an_ninh.md` mục 8).
- **Tin nhiều nhóm:** nhóm phụ viết thành một nhánh ngắn và có dòng nhãn riêng.
- **`IO` (sự kiện bên trong ngân hàng):** đoạn 1 nói rõ sự kiện là tín hiệu, quyết định hay sự cố; đoạn 2 thường là "mọi phân khúc cùng lúc" (mẫu `P3`) hoặc nhóm khách mà tín hiệu xuất hiện; đoạn 7 là trọng tâm – phản ứng của ngân hàng quyết định phần lớn thiệt hại. Không kết luận nguyên nhân sự cố hay trách nhiệm (`guardrails.md` mục 21).
- **Tin thuộc một cụm (`[CUM]`):** đoạn 1 nêu tin là một phần của cụm nào và đã có bao nhiêu nguyên nhân; đoạn 3 nói phần cộng dồn (vì sao các nguyên nhân nhỏ cùng lúc nguy hiểm hơn từng cái riêng). Không nhắc điểm cụm.
