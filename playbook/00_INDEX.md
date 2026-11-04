---
id: INDEX
used_by: [Orchestrator, ALL]
steps: [0]
depends_on: []
load_when: Luôn nạp đầu tiên – file định tuyến, cho biết cần đọc file nào tiếp theo
version: v3.4
updated: 2026-11-04
---

# PLAYBOOK SUY LUẬN RỦI RO & CƠ HỘI (FEAR & GREED) – TECHCOMBANK (INDEX)

Bộ playbook gồm các module nhỏ. **Agent không đọc toàn bộ thư mục.** Mỗi agent chỉ nạp `00_INDEX.md` + gói ngữ cảnh của mình (mục 3), rồi nạp thêm file theo bộ định tuyến (mục 4).

**Phạm vi:** 3 phân khúc khách hàng – **KHCN** (gồm nhóm cá nhân và nhóm hộ kinh doanh), **SME**, **doanh nghiệp lớn** (mã `CIB`) – cộng với **cấp ngân hàng** cho các tác động chạm thẳng vào hoạt động của chính ngân hàng. Danh mục sản phẩm chốt 26/10/2026 từ techcombank.com.

**Mới ở v3.4:**
- Sắp xếp lại thư mục: cấp ngân hàng chuyển vào `core/06_ngan_hang.md`; tin outside-in chuyển vào `outside_in/news/`; what-if tách thành phần dùng chung `core/whatif_chung/`, phần outside-in `outside_in/whatif/` và phần inside-out `inside_out/whatif/`, mỗi phần có thư mục bài mẫu riêng.
- What-if inside-out mới: dự phóng bằng tỷ lệ chuyển trạng thái lịch sử, đo hai mặt của quyết định ngân hàng, sự cố vận hành, cảnh báo sớm DN; 4 bài mẫu có SQL.
- Viết lại `guardrails.md` (21 ràng buộc, mỗi ràng buộc có quy tắc, lý do, cách áp dụng), `core/01`–`06` và 19 file `industry/` thành câu mô tả cơ chế thay cho từ khóa; file ngành có thêm cột "Đo được bằng danh mục what-if" ở mục 5.

**Mới ở v3.3:** module what-if cho agent What-if (Opus): biến rủi ro thành kịch bản có số đo và SQL Databricks; biến số chỉ lấy từ danh mục feature của ngân hàng; thiếu dữ liệu thì khai báo `GAP`; dòng nhãn `[WI]`.

**Mới ở v3.2:** bảng (c) của 4 file phân khúc có keyword theo mức ưu tiên **P1**–**P3** (giải thích ở đầu mục (c)) và cột "Hành vi khuyến nghị khi xảy ra" (việc con người làm, dữ liệu what-if, stress test); bỏ mục (d) tín hiệu sớm nội bộ; mục (e) thành bảng hướng lan có kênh, độ trễ, tín hiệu kiểm chứng, chiều cơ hội.

**Mới ở v3.1:** thêm module ngành `industry/` – 1 file định tuyến (biến số bên ngoài → ngành) và 18 file ngành Việt Nam độc lập (`I01`–`I18`), mỗi file mô tả tác động lên KHCN cá nhân, hộ kinh doanh, SME, DN lớn theo chiều thách thức và cơ hội.

**Mới ở v3.0:**
- Gộp hộ kinh doanh vào KHCN; bỏ phân khúc nhà đầu tư, chuyển sang `core/06_ngan_hang.md`.
- Thêm module tin outside-in (nay ở `outside_in/news/`): tin tác động trực tiếp (`TT`), gián tiếp (`GT`), và gian lận, lừa đảo, an ninh mạng (`GL`), mỗi nhóm một cách suy luận.
- Dòng nhãn `[FG]` thêm trường `loai_tin`; phân khúc trong nhãn là `KHCN`, `SME`, `CIB`, `NH`.

