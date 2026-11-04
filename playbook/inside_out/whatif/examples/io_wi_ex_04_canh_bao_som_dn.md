---
id: IO-WI-EX-04
used_by: [What-if, Critic]
load_when: Tín hiệu cảnh báo sớm nội bộ ở phía DN (dòng tiền vào giảm, lương giảm, OD căng, quá hạn) và cần đo rủi ro tập trung cùng phần lan sang nhân viên
version: v3.4
updated: 2026-11-04
---

# Bài mẫu what-if inside-out 04 – Cảnh báo sớm dòng tiền DN: nếu nhóm DN có điểm cao chậm trả lương

## 1. Sự kiện nội bộ
Không có tin bên ngoài nào; chính dữ liệu giao dịch của ngân hàng cho thấy một nhóm DN có dòng tiền vào 3 tháng gần đây thấp hơn bình quân 12 tháng, lương chi ra giảm, thấu chi gần chạm hạn mức. Đây là tín hiệu `S01` (lương giảm) và `S10` (hoạt động giảm) phía DN trong `inside_out/signals.md`, chạm `CIB-LN-01`, `SME-LN-01` và qua kênh `L02` chạm khoản vay của nhân viên. Câu hỏi: **nhóm DN nào có nhiều tín hiệu cùng lúc, dư nợ bao nhiêu, và nếu một phần trong số đó chậm hoặc ngừng trả lương thì bao nhiêu dư nợ KHCN của nhân viên bị kéo theo**.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Mọi DN có dữ liệu dòng tiền trong tháng `:as_of_month`, nhóm theo `industry_group` |
| Điểm cảnh báo (0–5) | Cộng 1 cho mỗi tín hiệu: dòng vào 3 tháng / 12 tháng < `:in_trend_limit`; lương 3 tháng < lương 6 tháng × `:payroll_drop_ratio`; OD lớn nhất tháng ≥ `:od_ur_high`; quá hạn tháng > 0; số ngày có giao dịch tháng / bình quân 6 tháng < `:days_ratio_limit` |
| Cú sốc | DN có điểm ≥ `:score_trigger` ngừng trả lương với xác suất `payroll_stop_share` |
| Công thức | Phần nhân viên: `EAR_kỳ_vọng = payroll_stop_share × Σ OS` của nhân viên có số tháng đệm `M = B / P < :buffer_months` ở các DN vượt ngưỡng |
| Mức độ | Cơ sở (chỉ đếm, không sốc); vừa; nặng |
| Biến kết quả | Số DN và dư nợ DN theo mức điểm; số nhân viên và dư nợ nhân viên đệm mỏng; dư nợ nhân viên chịu rủi ro kỳ vọng |

Điểm cảnh báo là công cụ sắp xếp ưu tiên, không phải xếp hạng tín dụng; các ngưỡng là tham số để bộ phận rủi ro chỉnh.

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò |
|---|---|---|---|
| Xu hướng dòng vào | `trio_a_hashed_corp_atxca_txn.atxca_txn_amt_in_avg_l3v12m` | F | Tín hiệu 1 |
| Lương 3 và 6 tháng | `trio_a_hashed_corp_atxca_txn_ews.atxca_txn_amt_payroll_avg_l3m`, `_l6m` | F | Tín hiệu 2 (`S01`) |
| OD | `trio_a_hashed_corp_b.b_monthend_od_ur_max_l1m` | F | Tín hiệu 3 |
| Quá hạn DN | `trio_a_hashed_corp_b.b_max_monthly_dpd_max_l1m` | F | Tín hiệu 4 |
| Ngày có giao dịch | `trio_a_hashed_corp_atxca_txn.atxca_num_day_have_txn_l1_v_avgl6m` | F | Tín hiệu 5 (`S10` thay thế) |
| Dư nợ DN | `trio_a_hashed_corp_b.b_monthend_on_os_max_l1m` | F | Phơi nhiễm DN |
| Ngành | `cus_info.industry_group` | F | Nhóm |
| Nhân viên | `cus_payroll.company_code`, `customer_code`, `month_id` | F | Kênh `L02` |
| Dư nợ, khoản trả nhân viên | `cus_lending.total_outstanding`, `total_monthly_payment` | F | Phơi nhiễm KHCN |
| Đệm nhân viên | `cus_nonlending.ca_eob_balance` | F | Số tháng đệm |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:in_trend_limit` | 0.8 | 0.8 | Giả định: dòng vào 3 tháng thấp hơn 80% bình quân 12 tháng |
| `:payroll_drop_ratio` | 0.9 | 0.9 | Giả định |
| `:od_ur_high` | 0.9 | 0.9 | Giả định |
| `:days_ratio_limit` | 0.7 | 0.7 | Giả định |
| `:score_trigger` | 3 | 3 | Giả định: từ 3 tín hiệu cùng lúc |
| `:payroll_stop_vua` / `_nang` | 0.2 | 0.5 | Giả định – nên thay bằng tỷ lệ lịch sử: trong DN từng có điểm ≥ 3, bao nhiêu phần trăm ngừng chi lương sau 3 tháng (cách tính như bài 01) |
| `:buffer_months` | 2 | 2 | Giả định |
| `:min_group_size` | 20 | 20 | Giả định (DN ít, có thể hạ và ghi lý do) |

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP`: nộp thuế, hóa đơn điện, cảng (`S10` trực tiếp), chuỗi anchor–spoke (`S11`), quan hệ chủ DN – DN (`L01`, `S12`).
- Thay thế: "số ngày có giao dịch" thay cho mức độ hoạt động của DN.
- Cần xác nhận: nối `cus_info`, `cus_payroll.company_code` (customer_code) với bảng `trio_corp_*` (cusid) qua `cus_key`.
- Không nêu tên DN trong báo cáo; danh sách DN cụ thể (nếu cần) chỉ lấy trong hệ thống nội bộ bằng truy vấn riêng có kiểm soát truy cập, không qua what-if.

