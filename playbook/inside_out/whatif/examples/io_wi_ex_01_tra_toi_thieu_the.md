---
id: IO-WI-EX-01
used_by: [What-if, Critic]
load_when: Một tín hiệu nội bộ đang xấu đi (ví dụ S05 trả tối thiểu thẻ, S04 dùng hạn mức tăng) và cần dự phóng bao nhiêu khách, bao nhiêu dư nợ chuyển sang quá hạn nếu xu hướng kéo dài
version: v3.4
updated: 2026-11-04
---

# Bài mẫu what-if inside-out 01 – Số khách trả tối thiểu thẻ tăng: dự phóng quá hạn bằng tỷ lệ lịch sử

## 1. Sự kiện nội bộ
Bộ phận theo dõi danh mục thẻ thấy số khách chỉ trả mức tối thiểu (`S05`) tăng liên tục mấy tháng gần đây. Theo `inside_out/signals.md`, đây là tín hiệu "sắp quá hạn" của KHCN, chạm `CN-CARD-01` (mức **P2** trong bảng (c)). Câu hỏi của người ra quyết định: **nếu xu hướng giữ nguyên thêm 3 tháng, bao nhiêu khách và bao nhiêu số dư thẻ có thể chuyển sang quá hạn, nhóm khách nào nặng nhất**. Kịch bản không giả định tỷ lệ chuyển mà tính nó từ chính dữ liệu các tháng trước.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách có thẻ tín dụng, chưa quá hạn ở thời điểm gốc; chia theo hạng (`priority_class`) |
| Trạng thái A (tín hiệu) | Số lần trả tối thiểu trong 3 tháng `buncc_num_min_paid_cnt_l3m ≥ :min_paid_trigger` |
| Trạng thái B (hậu quả) | Số ngày quá hạn lớn nhất trong tháng `b_num_dpd_max_l1m > :dpd_days` |
| Công thức | Tỷ lệ lịch sử `rate_A = khách A ở t0 có B ở t0+h / khách A ở t0` (chỉ khách chưa quá hạn ở t0); đối chứng `rate_notA` cho khách không có A. Dự phóng: `số khách B kỳ vọng = rate_A × số khách A hiện tại`; `số dư B kỳ vọng = rate_A × Σ số dư thẻ ước tính của nhóm A` |
| Mức độ | Cơ sở (tỷ lệ lịch sử); nặng (tỷ lệ lịch sử × `:stress_mult`) |
| Biến kết quả | Tỷ lệ lịch sử của nhóm A và đối chứng, cỡ nhóm, số khách và số dư thẻ dự phóng chuyển quá hạn |

`rate_A` so với `rate_notA` cho biết tín hiệu `S05` có thật sự báo trước quá hạn ở danh mục này hay không. Nếu hai tỷ lệ gần nhau, tín hiệu không có giá trị dự báo và kịch bản dừng ở đó.

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò | Ghi chú |
|---|---|---|---|---|
| Trả tối thiểu | `trio_a_hashed_rbg_buncc_payment.buncc_num_min_paid_cnt_l3m` | F | Trạng thái A | Ở hai tháng: gốc và hiện tại |
| Hạn mức thẻ | `trio_a_hashed_rbg_buncc_payment.buncc_amt_card_limit_max_l1m` | F | Ước tính số dư | |
| Tỷ lệ sử dụng | `trio_a_hashed_rbg_buncc_payment.buncc_amt_ur_med_l1m` | F | Ước tính số dư | Số dư ≈ hạn mức × tỷ lệ sử dụng trung vị – thay thế, vì danh mục không có số dư thẻ |
| Quá hạn | `trio_a_hashed_b_credit_history.b_num_dpd_max_l1m` | F | Trạng thái B; loại khách đã quá hạn ở t0 | |
| Hạng khách | `cus_info.priority_class` | F | Nhóm | Giá trị qua K1 |

