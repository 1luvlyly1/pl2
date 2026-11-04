---
id: WC-00-QUY-TAC
used_by: [What-if]
steps: [whatif-1, whatif-2, whatif-3, whatif-4, whatif-5, whatif-6]
depends_on: [00_INDEX.md]
load_when: Luôn nạp khi gọi agent What-if, dù rủi ro đến từ tin bên ngoài (outside-in) hay từ sự kiện bên trong ngân hàng (inside-out)
version: v3.4
updated: 2026-11-04
---

# What-if dùng chung – vai trò, quy trình, quy tắc cứng

## 1. What-if làm gì
Playbook trả lời câu hỏi định tính: sự kiện chạm ai, lan qua đâu, rơi vào sản phẩm nào. What-if trả lời câu hỏi định lượng tiếp theo: **nếu điều đó xảy ra ở một mức nhất định, bao nhiêu khách và bao nhiêu dư nợ, số dư bị ảnh hưởng**. Agent What-if (Opus) dựng kịch bản, tự suy luận công thức và viết SQL; người dùng chạy SQL trên Databricks và đọc kết quả.

Điểm cốt lõi: **công thức do agent suy luận, còn mọi biến số đo từ dữ liệu phải là cột có trong danh mục feature của ngân hàng** (`wc_01a_catalog_khcn.md`, `wc_01b_catalog_dn.md`; bản máy đọc `feature_catalog.csv`). Khi tín hiệu cần đo không có cột tương ứng, agent khai báo thiếu dữ liệu (`GAP`) và đề xuất cột cần bổ sung, chứ không tự đặt ra một cột "chắc là có".

## 2. Hai cửa vào và phần riêng của mỗi cửa
| Cửa vào | Đầu vào agent nhận | Phần riêng | Bài mẫu |
|---|---|---|---|
| **Outside-in** – rủi ro từ tin bên ngoài | Bài văn xuôi của playbook, dòng `[FG]`, có thể kèm dòng `[CUM]` của cụm tín hiệu | `outside_in/whatif/oi_wi_00_index.md`: lấy độ lớn cú sốc từ con số trong tin, dựng chuỗi nhiều bước, cộng dồn nguyên nhân của cụm | `outside_in/whatif/examples/` |
| **Inside-out** – rủi ro từ bên trong ngân hàng | Mô tả sự kiện nội bộ: tín hiệu nội bộ đang xấu đi, quyết định của ngân hàng (lãi suất, hạn mức, phí, khẩu vị), sự cố hệ thống, rủi ro tập trung | `inside_out/whatif/io_wi_00_index.md`: lấy độ lớn cú sốc từ thông số quyết định hoặc từ tỷ lệ lịch sử tính bằng chính dữ liệu; đo rủi ro do phản ứng của ngân hàng | `inside_out/whatif/examples/` |

Phần dùng chung nằm trong thư mục này và áp dụng cho cả hai cửa.

| File | Nội dung | Nạp khi |
|---|---|---|
| `wc_00_quy_tac.md` | File này: quy trình, quy tắc cứng, vấn đề dữ liệu đã biết | Luôn |
| `wc_01a_catalog_khcn.md` | Danh mục cột của bảng khách hàng, khoản vay và bảng hành vi KHCN | Luôn |
| `wc_01b_catalog_dn.md` | Danh mục cột của bảng doanh nghiệp (SME, CIB) | Khi rủi ro chạm SME, CIB hoặc chuỗi DN → nhân viên |
| `wc_02_signal_map.md` | Mỗi tín hiệu playbook (`S`, `F`, `G`, `X`) và nhóm sản phẩm đo bằng cột nào, cột nào chỉ đo gần đúng, tín hiệu nào chưa có dữ liệu | Luôn |
| `wc_03_cong_thuc.md` | Cách chọn quần thể, đặt cú sốc, mức độ, các mẫu công thức | Luôn |
| `wc_04_sql.md` | Quy ước SQL Databricks, khóa khách hàng, kỳ dữ liệu, truy vấn khám phá, script kiểm tra | Luôn |
| `wc_05_dau_ra.md` | Khuôn đầu ra 8 phần và dòng nhãn `[WI]` | Luôn |
| `feature_catalog.csv` | Danh mục máy đọc, dùng cho script kiểm tra | Không nạp cho agent |

