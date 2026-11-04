---
id: WC-01A-CATALOG-KHCN
used_by: [What-if]
steps: [whatif-2, whatif-4]
depends_on: [core/whatif_chung/wc_00_quy_tac.md]
load_when: Luôn nạp khi viết kịch bản what-if hoặc SQL chạm các bảng dưới đây
version: v3.4
updated: 2026-11-04
---

# Danh mục feature – khách hàng, khoản vay, KHCN

Schema đầy đủ: `tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.<bảng>`. Bảng `cus_*` khóa `customer_code`; bảng `trio_a_hashed_*` khóa `cusid` + `month`. Hai khóa được nối qua `cus_key` sau Phase 2 – xem `core/whatif_chung/wc_04_sql.md` mục 2.

Cột **Cờ**: `F` feature dùng được · `?` danh mục để trống cờ – dùng được nhưng ghi "cần xác nhận" · `A` thuộc tính cờ 0 – chỉ dùng khi đã xác nhận · `K` khóa, cột thời gian (không phải biến). **Chỉ được dùng cột có trong file này** (bản máy đọc: `core/whatif_chung/feature_catalog.csv`).


## `cus_info` – Thông tin khách hàng (tĩnh)
Khóa: `customer_code` · Thời gian: – (không có cột thời gian). Lọc quần thể: tỉnh, nhóm khách, tuổi, giới tính, ngành GSO (DN), phân khúc, hạng ưu tiên. `c_addr_province`: tỉnh theo địa chỉ khách (mô tả gốc ghi nhầm là "collateral id"). Giá trị mã (`sector`, `gso_code`, `customer_segment`) phải tra bằng truy vấn khám phá, không đoán.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `c_addr_province` | STRING |  |  | F | tỉnh theo địa chỉ khách (mô tả gốc ghi nhầm "collateral id of customer code") |
| `sector` | BIGINT |  |  | F | sector code of customer (classify group of customer retail, corp,...) |
| `age` | INT |  |  | F | age of customer |
| `gender` | string |  |  | F | gender of customer |
| `gso_code` | INT |  |  | F | code of industry of corp, sme customer |
| `customer_segment` | string |  |  | F | economy segment of retail customer |
| `priority_class` | string |  |  | F | tier priority of customer (non-priority, inspire, priority, private) |
| `industry_group` | string |  |  | F | group of industry group of corp, sme customer |
| `gso_description` | string |  |  | F | description for gso code |

## `cus_persona` – Persona khách hàng
Khóa: `customer_code` · Thời gian: –. Một khách có nhiều persona. Giá trị `classfication_value` phải tra bằng truy vấn khám phá.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `classfication_value` | STRING |  |  | F | persona of customer (1 customer N persona) |

## `cus_payroll` – Lương qua ngân hàng
Khóa: `customer_code` · Thời gian: `month_id` (năm-tháng). `company_code` = mã khách hàng của DN trả lương → nối nhân viên với DN (kênh `L02`). `month_income`: thu nhập tháng.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `company_code` | STRING |  |  | F | Customer ID of company |
| `month_income` | double |  |  | F | income of customer |
| `month_id` | date (year month) |  |  | F | paymonth |

## `cus_lending` – Khoản vay
Khóa: `customer_code` (nhiều dòng mỗi khách) · Thời gian: `ds_partition_date`. Cộng theo khách trước khi tính. Không có lãi suất hợp đồng, kỳ hạn còn lại, ngày đáo hạn. `total_monthly_payment` ghi "nice to have" – kiểm tra tỷ lệ null trước khi dùng.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `secured_type` | STRING |  |  | F | type of loan: secured or unsecured |
| `product_name` | STRING |  |  | F | name of loan product |
| `granted_limit` | BIGINT |  |  | F | total limit of loan |
| `total_outstanding` | Decimal |  |  | F | outstanding balance of loan |
| `total_monthly_payment` | Decimal |  |  | F | monthly payment of loan (based on which loan product, nice to have value) |
| `ds_partition_date` | date |  |  | F | business date |

## `cus_coll_transformed` – Tài sản bảo đảm
Khóa: `customer_code` (nhiều dòng mỗi khách) · Thời gian: `ds_partition_date` (mỗi tháng một bản). Gắn với khách, không gắn với từng khoản vay → LTV tính ở cấp khách. `nominal_value` có cờ 0 trong danh mục: dùng được trong SQL nhưng phải xác nhận. Danh mục còn ghi `ds_parition_date` (sai chính tả) và `td_mm_current_balance` dưới bảng này – nghi nhầm bảng, không dùng tới khi xác nhận.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `coll_id` | STRING |  |  | A | tỉnh theo địa chỉ khách (mô tả gốc ghi nhầm "collateral id of customer code") |
| `nominal_value` | BIGINT |  |  | A | nominal value of collateral |
| `coll_source` | string |  |  | F | owner of collateral (Cua chinh KH - Khong HT tu von vay, 1 Cua chinh khach hang, Cua chinh KH - Khong HT tu von vay,...) |
| `tsdb_mt` | string |  |  | F | kind of collateral |
| `ds_partition_date` | date |  |  | F | The source ds_partition_date this row was taken from (one per month), kept for audit. |
| `ds_parition_date` | date |  |  | ? | business date |
| `td_mm_current_balance` | decimal |  |  | ? | balance of term deposit on branch end of business |

