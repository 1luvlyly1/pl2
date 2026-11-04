---
id: WC-01B-CATALOG-DN
used_by: [What-if]
steps: [whatif-2, whatif-4]
depends_on: [core/whatif_chung/wc_00_quy_tac.md]
load_when: Luôn nạp khi viết kịch bản what-if hoặc SQL chạm các bảng dưới đây
version: v3.4
updated: 2026-11-04
---

# Danh mục feature – doanh nghiệp (SME, CIB)

Schema đầy đủ: `tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.<bảng>`. Lọc DN theo ngành dùng `cus_info.gso_code`, `industry_group`, `gso_description` (file `wc_01a_catalog_khcn.md`).

Cột **Cờ**: `F` feature dùng được · `?` danh mục để trống cờ – dùng được nhưng ghi "cần xác nhận" · `A` thuộc tính cờ 0 – chỉ dùng khi đã xác nhận · `K` khóa, cột thời gian (không phải biến). **Chỉ được dùng cột có trong file này** (bản máy đọc: `core/whatif_chung/feature_catalog.csv`).


## `trio_a_hashed_corp_b` – Tín dụng DN (SME, CIB)
Khóa: `cusid` · Thời gian: `month`. DPD, giá trị TSBĐ cuối tháng, tỷ lệ sử dụng thấu chi, tổng dư nợ nội bảng (vay, trái phiếu).

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `b_flag_dpd_gt0_sum_l3m` | int | L3M | sum | F | Sum of flag customer has day past due > 0 in the month in last 3 months |
| `b_flag_dpd_gt0_sum_l6m` | int | L6M | sum | F | Sum of flag customer has day past due > 0 in the month in last 6 months |
| `b_max_monthly_dpd_max_l12m` | int | L12M | max | F | Maximum of day past due of the customer in last 12 months |
| `b_max_monthly_dpd_max_l1m` | int | L1M | max | F | Maximum of day past due of the customer in last 1 month |
| `b_max_monthly_dpd_max_l3m` | int | L3M | max | F | Maximum of day past due of the customer in last 3 months |
| `b_max_monthly_dpd_max_l6m` | int | L6M | max | F | Maximum of day past due of the customer in last 6 months |
| `b_monthend_coll_value_min_l1m` | double | L1M | min | F | Minimum of Collateral value at month-end in last 1 month |
| `b_monthend_od_ur_avg_l3m` | double | L3M | average | F | Average of Utilization rate of overdraft limit at month-end in last 3 months |
| `b_monthend_od_ur_max_l1m` | double | L1M | max | F | Maximum of Utilization rate of overdraft limit at month-end in last 1 month |
| `b_monthend_od_ur_max_l3m` | double | L3M | max | F | Maximum of Utilization rate of overdraft limit at month-end in last 3 months |
| `b_monthend_on_os_max_l1m` | double | L1M | max | F | Maximum of Total on-balance sheet outstanding at month-end (Loan, Bond) in last 1 month |

## `trio_a_hashed_corp_atxca_balance` – Số dư ngoại tệ DN
Khóa: `cusid` · Thời gian: `month`.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `atxca_bal_fcy_avg_l1m` | double | l1m | avg | F | average daily foreign currency balance for current accounts over the last 1 month |
| `atxca_bal_fcy_avg_l3m` | double | l3m | avg | F | average daily foreign currency balance for current accounts over the last 3 months |

