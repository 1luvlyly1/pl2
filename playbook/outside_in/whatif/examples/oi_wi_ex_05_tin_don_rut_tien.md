---
id: OI-WI-EX-05
used_by: [What-if, Critic]
load_when: Rủi ro thanh khoản do tin đồn, rút tiền hàng loạt, cạnh tranh lãi suất huy động – cấp ngân hàng (NH-LQ) theo địa bàn và hạng khách
version: v3.4
updated: 2026-11-04
nguon_test: TC-04
---

# Bài mẫu what-if 05 – Tin đồn thanh khoản lan tới hai tỉnh

## 1. Rủi ro gốc
TC-04 (tin giả định): mạng xã hội lan truyền tin một ngân hàng khác khó khăn thanh khoản; người dân hai tỉnh xếp hàng rút tiền ở ngân hàng đó. Playbook xếp ô C (sợ hãi), chạm `CN-PAY-02` `CN-ACC-01` `CN-DEP-01` mức P1 và cấp ngân hàng `NH-LQ-01` `NH-LQ-02`. Hành vi khuyến nghị: tăng tiếp quỹ CDM ở hai tỉnh, kịch bản trả lời tin đồn, **what-if rút gấp 3 trong 48 giờ**. Kịch bản đo: nếu tâm lý lây sang khách của ngân hàng tại hai tỉnh, lượng tiền có thể rời đi theo hạng khách và loại tiền gửi là bao nhiêu, và dấu hiệu rút tiền đã xuất hiện chưa.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách có `c_addr_province` thuộc `:province_list` (hai tỉnh trong tin – tin giả định không nêu tên, người dùng điền); nhóm đối chứng: các tỉnh còn lại |
| Cú sốc | Tỷ lệ rút theo loại tiền: CASA `runoff_ca`, tiền gửi online `runoff_td_az`, tại quầy `runoff_td_mm`, quỹ, trái phiếu `runoff_inv`; theo hạng khách nhân `:tier_mult_<hạng>` |
| Công thức | `outflow = Σ_loại runoff_loại · tier_mult · số dư_loại`; mức nặng = mức vừa × `:stress_mult` (hành vi khuyến nghị "gấp 3") |
| Mức độ | Cơ sở (0), vừa, nặng |
| Biến kết quả | Dòng ra theo tỉnh × hạng × loại tiền; dấu hiệu sớm `F01` `F02` `S06` ở kỳ quan sát (so với nhóm đối chứng) |

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò |
|---|---|---|---|
| Tỉnh, hạng | `cus_info.c_addr_province`, `priority_class` | F | Lọc, nhóm |
| CASA | `cus_nonlending.ca_eob_balance` | F | Số dư bị rút |
| Tiền gửi | `cus_nonlending.td_az_eob_balance`, `td_mm_eob_balance` | ? | Số dư bị rút |
| Đầu tư | `cus_nonlending.fund_eob_balance`, `bond_eob_balance` | ? | Bán lại (`S08`) |
| `F01` | `trio_a_hashed_rbg_a_aum.a_amt_aum_slope_l1m`, `a_amt_aum_avg_l1m`, `a_amt_aum_avg_l3m` | F | Tiền rời đi |
| `F02` | `trio_a_hashed_rbg_atxca_balance.atxca_bal_avg_l1m`, `_l3m`; `trio_a_hashed_rbg_asv_balance.asvtd_bal_avg_l1m`, `_l3m` | F | Kỳ hạn → không kỳ hạn |
| `S06` | `trio_a_hashed_rbg_asv_balance.asvtd_bal_close_early_avg_l1m`, `asvtd_num_acc_close_early_avg_l1m`, `_l3m` | F | Tất toán trước hạn |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:runoff_ca` | 0.05 | ×3 | Giả định – thay bằng tỷ lệ của khung stress test thanh khoản nội bộ |
| `:runoff_td_az` | 0.03 | ×3 | Giả định: online tất toán dễ hơn |
| `:runoff_td_mm` | 0.02 | ×3 | Giả định |
| `:runoff_inv` | 0.02 | ×3 | Giả định |
| `:tier_mult_priority` / `_other` | 1.5 / 1.0 | như vừa | Giả định: khách số dư lớn phản ứng nhanh hơn với tin đồn; tên hạng lấy từ K1 |
| `:stress_mult` | 1 | 3 | Hành vi khuyến nghị TC-04 "rút gấp 3" |
| `:priority_values` | – | – | K1 (các giá trị `priority_class` coi là hạng cao) |

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP`: `S07` rút tiền mặt CDM theo ngày – không có cột, nên **không tính được "gấp 3 trong 48 giờ" theo nghĩa đen**; kịch bản dùng tỷ lệ trên số dư thay thế. Đề xuất bổ sung giao dịch rút tiền theo ngày và theo điểm CDM.
- `GAP`: bộ đệm thanh khoản cấp ngân hàng (LCR, tài sản thanh khoản cao) – kết quả chỉ là **dòng ra giả định**, so với bộ đệm do bộ phận ALM thực hiện.
- `GAP`: `S14` khiếu nại, `F01` ngân hàng nhận – không có cột.
- Cần xác nhận: `cus_nonlending` là bản chụp mới nhất (không có cột kỳ); cột `td_*`, `fund_*`, `bond_*` cờ trống; nối `cus_*` – `trio_*` qua `cus_key`.
- Chiều cơ hội `O6` (tiền tìm nơi an toàn chuyển đến) không đo được – cần dữ liệu chuyển khoản đến theo ngân hàng nguồn.

