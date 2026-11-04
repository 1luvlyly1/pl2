---
id: IO-WI-EX-02
used_by: [What-if, Critic]
load_when: Ngân hàng đang cân nhắc một quyết định siết (cắt hạn mức thẻ, thấu chi, tăng lãi suất, giảm khẩu vị) và cần đo cả phần rủi ro giảm được lẫn rủi ro thứ cấp do quyết định tạo ra
version: v3.4
updated: 2026-11-04
---

# Bài mẫu what-if inside-out 02 – Cân nhắc cắt hạn mức thẻ của nhóm dùng nhiều: đo hai mặt của quyết định

## 1. Sự kiện nội bộ
Sau khi thấy tín hiệu `S04` (tỷ lệ dùng hạn mức tăng nhanh) và `S05` (trả tối thiểu tăng), ngân hàng cân nhắc cắt một phần hạn mức thẻ của nhóm đang dùng trên 90% hạn mức. `inside_out/bank_response_risks.md` cảnh báo đúng phản ứng này: "siết hạn mức tín chấp/thấu chi – khách đang căng thẳng mất nguồn đệm, quá hạn tăng nhanh hơn". Câu hỏi: **quyết định giảm được bao nhiêu phơi nhiễm, và đẩy bao nhiêu khách vượt hạn mức, trong đó bao nhiêu người đang trả nợ tốt và bao nhiêu người không có tiền đệm**.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách có thẻ, tỷ lệ dùng trung vị tháng `buncc_amt_ur_med_l1m ≥ :ur_target` |
| Cú sốc | Hạn mức mới `L' = L·(1 − limit_cut)` |
| Công thức | Số dư ước tính `bal = L·ur`; tỷ lệ dùng sau cắt `ur' = ur / (1 − limit_cut)`; **mặt lợi**: hạn mức chưa dùng bị thu hẹp `freed = max(0, L − bal) − max(0, L' − bal)`; **mặt hại**: khách bị đẩy vượt hạn mức `ur' ≥ 1`, trong đó khách tốt (chưa từng quá hạn 6 tháng) và khách không có đệm (`CASA < :buffer_min_ratio × bal`) |
| Mức độ | Cơ sở (không cắt); vừa; nặng |
| Biến kết quả | Hạn mức thu hẹp, số khách và số dư bị đẩy vượt hạn mức, phần khách tốt bị chạm, phần khách không có đệm, quá hạn hiện tại |

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò |
|---|---|---|---|
| Hạn mức `L` | `trio_a_hashed_rbg_buncc_payment.buncc_amt_card_limit_max_l1m` | F | Cú sốc áp lên |
| Tỷ lệ dùng `ur` | `trio_a_hashed_rbg_buncc_payment.buncc_amt_ur_med_l1m` | F | Lọc nhóm, tính `ur'` |
| Số ngày dùng trên 90% | `trio_a_hashed_rbg_buncc_payment.buncc_num_day_ur_gt90pc_cnt_l3m` | F | Mức căng kéo dài |
| Trả tối thiểu | `trio_a_hashed_rbg_buncc_payment.buncc_num_min_paid_cnt_l3m` | F | `S05` |
| Lịch sử quá hạn | `trio_a_hashed_b_credit_history_monthly.b_num_mth_gt0_dpd_cnt_l6m` | F | Tách khách tốt |
| Quá hạn hiện tại | `trio_a_hashed_b_credit_history.b_num_dpd_max_l1m` | F | Hiện trạng |
| CASA | `trio_a_hashed_rbg_atxca_balance.atxca_bal_avg_l1m` | F | Đệm |
| Thấu chi tín chấp | `trio_a_hashed_bunod_ur.bunod_amt_ur_med_l1m` | F | Khách còn nguồn đệm khác hay không |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:limit_cut_vua` / `_nang` | 0.2 | 0.4 | Thông số phương án do bộ phận thẻ cung cấp; khi chưa có, giả định hai mức để thấy độ nhạy |
| `:ur_target` | 0.9 | 0.9 | Phạm vi áp dụng của phương án |
| `:buffer_min_ratio` | 0.5 | 0.5 | Giả định: CASA dưới một nửa số dư thẻ coi là không đủ đệm |
| `:od_ur_high` | 0.9 | 0.9 | Giả định |
| `:min_group_size` | 20 | 20 | Giả định |

## 5. Thiếu dữ liệu và cần xác nhận
- Thay thế: số dư thẻ ước tính bằng hạn mức × tỷ lệ dùng trung vị (danh mục không có số dư cuối tháng).
- `GAP`: không biết khách có thẻ hay khoản vay ở ngân hàng khác để chuyển sang; không đo được khả năng mất khách tốt, chỉ đếm được số khách tốt bị chạm.
- Cần xác nhận: tỷ lệ dùng là trên hạn mức của thẻ lớn nhất hay tổng hạn mức; nối các bảng `trio_*` trên (`cusid`, `month`).

## 6. SQL
```sql
-- K1. Phân bố tỷ lệ dùng hạn mức thẻ (để chọn :ur_target)
SELECT percentile_approx(cc.buncc_amt_ur_med_l1m, array(0.5, 0.75, 0.9, 0.95)) AS ur_quantiles,
       COUNT(*) AS n_card_holders
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
WHERE cc.month = :as_of_month;
```

```sql
-- Tham số
-- :as_of_month       DATE    tháng quan sát                                     '2026-10-01'
-- :ur_target         DOUBLE  phạm vi phương án                                 0.9
-- :limit_cut_vua     DOUBLE  thông số phương án hoặc giả định                  0.2
-- :limit_cut_nang    DOUBLE  thông số phương án hoặc giả định                  0.4
-- :buffer_min_ratio  DOUBLE  giả định                                          0.5
-- :od_ur_high        DOUBLE  giả định                                          0.9
-- :min_group_size    INT     giả định                                          20
WITH
pop AS (
  SELECT cc.cusid AS cus_key,
         cc.buncc_amt_card_limit_max_l1m                       AS card_limit,
         cc.buncc_amt_ur_med_l1m                               AS ur,
         cc.buncc_amt_card_limit_max_l1m * cc.buncc_amt_ur_med_l1m AS bal,
         cc.buncc_num_day_ur_gt90pc_cnt_l3m                    AS days_ur90_l3m,
         cc.buncc_num_min_paid_cnt_l3m                         AS min_paid_l3m,
         chm.b_num_mth_gt0_dpd_cnt_l6m                         AS mth_dpd_l6m,
         ch.b_num_dpd_max_l1m                                  AS dpd_now,
         ca.atxca_bal_avg_l1m                                  AS casa,
         od.bunod_amt_ur_med_l1m                               AS od_ur
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history_monthly chm
    ON chm.cusid = cc.cusid AND chm.month = cc.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history ch
    ON ch.cusid = cc.cusid AND ch.month = cc.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_atxca_balance ca
    ON ca.cusid = cc.cusid AND ca.month = cc.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_bunod_ur od
    ON od.cusid = cc.cusid AND od.month = cc.month
  WHERE cc.month = :as_of_month
    AND cc.buncc_amt_ur_med_l1m >= :ur_target
),
scen AS (
  SELECT * FROM VALUES ('0_co_so', 0.0D), ('1_vua', CAST(:limit_cut_vua AS DOUBLE)), ('2_nang', CAST(:limit_cut_nang AS DOUBLE))
  AS t(scenario, limit_cut)
),
shocked AS (
  SELECT sn.scenario, p.*,
         CASE WHEN COALESCE(p.mth_dpd_l6m, 0) = 0 THEN 'khach_tot' ELSE 'da_tung_qua_han' END AS history_group,
         p.ur / NULLIF(1 - sn.limit_cut, 0)                                               AS ur_after,
         greatest(0.0D, p.card_limit - p.bal) - greatest(0.0D, p.card_limit * (1 - sn.limit_cut) - p.bal) AS freed_limit
  FROM pop p CROSS JOIN scen sn
)
SELECT scenario, history_group,
       COUNT(*)                                                                  AS n_customers,
       SUM(bal)                                                                  AS bal_est_total,
       SUM(freed_limit)                                                          AS limit_freed,                -- mặt lợi
       SUM(CASE WHEN ur_after >= 1 THEN 1 ELSE 0 END)                            AS n_pushed_over_limit,        -- mặt hại
       SUM(CASE WHEN ur_after >= 1 THEN bal ELSE 0 END)                          AS bal_pushed_over_limit,
       SUM(CASE WHEN ur_after >= 1 AND COALESCE(casa, 0) < :buffer_min_ratio * bal THEN 1 ELSE 0 END) AS n_over_limit_no_buffer,
       SUM(CASE WHEN ur_after >= 1 AND od_ur >= :od_ur_high THEN 1 ELSE 0 END)   AS n_over_limit_od_also_high,
       SUM(CASE WHEN min_paid_l3m > 0 THEN 1 ELSE 0 END)                         AS n_min_paid_now,
       SUM(CASE WHEN dpd_now > 0 THEN 1 ELSE 0 END)                              AS n_dpd_now
