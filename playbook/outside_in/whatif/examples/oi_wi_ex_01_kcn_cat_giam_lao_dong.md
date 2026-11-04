---
id: OI-WI-EX-01
used_by: [What-if, Critic]
load_when: Rủi ro mất việc, giảm thu nhập của người lao động theo DN, ngành, KCN (kênh `L02`)
version: v3.4
updated: 2026-11-04
nguon_test: TC-13
---

# Bài mẫu what-if 01 – Nhà máy điện tử cắt 30% lao động

## 1. Rủi ro gốc
Bài playbook cho TC-13 (tin giả định: nhà máy điện tử vốn nước ngoài ở Bắc Ninh cắt khoảng 30% lao động) kết luận bước 1 "có khả năng cao": người lao động mất thu nhập, chạm `CIB-PAY-06` P1 và `CN-LN-06` `CN-CARD-01` `CN-LN-05` P2. Cột "Hành vi khuyến nghị" của `CN-LN-05` ghi "what-if 30% nhân sự nghỉ việc". Kịch bản đo: nếu một phần nhân viên của nhóm DN này mất lương, bao nhiêu dư nợ nằm ở người **không đủ tiền đệm** để trả nợ vài tháng.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách nhận lương qua ngân hàng trong tháng `:as_of_month` từ DN có `gso_code` thuộc ngành điện tử và tỉnh địa chỉ thuộc `:province_list` |
| Cú sốc | Tỷ lệ mất việc `job_loss_share`; người mất việc có thu nhập về 0 |
| Công thức | `M = B / P` (tháng đệm); `EAR_kỳ_vọng = job_loss_share · Σ OS` của khách có `M < :buffer_months`; khách không vay chỉ đếm |
| Mức độ | Cơ sở (0), vừa, nặng |
| Biến kết quả | Dư nợ chịu rủi ro kỳ vọng, số khách đệm mỏng kỳ vọng, khách đang dùng thẻ > `:ur_limit`, khách đang quá hạn |

Vì không biết ai bị cắt, kịch bản dùng **giá trị kỳ vọng** (nhân tỷ lệ với tổng), không chọn ngẫu nhiên khách.

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò | Ghi chú |
|---|---|---|---|---|
| Ngành DN | `cus_info.gso_code`, `gso_description` | F | Lọc DN | Giá trị qua K1 |
| Tỉnh DN | `cus_info.c_addr_province` | F | Lọc DN | Mô tả gốc ghi nhầm – cần xác nhận |
| Quan hệ DN–nhân viên | `cus_payroll.company_code`, `customer_code`, `month_id` | F | Lọc quần thể | |
| Thu nhập `I` | `cus_payroll.month_income` | F | DSR trước sốc | |
| Dư nợ `OS`, khoản trả `P` | `cus_lending.total_outstanding`, `total_monthly_payment` | F | Phơi nhiễm, mẫu số `M` | `P` "nice to have" – báo null |
| Loại khoản vay | `cus_lending.secured_type` | F | Tách có/không bảo đảm | Giá trị qua K2 |
| Đệm `B` | `cus_nonlending.ca_eob_balance`, `td_az_eob_balance`, `td_mm_eob_balance` | F, ?, ? | Tử số `M` | |
| Thẻ | `trio_a_hashed_rbg_buncc_payment.buncc_amt_ur_med_l1m` | F | `S04` | |
| Quá hạn | `trio_a_hashed_b_credit_history.b_num_dpd_max_l1m` | F | Hiện trạng | |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:job_loss_vua` / `:job_loss_nang` | 0.30 | 0.50 | Vừa: tin TC-13 "khoảng 30%". Nặng: giả định – lan sang nhà cung cấp cùng KCN |
| `:buffer_months` | 3 | 3 | Giả định: thời gian tìm việc mới |
| `:ur_limit` | 0.9 | 0.9 | Giả định |
| `:gso_list`, `:province_list`, `:secured_value` | – | – | Từ K1, K2 |
| `:min_group_size` | 20 | 20 | Giả định |

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP` bước 2 (HKD, SME quanh KCN): `S02` `S03` doanh thu QR, `S11` chuỗi cung ứng – không có cột. Đề xuất bổ sung doanh thu nhận tiền theo tháng và quan hệ người mua–người bán.
- `GAP` bước 3 (chủ nhà trọ): không có cột thu tiền thuê.
- Cần xác nhận: nối `cus_*` với `trio_*` qua `cus_key` (Phase 2); `company_code` cùng hệ khóa với `customer_code`; nghĩa `c_addr_province`; cột `td_*` cờ trống.
- Quần thể phình: tin nói **một** nhà máy, dữ liệu lọc theo ngành và tỉnh. Có thể thu hẹp bằng cách chọn `company_code` từ K1 (chỉ dùng mã, không ghi tên DN).

