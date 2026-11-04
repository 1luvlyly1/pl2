---
id: WC-02-SIGNAL-MAP
used_by: [What-if]
steps: [whatif-2]
depends_on: [core/whatif_chung/wc_00_quy_tac.md, core/whatif_chung/wc_01a_catalog_khcn.md, core/whatif_chung/wc_01b_catalog_dn.md]
load_when: Luôn nạp ở bước ánh xạ dữ liệu
version: v3.4
updated: 2026-11-04
---

# Ánh xạ tín hiệu và sản phẩm → cột dữ liệu

Viết tắt bảng (tên đầy đủ ở `wc_01a`, `wc_01b`): `info` `persona` `payroll` `lending` `coll` `nonlend` = `cus_*` · `ch` `chm` = `trio_a_hashed_b_credit_history`, `_monthly` · `od` = `bunod_ur` · `aum` `asv` `ca` `svc` `cc` `cpb` = `trio_a_hashed_rbg_a_aum`, `_asv_balance`, `_atxca_balance`, `_atxca_service_channel`, `_buncc_payment`, `_cpb` · `cb` `cfx` `ctx` `ews` = `trio_a_hashed_corp_b`, `_corp_atxca_balance`, `_corp_atxca_txn`, `_corp_atxca_txn_ews`.

Mức khớp: **Trực tiếp** – cột đo đúng tín hiệu · **Thay thế** – đo gần đúng, phải nói vì sao · **GAP** – không có cột, khai báo thiếu dữ liệu.

## 1. Tín hiệu nội bộ `S01`–`S16`
| Mã | Tín hiệu | Mức | Cột | Cách đọc, giới hạn |
|---|---|---|---|---|
| `S01` | Lương trễ, giảm quỹ, giảm người | Trực tiếp | `payroll.month_income`, `payroll.company_code`, `payroll.month_id`; `ews.atxca_txn_amt_payroll_avg_l3m` / `_l6m`; `ctx.atxca_rto_txn_amt_payroll_vs_txn_num_payroll_avg_l3m`; `svc.atxca_amt_sal_sum_l1m` | Đếm nhân viên và tổng lương theo `company_code` qua các `month_id`; phía DN so lương bình quân 3 tháng với 6 tháng. Không đo được "trễ ngày" |
| `S02` | Doanh thu QR, POS giảm theo địa bàn | GAP (HKD) · Thay thế (DN) | DN: `ews.atxca_txn_amt_in_avg_l3m` vs `_l12m`, `ctx.atxca_txn_amt_in_avg_l3v12m` | Dòng vào tài khoản DN, không tách được QR/POS. HKD không có cột doanh thu |
| `S03` | Số người trả tiền giảm | GAP | – | Đề xuất bổ sung: số người trả duy nhất theo tháng |
| `S04` | Sử dụng hạn mức tăng nhanh | Trực tiếp | `cc.buncc_amt_ur_med_l1m` vs `_l3m` `_l6m`, `cc.buncc_num_day_ur_gt90pc_cnt_l3m`; `od.bunod_amt_ur_med_l1m` vs `_l6m`, `od.bunod_pct_day_ur_gt90pc_cnt_l1m`; DN: `cb.b_monthend_od_ur_max_l1m` vs `_avg_l3m` | Tăng = l1m cao hơn l3m/l6m vượt `:ur_jump` |
| `S05` | Chuyển sang trả tối thiểu thẻ | Trực tiếp | `cc.buncc_num_min_paid_cnt_l3m` vs `_l6m`, `cc.buncc_amt_paid_vs_min_paid_med_l3m` vs `_l6m` | Tỷ lệ trả/tối thiểu tiến về 1 là tín hiệu xấu |
| `S06` | Tất toán tiết kiệm trước hạn | Trực tiếp (phần tất toán) · GAP (vay cầm cố tiền gửi) | `asv.asvtd_bal_close_early_avg_l1m` vs `_l3m`, `asv.asvtd_num_acc_close_early_avg_l1m` vs `_l3m` | Vay cầm cố tiền gửi: tra `lending.product_name` bằng truy vấn khám phá; không có thì GAP |
| `S07` | Rút tiền mặt CDM tăng | GAP | Thay thế yếu: `aum.a_amt_aum_slope_l1m`, `ca.atxca_bal_avg_l1m` vs `_l3m` | Chỉ thấy tiền rời ngân hàng, không biết rút mặt hay chuyển khoản |
| `S08` | Bán lại iBond, rút iFund | Thay thế | `nonlend.bond_total_sell_value`, `nonlend.fund_total_sell_value`, `_eob_balance` (cờ `?`) | Không có chiều tổ chức phát hành, ngành; không có mốc thời gian để so kỳ |
| `S09` | Hủy bảo hiểm sớm | Thay thế | `nonlend.banca_ape`, `nonlend.banca_eob_balance`, `nonlend.banca_maintenance_time` | Chỉ có mức hiện tại, không có cờ hủy |
| `S10` | Nộp NSNN trễ, hóa đơn điện, cảng giảm | GAP (DN) | KHCN có `svc.atxca_amt_out_electricity_sum_l1m` (chi điện hộ gia đình, không phải DN) | |
| `S11` | Spoke SCF cùng anchor chậm trả | GAP | – | Không có quan hệ anchor–spoke |
| `S12` | Chủ DN rút tiết kiệm, DN tăng hạn mức | GAP (liên kết chủ–DN) | Hai vế riêng: `asv.*close_early*` và `cb.b_monthend_od_ur_*` | `payroll.company_code` là quan hệ người làm công, không phải chủ sở hữu |
| `S13` | Đăng nhập lạ, thiết bị mới | GAP | – | |
| `S14` | Khiếu nại tăng theo chủ đề | GAP | – | |
| `S15` | MTM âm trên vị thế FX | GAP | Bối cảnh: `cfx.atxca_bal_fcy_avg_l1m`, `ctx.atxca_rto_txn_num_fcy_vs_txn_num_avg_l3m` | Chỉ cho biết DN có dùng ngoại tệ |
| `S16` | Doanh thu HKD về TK cá nhân | GAP | – | |

