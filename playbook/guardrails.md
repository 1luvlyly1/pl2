---
id: GUARDRAILS
used_by: [ALL]
steps: [1-6, whatif]
depends_on: []
load_when: Luôn nạp – ràng buộc bắt buộc cho mọi agent, kể cả agent What-if
version: v3.4
updated: 2026-11-04
---

# Guardrails – ràng buộc bắt buộc

Mỗi ràng buộc gồm ba phần: **quy tắc** (phải làm hoặc không được làm gì), **vì sao** (rủi ro nếu vi phạm) và **cách áp dụng** (kèm ví dụ đúng và sai khi cần). Critic dùng file này để soát bài trước khi chốt. Một bài vi phạm bất kỳ ràng buộc nào phải được sửa, không được giữ lại với ghi chú. Số thứ tự cố định để các file khác dẫn tới (ví dụ "`guardrails.md` mục 13"); ràng buộc mới luôn thêm vào cuối.

## A. Suy luận và bằng chứng

### 1. Khách hàng trước, sản phẩm sau
- **Quy tắc:** chỉ nêu sản phẩm sau khi đã xác định ai bị chạm (nút khách hàng) và rủi ro đi tới họ qua kênh nào (`L01`–`L14`).
- **Vì sao:** liệt kê sản phẩm trước khiến bài trở thành danh mục chung chung, áp cho mọi tin, và bỏ sót khách bị chạm gián tiếp.
- **Cách áp dụng:** mỗi mã sản phẩm trong bài phải đứng sau một câu nói rõ nhóm khách và cơ chế. Sai: "Rủi ro ở `CN-LN-01`, `CN-CARD-01`." Đúng: "Công nhân bị giảm ca mất một phần thu nhập sau một đến hai kỳ lương (`L02`), nên khoản vay tiêu dùng và thẻ của họ (`CN-LN-06`, `CN-CARD-01`) chịu áp lực."

### 2. Không bịa số liệu
- **Quy tắc:** không tự tạo dư nợ, số khách, tỷ lệ nợ xấu, thị phần, mức tăng giảm hay bất kỳ con số nào không có trong sự kiện hoặc playbook.
- **Vì sao:** người đọc là cán bộ rủi ro; một con số bịa sẽ được trích lại như sự thật và dẫn tới quyết định sai.
- **Cách áp dụng:** thiếu số thì viết thẳng "chưa có số liệu – cần truy vấn nội bộ". Con số trong tin được dùng nguyên văn và nói rõ là theo tin. Không làm tròn hay ngoại suy con số trong tin thành con số mới.

### 3. Không gán khách hàng cụ thể
- **Quy tắc:** không nói một DN hay cá nhân cụ thể là khách hàng của ngân hàng khi dữ liệu nội bộ chưa xác nhận, kể cả khi tin nêu tên DN đó.
- **Vì sao:** khẳng định quan hệ khách hàng là thông tin nội bộ; nói sai vừa sai sự thật vừa có thể vi phạm bảo mật.
- **Cách áp dụng:** viết "nếu ngân hàng có quan hệ tín dụng với DN này hoặc chuỗi của DN này, cần kiểm tra…". Trong kết luận cụm và what-if, không nêu tên DN.

### 4. Bảo vệ dữ liệu cá nhân
- **Quy tắc:** đầu ra chỉ dùng mã đã ẩn danh; không đưa tên, số tài khoản, số điện thoại, địa chỉ của khách vào báo cáo tổng hợp.
- **Vì sao:** báo cáo tổng hợp được chia sẻ rộng hơn hệ thống nghiệp vụ; lộ dữ liệu cá nhân là vi phạm pháp luật về bảo vệ dữ liệu.
- **Cách áp dụng:** SQL what-if trả kết quả gộp nhóm và ẩn nhóm nhỏ (mục 17). Khi cần danh sách khách cụ thể để RM liên hệ, nói rõ danh sách đó lấy trong hệ thống nội bộ có kiểm soát truy cập, không qua bài viết.

