---
id: OI-WI-EX-04
used_by: [What-if, Critic]
load_when: Cụm nhiều nguyên nhân dồn vào một ngành DN (thuế quan, cước, chi phí) và lan sang nhân viên – SME, CIB
version: v3.4
updated: 2026-11-04
nguon_test: TC-15
---

# Bài mẫu what-if 04 – DN gỗ xuất khẩu: thuế quan và cước cùng ép, lan sang người lao động

## 1. Rủi ro gốc
Cụm TC-15 mở 18/06/2026 (`nganh=I05 × vai_tro=dn_xuat_khau × thi_truong=my`, `nhieu_nguyen_nhan`, mức "có thể"): thuế quan Mỹ (16/06, 19/06, 24/07), cước container +23% (18/06), quy định xanh EU, chi phí vốn (20/06). Agent cụm kết luận biên lợi nhuận bị ép từ nhiều phía, chạm `CIB-LN-*` `SME-LN-01` (P2) và chuỗi DN → xưởng vệ tinh → công nhân. Kịch bản đo: dòng tiền DN sau **hai cú sốc cùng lúc** (dòng vào giảm, chi phí vận chuyển tăng), khả năng trả lương, và phần dư nợ KHCN của nhân viên các DN bị căng.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | DN có `gso_code` thuộc ngành gỗ, đồ gỗ (K1); "xuất khẩu" xác định gần đúng bằng tỷ lệ giao dịch ngoại tệ ≥ `:fcy_share_min` |
| Cú sốc | Dòng vào giảm `in_cut`; dòng ra tăng do cước: `logistics_share × freight_up` |
| Công thức | `in' = in3·(1−in_cut)`; `out_est = in3·r/(1−r)` với `r` = tỷ lệ dòng ra trên tổng giao dịch; `out' = out_est·(1 + logistics_share·freight_up)`; `net' = in' − out'`; độ phủ lương `cov' = in' / payroll3` |
| Mức độ | Cơ sở; chỉ thuế; chỉ cước; gộp vừa; gộp nặng |
| Biến kết quả | Số DN và dư nợ có `net' < 0`, có `cov' < :cov_limit`; nhân viên và dư nợ KHCN của nhân viên ở các DN `cov' < :cov_limit` |

