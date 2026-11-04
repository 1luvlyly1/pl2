---
id: OI-WI-EX-00
used_by: [What-if]
load_when: Chọn 1 bài mẫu gần nhất trước khi dựng kịch bản what-if cho rủi ro từ tin bên ngoài
version: v3.4
updated: 2026-11-04
---

# Bài mẫu what-if outside-in – danh sách và cách chọn

Rủi ro bắt nguồn từ tin bên ngoài, đi qua playbook rồi mới tới what-if. Bài mẫu cho rủi ro từ bên trong ngân hàng ở `inside_out/whatif/examples/`.

Mỗi bài theo đúng khuôn `core/whatif_chung/wc_05_dau_ra.md` (8 phần), SQL đã qua `validate_whatif_sql.py` (0 lỗi) và chạy thử trên Spark với bảng rỗng dựng từ danh mục. Không bài nào chứa số liệu kết quả – chỉ có tham số, nguồn của tham số và cách đọc.

| Bài | Rủi ro (test case) | Mẫu công thức | Điểm cần học |
|---|---|---|---|
| `oi_wi_ex_01_kcn_cat_giam_lao_dong.md` | DN cắt lao động → nhân viên (TC-13) | Tháng đệm, dư nợ chịu rủi ro kỳ vọng | Dùng `cus_payroll.company_code` nối DN với nhân viên (`L02`); tỷ lệ mất việc nhân với tổng, không chọn ngẫu nhiên khách |
| `oi_wi_ex_02_vay_mua_nha_tha_noi.md` | Lãi thả nổi, giá TSBĐ giảm (TC-20, TC-02) | DSR, LTV, căng kép | Suy tham số từ con số trong tin bằng công thức nêu rõ; thu nhập dự phòng từ lương vào CASA; báo nguồn thu nhập |
| `oi_wi_ex_03_nong_ho_tay_nguyen.md` | Cụm vùng × nhóm người, 3 nguyên nhân (TC-16) | Tháng đệm cộng dồn `Π(1−draw_k)`, điểm căng | Xử lý khi thiếu biến thu nhập; mỗi nguyên nhân cụm là một tham số; đo phần cộng dồn |
| `oi_wi_ex_04_dn_go_xuat_khau.md` | Cụm ngành DN, thuế + cước (TC-15) | Dòng tiền ròng, độ phủ lương | Bảng `trio_corp_*`; cột thay thế cho "xuất khẩu"; lan sang nhân viên trong cùng truy vấn |
| `oi_wi_ex_05_tin_don_rut_tien.md` | Tin đồn, rút tiền hai tỉnh (TC-04) | Dòng ra tiền gửi theo hạng | Nhóm đối chứng; dấu hiệu sớm `F01` `F02` `S06`; ghi rõ không có bộ đệm thanh khoản |
| `oi_wi_ex_06_lua_dao_nguoi_tre.md` | Tin `GL` nhắm người trẻ (TC-19) | Phơi nhiễm (chỉ đếm) | Không mô phỏng thiệt hại; `X01`–`X03` là GAP; không kết luận khách đã bị lừa |

## Chọn bài
| Rủi ro mới | Bài |
|---|---|
| Thu nhập người lao động theo DN, KCN, ngành | 01 |
| Lãi suất, khoản trả nợ, giá BĐS, TSBĐ của KHCN | 02 |
| Cụm theo vùng, nông hộ, nhóm thiếu biến thu nhập | 03 |
| DN theo ngành: thuế quan, giá đầu vào, cước, tỷ giá | 04 |
| Thanh khoản, tin đồn, cạnh tranh huy động | 05 |
| Gian lận, lừa đảo, an ninh mạng | 06 |
