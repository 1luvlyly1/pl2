---
id: OI-WI-EX-03
used_by: [What-if, Critic]
load_when: Cụm rủi ro theo vùng và nhóm người ([CUM]) khi dữ liệu không có thu nhập trực tiếp của nhóm – cách xử lý GAP và cộng dồn nhiều nguyên nhân
version: v3.4
updated: 2026-11-04
nguon_test: TC-16
---

# Bài mẫu what-if 03 – Nông hộ Tây Nguyên: cụm ba nguyên nhân, thiếu dữ liệu thu nhập

## 1. Rủi ro gốc
Cụm TC-16 mở ngày 18/07/2026 với khóa `vung=tay_nguyen × vai_tro=nong_ho`, ba nguyên nhân: giá tiêu giảm (02/07), giá cà phê giảm (10/07), dịch tả lợn ở Đắk Lắk (18/07); tin ngược chiều 15/07 (tiêu tăng lại). Agent cụm kết luận mức "có thể": cách chia nhỏ rủi ro của nông hộ (cà phê, tiêu xen canh, chăn nuôi thêm) thất bại cùng lúc; sản phẩm chạm `CN-LN-08`, `CN-CARD-*`, `HKD-LN-01` (đại lý thu mua, vật tư bán chịu). Bài này minh họa hai điều: **xử lý thiếu dữ liệu** (không có thu nhập nông hộ) và **cộng dồn nhiều nguyên nhân** trong một kịch bản.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách cá nhân có `c_addr_province` thuộc `:province_list` (Tây Nguyên, tra K1) và – nếu K2 tìm được – `customer_segment` hoặc persona nông nghiệp |
| Cú sốc | Không đo được thu nhập nông hộ → sốc đặt lên **đệm thanh khoản**: mỗi nguyên nhân `k` làm hộ rút một phần đệm `draw_k` để bù thu nhập |
| Công thức | Đệm sau sốc `B' = B · Π(1 − draw_k)`; tháng đệm `M' = B' / P`; điểm căng hiện tại `stress = [S04] + [S05] + [S06] + [DPD>0]` (0–4) |
| Mức độ | Cơ sở; từng nguyên nhân riêng (tiêu, cà phê, lợn); gộp ba nguyên nhân – vừa và nặng |
| Biến kết quả | Số khách và dư nợ có `M' < :buffer_months` theo tỉnh × điểm căng; phần tăng thêm khi gộp so với nguyên nhân lớn nhất |

`Π(1 − draw_k)` cho phép thấy phần **cộng dồn**: ba cú sốc nhỏ có thể đẩy nhóm qua ngưỡng mà từng cú sốc riêng không đẩy được – đúng tinh thần cụm.

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò |
|---|---|---|---|
| Tỉnh | `cus_info.c_addr_province` | F | Lọc (cần xác nhận nghĩa) |
| Nhóm khách | `cus_info.sector`, `customer_segment`; `cus_persona.classfication_value` | F | Lọc nông nghiệp nếu có giá trị phù hợp |
| `OS`, `P` | `cus_lending.total_outstanding`, `total_monthly_payment` | F | Phơi nhiễm, mẫu số |
| `B` | `cus_nonlending.ca_eob_balance`, `td_az_eob_balance`, `td_mm_eob_balance` | F, ?, ? | Đệm |
| `S04` | `trio_a_hashed_rbg_buncc_payment.buncc_amt_ur_med_l1m`, `_l6m`; `trio_a_hashed_bunod_ur.bunod_amt_ur_med_l1m`, `_l6m` | F | Điểm căng |
| `S05` | `trio_a_hashed_rbg_buncc_payment.buncc_num_min_paid_cnt_l3m` | F | Điểm căng |
| `S06` | `trio_a_hashed_rbg_asv_balance.asvtd_num_acc_close_early_avg_l1m` | F | Điểm căng |
| Quá hạn | `trio_a_hashed_b_credit_history.b_num_dpd_max_l1m` | F | Điểm căng |
| Xu hướng tài sản | `trio_a_hashed_rbg_a_aum.a_amt_aum_slope_l3m` | F | Đọc kèm (`F01` thay thế) |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:draw_tieu` | 0.10 | 0.20 | Giả định. Tin 02/07: giá tiêu giảm 2.000–4.000 đồng/kg; tin ngược 15/07 tiêu tăng lại → mức vừa thấp |
| `:draw_caphe` | 0.15 | 0.30 | Giả định. Tin 10/07: cà phê giảm 2.500 đồng/kg; cà phê là cây chính nên đặt cao hơn tiêu |
| `:draw_lon` | 0.10 | 0.25 | Giả định. Tin 18/07: dịch ở 113 hộ, tiêu hủy hơn 8.500 con – cục bộ |
| `:buffer_months` | 6 | 6 | Giả định: thu nhập nông hộ theo mùa vụ, cần đệm dài hơn người làm công |
| `:ur_jump` | 0.15 | 0.15 | Giả định: mức tăng tỷ lệ dùng hạn mức l1m so với l6m coi là `S04` |
| `:province_list`, `:segment_list` | – | – | K1, K2 |

Không lấy số trong tin (đồng/kg) làm % thu nhập: không có giá vốn, sản lượng, diện tích – mọi `draw_k` là giả định và phải ghi như vậy.

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP` thu nhập nông hộ, sản lượng, mùa vụ – không có cột. Đề xuất bổ sung: dòng tiền vào CASA cá nhân theo tháng (tương tự `atxca_txn_amt_in_avg_*` của DN) để đo trực tiếp.
- `GAP` `S02` `S07` theo vùng (QR, CDM) – không có cột.
- `GAP` `HKD-LN-01` (đại lý thu mua, vật tư bán chịu): không có cờ HKD; nếu K2 tìm được giá trị HKD trong `customer_segment`/persona thì chạy lại với bộ lọc đó.
- Cần xác nhận: tên tỉnh trong dữ liệu là tên trước hay sau sắp xếp đơn vị hành chính 2025 (K1 trả cả hai nếu có); nếu là tên tỉnh mới, quần thể có thể gồm cả vùng ngoài Tây Nguyên → ghi "quần thể phình". Persona: một khách nhiều dòng → lọc bằng `EXISTS`.
- Ngoài phạm vi: không gộp ba tin thành một nguyên nhân "nông nghiệp" (TC-16 "Không được").