`out_est` là **suy ra** từ tỷ lệ, giả định `r = dòng ra / (dòng vào + dòng ra)` theo tên cột – cần xác nhận định nghĩa.

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò |
|---|---|---|---|
| Ngành | `cus_info.gso_code`, `gso_description`, `industry_group` | F | Lọc |
| `in3`, `in12` | `trio_a_hashed_corp_atxca_txn_ews.atxca_txn_amt_in_avg_l3m`, `_l12m` | F | Dòng vào |
| `payroll3` | `trio_a_hashed_corp_atxca_txn_ews.atxca_txn_amt_payroll_avg_l3m` | F | Độ phủ lương (`S01`) |
| `r` | `trio_a_hashed_corp_atxca_txn.atxca_rto_txn_amt_out_vs_txn_amt_avg_l3m` | F | Suy ra dòng ra |
| Xu hướng | `trio_a_hashed_corp_atxca_txn.atxca_txn_amt_in_avg_l3v12m` | F | `< 1` = đã giảm trước sốc |
| Ngoại tệ | `trio_a_hashed_corp_atxca_txn.atxca_rto_txn_num_fcy_vs_txn_num_avg_l3m`; `trio_a_hashed_corp_atxca_balance.atxca_bal_fcy_avg_l1m` | F | Thay thế cờ xuất khẩu |
| Dư nợ, OD, quá hạn, TSBĐ | `trio_a_hashed_corp_b.b_monthend_on_os_max_l1m`, `b_monthend_od_ur_max_l1m`, `b_max_monthly_dpd_max_l1m`, `b_monthend_coll_value_min_l1m` | F | Phơi nhiễm |
| Nhân viên | `cus_payroll.company_code`, `customer_code`, `month_id` | F | Lan sang KHCN (`L02`) |
| Dư nợ nhân viên | `cus_lending.total_outstanding` | F | Phơi nhiễm KHCN |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:in_cut_vua` / `_nang` | 0.06 | 0.20 | Vừa: tin 12/08/2026 "đồ nội thất sang Mỹ giảm khoảng 6%". Nặng: giả định – thuế với gỗ dán tới 208,88% (tin 19/06) làm mất hẳn một nhóm hàng |
| `:freight_up` | 0.23 | 0.23 | Tin 18/06/2026: cước container 40 feet tăng 23% trong một tuần |
| `:logistics_share_vua` / `_nang` | 0.10 | 0.15 | Giả định: tỷ trọng vận chuyển trong dòng ra của DN xuất khẩu |
| `:fcy_share_min` | 0.2 | 0.2 | Giả định |
| `:cov_limit` | 1.5 | 1.5 | Giả định: dòng vào dưới 1,5 lần quỹ lương là căng |
| `:ur_limit` | 0.9 | 0.9 | Giả định |
| `:gso_list` | – | – | K1 |

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP`: thị trường xuất khẩu (Mỹ, EU) – không có cột; `S10` (thuế, hóa đơn cảng), `S11` (chuỗi anchor–spoke, xưởng vệ tinh), `S15` (MTM ngoại tệ); lãi suất vay DN (nguyên nhân chi phí vốn 20/06 không đưa được vào sốc); hạn mức L/C, bảo lãnh.
- Thay thế: "DN xuất khẩu" ≈ tỷ lệ giao dịch ngoại tệ – sẽ lẫn DN nhập khẩu nguyên liệu.
- Cần xác nhận: định nghĩa `rto_txn_amt_out_vs_txn_amt`; nối `cus_info` (customer_code) với `trio_corp_*` (cusid) và `cus_payroll.company_code` qua `cus_key`.
- Ngoài phạm vi: tin 12/08 là tin xác nhận – dùng làm **độ lớn** cú sốc, không đếm làm nguyên nhân cụm.

## 6. SQL
```sql
-- K1. Mã ngành gỗ (từ khóa đề xuất: 'gỗ', 'nội thất', 'lâm sản')
SELECT i.gso_code, i.gso_description, i.industry_group, COUNT(*) AS n_customers
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
WHERE lower(i.gso_description) LIKE concat('%', lower(:gso_keyword), '%')
GROUP BY i.gso_code, i.gso_description, i.industry_group
ORDER BY n_customers DESC;

-- K2. Phân bố tỷ lệ giao dịch ngoại tệ trong ngành đã chọn (để đặt :fcy_share_min)
SELECT percentile_approx(ct.atxca_rto_txn_num_fcy_vs_txn_num_avg_l3m, array(0.25, 0.5, 0.75, 0.9)) AS fcy_ratio_quantiles,
       COUNT(*) AS n_firms
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_atxca_txn ct
JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
  ON i.customer_code = ct.cusid
WHERE ct.month = :as_of_month
  AND find_in_set(CAST(i.gso_code AS STRING), :gso_list) > 0;
```

