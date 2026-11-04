---
id: WC-03-CONG-THUC
used_by: [What-if]
steps: [whatif-3]
depends_on: [core/whatif_chung/wc_00_quy_tac.md, core/whatif_chung/wc_02_signal_map.md]
load_when: Luôn nạp khi dựng kịch bản what-if, cho cả cửa outside-in và inside-out
version: v3.4
updated: 2026-11-04
---

# Dựng kịch bản what-if – phần dùng chung

Một kịch bản gồm bốn thành phần: **quần thể** (ai được đo), **cú sốc** (biến nào thay đổi, thay đổi bao nhiêu), **công thức** (cú sốc biến thành ảnh hưởng thế nào) và **mức độ** (cơ sở, vừa, nặng). Agent tự suy luận công thức phù hợp với rủi ro; các mẫu ở mục 4 là điểm xuất phát, không phải danh sách đóng. Cách lấy độ lớn cú sốc khác nhau giữa hai cửa vào và nằm ở file riêng của từng cửa.

## 1. Quần thể: chuyển "ai bị chạm" thành bộ lọc dữ liệu
Bài playbook mô tả nhóm khách bằng lời (công nhân KCN Bắc Ninh, người vay mua nhà hết ưu đãi, DN gỗ xuất khẩu). Agent chuyển mô tả đó thành bộ lọc trên cột có thật:

| Mô tả trong playbook | Bộ lọc dữ liệu | Lưu ý |
|---|---|---|
| Theo vùng (tỉnh, khu công nghiệp) | `cus_info.c_addr_province` thuộc `:province_list` | Không có cột KCN; lọc tỉnh sẽ rộng hơn KCN |
| Theo ngành của DN | `cus_info.gso_code` thuộc `:gso_list`, hoặc `industry_group` | Mã ngành tra bằng từ khóa trên `gso_description` |
| Người lao động của một DN hay một ngành (kênh `L02`) | Khách có `cus_payroll.company_code` thuộc tập DN đã lọc | Chỉ thấy người nhận lương qua ngân hàng |
| Theo tuổi, giới | `cus_info.age`, `gender` | Kiểm tra tỷ lệ null của `age` trước |
| Theo phân khúc, hạng | `cus_info.sector`, `customer_segment`, `priority_class`; `cus_persona.classfication_value` | Một khách có nhiều persona; lọc bằng `EXISTS` |
| Theo sản phẩm | `cus_lending.product_name`, `secured_type`; có dòng trong bảng thẻ, thấu chi | Tên sản phẩm tra bằng truy vấn khám phá |

Khi mô tả trong playbook không có cột tương ứng (ví dụ "hộ kinh doanh mặt phố", "nông hộ"), agent dùng bộ lọc gần nhất rộng hơn và ghi rõ "quần thể bị phình" để người đọc biết kết quả là cận trên, hoặc ghi `GAP` nếu bộ lọc gần nhất quá xa.

## 2. Cú sốc: biến nào thay đổi
| Loại cú sốc | Tham số mẫu | Áp lên cột | Ví dụ |
|---|---|---|---|
| Thu nhập giảm hoặc mất | `:income_cut`, `:job_loss_share` | `cus_payroll.month_income`, `trio_a_hashed_rbg_atxca_service_channel.atxca_amt_sal_sum_l1m` | DN cắt lao động; ngành giảm ca |
| Khoản trả nợ tăng | `:pmt_uplift` | `cus_lending.total_monthly_payment` | Hết ưu đãi lãi suất; ngân hàng tăng biên độ |
| Giá tài sản bảo đảm giảm | `:coll_haircut` | `cus_coll_transformed.nominal_value`, `trio_a_hashed_corp_b.b_monthend_coll_value_min_l1m` | Giá nhà thứ cấp giảm |
| Dòng tiền vào DN giảm | `:inflow_cut` | `trio_a_hashed_corp_atxca_txn_ews.atxca_txn_amt_in_avg_l3m` | Thuế quan, mất đơn hàng |
| Tiền gửi bị rút | `:runoff_<loại>` | `cus_nonlending.ca_eob_balance`, `td_az_eob_balance`, `td_mm_eob_balance` | Tin đồn, đối thủ tăng lãi suất |
| Hạn mức bị dùng nhiều hơn hoặc bị cắt | `:ur_add`, `:limit_cut` | `buncc_amt_ur_*`, `bunod_amt_ur_*`, `buncc_amt_card_limit_max_l1m`, `b_monthend_od_ur_*` | Khách căng tiền; ngân hàng siết hạn mức |
| Thời gian (xu hướng kéo dài) | `:horizon_months` | Tỷ lệ chuyển trạng thái tính từ lịch sử (`inside_out/whatif/io_wi_00_index.md` mục 3) | Tín hiệu trả tối thiểu thẻ tiếp tục tăng |