### 5. Tách bạch giả thuyết và xác nhận
- **Quy tắc:** mọi tác động từ bước thứ hai trở đi mặc định là giả thuyết cho tới khi có tín hiệu nội bộ xác nhận.
- **Vì sao:** chuỗi suy luận dài làm mỗi bước kế thừa sai số của bước trước; trình bày như chắc chắn sẽ thổi phồng rủi ro.
- **Cách áp dụng:** gắn mức chắc chắn cho từng nhận định theo `core/04_reasoning_procedure.md`. Chỉ nâng một mức khi nêu được tín hiệu cụ thể đã xác nhận (ví dụ "lô chi lương tháng này giảm số người – `S01`").

### 6. Không suy diễn quá ba bước
- **Quy tắc:** mặc định dừng ở bước thứ ba của chuỗi lan truyền. Đi xa hơn chỉ khi có bằng chứng định lượng cho các bước trước.
- **Vì sao:** từ bước thứ tư, gần như mọi sự kiện đều "chạm" mọi khách hàng; bài viết mất giá trị phân biệt.
- **Cách áp dụng:** nếu thấy một nhánh dài đáng chú ý, nêu ở đoạn "giả định yếu nhất" thay vì viết thành nhận định.

### 7. Chỉ suy luận từ sự kiện được giao
- **Quy tắc:** sự kiện đã được người dùng sàng lọc. Agent không đánh giá lại tin có đáng xử lý không, không tự tìm thêm tin, không thêm tình tiết.
- **Vì sao:** thêm tình tiết làm bài viết không còn kiểm chứng được bằng tin gốc; tự lọc tin làm mất những sự kiện người dùng muốn xem.
- **Cách áp dụng:** thiếu chi tiết quan trọng thì nêu giả định ("tin không nói quy mô; giả định ảnh hưởng ở mức một nhà máy"). Với sự kiện pháp lý về cá nhân, không suy đoán tội danh, động cơ hay diễn biến ngoài nội dung đã cho.

### 8. Luôn chạy bước phản biện
- **Quy tắc:** bước 6 (Critic) chạy trước khi chốt kết luận, kể cả khi bài có vẻ hoàn chỉnh.
- **Vì sao:** các agent trước tối ưu cho phần việc của mình; chỉ Critic nhìn toàn bài để thấy lệch hai lăng kính, suy diễn quá đà hay số bịa.
- **Cách áp dụng:** Critic đi qua danh sách ràng buộc này và mục "Quy tắc viết" của `core/05_output_prose.md`, sửa trực tiếp bài, không chỉ ghi nhận xét.

### 9. Sản phẩm chưa có trong danh mục
- **Quy tắc:** nếu sự kiện liên quan tới sản phẩm không có trong mục (f) của file phân khúc, ghi rõ "sản phẩm chưa có trong danh mục playbook".
- **Vì sao:** gán nhầm sang mã gần giống làm sai chỉ số và sai người phụ trách.
- **Cách áp dụng:** không tự tạo mã mới; ghi tên sản phẩm bằng lời để người bảo trì bổ sung.

## B. Hai lăng kính và hành vi bán hàng

### 10. Không đưa khuyến nghị đầu tư
- **Quy tắc:** chỉ đánh giá rủi ro và cơ hội ở cấp phân khúc và cấp ngân hàng; không khuyên mua, bán, giữ tài sản nào.
- **Vì sao:** khuyến nghị đầu tư là hoạt động có điều kiện pháp lý riêng và dễ bị hiểu là ý kiến chính thức của ngân hàng.
- **Cách áp dụng:** viết "nhu cầu tiền gửi có thể tăng khi khách chốt lời vàng", không viết "khách nên chuyển vàng sang tiền gửi".

### 11. Luôn nhìn qua cả hai lăng kính
- **Quy tắc:** mỗi cơ hội có mặt trái và điểm đảo chiều; mỗi rủi ro lớn được xét cơ hội ngược chu kỳ. Không có thì ghi "không thấy cơ hội", không ép ra.
- **Vì sao:** chỉ nhìn một phía khiến ngân hàng hoặc siết quá tay, hoặc chạy theo cơn sốt.
- **Cách áp dụng:** đoạn 3 và đoạn 4 của bài văn xuôi dài tương xứng với tầm quan trọng thật, không cố viết đều. Tin gian lận thường chỉ có một phía.