## 6. SQL
```sql
-- K1. Hạng khách và số dư theo tỉnh (chọn province_list, priority_values)
SELECT i.c_addr_province, i.priority_class, COUNT(*) AS n_customers,
       SUM(n.ca_eob_balance) AS ca_total
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_nonlending n
  ON n.customer_code = i.customer_code
GROUP BY i.c_addr_province, i.priority_class
ORDER BY i.c_addr_province, i.priority_class;
```

```sql
-- Tham số
-- :as_of_month         DATE    kỳ quan sát                                  '2026-10-01'
-- :province_list       STRING  hai tỉnh trong tin (người dùng điền theo K1)
-- :priority_values     STRING  từ K1
-- :runoff_ca           DOUBLE  giả định                                     0.05
-- :runoff_td_az        DOUBLE  giả định                                     0.03
-- :runoff_td_mm        DOUBLE  giả định                                     0.02
-- :runoff_inv          DOUBLE  giả định                                     0.02
-- :tier_mult_priority  DOUBLE  giả định                                     1.5
-- :tier_mult_other     DOUBLE  giả định                                     1.0
-- :stress_mult         DOUBLE  hành vi khuyến nghị TC-04 "gấp 3"            3
-- :min_group_size      INT     giả định                                     20
WITH
pop AS (
  SELECT i.customer_code AS cus_key,
         CASE WHEN find_in_set(i.c_addr_province, :province_list) > 0 THEN i.c_addr_province ELSE 'doi_chung' END AS area,
         CASE WHEN find_in_set(i.priority_class, :priority_values) > 0 THEN 'hang_cao' ELSE 'hang_khac' END AS tier
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
),
bal AS (
  SELECT n.customer_code AS cus_key,
         COALESCE(n.ca_eob_balance, 0)    AS ca,
         COALESCE(n.td_az_eob_balance, 0) AS td_az,
         COALESCE(n.td_mm_eob_balance, 0) AS td_mm,
         COALESCE(n.fund_eob_balance, 0) + COALESCE(n.bond_eob_balance, 0) AS inv
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_nonlending n
),
early AS (
  SELECT au.cusid AS cus_key,
         au.a_amt_aum_slope_l1m AS aum_slope,
         au.a_amt_aum_avg_l1m / NULLIF(au.a_amt_aum_avg_l3m, 0)       AS aum_l1_vs_l3,
         ca.atxca_bal_avg_l1m / NULLIF(ca.atxca_bal_avg_l3m, 0)       AS casa_l1_vs_l3,
         sv.asvtd_bal_avg_l1m / NULLIF(sv.asvtd_bal_avg_l3m, 0)       AS td_l1_vs_l3,
         sv.asvtd_num_acc_close_early_avg_l1m                         AS close_early_l1,
         sv.asvtd_num_acc_close_early_avg_l3m                         AS close_early_l3
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_a_aum au
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_atxca_balance ca
    ON ca.cusid = au.cusid AND ca.month = au.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_asv_balance sv
    ON sv.cusid = au.cusid AND sv.month = au.month
  WHERE au.month = :as_of_month
),
base AS (
  SELECT p.area, p.tier, b.ca, b.td_az, b.td_mm, b.inv, e.aum_slope, e.aum_l1_vs_l3, e.casa_l1_vs_l3, e.td_l1_vs_l3,
         e.close_early_l1, e.close_early_l3,
         CASE WHEN p.tier = 'hang_cao' THEN CAST(:tier_mult_priority AS DOUBLE) ELSE CAST(:tier_mult_other AS DOUBLE) END AS tier_mult
  FROM pop p
  JOIN bal b ON b.cus_key = p.cus_key
  LEFT JOIN early e ON e.cus_key = p.cus_key
),
scen AS (
  SELECT * FROM VALUES ('0_co_so', 0.0D), ('1_vua', 1.0D), ('2_nang', CAST(:stress_mult AS DOUBLE)) AS t(scenario, mult)
)
SELECT sn.scenario, b.area, b.tier,
       COUNT(*)                                                     AS n_customers,
       SUM(b.ca)                                                    AS ca_total,
       SUM(b.td_az + b.td_mm)                                       AS td_total,
       SUM(b.inv)                                                   AS inv_total,
       SUM(least(1.0D, sn.mult * b.tier_mult * :runoff_ca)    * b.ca)    AS outflow_ca,
       SUM(least(1.0D, sn.mult * b.tier_mult * :runoff_td_az) * b.td_az
         + least(1.0D, sn.mult * b.tier_mult * :runoff_td_mm) * b.td_mm) AS outflow_td,
       SUM(least(1.0D, sn.mult * b.tier_mult * :runoff_inv)   * b.inv)   AS outflow_inv,
       AVG(CASE WHEN b.aum_slope < 0 THEN 1.0 ELSE 0.0 END)          AS share_aum_falling,
       percentile_approx(b.casa_l1_vs_l3, 0.5)                      AS casa_l1_vs_l3_median,
       percentile_approx(b.td_l1_vs_l3, 0.5)                        AS td_l1_vs_l3_median,
       SUM(b.close_early_l1) / NULLIF(SUM(b.close_early_l3), 0)     AS close_early_l1_vs_l3
FROM base b
CROSS JOIN scen sn
GROUP BY sn.scenario, b.area, b.tier
HAVING COUNT(*) >= :min_group_size
ORDER BY sn.scenario, b.area, b.tier;
```