## 2. Hành vi sợ, tham và tín hiệu gian lận
| Mã | Mức | Cột | Ghi chú |
|---|---|---|---|
| `F01` chuyển tiền gửi đi | Thay thế | `aum.a_amt_aum_slope_l1m` `_l3m`, `aum.a_amt_aum_avg_l1m` vs `_l3m`, `ca.atxca_bal_avg_l1m` vs `_l3m` | Không biết ngân hàng nhận |
| `F02` kỳ hạn dài → ngắn, không kỳ hạn | Thay thế | `asv.asvtd_bal_avg_l1m` giảm cùng `ca.atxca_bal_avg_l1m` tăng | Không có kỳ hạn từng sổ |
| `F03` bán TSBĐ trả nợ trước hạn | Thay thế | `coll.coll_id` biến mất giữa hai `ds_partition_date` cùng `lending.total_outstanding` giảm | Không có giá bán |
| `F04` còn hạn mức nhưng ngừng giải ngân | Trực tiếp (DN) | `cb.b_monthend_od_ur_max_l1m` vs `_avg_l3m`; `lending.granted_limit` vs `lending.total_outstanding` | |
| `G03` dồn vào một sản phẩm đầu tư | Thay thế | `nonlend.fund_eob_balance`, `nonlend.bond_eob_balance` / `aum.a_amt_aum_avg_l1m` | Không có chiều tổ chức phát hành |
| `G04` vay mua BĐS thứ hai, thứ ba | Trực tiếp | Đếm khoản `lending` có `secured_type` bảo đảm theo khách; `coll.tsdb_mt`; `ch.b_flag_mortgage_l1m` | Giá trị `secured_type`, `tsdb_mt` tra khám phá. Mô tả gốc của `b_flag_mortgage_l1m` ghi "auto mortgage" – xác nhận nghĩa |
| `G05` xin tăng hạn mức theo doanh thu đỉnh | Thay thế | `lending.granted_limit` / `ews.atxca_txn_amt_in_avg_l12m` | |
| `G01` `G02` `G06` `G07` | GAP | – | Không có đích chuyển tiền, vị thế phái sinh |
| `X01`–`X08` | GAP | Chỉ đo được quy mô phơi nhiễm: số khách, số dư `nonlend.ca_eob_balance`, `ca.atxca_bal_avg_l1m` theo nhóm | What-if gian lận chỉ dừng ở "quy mô có thể bị chạm" |