FROM shocked
GROUP BY scenario, history_group
HAVING COUNT(*) >= :min_group_size
ORDER BY scenario, history_group;
```

## 7. Cách đọc kết quả và hành động
- Đặt `limit_freed` (mặt lợi) cạnh `n_pushed_over_limit` và `n_over_limit_no_buffer` (mặt hại) cho từng mức cắt. Nếu phần lớn người bị đẩy vượt hạn mức nằm ở nhóm `khach_tot`, quyết định chạm oan khách tốt và dễ làm họ chuyển đi.
- `n_over_limit_od_also_high` là nhóm mất cả hai nguồn đệm (thẻ và thấu chi) – nhóm này có khả năng quá hạn nhanh nhất sau quyết định, đúng vòng phản hồi trong `bank_response_risks.md`.
- Điều kiện để quyết định đáng làm thường là: chỉ áp dụng cho nhóm `da_tung_qua_han`, hoặc chỉ cắt phần hạn mức chưa dùng (không đẩy ai vượt hạn mức). Agent nêu điều kiện, người ra quyết định chọn.
- Sau khi áp dụng, theo dõi `S04`, `S05` và quá hạn của đúng nhóm bị cắt hằng tháng.

## 8. Dòng nhãn
```
[WI] cua=IO | rui_ro=CN-CARD-01,NH-RP-01 | kich_ban=cat_han_muc_the_nhom_dung_nhieu | quan_the=the_ur_tren_nguong | soc=limit_cut=0.2/0.4 | cong_thuc=han_muc_cang,hai_mat_quyet_dinh | bang=trio_rbg_buncc_payment,trio_b_credit_history,trio_rbg_atxca_balance | gap=no_ngan_hang_khac | xac_nhan=2 | muc=co_the
```
