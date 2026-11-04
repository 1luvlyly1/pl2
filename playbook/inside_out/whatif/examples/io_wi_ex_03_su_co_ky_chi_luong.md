---
id: IO-WI-EX-03
used_by: [What-if, Critic]
load_when: Sự cố vận hành của ngân hàng (ngân hàng số, chi lương, thanh toán) rơi vào thời điểm nhạy cảm và cần đo quy mô khách bị chạm, ai không có tiền đệm
version: v3.4
updated: 2026-11-04
---

# Bài mẫu what-if inside-out 03 – Ngân hàng số gián đoạn đúng kỳ chi lương

## 1. Sự kiện nội bộ
Bài mẫu playbook `examples/ex_P3_toan_he_thong.md` mô tả một sự cố giả định: ngân hàng số cá nhân và doanh nghiệp gián đoạn nhiều giờ vào cuối tháng, đúng kỳ trả lương. Playbook kết luận lương trả muộn có thể làm nhân viên trễ các khoản trả nợ cá nhân (kênh `L02`), chạm `SME-PAY-06`, `CIB-PAY-06` và `CN-DIG-01`. Câu hỏi what-if cho ban điều hành và bộ phận vận hành: **nếu một phần lô lương của kỳ này bị trễ, bao nhiêu người nhận lương bị chạm, tổng tiền lương bị trễ là bao nhiêu, và bao nhiêu người không có đủ tiền trong tài khoản để trả khoản nợ của tháng**. Kết quả dùng để quyết định phạm vi miễn phí phạt trả chậm và thứ tự ưu tiên khôi phục.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách nhận lương qua ngân hàng trong tháng `:as_of_month`; nhóm theo quy mô DN trả lương (số nhân viên nhận lương) |
| Cú sốc | Phần lô lương bị trễ `batch_share` (tỷ lệ lô rơi vào thời gian gián đoạn) |
| Công thức | Người bị chạm kỳ vọng = `batch_share × số người`; lương bị trễ = `batch_share × Σ lương`; người **không có đệm** = có khoản trả nợ và CASA nhỏ hơn khoản trả tháng (`CASA < P`); khoản trả có nguy cơ trễ = `batch_share × Σ P` của nhóm không có đệm |
| Mức độ | Vừa (một phần lô); nặng (toàn bộ lô của ngày gián đoạn) |
| Biến kết quả | Số người, tổng lương bị trễ, số người không có đệm và tổng khoản trả có nguy cơ trễ, theo quy mô DN |

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò |
|---|---|---|---|
| Người nhận lương, DN trả lương | `cus_payroll.customer_code`, `company_code`, `month_id` | F | Quần thể, quy mô DN |
| Lương tháng | `cus_payroll.month_income` | F | Lương bị trễ |
| Khoản trả tháng `P` | `cus_lending.total_monthly_payment` | F | Nghĩa vụ trong tháng; báo null |
| CASA | `cus_nonlending.ca_eob_balance` | F | Đệm |
| Thẻ | `trio_a_hashed_rbg_buncc_payment.buncc_amt_ur_med_l1m` | F | Người đang dùng thẻ gần hết hạn mức thì không dùng thẻ để bù |

## 4. Tham số
| Tham số | Vừa | Nặng | Nguồn |
|---|---|---|---|
| `:batch_share_vua` / `_nang` | 0.3 | 1.0 | Thông số vận hành: tỷ lệ lô lương xử lý trong khung giờ gián đoạn. Khi chưa có, giả định hai mức |
| `:size_small` / `:size_large` | 50 / 500 | như vừa | Giả định: ranh giới DN nhỏ, vừa, lớn theo số nhân viên nhận lương qua ngân hàng |
| `:ur_limit` | 0.9 | 0.9 | Giả định |
| `:min_group_size` | 20 | 20 | Giả định |

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP`: ngày đến hạn của từng khoản vay – không biết khoản nào đến hạn trong những ngày bị trễ, nên kết quả là cận trên (coi mọi khoản trả tháng là có nguy cơ).
- `GAP`: ngày và giờ của lô lương; doanh thu QR, Soundbox của hộ kinh doanh trong thời gian gián đoạn (`S02`); khiếu nại (`S14`); đăng nhập lạ sau sự cố (`S13`) – các tín hiệu playbook yêu cầu nhưng danh mục không có.
- Cần xác nhận: `cus_nonlending` là số dư cuối ngày mới nhất – có thể không phản ánh số dư đúng ngày sự cố.
- Không mô phỏng lừa đảo lợi dụng sự cố; phần đó theo `outside_in/news/nw_03_gian_lan_an_ninh.md` ở mức nhận diện.

## 6. SQL
```sql
-- K1. Phân bố quy mô DN trả lương (để chọn :size_small, :size_large)
SELECT percentile_approx(n_staff, array(0.5, 0.75, 0.9, 0.99)) AS staff_per_employer_quantiles,
       COUNT(*) AS n_employers