## 3. Biến kết quả (đo hậu quả của kịch bản)
| Ý nghĩa | KHCN | DN |
|---|---|---|
| Quá hạn hiện tại | `ch.b_num_dpd_max_l1m`, `ch.b_bal_dpd_max_l1m` | `cb.b_max_monthly_dpd_max_l1m` |
| Lịch sử quá hạn | `chm.b_num_mth_gt0_dpd_cnt_l6m`, `chm.b_num_mth_gt30_dpd_cnt_l12m` | `cb.b_flag_dpd_gt0_sum_l6m`, `cb.b_max_monthly_dpd_max_l12m` |
| Nhóm nợ TCB và CIC | `ch.b_ln_class_tcb_cic_max_l1m` | – |
| Dư nợ | `lending.total_outstanding` (cộng theo khách) | `cb.b_monthend_on_os_max_l1m` |
| Nghĩa vụ trả hằng tháng | `lending.total_monthly_payment` (kiểm null) | GAP – thay thế bằng dòng ra `ctx.atxca_rto_txn_amt_out_vs_txn_amt_avg_l3m` |
| Thu nhập | `payroll.month_income`; dự phòng `svc.atxca_amt_sal_sum_l1m` | Dòng vào `ews.atxca_txn_amt_in_avg_l3m` |
| Đệm thanh khoản | `nonlend.ca_eob_balance`, `nonlend.td_az_eob_balance`, `nonlend.td_mm_eob_balance` (cờ `?`), `aum.a_amt_aum_min_l6m` | `cfx.atxca_bal_fcy_avg_l1m` (chỉ ngoại tệ); số dư VND DN – GAP |
| Tài sản bảo đảm | `coll.nominal_value` (cờ `A`), `coll.tsdb_mt` | `cb.b_monthend_coll_value_min_l1m` |

## 4. Nhóm sản phẩm playbook → bảng
| Mã sản phẩm | Bảng chính | Lọc |
|---|---|---|
| `CN-LN-01` `CN-LN-02` vay mua nhà, thế chấp | `lending`, `coll`, `ch`, `chm` | `lending.product_name` / `secured_type` theo khám phá |
| `CN-LN-05` `CN-LN-06` tín chấp, thấu chi | `lending`, `od`, `ch.b_flag_uns_only_l1m`, `ch.bun_num_ctr_cnt_l3m` | |
| `CN-CARD-*` | `cc` | |
| `CN-ACC-*` `CN-DEP-*` `CN-PAY-*` | `nonlend`, `ca`, `asv`, `aum`, `svc` | |
| `CN-INV-*` | `nonlend.fund_*`, `nonlend.bond_*` (cờ `?`) | |
| `CN-INS-*` | `nonlend.banca_*` | |
| `HKD-*` | Không có cờ HKD riêng; thử `info.customer_segment`, `persona.classfication_value` qua khám phá | Không tìm được giá trị HKD → GAP cho cả nhóm |
| `SME-LN-*` `CIB-LN-*` | `cb` | Phân biệt SME/CIB bằng `info.sector`, `info.customer_segment` (khám phá) |
| `SME-ACC-*` `CIB-ACC-*` `CIB-PAY-*` | `ctx`, `ews`, `cfx` | |
| `CIB-PAY-06` `SME-PAY-*` chi lương | `payroll` theo `company_code`, `ews.atxca_txn_amt_payroll_*` | |
| `CIB-TF-*` `CIB-FX-*` | `cfx`, `ctx.atxca_rto_txn_num_fcy_vs_txn_num_avg_*` | Không có hạn mức L/C, bảo lãnh → GAP |
| `NH-LQ-*` | Cộng `nonlend` / `aum` theo nhóm | Không có bộ đệm thanh khoản, LCR → GAP; chỉ tính được dòng ra giả định |