## 1. Quy tắc chung
1. **Đầu vào là sự kiện đã được người dùng sàng lọc.** Agent không lọc, không tự tìm thêm tin. Việc xếp nhóm tin chỉ để chọn cách suy luận.
2. Mỗi sự kiện đi qua quy trình 6 bước (`core/04_reasoning_procedure.md`). Không nhảy thẳng tới sản phẩm.
3. **Khách hàng trước, sản phẩm sau:** chỉ tra sản phẩm sau khi đã biết ai bị chạm hoặc hưởng lợi, và qua kênh nào.
4. **Hai lăng kính:** luôn hỏi cả "ai thiệt" và "ai lợi". Mỗi cơ hội có mặt trái; không ép ra cơ hội khi không có (thường gặp với tin `GL`).
5. Kết quả là **một bài văn xuôi** theo `core/05_output_prose.md`, kết thúc bằng 1–3 dòng nhãn `[FG]`. Không JSON, agent không tự chấm điểm.
6. Mỗi nhận định nói rõ: lan qua kênh nào, sau bao lâu, mức chắc chắn, tín hiệu nội bộ nào để kiểm chứng.
7. Không bịa số liệu. Thiếu dữ liệu thì viết rõ là chưa có.

## 2. Cấu trúc thư mục
| Thư mục, file | Nội dung |
|---|---|
| `00_INDEX.md` | File này – định tuyến |
| `guardrails.md` | 21 ràng buộc bắt buộc, mỗi ràng buộc có quy tắc, lý do và cách áp dụng |
| **`core/`** – nền tảng dùng chung | |
| `core/01_risk_codes.md` | Mã loại rủi ro `CR` `CL` `LQ` `MR` `OR` `FR` `CO` `RP` `BR` `INS`: định nghĩa, khi nào xuất hiện, dễ nhầm với gì |
| `core/02_concepts_patterns.md` | Outside-in và inside-out, ba mẫu lan truyền `P1`–`P3`, hộ kinh doanh là nút lai, cấp ngân hàng, vòng phản hồi, một tin và nhiều tin |
| `core/03_linkage_graph.md` | 14 kênh liên kết `L01`–`L14`: cơ chế, độ trễ, dữ liệu nối hai đầu, đo được bằng danh mục what-if hay chưa |
| `core/04_reasoning_procedure.md` | Quy trình 6 bước, đầu vào và đầu ra của từng bước, chuyển sang what-if, mức chắc chắn |
| `core/05_output_prose.md` | Mẫu viết 7 đoạn (nhiệm vụ, phải có, tránh), dòng nhãn `[FG]`, biến thể theo nhóm tin, `IO` và cụm |
| `core/06_ngan_hang.md` | Cấp ngân hàng (`NH-`, `IR-`): sáu đường tác động, bảng độ nhạy kèm hành vi khuyến nghị, cơ hội, tín hiệu |
| `core/whatif_chung/` | What-if dùng chung: quy tắc (`wc_00`), danh mục feature (`wc_01a`, `wc_01b`, `feature_catalog.csv`), ánh xạ tín hiệu → cột (`wc_02`), công thức (`wc_03`), quy ước SQL (`wc_04`), khuôn đầu ra và nhãn `[WI]` (`wc_05`) |
| **`outside_in/`** – rủi ro từ bên ngoài | |
| `outside_in/news/nw_00_router.md` | Xếp tin vào `TT` / `GT` / `GL`, tin nhiều nhóm, tin ở nước khác |
| `outside_in/news/nw_01_truc_tiep.md` · `nw_02_gian_tiep.md` · `nw_03_gian_lan_an_ninh.md` | Cách suy luận cho từng nhóm tin |
| `outside_in/whatif/oi_wi_00_index.md` | What-if cho rủi ro từ tin: độ lớn cú sốc từ tin, chuỗi nhiều bước, cụm `[CUM]` |
| `outside_in/whatif/examples/` | 6 bài mẫu what-if outside-in có SQL (`oi_wi_ex_00_index.md`) |
| **`inside_out/`** – rủi ro từ bên trong ngân hàng | |
| `inside_out/signals.md` | 16 tín hiệu nội bộ `S01`–`S16` |
| `inside_out/bank_response_risks.md` | Rủi ro do phản ứng của ngân hàng, pha sợ và pha tham |
| `inside_out/whatif/io_wi_00_index.md` | What-if cho sự kiện nội bộ: bốn loại sự kiện, tỷ lệ lịch sử, đo hai mặt của quyết định, vòng phản hồi |
| `inside_out/whatif/examples/` | 4 bài mẫu what-if inside-out có SQL (`io_wi_ex_00_index.md`) |
| **Các module khác** | |
| `fear_greed/fg_01_dual_lens.md` · `fg_02_behavior_signals.md` · `fg_03_opportunity_map.md` | Hai lăng kính, ma trận ô A–D, tín hiệu `F`/`G`, bản đồ cơ hội `O1`–`O6` |
| `industry/ind_00_index.md` | Định tuyến ngành: ma trận biến số → ngành kèm cơ chế, cách chọn file ngành |
| `industry/ind_01`…`ind_18` | 18 file ngành Việt Nam (`I01`–`I18`, danh sách ở `ind_00_index.md` mục 2) |
| `segments/seg_01a_KHCN_ca_nhan.md` · `seg_01b_KHCN_ho_kinh_doanh.md` · `seg_02_SME.md` · `seg_03_DN_lon.md` | Bốn file phân khúc |
| `examples/` | 10 bài mẫu văn xuôi playbook (mục 4c) |