## 6. SQL
```sql
-- K1. Tên tỉnh trong dữ liệu (tìm các tỉnh Tây Nguyên, cả tên cũ và mới)
SELECT i.c_addr_province, COUNT(*) AS n_customers
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
GROUP BY i.c_addr_province
ORDER BY i.c_addr_province;

-- K2. Nhóm khách, persona trong các tỉnh đã chọn (tìm giá trị nông nghiệp, HKD)
SELECT i.sector, i.customer_segment, ps.classfication_value, COUNT(DISTINCT i.customer_code) AS n_customers
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_persona ps
  ON ps.customer_code = i.customer_code
WHERE find_in_set(i.c_addr_province, :province_list) > 0
GROUP BY i.sector, i.customer_segment, ps.classfication_value
ORDER BY n_customers DESC;
```

```sql
-- Tham số
-- :as_of_month    DATE    kỳ quan sát                                  '2026-10-01'
-- :as_of_date     DATE    ngày chụp cus_lending                        '2026-10-31'
-- :province_list  STRING  từ K1
-- :segment_list   STRING  từ K2 (giá trị customer_segment; để '' nếu không lọc)
-- :draw_tieu_vua / :draw_tieu_nang     DOUBLE  giả định  0.10 / 0.20
-- :draw_caphe_vua / :draw_caphe_nang   DOUBLE  giả định  0.15 / 0.30
-- :draw_lon_vua / :draw_lon_nang       DOUBLE  giả định  0.10 / 0.25
-- :buffer_months  DOUBLE  giả định: thu nhập theo mùa vụ               6
-- :ur_jump        DOUBLE  giả định                                     0.15
-- :min_group_size INT     giả định                                     20
WITH
pop AS (
  SELECT i.customer_code AS cus_key, i.c_addr_province AS province
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
  WHERE find_in_set(i.c_addr_province, :province_list) > 0
    AND (:segment_list = '' OR find_in_set(i.customer_segment, :segment_list) > 0)
),
loans AS (
  SELECT l.customer_code AS cus_key, SUM(l.total_outstanding) AS os, SUM(l.total_monthly_payment) AS pmt
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
  WHERE l.ds_partition_date = :as_of_date
  GROUP BY l.customer_code
),
buffer AS (
  SELECT n.customer_code AS cus_key,
         COALESCE(n.ca_eob_balance, 0) + COALESCE(n.td_az_eob_balance, 0) + COALESCE(n.td_mm_eob_balance, 0) AS buf
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_nonlending n
),
sig AS (
  SELECT ch.cusid AS cus_key,
         CASE WHEN cc.buncc_amt_ur_med_l1m - cc.buncc_amt_ur_med_l6m > :ur_jump
                OR od.bunod_amt_ur_med_l1m - od.bunod_amt_ur_med_l6m > :ur_jump THEN 1 ELSE 0 END AS s04,
         CASE WHEN cc.buncc_num_min_paid_cnt_l3m > 0 THEN 1 ELSE 0 END                         AS s05,
         CASE WHEN sv.asvtd_num_acc_close_early_avg_l1m > 0 THEN 1 ELSE 0 END                  AS s06,
         CASE WHEN ch.b_num_dpd_max_l1m > 0 THEN 1 ELSE 0 END                                  AS dpd,
         au.a_amt_aum_slope_l3m AS aum_slope
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history ch
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
    ON cc.cusid = ch.cusid AND cc.month = ch.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_bunod_ur od
    ON od.cusid = ch.cusid AND od.month = ch.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_asv_balance sv
    ON sv.cusid = ch.cusid AND sv.month = ch.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_a_aum au
    ON au.cusid = ch.cusid AND au.month = ch.month
  WHERE ch.month = :as_of_month
),
base AS (
  SELECT p.cus_key, p.province, lo.os, lo.pmt, COALESCE(b.buf, 0) AS buf,
         COALESCE(g.s04, 0) + COALESCE(g.s05, 0) + COALESCE(g.s06, 0) + COALESCE(g.dpd, 0) AS stress,
         g.aum_slope
  FROM pop p
  JOIN loans lo ON lo.cus_key = p.cus_key          -- chỉ khách có dư nợ
  LEFT JOIN buffer b ON b.cus_key = p.cus_key
  LEFT JOIN sig    g ON g.cus_key = p.cus_key
),
scen AS (
  SELECT * FROM VALUES
    ('0_co_so',        0.0D, 0.0D, 0.0D),
    ('1_tieu_vua',     CAST(:draw_tieu_vua AS DOUBLE), 0.0D, 0.0D),
    ('2_caphe_vua',    0.0D, CAST(:draw_caphe_vua AS DOUBLE), 0.0D),
    ('3_lon_vua',      0.0D, 0.0D, CAST(:draw_lon_vua AS DOUBLE)),
    ('4_cum_vua',      CAST(:draw_tieu_vua AS DOUBLE),  CAST(:draw_caphe_vua AS DOUBLE),  CAST(:draw_lon_vua AS DOUBLE)),
    ('5_cum_nang',     CAST(:draw_tieu_nang AS DOUBLE), CAST(:draw_caphe_nang AS DOUBLE), CAST(:draw_lon_nang AS DOUBLE))
  AS t(scenario, d_tieu, d_caphe, d_lon)
),
shocked AS (
  SELECT sn.scenario, b.province, b.stress, b.os, b.pmt, b.aum_slope,
         b.buf * (1 - sn.d_tieu) * (1 - sn.d_caphe) * (1 - sn.d_lon) / NULLIF(b.pmt, 0) AS buffer_m_after
  FROM base b CROSS JOIN scen sn
)
SELECT scenario, province,
       CASE WHEN stress >= 2 THEN '2+' ELSE CAST(stress AS STRING) END              AS stress_score,
       COUNT(*)                                                                    AS n_customers,
       SUM(os)                                                                     AS os_total,
       SUM(CASE WHEN buffer_m_after < :buffer_months THEN 1 ELSE 0 END)            AS n_thin_buffer,
       SUM(CASE WHEN buffer_m_after < :buffer_months THEN os ELSE 0 END)           AS os_thin_buffer,
       SUM(CASE WHEN aum_slope < 0 THEN 1 ELSE 0 END)                              AS n_aum_falling,
       SUM(CASE WHEN pmt IS NULL OR pmt = 0 THEN 1 ELSE 0 END)                     AS n_excluded_null_pmt
FROM shocked
GROUP BY scenario, province, stress_score
HAVING COUNT(*) >= :min_group_size
ORDER BY scenario, province, stress_score;
```