FROM (
  SELECT p.company_code, COUNT(DISTINCT p.customer_code) AS n_staff
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
  WHERE trunc(p.month_id, 'MM') = :as_of_month
  GROUP BY p.company_code
) x;
```

```sql
-- Tham số
-- :as_of_month      DATE    kỳ lương bị ảnh hưởng (ngày đầu tháng)            '2026-10-01'
-- :as_of_date       DATE    ngày chụp cus_lending                             '2026-10-31'
-- :batch_share_vua  DOUBLE  thông số vận hành hoặc giả định                   0.3
-- :batch_share_nang DOUBLE  thông số vận hành hoặc giả định                   1.0
-- :size_small       INT     giả định                                          50
-- :size_large       INT     giả định                                          500
-- :ur_limit         DOUBLE  giả định                                          0.9
-- :min_group_size   INT     giả định                                          20
WITH
pay AS (
  SELECT p.customer_code AS cus_key, p.company_code AS employer_key, SUM(p.month_income) AS salary
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
  WHERE trunc(p.month_id, 'MM') = :as_of_month
  GROUP BY p.customer_code, p.company_code
),
emp_size AS (
  SELECT employer_key, COUNT(DISTINCT cus_key) AS n_staff FROM pay GROUP BY employer_key
),
loans AS (
  SELECT l.customer_code AS cus_key, SUM(l.total_monthly_payment) AS pmt,
         SUM(CASE WHEN l.total_monthly_payment IS NULL THEN 1 ELSE 0 END) AS n_pmt_null
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
  WHERE l.ds_partition_date = :as_of_date
  GROUP BY l.customer_code
),
casa AS (
  SELECT n.customer_code AS cus_key, COALESCE(n.ca_eob_balance, 0) AS casa_bal
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_nonlending n
),
card AS (
  SELECT cc.cusid AS cus_key, cc.buncc_amt_ur_med_l1m AS card_ur
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
  WHERE cc.month = :as_of_month
),
base AS (
  SELECT CASE WHEN es.n_staff < :size_small THEN '1_dn_nho'
              WHEN es.n_staff < :size_large THEN '2_dn_vua'
              ELSE '3_dn_lon' END                                         AS employer_size,
         py.salary, lo.pmt, lo.n_pmt_null, COALESCE(cs.casa_bal, 0) AS casa_bal, cd.card_ur,
         CASE WHEN lo.pmt > 0 AND COALESCE(cs.casa_bal, 0) < lo.pmt THEN 1 ELSE 0 END AS no_buffer
  FROM pay py
  JOIN emp_size es ON es.employer_key = py.employer_key
  LEFT JOIN loans lo ON lo.cus_key = py.cus_key
  LEFT JOIN casa  cs ON cs.cus_key = py.cus_key
  LEFT JOIN card  cd ON cd.cus_key = py.cus_key
),
scen AS (
  SELECT * FROM VALUES ('1_vua', CAST(:batch_share_vua AS DOUBLE)), ('2_nang', CAST(:batch_share_nang AS DOUBLE))
  AS t(scenario, batch_share)
)
SELECT sn.scenario, b.employer_size,
       COUNT(*)                                                               AS n_payees,
       sn.batch_share * COUNT(*)                                              AS n_payees_delayed_expected,
       sn.batch_share * SUM(b.salary)                                         AS salary_delayed_expected,
       SUM(b.no_buffer)                                                       AS n_no_buffer,
       sn.batch_share * SUM(CASE WHEN b.no_buffer = 1 THEN b.pmt ELSE 0 END)  AS pmt_at_risk_expected,
       SUM(CASE WHEN b.no_buffer = 1 AND b.card_ur >= :ur_limit THEN 1 ELSE 0 END) AS n_no_buffer_card_full,
       SUM(CASE WHEN b.n_pmt_null > 0 THEN 1 ELSE 0 END)                      AS n_excluded_null_pmt
FROM base b
CROSS JOIN scen sn
GROUP BY sn.scenario, sn.batch_share, b.employer_size
HAVING COUNT(*) >= :min_group_size
ORDER BY sn.scenario, b.employer_size;
```

## 7. Cách đọc kết quả và hành động
- `n_payees_delayed_expected` và `salary_delayed_expected` là quy mô để ban điều hành thông báo và chuẩn bị tổng đài; `n_no_buffer` và `pmt_at_risk_expected` là phạm vi cần miễn phí phạt trả chậm cho kỳ này.
- `n_no_buffer_card_full` là nhóm không thể tự bù bằng thẻ – ưu tiên khôi phục lô lương có nhiều người thuộc nhóm này (thường là DN đông công nhân).
- Nếu nhóm `3_dn_lon` chiếm phần lớn người bị chạm, ưu tiên khôi phục kênh chi lương doanh nghiệp (`CIB-PAY-06`) trước.
- Hành động theo playbook: thông báo rõ và nhanh để giảm khoảng trống cho lừa đảo mạo danh; tự động miễn phí trả chậm cho khoản đến hạn trong thời gian sự cố; không ghi nhận quá hạn do lỗi của ngân hàng.

## 8. Dòng nhãn
```
[WI] cua=IO | rui_ro=CIB-PAY-06,SME-PAY-06,CN-DIG-01,NH-OR-01 | kich_ban=gian_doan_ky_chi_luong | quan_the=nguoi_nhan_luong_ky_bi_anh_huong | soc=batch_share=0.3/1.0 | cong_thuc=quy_mo_pho_nhiem,dem_casa | bang=cus_payroll,cus_lending,cus_nonlending | gap=ngay_den_han,gio_lo_luong,S02,S13,S14 | xac_nhan=1 | muc=co_kha_nang_cao
```