## 3. Gói ngữ cảnh theo agent
| Agent | Bước | Luôn nạp | Nạp theo điều kiện |
|---|---|---|---|
| Orchestrator | 1–6 | `00_INDEX.md`, `core/04_reasoning_procedure.md`, `guardrails.md`, `outside_in/news/nw_00_router.md` | – |
| Propagation | 1–2 | `core/02_concepts_patterns.md`, `core/03_linkage_graph.md`, `fear_greed/fg_01_dual_lens.md`, `outside_in/news/nw_00_router.md` | **Một** file nhóm tin (`nw_01` / `nw_02` / `nw_03`); file phân khúc (mục 4); `industry/ind_00_index.md` và tối đa 3 file ngành (mục 4d); 1 bài mẫu (mục 4c) |
| Product-Impact | 3 | `core/01_risk_codes.md`, `fear_greed/fg_03_opportunity_map.md` | File phân khúc trên đường lan truyền; `core/06_ngan_hang.md` khi chạm cấp ngân hàng; mục 4 của file ngành đã nạp |
| Inside-out Monitor | 4–5 | `inside_out/signals.md`, `fear_greed/fg_02_behavior_signals.md`, `inside_out/bank_response_risks.md` | Cột "Hành vi khuyến nghị khi xảy ra" trong bảng (c) của file phân khúc (việc cần làm, dữ liệu what-if, stress test); `outside_in/news/nw_03_gian_lan_an_ninh.md` mục 5 với tin `GL`; mục 5 của file ngành đã nạp |
| What-if (Opus) | sau 6 | `guardrails.md`, `core/whatif_chung/wc_00_quy_tac.md`, `wc_01a_catalog_khcn.md`, `wc_02_signal_map.md`, `wc_03_cong_thuc.md`, `wc_04_sql.md`, `wc_05_dau_ra.md` | Rủi ro từ tin: `outside_in/whatif/oi_wi_00_index.md` và 1 bài ở `outside_in/whatif/examples/`. Sự kiện nội bộ: `inside_out/whatif/io_wi_00_index.md`, `inside_out/bank_response_risks.md` và 1 bài ở `inside_out/whatif/examples/`. Thêm `wc_01b_catalog_dn.md` khi chạm SME, CIB; bảng (c) file phân khúc trên đường lan truyền |
| Critic | 6 | `guardrails.md`, `core/05_output_prose.md`, `fear_greed/fg_01_dual_lens.md` | 1 bài mẫu; ghi chú của các agent trước |

Tin nhiều nhóm: nạp file của nhóm chính đầy đủ; nhóm phụ chỉ cần mục liên quan.

## 4. Bộ định tuyến

### 4a. Nhóm tin → file
| Nhóm | File |
|---|---|
| `TT` – giá hàng hóa, vàng, năng lượng, tỷ giá, lãi suất, thương mại, vận tải, trừng phạt, chính sách, xung đột | `outside_in/news/nw_01_truc_tiep.md` |
| `GT` – dân số, đại dịch, khí hậu, đô thị hóa, công nghệ, hành vi xã hội | `outside_in/news/nw_02_gian_tiep.md` |
| `GL` – gian lận, lừa đảo, rửa tiền, lỗ hổng CVE, ransomware, rò rỉ dữ liệu | `outside_in/news/nw_03_gian_lan_an_ninh.md` |