## 6. SQL
```sql
-- K1. DN điện tử theo tỉnh và số nhân viên nhận lương (chọn gso_list, province_list)
SELECT i.gso_code, i.gso_description, i.c_addr_province,
       COUNT(DISTINCT p.company_code)  AS n_employers,
       COUNT(DISTINCT p.customer_code) AS n_employees
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
  ON i.customer_code = p.company_code
WHERE trunc(p.month_id, 'MM') = :as_of_month
  AND lower(i.gso_description) LIKE concat('%', lower(:gso_keyword), '%')
GROUP BY i.gso_code, i.gso_description, i.c_addr_province
ORDER BY n_employees DESC;

-- K2. Giá trị secured_type và độ phủ khoản trả
SELECT l.secured_type,
       COUNT(*) AS n_loans,
       SUM(CASE WHEN l.total_monthly_payment IS NULL THEN 1 ELSE 0 END) AS n_pmt_null
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
WHERE l.ds_partition_date = :as_of_date
GROUP BY l.secured_type;
```

```sql
-- Tham số
-- :as_of_month    DATE    kỳ quan sát (ngày đầu tháng)                    '2026-10-01'
-- :as_of_date     DATE    ngày chụp cus_lending                            '2026-10-31'
-- :gso_list       STRING  từ K1                                            
-- :province_list  STRING  từ K1                                            
-- :secured_value  STRING  từ K2 (giá trị nghĩa là có bảo đảm)               
-- :job_loss_vua   DOUBLE  tin TC-13 "khoảng 30%"                           0.30
-- :job_loss_nang  DOUBLE  giả định: lan sang nhà cung cấp                  0.50
-- :buffer_months  DOUBLE  giả định: thời gian tìm việc                     3
-- :ur_limit       DOUBLE  giả định                                         0.9
-- :min_group_size INT     giả định                                         20
WITH
employer AS (
  SELECT i.customer_code AS employer_key
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
  WHERE find_in_set(CAST(i.gso_code AS STRING), :gso_list) > 0
    AND find_in_set(i.c_addr_province, :province_list) > 0
),
staff AS (
  SELECT p.customer_code AS cus_key, AVG(p.month_income) AS income
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
  JOIN employer e ON p.company_code = e.employer_key
  WHERE trunc(p.month_id, 'MM') BETWEEN add_months(:as_of_month, -2) AND :as_of_month
  GROUP BY p.customer_code
  HAVING MAX(trunc(p.month_id, 'MM')) = :as_of_month          -- còn nhận lương ở kỳ quan sát
),
loans AS (
  SELECT l.customer_code AS cus_key,
         SUM(l.total_outstanding) AS os,
         SUM(CASE WHEN l.secured_type = :secured_value THEN l.total_outstanding ELSE 0 END) AS os_secured,
         SUM(l.total_monthly_payment) AS pmt,
         SUM(CASE WHEN l.total_monthly_payment IS NULL THEN 1 ELSE 0 END) AS n_pmt_null
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
  WHERE l.ds_partition_date = :as_of_date
  GROUP BY l.customer_code
),
buffer AS (
  SELECT n.customer_code AS cus_key,
         COALESCE(n.ca_eob_balance, 0) + COALESCE(n.td_az_eob_balance, 0) + COALESCE(n.td_mm_eob_balance, 0) AS buf
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_nonlending n
),
card AS (
  SELECT cc.cusid AS cus_key, cc.buncc_amt_ur_med_l1m AS card_ur
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
  WHERE cc.month = :as_of_month
),
dpd AS (
  SELECT ch.cusid AS cus_key, ch.b_num_dpd_max_l1m AS dpd_now
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history ch
  WHERE ch.month = :as_of_month
),
base AS (
  SELECT s.cus_key, s.income, lo.os, lo.os_secured, lo.pmt, lo.n_pmt_null,
         COALESCE(b.buf, 0) AS buf, c.card_ur, d.dpd_now,
         CASE WHEN lo.pmt > 0 THEN COALESCE(b.buf, 0) / lo.pmt END AS buffer_m
  FROM staff s
  LEFT JOIN loans  lo ON lo.cus_key = s.cus_key
  LEFT JOIN buffer b  ON b.cus_key  = s.cus_key
  LEFT JOIN card   c  ON c.cus_key  = s.cus_key
  LEFT JOIN dpd    d  ON d.cus_key  = s.cus_key
),
scen AS (
  SELECT * FROM VALUES ('0_co_so', 0.0D), ('1_vua', CAST(:job_loss_vua AS DOUBLE)), ('2_nang', CAST(:job_loss_nang AS DOUBLE))
  AS t(scenario, job_loss_share)
)
SELECT sn.scenario,
       CASE WHEN bs.os IS NULL OR bs.os = 0 THEN 'khong_vay'
            WHEN bs.buffer_m IS NULL           THEN 'thieu_khoan_tra'
            WHEN bs.buffer_m < :buffer_months  THEN 'dem_mong'
            ELSE 'du_dem' END                                         AS buffer_group,
       COUNT(*)                                                       AS n_customers,
       SUM(bs.os)                                                     AS os_total,
       SUM(bs.os_secured)                                             AS os_secured_total,
       sn.job_loss_share * SUM(CASE WHEN bs.buffer_m < :buffer_months THEN bs.os ELSE 0 END) AS ear_expected,
       sn.job_loss_share * SUM(CASE WHEN bs.buffer_m < :buffer_months THEN 1 ELSE 0 END)     AS n_thin_buffer_expected,
       percentile_approx(bs.pmt / NULLIF(bs.income, 0), 0.5)          AS dsr_median_before,
       SUM(CASE WHEN bs.card_ur > :ur_limit THEN 1 ELSE 0 END)        AS n_card_ur_high,
       SUM(CASE WHEN bs.dpd_now > 0 THEN 1 ELSE 0 END)                AS n_dpd_now,
       SUM(CASE WHEN bs.n_pmt_null > 0 THEN 1 ELSE 0 END)             AS n_excluded_null_pmt
FROM base bs
CROSS JOIN scen sn
GROUP BY sn.scenario, sn.job_loss_share, buffer_group
HAVING COUNT(*) >= :min_group_size
ORDER BY sn.scenario, buffer_group;
```

