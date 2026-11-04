---
id: OI-WI-EX-06
used_by: [What-if, Critic]
load_when: Tin GL (gian lận, lừa đảo) – what-if chỉ ở mức đo quy mô phơi nhiễm khi dữ liệu tín hiệu gian lận không có
version: v3.4
updated: 2026-11-04
nguon_test: TC-19
---

# Bài mẫu what-if 06 – Lừa đảo nhắm vào người trẻ: đo quy mô, không mô phỏng thiệt hại

## 1. Rủi ro gốc
Cụm TC-19 mở 01/11/2026 (`phan_khuc=KHCN × kieu=mao_danh_co_quan_nha_nuoc × kenh=kenh_so`, cửa sổ 7 ngày, mức "có thể"): ba tin cảnh báo trang giả mạo, giả mạo bằng AI, cuộc gọi giả danh nhắm học sinh, sinh viên. Sản phẩm `CN-ACC-01` `CN-DIG-01` mức P1; tín hiệu playbook `X01` `X02` `X03`. Độ tuổi khớp 2/3 tin nên **không** vào khóa cụm, chỉ là nhóm cần ưu tiên kiểm tra. Bài này minh họa what-if khi dữ liệu **không có tín hiệu gian lận**: chỉ đo được quy mô nhóm cần cảnh báo chủ động và số dư có thể bị chạm, không mô phỏng thiệt hại.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Khách cá nhân, chia theo nhóm tuổi `:age_young_max` (nhóm ưu tiên) và phần còn lại; theo tỉnh nếu cần triển khai cảnh báo theo vùng |
| Cú sốc | Không áp sốc lên số dư (quy tắc `wc_03` mục 4: phơi nhiễm gian lận chỉ đếm). Mức "kịch bản" là **phạm vi cảnh báo**: hẹp (nhóm trẻ, có số dư ≥ `:bal_min`) và rộng (toàn bộ nhóm trẻ) |
| Công thức | Đếm khách, tổng và trung vị số dư CASA; tỷ lệ khách có lương vào tài khoản (người mới đi làm), có thẻ tín dụng |
| Biến kết quả | Số khách cần cảnh báo, số dư trong phạm vi, cơ cấu theo persona |

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò |
|---|---|---|---|
| Tuổi, tỉnh | `cus_info.age`, `c_addr_province` | F | Nhóm |
| Persona | `cus_persona.classfication_value` | F | Cơ cấu (một khách nhiều dòng) |
| Số dư | `cus_nonlending.ca_eob_balance`; `trio_a_hashed_rbg_atxca_balance.atxca_bal_avg_l1m` | F | Quy mô |
| Lương vào | `trio_a_hashed_rbg_atxca_service_channel.atxca_amt_sal_sum_l1m` | F | Người mới đi làm |
| Thẻ | `trio_a_hashed_rbg_buncc_payment.buncc_amt_card_limit_max_l1m` | F | Có thẻ tín dụng |

## 4. Tham số
| Tham số | Hẹp | Rộng | Nguồn |
|---|---|---|---|
| `:age_young_min` / `:age_young_max` | 18 / 25 | 18 / 25 | Giả định: tin 01/11/2026 nói "học sinh, sinh viên"; dưới 18 tuổi cần quy trình riêng nên không đưa vào |
| `:bal_min` | 0 cho rộng; người dùng đặt cho hẹp | – | Giả định: ưu tiên khách có số dư đáng kể |
| `:min_group_size` | 20 | 20 | Giả định |

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP`: `X01` (tài khoản mới nhận nhiều nguồn rồi chuyển đi), `X02` (báo lừa đảo, tra soát), `X03` (thiết bị, đăng nhập lạ), `S13` – không có cột. Đây là phần quan trọng nhất của rủi ro gian lận; đề xuất bổ sung: ngày mở tài khoản, số nguồn tiền vào khác nhau theo ngày, số lần đổi thiết bị, số yêu cầu tra soát.
- Không có dữ liệu → **không** kết luận khách của ngân hàng đã bị lừa (TC-19 "Không được"); kết quả chỉ là quy mô nhóm cần cảnh báo.
- Cần xác nhận: nối `cus_*` – `trio_*` qua `cus_key`; persona nhiều dòng mỗi khách → đếm theo persona sẽ trùng khách.
- An toàn: kịch bản không mô tả thủ đoạn; nội dung cảnh báo theo `outside_in/news/nw_03_gian_lan_an_ninh.md` (mức nhận diện).

## 6. SQL
```sql
-- K1. Phân bố tuổi (kiểm tra độ phủ cột age) và persona trong nhóm trẻ
SELECT CASE WHEN i.age IS NULL THEN 'null'
            WHEN i.age BETWEEN :age_young_min AND :age_young_max THEN 'tre'
            ELSE 'khac' END AS age_group,
       ps.classfication_value,
       COUNT(DISTINCT i.customer_code) AS n_customers
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_persona ps
  ON ps.customer_code = i.customer_code