```sql
-- Tham số
-- :as_of_month          DATE    kỳ quan sát                                   '2026-10-01'
-- :as_of_date           DATE    ngày chụp cus_lending                         '2026-10-31'
-- :gso_list             STRING  từ K1
-- :in_cut_vua           DOUBLE  tin 12/08/2026 sang Mỹ giảm khoảng 6%         0.06
-- :in_cut_nang          DOUBLE  giả định (thuế gỗ dán, tin 19/06/2026)        0.20
-- :freight_up           DOUBLE  tin 18/06/2026 cước +23%                      0.23
-- :logistics_share_vua  DOUBLE  giả định                                      0.10
-- :logistics_share_nang DOUBLE  giả định                                      0.15
-- :fcy_share_min        DOUBLE  giả định (đặt theo K2)                        0.2
-- :cov_limit            DOUBLE  giả định                                      1.5
-- :ur_limit             DOUBLE  giả định                                      0.9
-- :min_group_size       INT     giả định (DN ít hơn KHCN – có thể hạ, ghi lý do) 20
WITH
firm AS (
  SELECT i.customer_code AS cus_key, i.gso_description AS industry_desc
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
  WHERE find_in_set(CAST(i.gso_code AS STRING), :gso_list) > 0
),
flow AS (
  SELECT ew.cusid AS cus_key,
         ew.atxca_txn_amt_in_avg_l3m      AS in3,
         ew.atxca_txn_amt_payroll_avg_l3m AS payroll3,
         ct.atxca_rto_txn_amt_out_vs_txn_amt_avg_l3m   AS out_ratio,
         ct.atxca_txn_amt_in_avg_l3v12m               AS in_trend,
         ct.atxca_rto_txn_num_fcy_vs_txn_num_avg_l3m   AS fcy_ratio,
         cf.atxca_bal_fcy_avg_l1m                      AS fcy_bal,
         cb.b_monthend_on_os_max_l1m   AS os,
         cb.b_monthend_od_ur_max_l1m   AS od_ur,
         cb.b_max_monthly_dpd_max_l1m  AS dpd,
         cb.b_monthend_coll_value_min_l1m AS coll_value
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_atxca_txn_ews ew
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_atxca_txn ct
    ON ct.cusid = ew.cusid AND ct.month = ew.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_atxca_balance cf
    ON cf.cusid = ew.cusid AND cf.month = ew.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_b cb
    ON cb.cusid = ew.cusid AND cb.month = ew.month
  WHERE ew.month = :as_of_month
),
staff AS (                                   -- nhân viên nhận lương tháng quan sát và dư nợ KHCN của họ
  SELECT p.company_code AS cus_key,
         COUNT(DISTINCT p.customer_code) AS n_staff,
         SUM(lo.os_staff)                AS staff_os
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
  LEFT JOIN (
    SELECT l.customer_code, SUM(l.total_outstanding) AS os_staff
    FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
    WHERE l.ds_partition_date = :as_of_date
    GROUP BY l.customer_code
  ) lo ON lo.customer_code = p.customer_code
  WHERE trunc(p.month_id, 'MM') = :as_of_month
  GROUP BY p.company_code
),
base AS (
  SELECT f.cus_key, f.industry_desc, fl.*,
         CASE WHEN fl.fcy_ratio >= :fcy_share_min THEN 'xuat_nhap_khau' ELSE 'noi_dia' END AS fx_group,
         fl.in3 * fl.out_ratio / NULLIF(1 - fl.out_ratio, 0) AS out_est,
         st.n_staff, st.staff_os
  FROM firm f
  JOIN flow fl ON fl.cus_key = f.cus_key
  LEFT JOIN staff st ON st.cus_key = f.cus_key
),
scen AS (
  SELECT * FROM VALUES
    ('0_co_so',     0.0D,                            0.0D,                                    0.0D),
    ('1_chi_thue',  CAST(:in_cut_vua AS DOUBLE),     0.0D,                                    0.0D),
    ('2_chi_cuoc',  0.0D,                            CAST(:logistics_share_vua AS DOUBLE),    CAST(:freight_up AS DOUBLE)),
    ('3_gop_vua',   CAST(:in_cut_vua AS DOUBLE),     CAST(:logistics_share_vua AS DOUBLE),    CAST(:freight_up AS DOUBLE)),
    ('4_gop_nang',  CAST(:in_cut_nang AS DOUBLE),    CAST(:logistics_share_nang AS DOUBLE),   CAST(:freight_up AS DOUBLE))
  AS t(scenario, in_cut, logistics_share, freight_up)
),
shocked AS (
  SELECT sn.scenario, b.industry_desc, b.fx_group, b.os, b.od_ur, b.dpd, b.in_trend, b.n_staff, b.staff_os,
         b.in3 * (1 - sn.in_cut)                                                        AS in_after,
         b.in3 * (1 - sn.in_cut) - b.out_est * (1 + sn.logistics_share * sn.freight_up)  AS net_after,
         b.in3 * (1 - sn.in_cut) / NULLIF(b.payroll3, 0)                                AS cov_after
  FROM base b CROSS JOIN scen sn
)
SELECT scenario, industry_desc, fx_group,
       COUNT(*)                                                              AS n_firms,
       SUM(os)                                                               AS os_total,
       SUM(CASE WHEN net_after < 0 THEN 1 ELSE 0 END)                        AS n_net_negative,
       SUM(CASE WHEN net_after < 0 THEN os ELSE 0 END)                       AS os_net_negative,
       SUM(CASE WHEN cov_after < :cov_limit THEN 1 ELSE 0 END)               AS n_payroll_cov_low,
       SUM(CASE WHEN cov_after < :cov_limit THEN n_staff ELSE 0 END)         AS n_staff_at_risk,
       SUM(CASE WHEN cov_after < :cov_limit THEN staff_os ELSE 0 END)        AS staff_os_at_risk,
       SUM(CASE WHEN od_ur > :ur_limit THEN 1 ELSE 0 END)                    AS n_od_high,
       SUM(CASE WHEN in_trend < 1 THEN 1 ELSE 0 END)                         AS n_inflow_falling_before,
       SUM(CASE WHEN dpd > 0 THEN 1 ELSE 0 END)                              AS n_dpd_now,
       SUM(CASE WHEN net_after IS NULL OR cov_after IS NULL THEN 1 ELSE 0 END) AS n_excluded_null
FROM shocked
GROUP BY scenario, industry_desc, fx_group
HAVING COUNT(*) >= :min_group_size
ORDER BY scenario, industry_desc, fx_group;
```