## 3. Quy trình 6 bước
1. **Chọn rủi ro cần đo.** Chọn 1–3 rủi ro có sản phẩm ở mức ưu tiên **P1** hoặc **P2** và có hướng dẫn "Dữ liệu, what-if" trong cột "Hành vi khuyến nghị khi xảy ra" của bảng (c) file phân khúc. Rủi ro chỉ ở mức "giả thuyết" vẫn được đo nhưng phải gọi là kịch bản thăm dò, để người đọc không coi kết quả là cảnh báo.
2. **Ánh xạ sang dữ liệu.** Với từng tín hiệu và sản phẩm, tra `wc_02_signal_map.md` để biết cột cụ thể. Ghi rõ mỗi biến thuộc loại nào: cột đo trực tiếp; cột thay thế (nói vì sao nó chỉ gần đúng); hoặc thiếu dữ liệu (`GAP`).
3. **Dựng kịch bản.** Theo `wc_03_cong_thuc.md` và phần riêng của cửa vào: ai là quần thể, biến nào bị sốc và sốc bao nhiêu, công thức ảnh hưởng, ít nhất hai mức (vừa, nặng) cộng mức cơ sở để so.
4. **Viết SQL.** Theo `wc_04_sql.md`: truy vấn khám phá cho mọi giá trị mã chưa biết trước, rồi truy vấn chính. Mọi cột lấy từ bảng gốc viết kèm bí danh bảng.
5. **Tự kiểm.** Đối chiếu từng cột với danh mục, liệt kê cột cần xác nhận, chạy qua danh sách ở mục 5.
6. **Viết đầu ra.** Theo `wc_05_dau_ra.md`, kết thúc bằng dòng `[WI]`.

Agent What-if **không** chạy SQL, không thấy dữ liệu khách hàng và không tự đưa ra con số kết quả. Kết quả chỉ xuất hiện khi người dùng chạy SQL.

## 4. Quy tắc cứng
1. **Chỉ dùng bảng và cột có trong danh mục.** Không đổi tên cột, không đoán cột. Các thông tin hiện **không có** trong danh mục gồm: lãi suất hợp đồng, kỳ hạn còn lại, ngày hết ưu đãi, doanh thu QR, rút tiền CDM, quan hệ anchor–spoke, đăng nhập và thiết bị, khiếu nại. Cột dẫn xuất trong CTE được đặt tên tự do nhưng phải tính từ cột trong danh mục.
2. **Không đoán giá trị mã.** Tên tỉnh, `gso_code`, `product_name`, `secured_type`, `tsdb_mt`, `customer_segment`, `classfication_value`, `priority_class`, `sector` phải lấy bằng truy vấn khám phá. Trong truy vấn chính, chúng là tham số danh sách (ví dụ `:province_list`) để người dùng điền sau khi xem kết quả khám phá.
3. **Mọi số không đến từ dữ liệu là tham số có tên và có nguồn.** Nguồn là một trong ba loại: tin bên ngoài (ghi ngày và câu trích), quyết định hay thông số của ngân hàng (ghi văn bản hoặc người cung cấp), hoặc giả định (ghi lý do chọn mức đó). Không viết số giả định trực tiếp giữa câu SQL.
4. **SQL chỉ đọc.** Chỉ dùng `SELECT` và `WITH`; không ghi, sửa, tạo hay xóa bảng.
5. **Đầu ra chỉ ở dạng gộp nhóm.** Câu `SELECT` cuối không trả `customer_code`, `cusid`, `cus_key`, `company_code`, `coll_id`; nhóm có ít khách hơn `:min_group_size` bị ẩn để không lộ khách cụ thể.
6. **Không kết luận thay dữ liệu.** Agent không ước lượng kết quả kiểu "khoảng 2.000 khách bị ảnh hưởng". Agent chỉ mô tả kết quả nào thì nghĩa là gì và dẫn tới hành động nào.
7. **Khai báo thiếu dữ liệu đúng chỗ.** Tín hiệu không đo được ghi `GAP` kèm cột đề xuất bổ sung. Không lấp chỗ trống bằng một cột không liên quan chỉ để có số.
8. **Kế thừa `guardrails.md`.** Không nêu tên khách hay DN; tin gian lận chỉ ở mức nhận diện; không đề xuất cắt hạn mức hay thu hồi nợ đồng loạt; không dùng khó khăn của khách để bán sản phẩm.