## 7. Cách đọc kết quả và hành động
- `outflow_*` ở mức nặng của hai tỉnh là con số đưa cho ALM và vận hành tiền mặt so với bộ đệm và quỹ CDM chi nhánh; không tự kết luận "đủ" hay "thiếu".
- Dấu hiệu sớm: `share_aum_falling`, `td_l1_vs_l3_median` thấp hơn và `close_early_l1_vs_l3` cao hơn rõ so với dòng `doi_chung` → tin đồn đã lây sang khách của ngân hàng; nâng mức chắc chắn và kích hoạt kịch bản trả lời tin đồn.
- Không khác biệt với đối chứng → giữ ở mức theo dõi; không phát thông điệp gây chú ý thêm.
- Hành động theo bảng (c) `CN-PAY-02` `CN-DEP-01`: tăng tiếp quỹ CDM hai tỉnh, RM gọi khách hạng cao có số dư lớn, chuẩn bị trả lời chính thức. Không dùng tin đồn về ngân hàng khác để tiếp thị (`RP`).

## 8. Dòng nhãn
```
[WI] cua=OI | rui_ro=CN-PAY-02,CN-DEP-01,NH-LQ-01 | kich_ban=tin_don_rut_tien_2_tinh | quan_the=khach_2_tinh_va_doi_chung | soc=runoff_ca=0.05;td=0.02-0.03;inv=0.02;stress_mult=1/3 | cong_thuc=dong_ra_tien_gui | bang=cus_info,cus_nonlending,trio_rbg | gap=S07,LCR,S14,O6 | xac_nhan=3 | muc=co_the
```
