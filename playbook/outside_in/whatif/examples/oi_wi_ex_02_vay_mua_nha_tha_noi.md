---
id: OI-WI-EX-02
used_by: [What-if, Critic]
load_when: Rủi ro lãi suất thả nổi, hết ưu đãi, giá BĐS/TSBĐ giảm với khoản vay có bảo đảm KHCN
version: v3.4
updated: 2026-11-04
nguon_test: TC-20, TC-02
---

# Bài mẫu what-if 02 – Người vay mua nhà khi lãi suất thả nổi neo cao

## 1. Rủi ro gốc
TC-20 (4 tin từ 08/06 đến 27/08/2026, một nguyên nhân – không mở cụm) và TC-02 (lãi huy động bình quân 6,46%) cùng dẫn tới `CN-LN-01` `CN-LN-02` mức P2: người vay hết ưu đãi chuyển sang lãi thả nổi, khoản trả hằng tháng tăng; biến thể TC-20 thêm giá căn hộ thứ cấp giảm. Kịch bản đo hai lớp: **áp lực trả nợ** (DSR sau sốc) và **đệm TSBĐ** (LTV sau sốc giá).

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách có khoản vay thuộc `:mortgage_products` (tra K1) tại `:as_of_date` |
| Cú sốc | Khoản trả tăng `pmt_uplift`; giá TSBĐ giảm `coll_haircut` |
| Công thức | `DSR_sau = P·(1+pmt_uplift) / I`; `LTV_sau = OS / (C·(1−coll_haircut))`; căng kép = `DSR_sau > :dsr_limit` **và** `LTV_sau > :ltv_limit` |
| Mức độ | Cơ sở, vừa, nặng |
| Biến kết quả | Số khách và dư nợ theo nhóm DSR sau sốc; số khách căng kép; quá hạn hiện tại để đối chiếu |

**Suy ra tham số từ tin.** Không có lãi suất hợp đồng và kỳ hạn còn lại, nên đổi chênh lãi suất trong tin thành % tăng khoản trả theo công thức niên kim `P = r/(1−(1+r)^−n)` với kỳ hạn còn lại giả định 20 năm: 9% → 13% cho +30%; 9% → 16% cho +55% (kỳ hạn 15 năm: +25% và +45%). Đây là **giả định suy ra**, không phải dữ liệu khách.

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò | Ghi chú |
|---|---|---|---|---|
| Sản phẩm vay | `cus_lending.product_name` | F | Lọc | K1 |
| `OS`, `P` | `cus_lending.total_outstanding`, `total_monthly_payment` | F | DSR, LTV | Gộp theo khách; báo null |
| `I` chính | `cus_payroll.month_income` | F | DSR | Bình quân 3 tháng |
| `I` dự phòng | `trio_a_hashed_rbg_atxca_service_channel.atxca_amt_sal_sum_l1m` | F | DSR khi không có `cus_payroll` | Ghi rõ nguồn thu nhập trong kết quả |
| `C` | `cus_coll_transformed.nominal_value` | A | LTV | Cờ 0 – cần xác nhận |
| Loại TSBĐ | `cus_coll_transformed.tsdb_mt` | F | Chỉ lấy BĐS | K2 |
| Quá hạn | `trio_a_hashed_b_credit_history.b_num_dpd_max_l1m`, `trio_a_hashed_b_credit_history_monthly.b_num_mth_gt0_dpd_cnt_l6m` | F | Hiện trạng | |
| Thẻ trả tối thiểu | `trio_a_hashed_rbg_buncc_payment.buncc_num_min_paid_cnt_l3m` | F | `S05` | |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:pmt_uplift_vua` / `_nang` | 0.30 | 0.55 | Suy ra từ tin 08/06/2026 ("từ 8–10% lên 13–15%") và 04/08/2026 ("13–16%"), kỳ hạn còn lại giả định 20 năm |
| `:coll_haircut_vua` / `_nang` | 0.10 | 0.20 | Giả định: biến thể TC-20 "giá căn hộ thứ cấp giảm" không nêu mức |
| `:dsr_low` / `:dsr_limit` | 0.3 / 0.5 | 0.3 / 0.5 | Giả định – ranh nhóm thấp và ngưỡng nội bộ; thay bằng ngưỡng của ngân hàng |
| `:ltv_limit` | 0.8 | 0.8 | Giả định – thay bằng ngưỡng nội bộ |
| `:mortgage_products`, `:coll_type_list` | – | – | K1, K2 |

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP`: ngày hết ưu đãi, lãi suất hợp đồng, kỳ hạn còn lại – không có cột. Đề xuất bổ sung để thay tham số `pmt_uplift` bằng tính theo từng khoản; khi có, áp sốc chỉ cho khoản hết ưu đãi trong 6 tháng tới.
- `GAP`: `F03` (bán TSBĐ trả nợ trước hạn) chỉ đo gián tiếp.
- Cần xác nhận: `nominal_value` là giá trị định giá hay giá trị danh nghĩa; TSBĐ gắn theo khách (một khách nhiều khoản vay → LTV cấp khách); nối `cus_*` – `trio_*` qua `cus_key`.
- Ngoài phạm vi: không dự báo lãi suất (TC-20 "Không được").

