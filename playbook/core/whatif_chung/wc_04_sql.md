---
id: WC-04-SQL
used_by: [What-if]
steps: [whatif-4, whatif-5]
depends_on: [core/whatif_chung/wc_00_quy_tac.md, core/whatif_chung/wc_01a_catalog_khcn.md]
load_when: Luôn nạp khi viết SQL
version: v3.4
updated: 2026-11-04
---

# Quy ước SQL cho what-if

Phương ngữ: **Databricks SQL (Spark SQL)**, tham số đặt tên dạng `:ten`. SQL chỉ đọc.

## 1. Tên bảng và bí danh
- Luôn viết tên đầy đủ: `tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.<bảng>`.
- Mỗi bảng gốc có bí danh ngắn; **mọi cột lấy từ bảng gốc viết `bí_danh.cột`** – script kiểm tra dựa vào quy ước này để đối chiếu danh mục. Cột dẫn xuất trong CTE đặt tên tự do (tiếng Anh, snake_case).
- Bí danh khuyến nghị: `i` info · `ps` persona · `p` payroll · `l` lending · `cl` coll · `n` nonlend · `ch` `chm` · `od` · `au` aum · `sv` asv · `ca` · `sc` svc · `cc` · `cb` · `cf` cfx · `ct` ctx · `ew` ews · `sn` bảng mức độ kịch bản. **Một bí danh chỉ trỏ một bảng trong cả câu** (kể cả CTE khác) – script kiểm tra báo lỗi nếu trùng.

## 2. Khóa khách hàng
Danh mục ghi: `customer_code` (bảng `cus_*`) và `cusid` (bảng `trio_*`) đều được thay bằng `cus_key` ở Phase 2. Quy ước:
```sql
-- Đổi tên về cus_key ngay khi đọc bảng gốc
cus AS (SELECT i.customer_code AS cus_key, ... FROM <...>.cus_info i),
trio_cc AS (SELECT cc.cusid AS cus_key, ... FROM <...>.trio_a_hashed_rbg_buncc_payment cc WHERE cc.month = :as_of_month)
```
- Giả định: sau Phase 2 hai khóa trùng giá trị. Ghi giả định này trong mục "Cần xác nhận" của mọi kịch bản nối chéo hai hệ.
- `cus_payroll.company_code` là mã khách hàng của DN → nối với `cus_key` của DN (cùng giả định).
- Không tự tạo bảng ánh xạ khóa.

## 3. Kỳ dữ liệu
| Bảng | Lọc kỳ |
|---|---|
| `trio_*` | `x.month = :as_of_month` (ngày đầu tháng). Các bảng `trio_*` nối với nhau trên (`cus_key`, `month`) |
| `cus_lending`, `cus_coll_transformed` | `x.ds_partition_date = :as_of_date` (ngày chụp, thường cuối tháng của `:as_of_month`) |
| `cus_payroll` | `trunc(p.month_id, 'MM')` trong khoảng `add_months(:as_of_month, -k)` … `:as_of_month` |
| `cus_info`, `cus_persona`, `cus_nonlending` | Không lọc kỳ (danh mục không có cột kỳ) |

Tham số kỳ luôn khai báo ở đầu file, cùng giá trị mẫu dạng chữ (`'2026-10-01'`), không phải số liệu.

## 4. Tham số
- Khai báo trong khối chú thích đầu SQL, mỗi dòng: `-- :ten  kiểu  nguồn (tin dd/mm/yyyy | giả định: lý do)  giá trị đề xuất`.
- Danh sách mã truyền dạng chuỗi phân cách dấu phẩy, lọc bằng `find_in_set(CAST(cot AS STRING), :list) > 0`.
- Ngưỡng ẩn nhóm nhỏ: `:min_group_size` (giả định đề xuất 20).
- Không viết số giả định trực tiếp trong biểu thức; hằng số được phép: 0, 1, 100 (đổi %), 12 (tháng/năm).