## 6. SQL
```sql
-- K1. Phân bố các tỷ lệ để đặt ngưỡng
SELECT percentile_approx(ct.atxca_txn_amt_in_avg_l3v12m,        array(0.1, 0.25, 0.5)) AS in_trend_q,
       percentile_approx(ct.atxca_num_day_have_txn_l1_v_avgl6m, array(0.1, 0.25, 0.5)) AS days_ratio_q,
       percentile_approx(cb.b_monthend_od_ur_max_l1m,           array(0.5, 0.75, 0.9)) AS od_ur_q,
       COUNT(*) AS n_firms
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_atxca_txn ct
LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_b cb
  ON cb.cusid = ct.cusid AND cb.month = ct.month
WHERE ct.month = :as_of_month;
```

```sql
-- Tham số
-- :as_of_month         DATE    tháng quan sát                                '2026-10-01'
-- :as_of_date          DATE    ngày chụp cus_lending                         '2026-10-31'
-- :in_trend_limit      DOUBLE  giả định                                      0.8
-- :payroll_drop_ratio  DOUBLE  giả định                                      0.9
-- :od_ur_high          DOUBLE  giả định                                      0.9
-- :days_ratio_limit    DOUBLE  giả định                                      0.7
-- :score_trigger       INT     giả định                                      3
-- :payroll_stop_vua    DOUBLE  giả định (nên thay bằng tỷ lệ lịch sử)        0.2
-- :payroll_stop_nang   DOUBLE  giả định                                      0.5
-- :buffer_months       DOUBLE  giả định                                      2
-- :min_group_size      INT     giả định                                      20
WITH
firm AS (
  SELECT ct.cusid AS cus_key,
         cb.b_monthend_on_os_max_l1m AS firm_os,
         CASE WHEN ct.atxca_txn_amt_in_avg_l3v12m < :in_trend_limit THEN 1 ELSE 0 END
       + CASE WHEN ew.atxca_txn_amt_payroll_avg_l3m < ew.atxca_txn_amt_payroll_avg_l6m * :payroll_drop_ratio THEN 1 ELSE 0 END
       + CASE WHEN cb.b_monthend_od_ur_max_l1m >= :od_ur_high THEN 1 ELSE 0 END
       + CASE WHEN cb.b_max_monthly_dpd_max_l1m > 0 THEN 1 ELSE 0 END
       + CASE WHEN ct.atxca_num_day_have_txn_l1_v_avgl6m < :days_ratio_limit THEN 1 ELSE 0 END AS ews_score
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_atxca_txn ct
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_atxca_txn_ews ew
    ON ew.cusid = ct.cusid AND ew.month = ct.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_corp_b cb
    ON cb.cusid = ct.cusid AND cb.month = ct.month
  WHERE ct.month = :as_of_month
),
ind AS (
  SELECT i.customer_code AS cus_key, i.industry_group AS industry
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
),
staff_loan AS (                          -- nhân viên: dư nợ, khoản trả, đệm, gộp theo DN trả lương
  SELECT p.company_code AS cus_key,
         COUNT(DISTINCT p.customer_code) AS n_staff,
         SUM(lo.os) AS staff_os,
         SUM(CASE WHEN lo.pmt > 0 AND COALESCE(n.ca_eob_balance, 0) / lo.pmt < :buffer_months THEN lo.os ELSE 0 END) AS staff_os_thin,
         SUM(CASE WHEN lo.pmt > 0 AND COALESCE(n.ca_eob_balance, 0) / lo.pmt < :buffer_months THEN 1 ELSE 0 END)     AS n_staff_thin
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
  LEFT JOIN (
    SELECT l.customer_code, SUM(l.total_outstanding) AS os, SUM(l.total_monthly_payment) AS pmt
    FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
    WHERE l.ds_partition_date = :as_of_date
    GROUP BY l.customer_code
  ) lo ON lo.customer_code = p.customer_code
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_nonlending n
    ON n.customer_code = p.customer_code
  WHERE trunc(p.month_id, 'MM') = :as_of_month
  GROUP BY p.company_code
),
base AS (
  SELECT COALESCE(d.industry, 'khong_ro') AS industry,
         CASE WHEN f.ews_score >= :score_trigger THEN 'vuot_nguong' ELSE CAST(f.ews_score AS STRING) END AS score_group,
         CASE WHEN f.ews_score >= :score_trigger THEN 1 ELSE 0 END AS triggered,
         f.firm_os, s.n_staff, s.staff_os, s.staff_os_thin, s.n_staff_thin
  FROM firm f
  LEFT JOIN ind d ON d.cus_key = f.cus_key
  LEFT JOIN staff_loan s ON s.cus_key = f.cus_key
),
scen AS (
  SELECT * FROM VALUES ('0_co_so', 0.0D), ('1_vua', CAST(:payroll_stop_vua AS DOUBLE)), ('2_nang', CAST(:payroll_stop_nang AS DOUBLE))
  AS t(scenario, stop_share)
)
SELECT sn.scenario, b.industry, b.score_group,
       COUNT(*)                                                   AS n_firms,
       SUM(b.firm_os)                                             AS firm_os_total,
       SUM(b.n_staff)                                             AS n_staff,
       SUM(b.staff_os)                                            AS staff_os_total,
       SUM(b.n_staff_thin)                                        AS n_staff_thin_buffer,
       sn.stop_share * SUM(b.triggered * b.staff_os_thin)         AS staff_ear_expected
FROM base b
CROSS JOIN scen sn
GROUP BY sn.scenario, sn.stop_share, b.industry, b.score_group
HAVING COUNT(*) >= :min_group_size
ORDER BY sn.scenario, b.industry, b.score_group;
```