**Nguồn độ lớn cú sốc** (bắt buộc ghi cho từng tham số):
- **Tin bên ngoài:** con số trong tin, kèm ngày và câu trích. Cách dùng ở `outside_in/whatif/oi_wi_00_index.md` mục 3.
- **Thông số của ngân hàng:** mức tăng lãi suất, mức cắt hạn mức, thời gian sự cố mà ngân hàng đang cân nhắc. Cách dùng ở `inside_out/whatif/io_wi_00_index.md` mục 3.
- **Lịch sử dữ liệu:** tỷ lệ tính được từ chính các tháng trước trong danh mục (ví dụ trong những khách đã trả tối thiểu thẻ 3 tháng, bao nhiêu phần trăm quá hạn sau 3 tháng). Đây là nguồn tốt nhất khi có, vì không cần giả định.
- **Giả định:** khi ba nguồn trên không có. Ghi lý do chọn mức và luôn cho ít nhất hai mức để thấy độ nhạy.

Agent được phép suy ra tham số từ con số có sẵn bằng một phép tính nêu rõ (ví dụ đổi chênh lệch lãi suất thành phần trăm tăng khoản trả theo công thức niên kim với kỳ hạn còn lại giả định). Kết quả phép suy ra vẫn gọi là giả định.

## 3. Mức độ
| Mức | Cách đặt | Mục đích |
|---|---|---|
| Cơ sở | Cú sốc bằng 0, đo hiện trạng | Luôn có, để thấy nhóm nào đã căng trước sự kiện |
| Vừa | Con số trong tin, thông số ngân hàng đang cân nhắc, hoặc giả định trung bình | Kịch bản có khả năng xảy ra |
| Nặng | Cận trên trong tin, gấp 1,5–2 lần mức vừa, hoặc theo hành vi khuyến nghị (ví dụ "rút gấp 3") | Stress test |
| Ngược | Cú sốc đổi dấu | Đo quy mô cơ hội khi playbook có chiều cơ hội |
| Từng nguyên nhân và gộp | Một dòng cho từng nguyên nhân, một dòng gộp | Khi rủi ro có nhiều nguyên nhân cùng lúc, để thấy phần cộng dồn |

## 4. Mẫu công thức
Ký hiệu: `P` khoản trả hằng tháng, `I` thu nhập hằng tháng, `B` đệm thanh khoản (CASA cộng tiền gửi), `OS` dư nợ, `C` giá trị tài sản bảo đảm.

| Mẫu | Công thức | Khi nào dùng | Cách đọc |
|---|---|---|---|
| Tỷ lệ nợ trên thu nhập (DSR) | `DSR = P / I`; sau sốc `P·(1+pmt_uplift) / (I·(1−income_cut))` | Vay mua nhà, tín chấp, khi khoản trả hoặc thu nhập đổi | Vượt `:dsr_limit` là căng |
| Số tháng đệm | `M = B / P` | Người có thể mất thu nhập | `M < :buffer_months` là không đủ tiền trả nợ trong thời gian tìm nguồn thu mới |
| Dư nợ chịu rủi ro kỳ vọng | `EAR = Σ OS` của khách bị gắn cờ căng; với tỷ lệ mất việc: `job_loss_share · Σ OS` | Mọi kịch bản tín dụng | Nhân tỷ lệ với tổng, không chọn ngẫu nhiên khách |
| LTV | `LTV = OS / C`; sau sốc `OS / (C·(1−coll_haircut))` | Thế chấp | Vượt `:ltv_limit` là đệm tài sản mỏng |
| Độ phủ lương của DN | `cov = in·(1−inflow_cut) / payroll` | DN bị sốc doanh thu, lan sang nhân viên | Dưới `:cov_limit` là nguy cơ chậm lương (`S01`) |
| Hạn mức căng | `ur' = least(1, ur + ur_add)`; khi cắt hạn mức `ur' = ur / (1 − limit_cut)` | Thẻ, thấu chi, OD DN | `ur' ≥ 1` là khách bị đẩy vượt hạn mức |
| Dòng ra tiền gửi | `outflow = Σ_loại runoff_loại · số dư_loại` | Tin đồn, cạnh tranh lãi suất | So với bộ đệm thanh khoản do ALM nắm |
| Tỷ lệ chuyển trạng thái | `rate = (số khách trạng thái A tại t có trạng thái B tại t+h) / (số khách trạng thái A tại t)` | Tín hiệu nội bộ đang xấu đi, cần dự phóng | Áp tỷ lệ lịch sử lên nhóm đang có trạng thái A |
| Phơi nhiễm gian lận | Đếm khách, tổng số dư trong quần thể | Tin gian lận | Không mô phỏng thiệt hại |

Khi một khách thiếu biến (thu nhập null, khoản trả null), loại khách đó khỏi phép tính liên quan và **báo số khách bị loại** trong kết quả. Không thay null bằng 0 ở mẫu số, vì như vậy khách sẽ trông như không có rủi ro.

## 5. Khám phá trước khi lọc
Mọi bộ lọc theo giá trị mã đi kèm một truy vấn khám phá (`wc_04_sql.md` mục 5) trả danh sách giá trị và số khách. Agent đề xuất từ khóa tìm (ví dụ `gso_description` chứa "gỗ"); người dùng chọn giá trị rồi điền vào tham số. Truy vấn khám phá cũng nên trả tỷ lệ null của các cột sẽ dùng, để biết trước kết quả có đáng tin không.
