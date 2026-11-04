---
id: FG-DUAL-LENS
used_by: [Orchestrator, Propagation, Critic]
steps: [1, 2, 6]
depends_on: [core/02_concepts_patterns.md]
load_when: Luôn nạp ở bước 1 – mọi sự kiện đều được nhìn qua hai lăng kính Fear (rủi ro) và Greed (cơ hội)
version: v2.1
updated: 2026-11-02
---

# Hai lăng kính Fear & Greed

## 1. Nguyên tắc
Mỗi sự kiện đều được nhìn qua **hai lăng kính**, kể cả khi sự kiện nghe có vẻ chỉ tốt hoặc chỉ xấu.

| Lăng kính | Câu hỏi | Kết quả |
|---|---|---|
| **Fear – Rủi ro** | Ai thiệt? Dòng tiền của ai giảm? Sản phẩm nào chịu rủi ro? | Rủi ro cần phòng ngừa (playbook rủi ro hiện có) |
| **Greed – Cơ hội** | Ai hưởng lợi? Dòng tiền của ai tăng? Nhu cầu tài chính mới nào phát sinh? | Cơ hội kinh doanh, kèm mặt trái |

Ba quy tắc ràng buộc hai lăng kính với nhau:
1. **Một sự kiện thường vừa là Fear với nhóm này vừa là Greed với nhóm khác.** Giá cà phê tăng có lợi cho người trồng và nhà xuất khẩu, nhưng có hại cho quán cà phê và nhà rang xay.
2. **Không có cơ hội nào không có mặt trái.** Mỗi cơ hội phải nêu điều kiện để nó biến thành rủi ro (điểm đảo chiều).
3. **Mỗi rủi ro lớn phải được kiểm tra xem có cơ hội ngược chu kỳ không**, ví dụ khách hàng tốt bị nơi khác siết tín dụng, hoặc tiền gửi tìm nơi an toàn hơn. Nếu không có thì viết rõ là không có; không ép ra cơ hội.

## 2. Hai trục: tác động cơ bản và tâm lý khách hàng
Fear & Greed có hai tầng, agent phải tách riêng:

- **Tác động cơ bản:** sự kiện làm dòng tiền thật của khách hàng tăng hay giảm (doanh thu, thu nhập, giá tài sản, chi phí).
- **Tâm lý khách hàng:** khách hàng phản ứng bình thường, **sợ hãi** (rút tiền, bán tháo, co lại) hay **tham lam** (đổ xô mua, vay để đầu cơ, mở rộng theo giá đỉnh).

Tâm lý có thể khuếch đại hoặc đi ngược tác động cơ bản. Một tin đồn không có tác động cơ bản vẫn có thể gây rút tiền hàng loạt. Một đợt tăng giá có thật vẫn có thể bị khách hàng đẩy thành bong bóng.

**Cách xác định tâm lý:** chỉ kết luận khi sự kiện mô tả rõ hành vi ("đổ xô", "sốt", "lập đỉnh", "cháy hàng", "bán tháo", "xếp hàng rút tiền", "mất niềm tin", "tin đồn") hoặc khi có tín hiệu nội bộ (`fear_greed/fg_02_behavior_signals.md`). Không có các dấu hiệu đó thì ghi **"tâm lý chưa rõ"** và liệt kê tín hiệu cần kiểm tra.

## 3. Ma trận bốn ô
Xếp sự kiện (hoặc từng nhánh của sự kiện) vào một ô. Một sự kiện có thể có nhánh ở nhiều ô khác nhau.

| | **Tâm lý bình thường / chưa rõ** | **Tâm lý cực đoan** |
|---|---|---|
| **Tác động cơ bản có lợi** | **Ô A – Cơ hội lành mạnh.** Mở rộng có kiểm soát theo dòng tiền thật. | **Ô B – Cơ hội nóng (Greed).** Cơ hội ngắn hạn có thật nhưng rủi ro đang tích tụ: đòn bẩy, định giá tài sản theo đỉnh, bán sai đối tượng. Mở rộng có trần. |
| **Tác động cơ bản bất lợi** | **Ô D – Rủi ro cơ bản.** Xử lý theo playbook rủi ro. Tìm cơ hội ngược chu kỳ: giữ chân khách tốt, hỗ trợ cơ cấu, tiền gửi tìm nơi an toàn. | **Ô C – Rủi ro khuếch đại (Fear).** Rủi ro thanh khoản và danh tiếng lan nhanh hơn tác động thật. Ưu tiên thanh khoản, truyền thông, chống lừa đảo. |

**Trường hợp đặc biệt:** tác động cơ bản gần như bằng 0 nhưng tâm lý cực đoan (tin đồn, phong trào đầu tư) → xếp vào ô B hoặc C theo hướng tâm lý, và ghi rõ "rủi ro do hành vi, không do cơ bản".