## 6. SQL
```sql
-- K1. Sản phẩm vay có bảo đảm
SELECT l.product_name, l.secured_type, COUNT(DISTINCT l.customer_code) AS n_customers,
       SUM(l.total_outstanding) AS os_total,
       AVG(CASE WHEN l.total_monthly_payment IS NULL THEN 1.0 ELSE 0.0 END) AS pmt_null_rate
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
WHERE l.ds_partition_date = :as_of_date
GROUP BY l.product_name, l.secured_type
ORDER BY os_total DESC;

-- K2. Loại TSBĐ và độ phủ giá trị
SELECT cl.tsdb_mt, COUNT(*) AS n_coll,
       AVG(CASE WHEN cl.nominal_value IS NULL OR cl.nominal_value = 0 THEN 1.0 ELSE 0.0 END) AS value_missing_rate
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_coll_transformed cl
WHERE cl.ds_partition_date = :as_of_date
GROUP BY cl.tsdb_mt
ORDER BY n_coll DESC;
```

```sql
-- Tham số
-- :as_of_month       DATE    kỳ quan sát                                      '2026-10-01'
-- :as_of_date        DATE    ngày chụp cus_lending, cus_coll_transformed      '2026-10-31'
-- :mortgage_products STRING  từ K1
-- :coll_type_list    STRING  từ K2
-- :pmt_uplift_vua    DOUBLE  suy ra từ tin 08/06/2026, kỳ hạn giả định 20 năm  0.30
-- :pmt_uplift_nang   DOUBLE  suy ra từ tin 04/08/2026, kỳ hạn giả định 20 năm  0.55
-- :coll_haircut_vua  DOUBLE  giả định                                          0.10
-- :coll_haircut_nang DOUBLE  giả định                                          0.20
-- :dsr_low           DOUBLE  giả định – ranh nhóm thấp                         0.3
-- :dsr_limit         DOUBLE  giả định – ngưỡng nội bộ                          0.5
-- :ltv_limit         DOUBLE  giả định – ngưỡng nội bộ                          0.8
-- :min_group_size    INT     giả định                                          20
WITH
mort AS (
  SELECT l.customer_code AS cus_key,
         SUM(l.total_outstanding)     AS os,
         SUM(l.total_monthly_payment) AS pmt,
         SUM(CASE WHEN l.total_monthly_payment IS NULL THEN 1 ELSE 0 END) AS n_pmt_null
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
  WHERE l.ds_partition_date = :as_of_date
    AND find_in_set(l.product_name, :mortgage_products) > 0
  GROUP BY l.customer_code
),
pay AS (
  SELECT p.customer_code AS cus_key, AVG(p.month_income) AS income_payroll
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
  WHERE trunc(p.month_id, 'MM') BETWEEN add_months(:as_of_month, -2) AND :as_of_month
  GROUP BY p.customer_code
),
sal AS (
  SELECT sc.cusid AS cus_key, sc.atxca_amt_sal_sum_l1m AS income_casa
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_atxca_service_channel sc
  WHERE sc.month = :as_of_month
),
coll AS (
  SELECT cl.customer_code AS cus_key, SUM(cl.nominal_value) AS coll_value
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_coll_transformed cl
  WHERE cl.ds_partition_date = :as_of_date
    AND find_in_set(cl.tsdb_mt, :coll_type_list) > 0
  GROUP BY cl.customer_code
),
cr AS (
  SELECT ch.cusid AS cus_key, ch.b_num_dpd_max_l1m AS dpd_now,
         chm.b_num_mth_gt0_dpd_cnt_l6m AS mth_dpd_l6m,
         cc.buncc_num_min_paid_cnt_l3m AS min_paid_l3m
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history ch
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history_monthly chm
    ON chm.cusid = ch.cusid AND chm.month = ch.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
    ON cc.cusid = ch.cusid AND cc.month = ch.month
  WHERE ch.month = :as_of_month
),
base AS (
  SELECT m.cus_key, m.os, m.pmt, m.n_pmt_null,
         COALESCE(py.income_payroll, s.income_casa) AS income,
         CASE WHEN py.income_payroll IS NOT NULL THEN 'payroll'
              WHEN s.income_casa IS NOT NULL THEN 'luong_casa' ELSE 'khong_co' END AS income_src,
         c.coll_value, r.dpd_now, r.mth_dpd_l6m, r.min_paid_l3m
  FROM mort m
  LEFT JOIN pay  py ON py.cus_key = m.cus_key
  LEFT JOIN sal  s  ON s.cus_key  = m.cus_key
  LEFT JOIN coll c  ON c.cus_key  = m.cus_key
  LEFT JOIN cr   r  ON r.cus_key  = m.cus_key
),
scen AS (
  SELECT * FROM VALUES
    ('0_co_so', 0.0D, 0.0D),
    ('1_vua',  CAST(:pmt_uplift_vua AS DOUBLE),  CAST(:coll_haircut_vua AS DOUBLE)),
    ('2_nang', CAST(:pmt_uplift_nang AS DOUBLE), CAST(:coll_haircut_nang AS DOUBLE))
  AS t(scenario, pmt_uplift, coll_haircut)
),
shocked AS (
  SELECT sn.scenario, b.*,
         b.pmt * (1 + sn.pmt_uplift) / NULLIF(b.income, 0)          AS dsr_after,
         b.os / NULLIF(b.coll_value * (1 - sn.coll_haircut), 0)      AS ltv_after
  FROM base b CROSS JOIN scen sn
)
SELECT scenario, income_src,
       CASE WHEN dsr_after IS NULL THEN 'khong_tinh_duoc'
            WHEN dsr_after <= :dsr_low THEN 'a_thap'
            WHEN dsr_after <= :dsr_limit THEN 'b_trung_binh'
            ELSE 'c_vuot_nguong' END                                       AS dsr_group,
       COUNT(*)                                                            AS n_customers,
       SUM(os)                                                             AS os_total,
       percentile_approx(dsr_after, 0.5)                                   AS dsr_median,
       SUM(pmt) / NULLIF(SUM(income), 0)                                   AS dsr_pooled,
       SUM(CASE WHEN ltv_after > :ltv_limit THEN 1 ELSE 0 END)             AS n_ltv_over,
       SUM(CASE WHEN dsr_after > :dsr_limit AND ltv_after > :ltv_limit THEN os ELSE 0 END) AS os_double_stress,
       SUM(CASE WHEN dpd_now > 0 THEN 1 ELSE 0 END)                        AS n_dpd_now,
       SUM(CASE WHEN min_paid_l3m > 0 THEN 1 ELSE 0 END)                   AS n_card_min_paid,
       SUM(CASE WHEN n_pmt_null > 0 OR coll_value IS NULL THEN 1 ELSE 0 END) AS n_excluded_null
FROM shocked
GROUP BY scenario, income_src, dsr_group
HAVING COUNT(*) >= :min_group_size
ORDER BY scenario, income_src, dsr_group;
```