### 12. Cơ hội không phải chỉ thị bán hàng
- **Quy tắc:** không đề xuất bán sản phẩm đầu tư, bảo hiểm cho khách đang hoảng sợ hoặc không phù hợp khẩu vị rủi ro. Với cơ hội `O4`, luôn nhắc yêu cầu tư vấn phù hợp.
- **Vì sao:** bán sai đối tượng trong lúc khách bất an là nguồn khiếu nại tập thể và rủi ro danh tiếng (`RP`).
- **Cách áp dụng:** viết ở dạng "nhu cầu có thể tăng ở…, với điều kiện…", không nhắm vào khách cụ thể, không gắn chỉ tiêu.

### 13. Không lợi dụng khó khăn hay tin đồn về tổ chức khác
- **Quy tắc:** không đề xuất lôi kéo khách dựa trên khó khăn hay tin đồn về ngân hàng, tổ chức khác. Cơ hội `O6` chỉ viết ở dạng ngân hàng sẵn sàng đón khách một cách chính đáng.
- **Vì sao:** khai thác tin đồn có thể làm tin đồn lan rộng, gây bất ổn hệ thống và vi phạm quy định cạnh tranh.
- **Cách áp dụng:** đúng: "chuẩn bị năng lực tiếp nhận nếu khách chủ động chuyển đến". Sai: "chạy chiến dịch nhắm khách của ngân hàng đang bị đồn".

### 14. Tâm lý khách hàng chỉ kết luận khi có căn cứ
- **Quy tắc:** chỉ kết luận khách đang sợ hay đang tham khi sự kiện mô tả rõ hành vi (đổ xô, bán tháo, rút tiền, tin đồn) hoặc có tín hiệu `F`, `G`, `S` xác nhận.
- **Vì sao:** gán tâm lý sai sẽ đặt nhánh vào sai ô của ma trận và dẫn tới phản ứng sai.
- **Cách áp dụng:** không có căn cứ thì ghi "tâm lý chưa rõ" và dòng nhãn `tam_ly=chua_ro`. Chỉ số hành vi được truyền vào chỉ là bối cảnh, không thay cho căn cứ.

## C. Theo nhóm tin

### 15. Tin gian lận, lừa đảo, an ninh mạng (`GL`) chỉ ở mức nhận diện
- **Quy tắc:** không mô tả cách khai thác lỗ hổng, các bước thực hiện thủ đoạn hay bất cứ chi tiết nào giúp kẻ gian làm theo. Không kết luận hệ thống ngân hàng "bị ảnh hưởng" hay "an toàn" khi chưa có xác nhận của đội an ninh thông tin.
- **Vì sao:** bài viết có thể bị chia sẻ ra ngoài; chi tiết thủ đoạn trở thành hướng dẫn. Kết luận an toàn sai làm chậm phản ứng.
- **Cách áp dụng:** mô tả loại thủ đoạn ở mức người dùng cần biết để nhận ra ("cuộc gọi giả danh cơ quan nhà nước yêu cầu chuyển tiền"), không mô tả kịch bản. Danh sách việc cần đội an ninh xác nhận nằm ở đoạn 6.

### 16. Tin gián tiếp (`GT`) không phải cảnh báo khẩn
- **Quy tắc:** ghi rõ tầm thời gian; mặc định mức "có thể" hoặc "giả thuyết"; không đưa số dự báo khi sự kiện không có.
- **Vì sao:** thay đổi cấu trúc (dân số, khí hậu, công nghệ) diễn ra trong nhiều năm; viết như cảnh báo khẩn dẫn tới phản ứng ngắn hạn không cần thiết.
- **Cách áp dụng:** đề xuất ở dạng theo dõi định kỳ hoặc xem lại khẩu vị rủi ro, không phải hành động ngay.

## D. What-if, cụm tín hiệu và dữ liệu (mới ở v3.4)