## 4. Điểm đảo chiều
Ô B là nơi rủi ro tương lai được sinh ra. Với mỗi nhánh ở ô B, agent phải nêu ít nhất một **điều kiện đảo chiều** có thể đẩy nhánh đó sang ô C hoặc D:

- Giá hàng hóa hoặc tài sản quay đầu.
- Lãi suất tăng trở lại, hoặc hết thời gian ưu đãi lãi suất.
- Quy định mới siết lại (tín dụng, trái phiếu, thuế).
- Tin xấu về một doanh nghiệp đầu ngành hoặc tổ chức phát hành lớn.
- Mùa vụ kết thúc, đơn hàng của doanh nghiệp đầu chuỗi giảm.

Ngược lại, ô C và D có thể có **điểm hồi phục**. Nếu sự kiện nêu ra thì ghi lại, nhưng không suy đoán khi nào thị trường hồi phục.

## 5. Sáu loại cơ hội
Dùng mã khi viết sản phẩm hưởng lợi.

| Mã | Loại cơ hội | Ví dụ |
|---|---|---|
| `O1` | Tín dụng mới / tăng hạn mức | Vốn lưu động cho DN xuất khẩu khi giá hàng hóa tăng |
| `O2` | Huy động & CASA | Tiền gửi mới sau mùa vụ; tài khoản lương của công nhân mới |
| `O3` | Thanh toán, FX & phí | L/C xuất khẩu, bán ngoại tệ, giao dịch thẻ, QR, bảo lãnh |
| `O4` | Bán chéo đầu tư, bảo hiểm | iBond, iFund, bảo hiểm tích lũy cho khách có tiền nhàn rỗi |
| `O5` | Chất lượng nợ cải thiện | Khách đang vay có dòng tiền tốt hơn, khả năng trả nợ tăng |
| `O6` | Giành khách / thị phần | HKD chuyển lên DN; tiền gửi tìm nơi an toàn; khách tốt bị nơi khác siết |

`O4` và `O6` là hai loại dễ sinh rủi ro hành vi bán hàng (`RP`). Luôn kèm điều kiện phù hợp sản phẩm và không lợi dụng khó khăn của bên khác (xem `guardrails.md`).

## 6. Ngân hàng cũng sợ và tham
Phản ứng của chính ngân hàng có thể đi theo tâm lý thị trường và làm nặng thêm vấn đề:

| Pha | Biểu hiện ở ngân hàng | Rủi ro sinh ra |
|---|---|---|
| Greed | Nới tiêu chuẩn cấp tín dụng theo giá đỉnh; đẩy chỉ tiêu bán iBond, bảo hiểm; tập trung vào ngành đang nóng | Tín dụng xấu đi khi đảo chiều; khiếu nại tư vấn sai; rủi ro tập trung |
| Fear | Siết đồng loạt, cắt hạn mức cả khách tốt; dừng phân phối sản phẩm đột ngột | Đẩy khách tốt vào khó khăn; mất khách; thị trường hiểu là tín hiệu xấu |

Chi tiết phản ứng theo từng trường hợp xem `inside_out/bank_response_risks.md`.

## 7. Bối cảnh chỉ số hành vi (khi có)
Khi hệ thống đã tính được **chỉ số hành vi** (0–100, từ dữ liệu giao dịch nội bộ), orchestrator có thể truyền vào kèm sự kiện, ví dụ: `Bối cảnh: chỉ số hành vi KHCN = 78 (Tham lam cực độ)`. Agent dùng như sau:

| Chỉ số hành vi | Agent phải làm thêm |
|---|---|
| ≥ 75 (Tham lam cực độ) | Với mọi cơ hội, soi kỹ tín hiệu `G` và nêu điểm đảo chiều; cảnh báo ngân hàng nới theo giá đỉnh |
| 55–74 (Tham lam) | Nêu ít nhất một tín hiệu `G` cho nhánh cơ hội chính |
| 45–54 (Trung lập) | Không điều chỉnh |
| 25–44 (Sợ hãi) | Nêu ít nhất một tín hiệu `F` cho nhánh rủi ro chính |
| ≤ 24 (Sợ hãi cực độ) | Xét rủi ro thanh khoản và lừa đảo trước, rồi mới tới cơ hội ngược chu kỳ |

Ba điều không được làm:
- Không dùng chỉ số để thay cho căn cứ trong sự kiện. Tâm lý trong ô ma trận vẫn chỉ kết luận theo `guardrails.md` mục 14; chỉ số chỉ là bối cảnh.
- Không nhận **chỉ số tin tức** làm đầu vào. Chỉ số này sinh ra từ chính output của agent; đưa ngược sẽ tạo vòng tự khuếch đại.
- Không có chỉ số thì bỏ qua mục này; không tự ước lượng chỉ số.