## `cus_nonlending` – Sản phẩm không vay: CASA, bảo hiểm, quỹ, trái phiếu, tiền gửi có kỳ hạn
Khóa: `customer_code` · Thời gian: `ds_partition_date` (không liệt kê trong danh mục – xác nhận). Các cột quỹ, trái phiếu, tiền gửi để trống cờ feature – dùng được, ghi "cần xác nhận". `az` = kênh online, `mm` = tại quầy.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `ca_eob_balance` | decimal |  |  | F | total casa amount of customer end of day |
| `banca_maintenance_time` | decimal |  |  | F | number of months from the purchase date of the earliest active insurrance to the present |
| `banca_relationship_time` | decimal |  |  | F | number of months from the purchase date of the earliest insurrance to the present |
| `banca_ape` | decimal |  |  | F | total annual Premium Equivalent of insurrance |
| `banca_eob_balance` | decimal |  |  | F | total balance of insurrance end of business |
| `fund_relationship_time` | decimal |  |  | F | number of months from the purchase date of the active fund to the present |
| `fund_total_purchase_value` | decimal |  |  | ? | total purchased amount of fund |
| `fund_total_sell_value` | decimal |  |  | ? | total sold amount of fund |
| `fund_eob_balance` | decimal |  |  | ? | total balance of fund end of business |
| `bond_relationship_time` | decimal |  |  | ? | number of months from the purchase date of the earliest bond to the present |
| `bond_total_purchase_value` | decimal |  |  | ? | total purchased amount of bond |
| `bond_total_sell_value` | decimal |  |  | ? | total sold amount of bond |
| `bond_eob_balance` | decimal |  |  | ? | total balance of bond end of business |
| `td_az_relationship_time` | decimal |  |  | ? | number of months from the purchase date of the earliest term deposit on online channel to the present |
| `td_az_eob_balance` | decimal |  |  | ? | balance of term deposit on online channel end of business |
| `td_az_maintenance_time` | decimal |  |  | ? | number of months from the purchase date of the earliest active term deposit on online channel to the present |
| `td_az_current_balance` | decimal |  |  | ? | balance of term deposit on online channel end of business |
| `td_mm_relationship_time` | decimal |  |  | ? | number of months from the purchase date of the earliest term deposit in branch to the present |
| `td_mm_maintenance_time` | decimal |  |  | ? | number of months from the purchase date of the earliest active term deposit in branch to the present |
| `td_mm_eob_balance` | decimal |  |  | ? | balance of term deposit on branch end of business |

## `trio_a_hashed_b_credit_history` – Lịch sử tín dụng KHCN (tháng)
Khóa: `cusid` · Thời gian: `month` (ngày đầu tháng). DPD, quá hạn, nhóm nợ tại TCB và CIC, số hợp đồng tín chấp.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `b_flag_credit_card_delinq_l1m` | INT | l1m |  | F | Flag a customer as delinquent on credit card for the last 1 month |
| `b_flag_mortgage_delinq_l1m` | INT | l1m |  | F | Flag a customer as delinquent on mortgage for the last 1 month |
| `b_flag_mortgage_delinq_l3m` | INT | l3m |  | F | Flag a customer as delinquent on mortgage for the last 3 months |
| `b_flag_mortgage_delinq_l6m` | INT | l6m |  | F | Flag a customer as delinquent on mortgage for the last 6 months |
| `b_flag_mortgage_l1m` | INT | l1m |  | F | Flag a customer having auto mortgage for the last 1 month |
| `b_flag_mortgage_l3m` | INT | l3m |  | F | Flag a customer having mortgage for the last 3 months |
| `b_flag_mortgage_l6m` | INT | l6m |  | F | Flag a customer having mortgage for the last 6 months |
| `b_flag_uns_only_l1m` | INT | l1m |  | F | Flag a customer only having unsecured for the last 1 month |
| `bun_num_ctr_cnt_l1m` | INT | l1m | cnt | F | Number of unsecured contracts a customer has for the last 1 month |
| `bun_num_ctr_cnt_l3m` | INT | l3m | cnt | F | Number of unsecured contracts a customer has for the last 3 months |
| `bun_num_ctr_cnt_l6m` | INT | l6m | cnt | F | Number of unsecured contracts a customer has for the last 6 months |
| `bun_per_oustanding_max_l1m` | DOUBLE | l1m | max | F | Max unsecured outstanding balance by customer last 1 month |
| `bun_per_oustanding_max_l3m` | DOUBLE | l3m | max | F | Max unsecured outstanding balance by customer last 3 months |
| `b_num_dpd_max_l1m` | INT | l1m | max | F | Max number of day past due in last 1 month |
| `b_bal_dpd_max_l1m` | DOUBLE | l1m | max | F | Max overdue balance in last 1 month |
| `b_ln_class_tcb_cic_max_l1m` | INT | l1m | max | F | Max loan class at tcb & cic in last 1 month |