### 4b. Đối tượng → file
| Dấu hiệu trong sự kiện / đường lan truyền | Nạp file |
|---|---|
| Cá nhân, hộ gia đình, người lao động, nông hộ, chủ DN với tư cách cá nhân; kênh `L01` `L02` `L04` `L05` `L06` | `segments/seg_01a_KHCN_ca_nhan.md` |
| Cửa hàng, tiểu thương, bán lẻ nhỏ, đại lý, thuế hộ kinh doanh, sức mua địa phương; kênh `L03` `L06` `L07` | `segments/seg_01b_KHCN_ho_kinh_doanh.md` **và** `seg_01a` |
| DN vừa và nhỏ, nhà cung cấp, nhà thầu mua sắm công; kênh `L01` `L02` `L03` `L07` `L12` | `segments/seg_02_SME.md` |
| Tập đoàn, ngành, xuất nhập khẩu, chủ đầu tư BĐS, tổ chức phát hành trái phiếu, DN đầu chuỗi; kênh `L03` `L04` `L05` `L08` | `segments/seg_03_DN_lon.md` |
| Thanh khoản, tỷ giá của ngân hàng, hệ thống, lỗ hổng, tài khoản bị lợi dụng, trừng phạt, danh tiếng, cổ phiếu TCB, xếp hạng; kênh `L09` `L10` `L11` `L13` `L14` | `core/06_ngan_hang.md` |

Mỗi lượt nạp tối đa **3 file phân khúc** (hai file KHCN tính là 2). Cần nhiều hơn thì tách lượt, rồi Critic viết gộp. `core/06_ngan_hang.md` và `fear_greed/fg_03_opportunity_map.md` không tính vào giới hạn này.

### 4c. Chọn bài mẫu
| Sự kiện | Bài mẫu |
|---|---|
| Tin `TT` gói nhiều kênh: xung đột, địa chính trị | `examples/ex_NW_01_xung_dot_trung_dong.md` |
| Tin `TT` giá một mặt hàng, có hành vi đổ xô, sốt | `examples/ex_FG_01_ca_phe_o_B.md` |
| Tin `TT` vĩ mô có lợi cho nhiều phân khúc | `examples/ex_FG_03_lai_suat_giam_o_A_B.md` |
| Tin `TT` bất lợi cho một ngành xuất khẩu | `examples/ex_P1_doanh_nghiep_truoc.md` |
| Tin `TT` biến cố pháp lý cá nhân, lãnh đạo DN | `examples/ex_P2_ca_nhan_truoc.md` |
| Tin đồn, hoảng loạn, rút tiền | `examples/ex_FG_02_tin_don_o_C.md` |
| Tin `GT` thay đổi cấu trúc dài hạn | `examples/ex_NW_02_ty_le_sinh_giam.md` |
| Tin `GL` lỗ hổng kỹ thuật, CVE | `examples/ex_NW_03_lo_hong_cve.md` |
| Tin `GL` thủ đoạn lừa đảo, gian lận ở nước khác | `examples/ex_NW_04_lua_dao_nuoc_ngoai.md` |
| Sự kiện inside-out (sự cố của chính ngân hàng) | `examples/ex_P3_toan_he_thong.md` |

### 4d. Biến số → ngành
Sau khi xếp nhóm tin, liệt kê biến số trong tin (giá gì, chính sách gì, ở vùng nào) rồi tra ma trận ở `industry/ind_00_index.md` mục 3. Nạp **tối đa 3 file ngành** chịu tác động mạnh hoặc nhanh nhất; ngành liên đới chỉ nêu qua mục 6 của file đã nạp. File ngành không tính vào giới hạn 3 file phân khúc. File ngành là kiến thức nền định tính: không suy ra số liệu, dư nợ theo ngành luôn ghi "cần truy vấn nội bộ".