## 7. Cách đọc kết quả và hành động
- **Phần cộng dồn**: `os_thin_buffer` của `4_cum_vua` trừ giá trị lớn nhất trong `1_`, `2_`, `3_` – đó là dư nợ chỉ lộ ra khi các nguyên nhân dồn lại. Phần này lớn thì kết luận cụm có cơ sở dữ liệu; nhỏ thì cụm chủ yếu do một nguyên nhân.
- Nhóm `stress_score = 2+` ở mức cơ sở đã căng trước cụm; ưu tiên RM chi nhánh.
- Kết quả theo tỉnh giúp kiểm chứng "tiêu chí vùng" của cụm; tỉnh không khác biệt → hạ mức cụm.
- Hành động: RM chi nhánh Tây Nguyên rà khoản vay sản xuất nông nghiệp trước mùa thu hoạch; cân nhắc giãn kỳ trả theo mùa vụ; theo dõi `S04` `S06` hằng tháng. Không thu hẹp tín dụng đồng loạt theo vùng.

## 8. Dòng nhãn
```
[WI] cua=OI | rui_ro=CN-LN-08,CN-CARD-01,HKD-LN-01 | kich_ban=cum_nong_ho_tay_nguyen | quan_the=ca_nhan_co_du_no_tinh_tay_nguyen | soc=draw_tieu=0.10/0.20;draw_caphe=0.15/0.30;draw_lon=0.10/0.25 | cong_thuc=thang_dem_cong_don,diem_cang | bang=cus_info,cus_lending,cus_nonlending,trio_rbg | gap=thu_nhap_nong_ho,S02,S07,HKD | xac_nhan=4 | muc=co_the
```