## 5. Danh sách tự kiểm
- Mọi `bí_danh.cột` trỏ tới bảng gốc đều có trong danh mục và đúng bảng.
- Không dùng hai cột bị chặn: `cus_coll_transformed.ds_parition_date` (sai chính tả) và `cus_coll_transformed.td_mm_current_balance` (nghi đặt nhầm bảng).
- Cột có cờ `?` hoặc `A` được liệt kê ở mục "Cần xác nhận" của đầu ra.
- Bảng `cus_*` có cột `ds_partition_date` thì lọc theo ngày chụp; bảng `trio_*` luôn lọc `month = :as_of_month`. Kịch bản dùng nhiều tháng lịch sử (inside-out) ghi rõ khoảng tháng.
- `cus_lending`, `cus_coll_transformed`, `cus_persona` được gộp về một dòng mỗi khách trước khi nối, để không nhân đôi dư nợ.
- Mọi phép chia dùng `NULLIF(…, 0)`; mọi ngưỡng là tham số.
- Câu cuối gộp nhóm và có `HAVING COUNT(*) >= :min_group_size`.
- Mỗi tham số danh sách mã có truy vấn khám phá tương ứng.
- Người dùng hoặc pipeline chạy hai script `index_spec/validate_whatif_sql.py` và `index_spec/spark_check_whatif_sql.py` trước khi đưa lên Databricks (`wc_04_sql.md` mục 8).

## 6. Vấn đề dữ liệu đã biết
Giữ nguyên cách xử lý dưới đây cho tới khi chủ dữ liệu xác nhận.

| Vấn đề | Vì sao quan trọng | Cách xử lý trong SQL |
|---|---|---|
| Hai hệ khóa: bảng `cus_*` dùng `customer_code`, bảng `trio_*` dùng `cusid`. Danh mục ghi Phase 2 thay cả hai bằng `cus_key` | Nếu hai mã không trùng giá trị, mọi truy vấn nối hai nhóm bảng ra kết quả rỗng hoặc sai | Đổi tên về `cus_key` ngay trong CTE đọc bảng; ghi giả định "hai khóa trùng giá trị sau Phase 2". Trước Phase 2 chỉ chạy truy vấn trong một hệ khóa |
| `cus_payroll.company_code` là mã khách hàng của DN trả lương | Đây là đường duy nhất nối DN với nhân viên (kênh `L02`) | Nối với `cus_key` của DN, cùng giả định hệ khóa |
| Mô tả gốc của `cus_info.c_addr_province` ghi "collateral id" | Có thể là lỗi mô tả; nếu không phải tỉnh thì mọi bộ lọc vùng sai | Dùng như tỉnh địa chỉ khách, ghi "cần xác nhận"; truy vấn khám phá sẽ cho thấy giá trị thật |
| `cus_coll_transformed.nominal_value` có cờ 0 | Là đầu vào chính của LTV | Dùng được, ghi "cần xác nhận" là giá trị định giá hay danh nghĩa |
| Các cột quỹ, trái phiếu, tiền gửi trong `cus_nonlending` để trống cờ | Ảnh hưởng mọi tính toán đệm thanh khoản | Dùng được, ghi "cần xác nhận" |
| `cus_nonlending` không có cột kỳ trong danh mục | Không so được hai thời điểm | Coi là bản chụp mới nhất; muốn đo thay đổi theo thời gian thì dùng bảng `trio_*` |
| `cus_lending.total_monthly_payment` ghi "nice to have" | Có thể thiếu nhiều | Luôn báo số khách bị loại do thiếu khoản trả; không thay null bằng 0 |
| Không có lãi suất hợp đồng, kỳ hạn còn lại, ngày hết ưu đãi | Không tính được cú sốc lãi suất cho từng khoản | Cú sốc khoản trả là tham số `:pmt_uplift_*`, suy ra bằng công thức nêu rõ |
| Không có `S02` `S03` `S07` `S11` `S13` `S14` `S15` `S16`, `X01`–`X08` | Nhiều tín hiệu của playbook không đo được | Ghi `GAP` theo `wc_02_signal_map.md` mục 1–2 |