## 5. Truy vấn khám phá (chạy trước, trả danh sách giá trị và số khách)
```sql
-- K1. Giá trị tỉnh
SELECT i.c_addr_province, COUNT(*) AS n_customers
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
GROUP BY i.c_addr_province ORDER BY n_customers DESC;

-- K2. Ngành DN theo từ khóa (từ khóa là tham số, agent đề xuất)
SELECT i.gso_code, i.gso_description, i.industry_group, COUNT(*) AS n_customers
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_info i
WHERE lower(i.gso_description) LIKE concat('%', lower(:gso_keyword), '%')
GROUP BY i.gso_code, i.gso_description, i.industry_group ORDER BY n_customers DESC;

-- K3. Sản phẩm vay
SELECT l.product_name, l.secured_type, COUNT(DISTINCT l.customer_code) AS n_customers
FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
WHERE l.ds_partition_date = :as_of_date
GROUP BY l.product_name, l.secured_type ORDER BY n_customers DESC;
```
Tương tự cho `tsdb_mt`, `coll_source`, `customer_segment`, `sector`, `priority_class`, `classfication_value`. Kèm truy vấn **độ phủ**: tỷ lệ null của cột sẽ dùng (`total_monthly_payment`, `month_income`, `nominal_value`).

## 6. CTE chuẩn
```sql
-- Dư nợ, khoản trả theo khách (cus_lending nhiều dòng mỗi khách)
loans AS (
  SELECT l.customer_code AS cus_key,
         SUM(l.total_outstanding)      AS os,
         SUM(l.granted_limit)          AS limit_amt,
         SUM(l.total_monthly_payment)  AS pmt,
         COUNT(*)                      AS n_loans,
         SUM(CASE WHEN l.total_monthly_payment IS NULL THEN 1 ELSE 0 END) AS n_pmt_null
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_lending l
  WHERE l.ds_partition_date = :as_of_date
    AND find_in_set(l.product_name, :product_list) > 0
  GROUP BY l.customer_code
),
-- Thu nhập: lương qua ngân hàng; dự phòng bằng lương vào CASA
income AS (
  SELECT p.customer_code AS cus_key, AVG(p.month_income) AS income
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_payroll p
  WHERE trunc(p.month_id, 'MM') BETWEEN add_months(:as_of_month, -2) AND :as_of_month
  GROUP BY p.customer_code
),
-- TSBĐ theo khách
coll AS (
  SELECT cl.customer_code AS cus_key, SUM(cl.nominal_value) AS coll_value
  FROM tcb_data_pt_apse_1_user_workbench_hackathon.ai_champion_trio.cus_coll_transformed cl
  WHERE cl.ds_partition_date = :as_of_date
  GROUP BY cl.customer_code
)
```

## 7. Câu cuối
- Mỗi mức độ là một dòng (dùng `CROSS JOIN` với bảng giá trị tham số `VALUES ('co_so', 0), ('vua', :x_vua), ('nang', :x_nang)`), hoặc cột riêng cho từng mức.
- Cột bắt buộc: nhóm (tỉnh, phân khúc, sản phẩm…), `n_customers`, chỉ số trước sốc, chỉ số sau sốc, chênh lệch, `n_excluded_null`.
- `HAVING COUNT(*) >= :min_group_size`. Không trả khóa khách hàng.

## 8. Kiểm tra tự động (người dùng hoặc pipeline chạy, agent không chạy)
| Script (`index_spec/`) | Kiểm | Lệnh |
|---|---|---|
| `validate_whatif_sql.py` | Bảng, cột có trong danh mục; cột bị chặn; cờ cần xác nhận; chỉ đọc; không trả khóa; lọc `month`; `HAVING :min_group_size` | `python3 validate_whatif_sql.py --catalog playbook/core/whatif_chung/feature_catalog.csv FILE.md` |
| `spark_check_whatif_sql.py` | Cú pháp và phân giải cột trên Spark cục bộ (bảng rỗng theo danh mục); `--smoke` chèn 1 dòng giả để chạy cả phần tính | `python3 spark_check_whatif_sql.py --smoke --catalog playbook/core/whatif_chung/feature_catalog.csv FILE.md` |

Đoạn CTE minh họa (không bắt đầu bằng `SELECT`/`WITH`) được bỏ qua khi chạy Spark.

## 9. Lỗi thường gặp
| Lỗi | Sửa |
|---|---|
| Nối `cus_lending` dòng-khoản-vay với bảng một-dòng-mỗi-khách → nhân đôi | Gộp theo khách trước |
| `AVG` của tỷ lệ thay cho tỷ lệ của tổng | Báo cả hai: trung vị theo khách (`percentile_approx`) và `SUM(P)/SUM(I)` |
| Lọc `trio_*` thiếu `month` → trộn nhiều tháng | Luôn lọc `month` |
| Thay null bằng 0 trong mẫu số | `NULLIF`, loại và đếm khách bị loại |
| So `l1m` với `l3m` như hai kỳ rời | `l3m` gồm cả `l1m`; ghi rõ khi diễn giải |