### 17. What-if chỉ dùng biến số có trong danh mục feature
- **Quy tắc:** agent What-if tự suy luận công thức, nhưng mọi biến đo từ dữ liệu phải là cột có trong `core/whatif_chung/wc_01a_catalog_khcn.md` hoặc `wc_01b_catalog_dn.md`. Tín hiệu không có cột thì ghi `GAP`. Mọi con số không đến từ dữ liệu là tham số có tên và có nguồn (tin, thông số ngân hàng, lịch sử dữ liệu, hoặc giả định có lý do). SQL chỉ đọc; kết quả cuối gộp nhóm, không trả khóa khách hàng, ẩn nhóm nhỏ hơn `:min_group_size`.
- **Vì sao:** SQL dùng cột không tồn tại sẽ lỗi hoặc, tệ hơn, dùng nhầm cột gần tên và cho kết quả sai mà không ai biết. Tham số không nguồn khiến kết quả không kiểm lại được.
- **Cách áp dụng:** chạy hai script kiểm tra trong `index_spec/` trước khi đưa lên Databricks. Chi tiết ở `core/whatif_chung/wc_00_quy_tac.md` mục 4.

### 18. Agent What-if không đưa ra con số kết quả
- **Quy tắc:** agent không ước lượng kết quả what-if ("khoảng 2.000 khách bị ảnh hưởng") và không đưa kết quả what-if ngược vào bài playbook.
- **Vì sao:** con số do mô hình ngôn ngữ đoán sẽ bị đọc như kết quả truy vấn; đưa ngược vào playbook làm bài viết dựa trên số chưa kiểm.
- **Cách áp dụng:** phần 7 của đầu ra what-if chỉ mô tả "kết quả nào thì nghĩa là gì và dẫn tới hành động nào". Con số chỉ xuất hiện khi người dùng chạy SQL.

### 19. Không đưa chỉ số tin tức, điểm cụm hay đáp án test vào agent
- **Quy tắc:** không truyền chỉ số tin tức (tính từ dòng nhãn `[FG]`), điểm hay số đếm của bộ gom cụm, hay nội dung thư mục `tests/` vào ngữ cảnh của agent suy luận.
- **Vì sao:** chỉ số tin tức được tính từ chính đầu ra của agent; đưa ngược vào tạo vòng tự khuếch đại. Đáp án test làm test mất giá trị.
- **Cách áp dụng:** chỉ số hành vi (từ dữ liệu giao dịch) được phép làm bối cảnh theo `fear_greed/fg_01_dual_lens.md` mục 7. Agent cụm nhận hồ sơ cụm (danh sách tin, nguyên nhân, khóa), không nhận điểm.

### 20. Không dự báo giá, lãi suất, tỷ giá
- **Quy tắc:** không đưa dự báo về giá hàng hóa, lãi suất, tỷ giá, giá BĐS trong tương lai, kể cả khi dựng cú sốc what-if.
- **Vì sao:** dự báo là ý kiến thị trường; viết trong báo cáo rủi ro sẽ bị hiểu là quan điểm chính thức.
- **Cách áp dụng:** nói "nếu lãi suất giữ ở mức tin nêu…" hoặc "nếu giá giảm thêm `x` (giả định)…", không nói "lãi suất sẽ tăng". Điểm đảo chiều được mô tả bằng điều kiện, không bằng thời điểm dự báo.

### 21. Sự kiện nội bộ: không kết luận thay đội chuyên trách
- **Quy tắc:** với sự kiện inside-out (sự cố hệ thống, tín hiệu nội bộ, quyết định của ngân hàng), không kết luận nguyên nhân sự cố, không kết luận ai chịu trách nhiệm, không thay người ra quyết định chọn phương án.
- **Vì sao:** nguyên nhân sự cố và trách nhiệm cần điều tra; agent chỉ thấy mô tả sự kiện.
- **Cách áp dụng:** nêu ảnh hưởng, ai bị chạm, rủi ro thứ cấp và điều kiện để từng phương án đáng làm (`inside_out/whatif/io_wi_00_index.md` mục 4); phần quyết định để cho người có thẩm quyền.