GROUP BY 1, ps.classfication_value
ORDER BY age_group, n_customers DESC;
```

```sql
-- Tham số
-- :as_of_month    DATE    kỳ quan sát                                         '2026-10-01'
-- :age_young_min  INT     giả định                                            18
-- :age_young_max  INT     giả định: "học sinh, sinh viên" (tin 01/11/2026)     25
-- :bal_min        DOUBLE  giả định: ngưỡng số dư cho phạm vi hẹp               người dùng đặt
-- :min_group_size INT     giả định                                            20
WITH
pop AS (
  SELECT i.customer_code AS cus_key, i.c_addr_province AS province,
         CASE WHEN i.age BETWEEN :age_young_min AND :age_young_max THEN 'tre' ELSE 'khac' END AS age_group
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
  WHERE i.age IS NOT NULL
),
bal AS (
  SELECT n.customer_code AS cus_key, n.ca_eob_balance AS ca_eod
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_nonlending n
),
beh AS (
  SELECT ca.cusid AS cus_key,
         ca.atxca_bal_avg_l1m AS ca_avg_l1m,
         CASE WHEN sc.atxca_amt_sal_sum_l1m > 0 THEN 1 ELSE 0 END          AS has_salary,
         CASE WHEN cc.buncc_amt_card_limit_max_l1m > 0 THEN 1 ELSE 0 END   AS has_card
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_atxca_balance ca
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_atxca_service_channel sc
    ON sc.cusid = ca.cusid AND sc.month = ca.month
  LEFT JOIN tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.trio_a_hashed_rbg_buncc_payment cc
    ON cc.cusid = ca.cusid AND cc.month = ca.month
  WHERE ca.month = :as_of_month
),
base AS (
  SELECT p.province, p.age_group, COALESCE(b.ca_eod, 0) AS ca_eod, e.ca_avg_l1m,
         COALESCE(e.has_salary, 0) AS has_salary, COALESCE(e.has_card, 0) AS has_card
  FROM pop p
  LEFT JOIN bal b ON b.cus_key = p.cus_key
  LEFT JOIN beh e ON e.cus_key = p.cus_key
),
scope AS (
  SELECT * FROM VALUES ('1_rong', 0.0D), ('2_hep', CAST(:bal_min AS DOUBLE)) AS t(scope_name, bal_floor)
)
SELECT s.scope_name, b.age_group, b.province,
       COUNT(*)                                       AS n_customers,
       SUM(b.ca_eod)                                  AS ca_total,
       percentile_approx(b.ca_eod, 0.5)               AS ca_median,
       percentile_approx(b.ca_avg_l1m, 0.5)           AS ca_avg_l1m_median,
       AVG(b.has_salary)                              AS share_with_salary,
       AVG(b.has_card)                                AS share_with_card
FROM base b
JOIN scope s ON b.ca_eod >= s.bal_floor
GROUP BY s.scope_name, b.age_group, b.province
HAVING COUNT(*) >= :min_group_size
ORDER BY s.scope_name, b.age_group, b.province;
```

## 7. Cách đọc kết quả và hành động
- `n_customers` của nhóm `tre` theo phạm vi là cỡ chiến dịch cảnh báo chủ động (thông báo trong ứng dụng, tin nhắn); `share_with_salary` cao → nhóm người mới đi làm, nên nội dung cảnh báo nhắm cả lừa đảo việc làm.
- So `ca_median` nhóm `tre` với `khac` để chọn kênh và mức ưu tiên; không suy ra thiệt hại.
- Hành động theo bảng (c) `CN-ACC-01` `CN-DIG-01`: cảnh báo chủ động cho khách trẻ; yêu cầu bộ phận chống gian lận chạy truy vấn nội bộ `X01`–`X03` (ngoài danh mục này). Ghi rõ "chưa có số liệu nội bộ, cần truy vấn".

## 8. Dòng nhãn
```
[WI] cua=OI | rui_ro=CN-ACC-01,CN-DIG-01 | kich_ban=pham_vi_canh_bao_nguoi_tre | quan_the=ca_nhan_18_25_theo_tinh | soc=none(chi_do_quy_mo);pham_vi=rong/hep | cong_thuc=phoi_nhiem_gian_lan | bang=cus_info,cus_nonlending,trio_rbg | gap=X01,X02,X03,S13 | xac_nhan=2 | muc=co_the
```