## `trio_a_hashed_corp_atxca_txn` – Dòng tiền giao dịch DN
Khóa: `cusid` · Thời gian: `month`. Dòng vào, dòng ra, ngày có giao dịch, lương, ngoại tệ; nhiều tỷ lệ so sánh 3/6/12 tháng (`l3v12m` < 1 nghĩa là 3 tháng gần đây thấp hơn bình quân 12 tháng). Một số mô tả gốc lẫn "top5day"/"10 days" – đọc theo tên cột.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `atxca_num_month_have_txn_cnt_l3m` | bigint | l3m | cnt | F | number of months having transactions last 3 months |
| `atxca_num_month_have_txn_cnt_l6m` | bigint | l6m | cnt | F | number of months having transactions last 6 months |
| `atxca_num_month_have_txn_cnt_l12m` | bigint | l12m | cnt | F | number of months having transactions last 12 months |
| `atxca_txn_amt_in_top5day_monthly_avg_l3m` | decimal(38,6) | l3m | avg | F | The average value in 3 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_avg_l6m` | decimal(38,6) | l6m | avg | F | The average value in 6 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_avg_l12m` | decimal(38,6) | l12m | avg | F | The average value in 12 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_max_l3m` | decimal(38,6) | l3m | max | F | The highest value in 3 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_max_l6m` | decimal(38,6) | l6m | max | F | The highest value in 6 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_max_l12m` | decimal(38,6) | l12m | max | F | The highest value in 12 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_min_l3m` | decimal(38,6) | l3m | min | F | The minimum value in 3 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_min_l6m` | decimal(38,6) | l6m | min | F | The minimum value in 6 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_amt_in_top5day_monthly_min_l12m` | decimal(38,6) | l12m | min | F | The minimum value in 12 months of inbound transaction amounts during the five days with the highest cash inflows |
| `atxca_txn_num_sum_l3m` | bigint | l3m | sum | F | The number of transactions last 3 months |
| `atxca_txn_num_sum_l6m` | bigint | l6m | sum | F | The number of transactions last 6 months |
| `atxca_txn_num_sum_l12m` | bigint | l12m | sum | F | The number of transactions last 12 months |
| `atxca_num_day_have_txn_avg_l3m` | decimal(38,6) | l3m | avg | F | The average of number of days having transactions last 3 months |
| `atxca_num_day_have_txn_avg_l6m` | decimal(38,6) | l6m | avg | F | The average of number of days having transactions last 6 months |
| `atxca_num_day_have_txn_avg_l12m` | decimal(38,6) | l12m | avg | F | The average of number of days having transactions last 12 months |
| `atxca_num_day_have_txn_min_l3m` | int | l3m | min | F | The minimum of number of days having transactions last 3 months |
| `atxca_num_day_have_txn_min_l6m` | int | l6m | min | F | The minimum of number of days having transactions last 6 months |
| `atxca_num_day_have_txn_min_l12m` | int | l12m | min | F | The minimum of number of days having transactions last 12 months |
| `atxca_num_day_have_txn_max_l3m` | int | l3m | max | F | The maximum of number of days having transactions last 12 months |
| `atxca_num_day_have_txn_max_l6m` | int | l6m | max | F | The maximum of number of days having transactions last 12 months |
| `atxca_num_day_have_txn_max_l12m` | int | l12m | max | F | The maximum of number of days having transactions last 12 months |
| `atxca_rto_num_day_higher_100m_vs_num_day_have_txn_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio between the number of days with transactions over 100 million and the number of transaction days per month |
| `atxca_rto_num_day_higher_100m_vs_num_day_have_txn_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio between the number of days with transactions over 100 million and the number of transaction days per month |
| `atxca_rto_num_day_higher_100m_vs_num_day_have_txn_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio between the number of days with transactions over 100 million and the number of transaction days per month |
| `atxca_rto_txn_amt_in_vs_num_day_have_txn_in_avg_l3m` | decimal(38,6) | l3m | avg | F | Amount of inflow transactions per day that has inflow transactions, average 3 months. |
| `atxca_rto_txn_amt_in_vs_num_day_have_txn_in_avg_l6m` | decimal(38,6) | l6m | avg | F | Amount of inflow transactions per day that has inflow transactions, average 6 months. |
| `atxca_rto_txn_amt_in_vs_num_day_have_txn_in_avg_l12m` | decimal(38,6) | l12m | avg | F | Amount of inflow transactions per day that has inflow transactions, average 12 months. |
| `atxca_rto_txn_amt_out_vs_txn_amt_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio of outgoing funds to the total inflows and outflows |
| `atxca_rto_txn_amt_out_vs_txn_amt_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio of outgoing funds to the total inflows and outflows |
| `atxca_rto_txn_amt_out_vs_txn_amt_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio of outgoing funds to the total inflows and outflows |
| `atxca_rto_txn_amt_out_top5day_monthly_vs_txn_amt_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio between the total cash outflow value in the 10 days with the highest cash outflows and the total cash in and outflow value |
| `atxca_rto_txn_amt_out_top5day_monthly_vs_txn_amt_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio between the total cash outflow value in the 10 days with the highest cash outflows and the total cash in and outflow value |
| `atxca_rto_txn_amt_out_top5day_monthly_vs_txn_amt_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio between the total cash outflow value in the 10 days with the highest cash outflows and the total cash in and outflow value |
| `atxca_rto_txn_amt_in_top10day_monthly_vs_txn_amt_in_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio between the total cash inflow value in the 10 days with the highest cash inflows and the total cash inflow value |
| `atxca_rto_txn_amt_in_top10day_monthly_vs_txn_amt_in_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio between the total cash inflow value in the 10 days with the highest cash inflows and the total cash inflow value |
| `atxca_rto_txn_amt_in_top10day_monthly_vs_txn_amt_in_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio between the total cash inflow value in the 10 days with the highest cash inflows and the total cash inflow value |
| `atxca_rto_txn_amt_in_top5day_monthly_vs_txn_amt_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio between the total cash inflow value in the 10 days with the highest cash inflows and the total cash in and outflow value |
| `atxca_rto_txn_amt_in_top5day_monthly_vs_txn_amt_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio between the total cash inflow value in the 10 days with the highest cash inflows and the total cash in and outflow value |
| `atxca_rto_txn_amt_in_top5day_monthly_vs_txn_amt_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio between the total cash inflow value in the 10 days with the highest cash inflows and the total cash in and outflow value |
| `atxca_rto_txn_amt_payroll_vs_txn_num_payroll_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio between payroll transaction amount and number of payroll transactions (0 value means no payroll) |
| `atxca_rto_txn_amt_payroll_vs_txn_num_payroll_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio between payroll transaction amount and number of payroll transactions (0 value means no payroll) |
| `atxca_rto_txn_amt_payroll_vs_txn_num_payroll_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio between payroll transaction amount and number of payroll transactions (0 value means no payroll) |
| `atxca_rto_txn_num_fcy_vs_txn_num_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio between number of foreign currency transaction and number of transactions |
| `atxca_rto_txn_num_fcy_vs_txn_num_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio between number of foreign currency transaction and number of transactions |
| `atxca_rto_txn_num_fcy_vs_txn_num_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio between number of foreign currency transaction and number of transactions |
| `atxca_rto_num_day_higher_50m_vs_num_day_have_txn_avg_l3m` | decimal(38,6) | l3m | avg | F | The 3-month average of the ratio between the number of days with transactions over 50 million and the number of transaction days per month |
| `atxca_rto_num_day_higher_50m_vs_num_day_have_txn_avg_l6m` | decimal(38,6) | l6m | avg | F | The 6-month average of the ratio between the number of days with transactions over 50 million and the number of transaction days per month |
| `atxca_rto_num_day_higher_50m_vs_num_day_have_txn_avg_l12m` | decimal(38,6) | l12m | avg | F | The 12-month average of the ratio between the number of days with transactions over 50 million and the number of transaction days per month |
| `atxca_txn_num_in_avg_l3v6m` | decimal(38,6) | l3v6m | avg/avg | F | Average number of inflow transactions, average last 3 months vs last 6 months |
| `atxca_txn_num_in_avg_l3v12m` | decimal(38,6) | l3v12m | avg/avg | F | Average number of inflow transactions, average last 3 months vs last 12 months |
| `atxca_txn_num_in_avg_l6v12m` | decimal(38,6) | l6v12m | avg/avg | F | Average number of inflow transactions, average last 6 months vs last 12 months |
| `atxca_txn_num_out_avg_l3v6m` | decimal(38,6) | l3v6m | avg/avg | F | Number of outflow transactions, average last 3 months vs last 6 months |
| `atxca_txn_num_out_avg_l3v12m` | decimal(38,6) | l3v12m | avg/avg | F | Number of outflow transactions, average last 3 months vs last 12 months |
| `atxca_txn_num_out_avg_l6v12m` | decimal(38,6) | l6v12m | avg/avg | F | Number of outflow transactions, average last 6 months vs last 12 months |
| `atxca_txn_amt_in_avg_l3v6m` | decimal(38,6) | l3v6m | avg/avg | F | Average ratio of inflow transaction amount over the last 3 months to inflow transaction amount over the last 6 months |
| `atxca_txn_amt_in_avg_l3v12m` | decimal(38,6) | l3v12m | avg/avg | F | Average ratio of inflow transaction amount over the last 3 months to inflow transaction amount over the last 12 months |
| `atxca_txn_amt_in_avg_l6v12m` | decimal(38,6) | l6v12m | avg/avg | F | Average ratio of inflow transaction amount over the last 6 months to inflow transaction amount over the last 12 months |
| `atxca_txn_amt_out_avg_l3v6m` | decimal(38,6) | l3v6m | avg/avg | F | Average ratio of outflow transaction amount over the last 3 months to outflow transaction amount over the last 6 months |
| `atxca_txn_amt_out_avg_l3v12m` | decimal(38,6) | l3v12m | avg/avg | F | Average ratio of outflow transaction amount over the last 3 months to outflow transaction amount over the last 12 months |
| `atxca_txn_amt_out_avg_l6v12m` | decimal(38,6) | l6v12m | avg/avg | F | Average ratio of outflow transaction amount over the last 6 months to outflow transaction amount over the last 12 months |
| `atxca_num_day_have_txn_avg_l3v6m` | decimal(38,6) | l3v6m | avg/avg | F | Average ratio of number of days having transactions over the last 3 months to number of days having transactions over the last 6 months |
| `atxca_num_day_have_txn_avg_l3v12m` | decimal(38,6) | l3v12m | avg/avg | F | Average ratio of number of days having transactions over the last 3 months to number of days having transactions over the last 12 months |
| `atxca_num_day_have_txn_avg_l6v12m` | decimal(38,6) | l6v12m | avg/avg | F | Average ratio of number of days having transactions over the last 6 months to number of days having transactions over the last 12 months |
| `atxca_rto_num_acc_active_avg_vs_num_day_have_txn_in_avg_l3m` | decimal(38,6) | l3m | avg/avg | F | The ratio of the average number of active accounts used to perform transactions over the past 3 months to the average number of days with transactions in the same 3-month period. |
| `atxca_rto_num_acc_active_avg_vs_num_day_have_txn_in_avg_l6m` | decimal(38,6) | l6m | avg/avg | F | The ratio of the average number of active accounts used to perform transactions over the past 6 months to the average number of days with transactions in the same 6-month period. |
| `atxca_rto_num_acc_active_avg_vs_num_day_have_txn_in_avg_l12m` | decimal(38,6) | l12m | avg/avg | F | The ratio of the average number of active accounts used to perform transactions over the past 12 months to the average number of days with transactions in the same 12-month period. |
| `atxca_txn_amt_out_top10day_monthly_vs_txn_amt_out_minl3_v_min6m` | decimal(38,6) | l3v6m | min/min | F | Ratio of the total amount of outflow transactions of 10 days with largest outflow transaction amount and total amount of outflow transactions, min last 3 months vs last 6 months |
| `atxca_txn_amt_out_top10day_monthly_vs_txn_amt_out_minl3_v_min12m` | decimal(38,6) | l3v12m | min/min | F | Ratio of the total amount of outflow transactions of 10 days with largest outflow transaction amount and total amount of outflow transactions, min last 3 months vs last 12 months |
| `atxca_txn_amt_out_top10day_monthly_vs_txn_amt_out_minl6_v_min12m` | decimal(38,6) | l6v12m | min/min | F | Ratio of the total amount of outflow transactions of 10 days with largest outflow transaction amount and total amount of outflow transactions, min last 6 months vs last 12 months |
| `atxca_num_day_have_txn_l1_v_avgl3m` | decimal(38,6) | l1vl3m | value/avg | F | The number of days having transactions, last 1 month vs the average over last 3 months |
| `atxca_num_day_have_txn_l1_v_avgl6m` | decimal(38,6) | l1vl6m | value/avg | F | The number of days having transactions, last 1 month vs the average over last 6 months |
| `atxca_num_day_have_txn_l1_v_avgl12m` | decimal(38,6) | l1vl12m | value/avg | F | The number of days having transactions, last 1 month vs the average over last 12 months |
| `atxca_num_day_have_txn_vola_l12m` | decimal(38,6) | l12m | (max-min)/sum | F | Volatility of number of days having transactions over last 12 months |
| `atxca_txn_amt_out_top5day_monthly_vs_txn_amt_l1_diff_avgl6m` | decimal(38,6) | l1_l6m | value-avg | F | Ratio between the total cash outflow value in the 5 days with the highest cash outflows and the total cash in and outflow value, last month subtracts the average of last 6 months |

## `trio_a_hashed_corp_atxca_txn_ews` – Cảnh báo sớm dòng tiền DN
Khóa: `cusid` · Thời gian: `month`. Độ lệch chuẩn dòng tiền ròng, dòng vào bình quân, lương bình quân 3/6 tháng – gần nhất với `S01` `S10` phía DN.

| Cột | Kiểu | Kỳ | Phép | Cờ | Mô tả |
|---|---|---|---|---|---|
| `atxca_net_flow_std_l6m` | double | l6m | std | F | The standard deviation of net flow (outflow minus inflow) last 6 months |
| `atxca_num_day_have_txn_in_sum_l1m` | double | l1m | sum | F | The sum of number of days having inbound transactions last 1 month |
| `atxca_num_day_have_txn_in_sum_l3m` | double | l3m | sum | F | The sum of number of days having inbound transactions last 3 months |
| `atxca_num_day_have_txn_in_sum_l6m` | double | l6m | sum | F | The sum of number of days having inbound transactions last 6 months |
| `atxca_txn_amt_fcy_avg_l3m` | double | l3m | avg | F | The average of foreign currency transaction amount last 3 months |
| `atxca_txn_amt_fcy_avg_l6m` | double | l6m | avg | F | The average of foreign currency transaction amount last 6 months |
| `atxca_txn_amt_in_avg_l12m` | double | l12m | avg | F | The average of inbound transaction amount last 12 months |
| `atxca_txn_amt_in_avg_l3m` | double | l3m | avg | F | The average of inbound transaction amount last 3 months |
| `atxca_txn_amt_in_avg_l6m` | double | l6m | avg | F | The average of inbound transaction amount last 6 months |
| `atxca_txn_amt_payroll_avg_l3m` | double | l3m | avg | F | The average of payroll transaction amount last 3 months |
| `atxca_txn_amt_payroll_avg_l6m` | double | l6m | avg | F | The average of payroll transaction amount last 6 months |