## 7. Cách đọc kết quả và hành động
- Dòng `score_group = vuot_nguong` theo ngành cho thấy rủi ro có tập trung ở một ngành không. Nếu có, chuyển sang playbook ngành (`industry/`) để tìm nguyên nhân bên ngoài – sự kiện nội bộ có thể là triệu chứng của một cụm tin chưa được gom.
- `staff_ear_expected` là phần lan sang KHCN; so với `firm_os_total` để thấy rủi ro qua nhân viên lớn hay nhỏ so với rủi ro trực tiếp của DN.
- Hành động theo bảng (c) `CIB-LN-01`, `SME-LN-01`: RM gọi DN vượt ngưỡng để hiểu nguyên nhân; theo dõi lô lương tháng sau (`S01`); với nhân viên đệm mỏng, chuẩn bị phương án giãn nợ có điều kiện. Không hạ hạn mức đồng loạt theo ngành chỉ vì điểm cảnh báo.

## 8. Dòng nhãn
```
[WI] cua=IO | rui_ro=CIB-LN-01,SME-LN-01,CN-LN-05 | kich_ban=canh_bao_som_dn_cham_luong | quan_the=dn_co_dong_tien_theo_nganh | soc=payroll_stop_share=0.2/0.5;score_trigger=3 | cong_thuc=diem_canh_bao,thang_dem,EAR_ky_vong | bang=trio_corp_*,cus_payroll,cus_lending,cus_nonlending | gap=S10,S11,S12,L01 | xac_nhan=1 | muc=co_the
```