## 7. Cách đọc kết quả và hành động
- So `os_total` của nhóm `c_vuot_nguong` giữa cơ sở, vừa, nặng: phần chuyển nhóm là dư nợ bị cú sốc lãi suất đẩy qua ngưỡng.
- `os_double_stress` là ưu tiên cao nhất: vừa khó trả vừa mỏng đệm TSBĐ – nơi `F03` (bán gấp TSBĐ) dễ xảy ra.
- Nhóm `income_src = khong_co` không đánh giá được DSR; đọc riêng, không gộp vào kết luận.
- Hành động theo bảng (c) `CN-LN-01`: lập danh sách khoản hết ưu đãi theo tháng (cần cột bổ sung); RM chủ động đề xuất cơ cấu kỳ hạn cho nhóm căng kép; theo dõi `S05`, `F03`. Không đề xuất thu hồi khoản vay đồng loạt.
- Chiều cơ hội (TC-02, `O2`): người gửi tiền hưởng lãi cao – đo bằng kịch bản ngược ở bài 05 (dòng tiền gửi), không đo ở đây.

## 8. Dòng nhãn
```
[WI] cua=OI | rui_ro=CN-LN-01,CN-LN-02 | kich_ban=tha_noi_va_giam_gia_tsbd | quan_the=vay_san_pham_mortgage_products | soc=pmt_uplift=0.30/0.55;coll_haircut=0.10/0.20 | cong_thuc=DSR,LTV | bang=cus_lending,cus_payroll,cus_coll_transformed | gap=ngay_het_uu_dai,lai_suat_hop_dong | xac_nhan=3 | muc=co_the
```