## `trio_a_hashed_b_credit_history_monthly` – Đếm tháng quá hạn
Khóa: `cusid` · Thời gian: `month`. Số tháng có DPD > 0, > 30 trong 3, 6, 12 tháng.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `b_num_mth_gt0_dpd_cnt_l12m` | INT | l12m | cnt | F | Number of months customer have DPD > 0 or overdue balance > 0 in last 12 months |
| `b_num_mth_gt0_dpd_cnt_l3m` | INT | l3m | cnt | F | Number of months customer have DPD > 0 or overdue balance > 0 in last 3 months |
| `b_num_mth_gt0_dpd_cnt_l6m` | INT | l6m | cnt | F | Number of months customer have DPD > 0 or overdue balance > 0 in last 6 months |
| `b_num_mth_gt30_dpd_cnt_l12m` | INT | l12m | cnt | F | Number of months customer have DPD > 30 in last 12 months |
| `b_num_mth_gt30_dpd_cnt_l3m` | INT | l3m | cnt | F | Number of months customer have DPD > 30 in last 3 months |
| `b_num_mth_gt30_dpd_cnt_l6m` | INT | l6m | cnt | F | Number of months customer have DPD > 30 in last 6 months |

## `trio_a_hashed_bunod_ur` – Tỷ lệ sử dụng thấu chi tín chấp
Khóa: `cusid` · Thời gian: `month`. Gần nhất với tín hiệu `S04` (hạn mức tăng nhanh).

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `bunod_amt_ur_max_l1m` | DOUBLE | l1m | max | F | Utilization rate |
| `bunod_amt_ur_max_l3m` | DOUBLE | l3m | max | F | Utilization rate |
| `bunod_amt_ur_max_l6m` | DOUBLE | l6m | max | F | Utilization rate |
| `bunod_amt_ur_med_l1m` | DOUBLE | l1m | med | F | Utilization rate |
| `bunod_amt_ur_med_l3m` | DOUBLE | l3m | med | F | Utilization rate |
| `bunod_amt_ur_med_l6m` | DOUBLE | l6m | med | F | Utilization rate |
| `bunod_pct_day_ur_gt90pc_cnt_l1m` | DOUBLE | l1m | cnt | F | Proportion of day have utilization rate higher than 90 percent |
| `bunod_pct_day_ur_gt90pc_cnt_l3m` | DOUBLE | l3m | cnt | F | Proportion of day have utilization rate higher than 90 percent |
| `bunod_pct_day_ur_gt90pc_cnt_l6m` | DOUBLE | l6m | cnt | F | Proportion of day have utilization rate higher than 90 percent |

## `trio_a_hashed_rbg_a_aum` – Tài sản quản lý (AUM) KHCN
Khóa: `cusid` · Thời gian: `month`. Trung bình, nhỏ nhất, độ dốc AUM – dùng cho rút tiền, chuyển tài sản.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `a_amt_aum_avg_l1m` | DECIMAL | l1m | avg | F | Average of customer Asset Under Management amount within last 1 month |
| `a_amt_aum_avg_l3m` | DECIMAL | l3m | avg | F | Average of customer Asset Under Management amount within last 3 months |
| `a_amt_aum_avg_l6m` | DECIMAL | l6m | avg | F | Average of customer Asset Under Management amount within last 6 months |
| `a_amt_aum_min_l6m` | DECIMAL | l6m | min | F | Minimum of customer Asset Under Management amount within last 6 months |
| `a_amt_aum_slope_l1m` | DOUBLE | l1m | slope | F | Linear regression slope of customer daily Asset Under Management amount within last 1 month |
| `a_amt_aum_slope_l3m` | DOUBLE | l3m | slope | F | Linear regression slope of customer daily Asset Under Management amount within last 3 months |
| `a_amt_aum_slope_l6m` | DOUBLE | l6m | slope | F | Linear regression slope of customer daily Asset Under Management amount within last 6 months |