## 4. Tham số
| Tham số | Giá trị | Nguồn |
|---|---|---|
| `:horizon_months` | 3 | Câu hỏi của người ra quyết định ("thêm 3 tháng") |
| `:min_paid_trigger` | 2 | Giả định: trả tối thiểu từ 2 lần trong 3 tháng mới coi là thói quen, không phải ngẫu nhiên |
| `:dpd_days` | 0 (mức nhẹ) hoặc 30 | Giả định; chạy cả hai để thấy quá hạn sớm và quá hạn thật |
| `:stress_mult` | 1.5 | Giả định cho mức nặng; thay bằng tỷ lệ của tháng gốc xấu nhất nếu chạy nhiều tháng gốc |
| `:priority_values` | – | K1 |
| `:min_group_size` | 20 | Giả định |

## 5. Thiếu dữ liệu và cần xác nhận
- Thay thế: số dư thẻ ước tính bằng hạn mức × tỷ lệ sử dụng trung vị, vì danh mục không có số dư thẻ cuối tháng. Đề xuất bổ sung số dư thẻ và số tiền đến hạn.
- Giả định của tỷ lệ lịch sử: 3 tháng tới giống giai đoạn lịch sử; chính sách thu nợ không đổi.
- Cần xác nhận: nối `cus_info` (customer_code) với bảng `trio_*` (cusid) qua `cus_key`; dữ liệu `trio_*` có đủ tháng gốc `:as_of_month − :horizon_months`.
- `b_num_dpd_max_l1m` là quá hạn của mọi khoản của khách, không riêng thẻ – kết quả là "khách có quá hạn", không phải "thẻ quá hạn".

## 6. SQL
```sql
-- K1. Hạng khách và độ phủ dữ liệu thẻ ở hai tháng
SELECT i.priority_class,
       COUNT(DISTINCT CASE WHEN cc.month = :as_of_month THEN cc.cusid END)                              AS n_card_now,
       COUNT(DISTINCT CASE WHEN cc.month = add_months(:as_of_month, -:horizon_months) THEN cc.cusid END) AS n_card_t0
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
  ON i.customer_code = cc.cusid
WHERE cc.month IN (:as_of_month, add_months(:as_of_month, -:horizon_months))
GROUP BY i.priority_class
ORDER BY i.priority_class;
```