## 7. Cách đọc kết quả và hành động
- `ear_expected` ở nhóm `dem_mong` là phần dư nợ cần ưu tiên; so mức vừa với nặng để thấy độ nhạy theo tỷ lệ cắt giảm.
- `n_card_ur_high` và `n_dpd_now` cao ngay ở mức cơ sở nghĩa là nhóm đã căng trước tin – mức chắc chắn của bước 1 tăng.
- `n_excluded_null_pmt` lớn → kết quả `dem_mong` bị đánh giá thấp; báo chủ dữ liệu trước khi dùng.
- Hành động theo bảng (c): RM liên hệ DN về kế hoạch nhân sự (`CIB-PAY-06`); rà khoản vay nhân viên nhóm `dem_mong`, ưu tiên giãn nợ có điều kiện; **không** hạ hạn mức đồng loạt cho công nhân KCN.

## 8. Dòng nhãn
```
[WI] cua=OI | rui_ro=CN-LN-05,CN-CARD-01 | kich_ban=mat_viec_dn_dien_tu | quan_the=nhan_luong_tu_dn_gso_dien_tu_tinh_chon | soc=job_loss_share=0.30/0.50 | cong_thuc=thang_dem,EAR_ky_vong | bang=cus_payroll,cus_lending,cus_nonlending | gap=S02,S03,S11 | xac_nhan=4 | muc=co_the
```