### 4e. Rủi ro → what-if
Chạy sau khi bài playbook đã qua Critic, khi có rủi ro mức **P1**/**P2** cần đo định lượng. Agent What-if nhận bài văn xuôi, dòng `[FG]` (và `[CUM]` nếu có) và chọn cửa vào:

| Sự kiện | Cửa vào | Bài mẫu |
|---|---|---|
| Tin bên ngoài (`TT`, `GT`, `GL`) hoặc cụm tin | `outside_in/whatif/oi_wi_00_index.md` | `outside_in/whatif/examples/oi_wi_ex_00_index.md` |
| Sự kiện nội bộ (`IO`): tín hiệu xấu đi, quyết định ngân hàng, sự cố, rủi ro tập trung | `inside_out/whatif/io_wi_00_index.md` | `inside_out/whatif/examples/io_wi_ex_00_index.md` |

Cả hai dùng phần chung `core/whatif_chung/`. Không đưa số liệu kết quả what-if ngược vào bài playbook (`guardrails.md` mục 18); kết quả do người dùng chạy SQL và đọc theo `wc_05_dau_ra.md` mục 7.

## 5. Tra nhanh mã
| Mã | Ý nghĩa | File |
|---|---|---|
| `CN-` | Sản phẩm KHCN – nhóm cá nhân | `segments/seg_01a_KHCN_ca_nhan.md` |
| `HKD-` | Sản phẩm KHCN – nhóm hộ kinh doanh | `segments/seg_01b_KHCN_ho_kinh_doanh.md` |
| `SME-` | Sản phẩm SME | `segments/seg_02_SME.md` |
| `CIB-` | Sản phẩm doanh nghiệp lớn | `segments/seg_03_DN_lon.md` |
| `NH-` `IR-` | Năng lực, hệ thống cấp ngân hàng; nhà đầu tư, xếp hạng | `core/06_ngan_hang.md` |
| `TT` `GT` `GL` | Nhóm tin outside-in | `outside_in/news/nw_00_router.md` |
| `GL1`–`GL4` | Loại tin gian lận, an ninh mạng | `outside_in/news/nw_03_gian_lan_an_ninh.md` |
| `X01`–`X08` | Tín hiệu gian lận, an ninh mạng | `outside_in/news/nw_03_gian_lan_an_ninh.md` |
| `L01`–`L14` | Kênh liên kết | `core/03_linkage_graph.md` |
| `S01`–`S16` | Tín hiệu nội bộ | `inside_out/signals.md`, đọc hai chiều ở `fear_greed/fg_02_behavior_signals.md` |
| `F01`–`F04` · `G01`–`G07` | Hành vi sợ hãi · tham lam | `fear_greed/fg_02_behavior_signals.md` |
| `O1`–`O6` · ô `A`–`D` | Loại cơ hội · ma trận tác động × tâm lý | `fear_greed/fg_01_dual_lens.md` |
| `I01`–`I18` | Ngành ở Việt Nam (chỉ dùng trong ghi chú giữa các agent, không đưa vào nhãn `[FG]`) | `industry/ind_00_index.md` |
| **P1** **P2** **P3** (in đậm, trong bảng (c) file phân khúc) | Mức ưu tiên keyword, khác với mẫu lan truyền `P1`–`P3`: P1 tác động ≤ 7 ngày, chạm tiền khách, thanh khoản, vận hành, tuân thủ; P2 tác động 1–3 tháng qua thu nhập, tỷ giá, lãi suất; P3 chậm, gián tiếp hoặc chỉ doanh thu phí; (+) chiều cơ hội. Tin khớp nhiều keyword → lấy mức cao nhất | `segments/` |
| `P1` `P2` `P3` | Mẫu lan truyền | `core/02_concepts_patterns.md` |
| `[FG]` | Dòng nhãn cuối kết luận | `core/05_output_prose.md` |
| `[WI]` | Dòng nhãn cuối kịch bản what-if; trường `cua=OI` (từ tin) hoặc `cua=IO` (nội bộ) | `core/whatif_chung/wc_05_dau_ra.md` |
| `GAP` | Tín hiệu playbook không có cột dữ liệu tương ứng | `core/whatif_chung/wc_02_signal_map.md` |

## 6. Quy tắc bảo trì
- Không đổi hoặc tái sử dụng mã cũ. Sản phẩm ngừng bán thì đánh dấu `(ngừng)` thay vì xóa.
- Sản phẩm mới: thêm vào bảng (c) **và** danh mục (f) của file phân khúc; nếu có thể hưởng lợi, thêm vào `fear_greed/fg_03_opportunity_map.md`.
- Chủ đề tin mới hay gặp: thêm một mục vào file nhóm tin tương ứng thay vì tạo file mới.
- Ngành mới: tạo file `industry/ind_NN_...md` theo khuôn 7 mục ở `industry/ind_00_index.md` mục 7, thêm dòng vào danh sách và ma trận của file đó; không ghi tên công ty, không ghi số liệu.
- Danh mục feature thay đổi: cập nhật `core/whatif_chung/feature_catalog.csv` trước, rồi sinh lại `wc_01a`/`wc_01b` từ file này; chạy lại 2 script kiểm tra trên `outside_in/whatif/examples/`.
- Giữ mỗi file dưới ~12 KB. Ngoại lệ đã biết: file phân khúc, danh mục feature và `industry/ind_00_index.md` (bảng tra cứu, đọc theo mục). File vượt ngưỡng thì tách và thêm dòng định tuyến ở mục 4.