```sql
-- Tham số
-- :as_of_month       DATE    tháng hiện tại (ngày đầu tháng)                   '2026-10-01'
-- :horizon_months    INT     câu hỏi "thêm 3 tháng"                            3
-- :min_paid_trigger  INT     giả định                                          2
-- :dpd_days          INT     giả định (0 hoặc 30)                              0
-- :stress_mult       DOUBLE  giả định cho mức nặng                             1.5
-- :priority_values   STRING  từ K1
-- :min_group_size    INT     giả định                                          20
WITH
tier AS (
  SELECT i.customer_code AS cus_key,
         CASE WHEN find_in_set(i.priority_class, :priority_values) > 0 THEN 'hang_cao' ELSE 'hang_khac' END AS tier
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
),
t0 AS (                                  -- trạng thái ở tháng gốc
  SELECT cc0.cusid AS cus_key,
         CASE WHEN cc0.buncc_num_min_paid_cnt_l3m >= :min_paid_trigger THEN 1 ELSE 0 END AS flag_a
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc0
  JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history ch0
    ON ch0.cusid = cc0.cusid AND ch0.month = cc0.month
  WHERE cc0.month = add_months(:as_of_month, -:horizon_months)
    AND COALESCE(ch0.b_num_dpd_max_l1m, 0) = 0           -- chỉ khách chưa quá hạn ở tháng gốc
),
t1 AS (                                  -- hậu quả sau h tháng
  SELECT ch1.cusid AS cus_key,
         CASE WHEN ch1.b_num_dpd_max_l1m > :dpd_days THEN 1 ELSE 0 END AS flag_b
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history ch1
  WHERE ch1.month = :as_of_month
),
hist AS (
  SELECT tr.tier,
         SUM(t0.flag_a)                                                        AS n_hist_a,
         SUM(t0.flag_a * COALESCE(t1.flag_b, 0)) / NULLIF(SUM(t0.flag_a), 0)   AS rate_a,
         SUM((1 - t0.flag_a) * COALESCE(t1.flag_b, 0)) / NULLIF(SUM(1 - t0.flag_a), 0) AS rate_not_a
  FROM t0
  JOIN tier tr ON tr.cus_key = t0.cus_key
  LEFT JOIN t1 ON t1.cus_key = t0.cus_key
  GROUP BY tr.tier
),
now_a AS (                               -- nhóm đang có tín hiệu ở hiện tại, chưa quá hạn
  SELECT tr.tier,
         COUNT(*)                                                         AS n_now_a,
         SUM(cc.buncc_amt_card_limit_max_l1m * cc.buncc_amt_ur_med_l1m)   AS card_bal_est_now_a
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
  JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_b_credit_history ch
    ON ch.cusid = cc.cusid AND ch.month = cc.month
  JOIN tier tr ON tr.cus_key = cc.cusid
  WHERE cc.month = :as_of_month
    AND cc.buncc_num_min_paid_cnt_l3m >= :min_paid_trigger
    AND COALESCE(ch.b_num_dpd_max_l1m, 0) = 0
  GROUP BY tr.tier
),
scen AS (
  SELECT * FROM VALUES ('1_lich_su', 1.0D), ('2_nang', CAST(:stress_mult AS DOUBLE)) AS t(scenario, mult)
)
SELECT sn.scenario, h.tier,
       h.n_hist_a, h.rate_a, h.rate_not_a,
       h.rate_a / NULLIF(h.rate_not_a, 0)                            AS lift_vs_control,
       n.n_now_a, n.card_bal_est_now_a,
       least(1.0D, sn.mult * h.rate_a) * n.n_now_a                   AS n_dpd_projected,
       least(1.0D, sn.mult * h.rate_a) * n.card_bal_est_now_a        AS card_bal_dpd_projected
FROM hist h
JOIN now_a n ON n.tier = h.tier
CROSS JOIN scen sn
WHERE h.n_hist_a >= :min_group_size AND n.n_now_a >= :min_group_size
ORDER BY sn.scenario, h.tier;
```

## 7. Cách đọc kết quả và hành động
- `lift_vs_control` lớn (tỷ lệ quá hạn của nhóm có tín hiệu cao gấp nhiều lần nhóm đối chứng) xác nhận `S05` có giá trị báo trước; gần 1 thì tín hiệu không đáng dùng để hành động.
- `n_dpd_projected`, `card_bal_dpd_projected` là quy mô cần chuẩn bị cho thu nợ sớm và dự phòng; so `hang_cao` với `hang_khac` để chọn kênh tiếp cận.
- Hành động theo bảng (c) `CN-CARD-01`: liên hệ sớm nhóm có tín hiệu để đề xuất trả góp dư nợ thẻ trước khi quá hạn; **không** cắt hạn mức đồng loạt nhóm này mà chưa chạy kịch bản 02 (siết hạn mức tạo rủi ro thứ cấp).
- Theo dõi lại sau 1 tháng: nếu tỷ lệ thực tế vượt mức nặng, chạy lại với nhiều tháng gốc để kiểm tra xu hướng.

## 8. Dòng nhãn
```
[WI] cua=IO | rui_ro=CN-CARD-01 | kich_ban=s05_tra_toi_thieu_du_phong_qua_han | quan_the=khach_the_chua_qua_han_theo_hang | soc=horizon_months=3;stress_mult=1/1.5 | cong_thuc=ty_le_chuyen_trang_thai | bang=trio_rbg_buncc_payment,trio_b_credit_history | gap=so_du_the | xac_nhan=3 | muc=co_the
```
