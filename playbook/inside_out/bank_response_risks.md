---
id: IO-BANK-RESPONSE
used_by: [Inside-out Monitor, Critic]
steps: [5]
depends_on: [core/02_concepts_patterns.md, fear_greed/fg_01_dual_lens.md]
load_when: Đánh giá rủi ro bậc 2 do chính phản ứng/quyết định của ngân hàng, ở cả pha sợ (siết) và pha tham (nới)
version: v3.4
updated: 2026-11-04
---

# Inside-out: rủi ro bậc 2 do phản ứng của ngân hàng

## Pha Fear – ngân hàng siết hoặc rút lui
| Phản ứng của ngân hàng | Rủi ro bậc 2 có thể phát sinh | Phân khúc chịu tác động |
|---|---|---|
| Siết hạn mức tín chấp/thấu chi | Khách đang căng thẳng mất nguồn đệm → DPD tăng nhanh hơn | KHCN, HKD |
| Tăng lãi suất cho vay | Khoản vay thả nổi tăng nghĩa vụ trả nợ | KHCN mua nhà, CIB trung dài hạn |
| Ngừng giải ngân dự án BĐS | CĐT thiếu dòng tiền → chậm bàn giao → người mua ngừng trả nợ (`L04`) | CIB, KHCN |
| Khóa/phong tỏa tài khoản hàng loạt (theo quy định xác thực/AML) | Gián đoạn kinh doanh HKD, khiếu nại tăng | HKD, KHCN |
| Giảm lãi suất huy động | Rút tiền gửi sang đối thủ | KHCN, SME |
| Chuyển đổi nền tảng (F@st EBank → Techcombank Business) | Rủi ro vận hành, lừa đảo lợi dụng thông báo chuyển đổi | SME, CIB |
| Tạm dừng phân phối iBond/sản phẩm đầu tư | Nhà đầu tư hiểu là tín hiệu xấu → bán lại hàng loạt | KHCN Priority |
| Siết đồng loạt cả ngành, kể cả khách tốt | Khách tốt chuyển sang ngân hàng khác; mất cơ hội ngược chu kỳ `O6` | SME, CIB |

## Pha Greed – ngân hàng nới hoặc đẩy bán
| Phản ứng của ngân hàng | Rủi ro bậc 2 có thể phát sinh | Phân khúc chịu tác động |
|---|---|---|
| Định giá TSBĐ và cấp hạn mức theo giá đỉnh (BĐS, nông sản) | Khi giá quay về, LTV vượt ngưỡng, nợ xấu tăng cùng lúc `CL` `CR` | KHCN, HKD, SME |
| Tăng hạn mức theo doanh thu mùa cao điểm | Hạn mức vượt khả năng trả ở mùa thấp điểm | HKD, SME |
| Đẩy chỉ tiêu bán iBond, iFund, bảo hiểm khi thị trường tăng | Tư vấn sai đối tượng; khiếu nại tập thể khi giá giảm `RP` | KHCN Priority |
| Tập trung tăng trưởng vào một ngành hoặc một chuỗi đang nóng | Rủi ro tập trung; nhà đầu tư lo ngại khi ngành đảo chiều (`L10`) | CIB, SME, NĐT |
| Ưu đãi lãi suất sâu để giành khách vay mua nhà | Cú sốc trả nợ khi hết ưu đãi | KHCN |
| Mở nhanh tài khoản, thẻ cho làn sóng khách mới mà không đủ kiểm tra | Tài khoản bị thuê, mượn cho lừa đảo `FR` `CO` | KHCN, HKD |

## Đo trước khi quyết định
Mỗi phản ứng trong hai bảng trên là một quyết định của ngân hàng, nên có thể đo trước bằng what-if inside-out: phần rủi ro giảm được nhờ quyết định đặt cạnh rủi ro thứ cấp do quyết định sinh ra (khách bị đẩy vượt hạn mức, khách tốt bị chạm oan, khách mất nguồn đệm). Phương pháp ở `inside_out/whatif/io_wi_00_index.md` mục 4; bài mẫu siết hạn mức thẻ ở `inside_out/whatif/examples/io_wi_ex_02_siet_han_muc_the.md`.