## 7. Cách đọc kết quả và hành động
- So `os_net_negative` giữa `1_chi_thue`, `2_chi_cuoc` và `3_gop_vua`: phần vượt quá tổng hai cú sốc riêng (do DN gần ngưỡng bị đẩy qua) là bằng chứng dữ liệu cho cụm `nhieu_nguyen_nhan`.
- `fx_group = xuat_nhap_khau` chịu sốc mạnh hơn `noi_dia` là kiểm chứng gần đúng cho tiêu chí "DN xuất khẩu"; không khác biệt → tiêu chí thị trường Mỹ chưa được dữ liệu ủng hộ.
- `n_staff_at_risk`, `staff_os_at_risk` là bước 2 của chuỗi (công nhân), đưa sang kịch bản bài 01 nếu cần đo sâu.
- `n_inflow_falling_before` cao ở mức cơ sở → tác động đã bắt đầu trước kỳ quan sát.
- Hành động theo bảng (c) `CIB-LN-*` `SME-LN-01`: RM rà kế hoạch đơn hàng và dòng tiền các DN `net_after < 0`; cân nhắc tài trợ vốn lưu động có kiểm soát thay vì giảm hạn mức đồng loạt; theo dõi `S01` theo DN. Không nêu tên DN trong báo cáo.

## 8. Dòng nhãn
```
[WI] cua=OI | rui_ro=CIB-LN-01,SME-LN-01,CIB-PAY-06 | kich_ban=cum_go_xuat_khau_thue_cuoc | quan_the=dn_gso_go_ty_le_ngoai_te | soc=in_cut=0.06/0.20;freight_up=0.23;logistics_share=0.10/0.15 | cong_thuc=dong_tien_rong,do_phu_luong | bang=trio_corp_*,cus_payroll,cus_lending | gap=thi_truong_xk,S10,S11,S15,lai_suat_dn | xac_nhan=3 | muc=co_the
```