## `trio_a_hashed_rbg_asv_balance` – Tiền gửi có kỳ hạn KHCN
Khóa: `cusid` · Thời gian: `month`. Số dư và tất toán trước hạn – gần nhất với `S06`.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `asvtd_bal_avg_l1m` | double | l1m |  | F | average balance over the last 1 month |
| `asvtd_bal_avg_l3m` | double | l3m |  | F | average balance over the last 3 months |
| `asvtd_bal_close_early_avg_l1m` | double | l1m |  | F | average closed early balance over the last 1 month |
| `asvtd_bal_close_early_avg_l3m` | double | l3m |  | F | average closed early balance over the last 3 months |
| `asvtd_num_acc_close_early_avg_l1m` | double | l1m |  | F | average number of closed early account over the last 1 month |
| `asvtd_num_acc_close_early_avg_l3m` | double | l3m |  | F | average number of closed early account over the last 3 months |

## `trio_a_hashed_rbg_atxca_balance` – Số dư CASA KHCN
Khóa: `cusid` · Thời gian: `month`.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `atxca_bal_avg_l1m` | double | l1m |  | F | average balance over the last 1 month |
| `atxca_bal_avg_l3m` | double | l3m |  | F | average balance over the last 3 months |

## `trio_a_hashed_rbg_atxca_service_channel` – Giao dịch CASA KHCN theo mục đích
Khóa: `cusid` · Thời gian: `month`. Lương vào (`S01` phía cá nhân), chi giáo dục, nhà ở, điện, nước.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `atxca_amt_out_education_sum_l1m` | DECIMAL | l1m | sum | F | transaction amount out for education |
| `atxca_amt_out_electricity_sum_l1m` | DECIMAL | l1m | sum | F | transaction amount out for electricity |
| `atxca_amt_out_housing_sum_l1m` | DECIMAL | l1m | sum | F | transaction amount out for housing |
| `atxca_amt_out_water_sum_l1m` | DECIMAL | l1m | sum | F | transaction amount out for water |
| `atxca_amt_sal_max_l1m` | DECIMAL | l1m | max | F | transaction amount in by salary |
| `atxca_amt_sal_sum_l1m` | DECIMAL | l1m | sum | F | transaction amount in by salary |

## `trio_a_hashed_rbg_buncc_payment` – Thẻ tín dụng
Khóa: `cusid` · Thời gian: `month`. Hạn mức, tỷ lệ sử dụng, trả tối thiểu – gần nhất với `S04` `S05`.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `buncc_amt_card_limit_max_l1m` | DECIMAL | l1m | max | F | credit card limit within last 1 month |
| `buncc_amt_card_limit_max_l3m` | DECIMAL | l3m | max | F | credit card limit within last 3 months |
| `buncc_amt_card_limit_max_l6m` | DECIMAL | l6m | max | F | credit card limit within last 6 months |
| `buncc_amt_paid_vs_min_paid_med_l3m` | DOUBLE | l3m | med | F | amount paid divide min paid within last 3 months |
| `buncc_amt_paid_vs_min_paid_med_l6m` | DOUBLE | l6m | med | F | amount paid divide min paid within last 6 months |
| `buncc_amt_ur_max_l1m` | DECIMAL | l1m | max | F | credit card utilization rate within last 1 month |
| `buncc_amt_ur_max_l3m` | DECIMAL | l3m | max | F | credit card utilization rate within last 3 months |
| `buncc_amt_ur_max_l6m` | DECIMAL | l6m | max | F | credit card utilization rate within last 6 months |
| `buncc_amt_ur_med_l1m` | DOUBLE | l1m | med | F | credit card utilization rate within last 1 month |
| `buncc_amt_ur_med_l3m` | DOUBLE | l3m | med | F | credit card utilization rate within last 3 months |
| `buncc_amt_ur_med_l6m` | DOUBLE | l6m | med | F | credit card utilization rate within last 6 months |
| `buncc_num_day_ur_gt90pc_cnt_l3m` | LONG | l3m | cnt | F | credit card number of days utilization rate higher than 90 percent within last 3 months |
| `buncc_num_day_ur_gt90pc_cnt_l6m` | LONG | l6m | cnt | F | credit card number of days utilization rate higher than 90 percent within last 6 months |
| `buncc_num_min_paid_cnt_l3m` | LONG | l3m | cnt | F | number of min paid within last 3 months |
| `buncc_num_min_paid_cnt_l6m` | LONG | l6m | cnt | F | number of min paid within last 6 months |

## `trio_a_hashed_rbg_cpb` – Hành vi vay trong quá khứ
Khóa: `cusid` · Thời gian: `month`.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `cpb_num_pbb_lv_ul_cnt` | bigint |  | cnt | F | Number of active unsecured contract |
