# Test case TC-09 đến TC-11 – Suy luận nhiều bước qua nhiều ngành

Trọng tâm: chọn đúng file ngành (tối đa 3), đi đúng kênh `L`, và **mức chắc chắn giảm theo số bước** (bước 1 "có khả năng cao", bước 2 "có thể", bước 3 trở đi "giả thuyết").

## TC-09 Eo biển Hormuz gần như đóng

- **Loại:** đa bước, một tin chạm nhiều ngành · Nguồn thật: [Tạp chí Kinh tế – Tài chính, 02/03/2026](https://tapchikinhtetaichinh.vn/eo-bien-hormuz-dong-cua-nhieu-nhom-nganh-bien-dong-manh-149856.html)
- **Đầu vào:** Từ chiều 28/02/2026, tàu qua eo biển Hormuz gần như dừng hẳn; các hãng tàu lớn đổi tuyến vòng qua Mũi Hảo Vọng, thêm 10–14 ngày hành trình. Nhóm dầu khí được đánh giá hưởng lợi; logistics và xuất nhập khẩu (dệt may, da giày, điện tử, nông sản tươi đi châu Âu) chịu áp lực chi phí và thời gian.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu toàn hệ thống qua giá thế giới; rủi ro ô D, cơ hội ô A |
| File ngành (≤ 3) | `ind_12_nang_luong.md` + `ind_11_logistics.md` + một trong `ind_10_du_lich_hang_khong.md` / `ind_03_det_may_da_giay.md`; ngành còn lại chỉ nêu qua mục 6 |
| Bước 1 (có khả năng cao) | Giá dầu, cước tăng → DN vận tải, hàng không, xuất khẩu đi EU thiệt; DN dầu khí lợi |
| Bước 2 (có thể) | Hãng bay → đại lý vé trong tài trợ chuỗi (`CIB-SCF-01`, `L03`); DN xuất khẩu chậm thu tiền (`CIB-TF-02`) |
| Bước 3 (giả thuyết) | Lạm phát nhập khẩu → kỳ vọng lãi suất tăng (`NH-MR-02`) → người vay thả nổi |
| Sản phẩm, ưu tiên | `CIB-SCF-01` P2; `CIB-TF-02` P2; `CIB-FX-01` P2; `SME-PAY-04` P2; `CN-CARD-01` P2 (giá xăng); `CN-PAY-01` P1 nếu có giao dịch tới khu vực xung đột |
| Cơ hội | DN năng lượng cần vốn lưu động, L/C (`O1` `O3`); phòng ngừa tỷ giá gắn hợp đồng thật |
| Bài mẫu gần nhất | `examples/ex_NW_01_xung_dot_trung_dong.md` |

- **Phải có:** rà soát trừng phạt (`NH-CO-01`); điểm đảo chiều khi tuyến mở lại; nêu ngành nào không nạp file nhưng có liên đới.
- **Không được:** nạp quá 3 file ngành; xếp bước 3 ở mức "có khả năng cao"; dự báo giá dầu.

## TC-10 Thuế bổ sung Mục 301, Việt Nam chịu 12,5%

- **Loại:** đa bước, buộc chọn ngành · Nguồn thật: [Trung tâm WTO, sau 24/07/2026](https://trungtamwto.vn/hiep-dinh-khac/33123-viet-nam-ung-pho-ra-sao-truoc-chinh-sach-thue-quan-moi-cua-hoa-ky)
- **Đầu vào:** Từ 24/07/2026, Mỹ áp thuế bổ sung theo Mục 301 với hàng hóa của 60 nền kinh tế; Việt Nam chịu 12,5% (trừ dòng hàng được miễn). Khoảng 37% kim ngạch xuất khẩu sang Mỹ chịu ảnh hưởng. Dệt may, da giày, gỗ, thủy sản chịu sức ép rõ nhất; điện tử còn dư địa nhưng cần lưu ý xuất xứ.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu DN trước; ô D |
| File ngành (≤ 3) | `ind_03_det_may_da_giay.md` + `ind_05_go_noi_that.md` + `ind_06_thuy_san.md`; `ind_04_dien_tu.md` chỉ nêu, không nạp |
| Bước 1 | DN xuất khẩu dệt may, gỗ, thủy sản: đơn hàng, giá bán (`CIB-TF-02` `CIB-LN-01` `SME-LN-01`, P2) |
| Bước 2 | Công nhân KCN (`L02`): `CN-LN-06` `CN-CARD-01` P2; nông hộ nuôi tôm, cá tra (thủy sản) |
| Bước 3 | HKD quanh KCN, nhà trọ (`L06`): `HKD-LN-01` P2, giả thuyết |
| Tín hiệu kiểm tra | `S01` `S10` `S02` `S04` |
| Cơ hội | Có thể: đẩy hàng trước hạn tạo đơn tạm thời; dịch chuyển thị trường |

- **Phải có:** phân biệt pha đẩy hàng trước hạn với xu hướng; nêu độ trễ từng bước.
- **Không được:** nạp cả 4 file ngành; tính số việc làm bị mất; nói biện pháp nhằm vào lao động cưỡng bức ở DN Việt Nam (bài nêu rõ không phải kết luận như vậy).

## TC-11 Dịch tả lợn châu Phi ở Đắk Lắk

- **Loại:** đa bước, hai chiều trong cùng chuỗi · Nguồn thật: [VOV, 18/07/2026](https://vov.vn/kinh-te/dak-lak-chu-dong-ung-pho-truoc-nguy-co-virus-moi-tren-dan-vat-nuoi-post1316200.vov)
- **Đầu vào:** Đắk Lắk ghi nhận dịch tả lợn châu Phi ở 113 hộ thuộc 30 xã, phường, tiêu hủy hơn 8.500 con. Có nguy cơ chủng lai mà vắc-xin hiện có chưa bảo hộ, và chủng lở mồm long móng SAT1 từ bên ngoài.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu cá nhân trước (nông hộ); ô D |
| File ngành | `ind_08_chan_nuoi_thuc_pham.md` (bắt buộc); có thể `ind_07_nong_san.md` (cùng nông hộ) |
| Bước 1 | Nông hộ chăn nuôi mất đàn (`CN-LN-06` `CN-LN-07` P2) |
| Bước 2 | Đại lý thức ăn, thuốc thú y bán chịu (`HKD-LN-01` P2); DN thức ăn chăn nuôi và nhà phân phối (`CIB-SCF-01` hoặc `CIB-LN-01`) |
| Bước 3 | Giá thịt tăng sau dịch → F&B, quán ăn chịu chi phí (giả thuyết) |
| Chiều cơ hội | Có thể: trang trại an toàn sinh học tăng giá bán; vốn tái đàn sau dịch (`O1`) – kèm rủi ro tái đàn ồ ạt |
| Tín hiệu kiểm tra | `S04` `S06` `S02` theo tỉnh |
| Nhãn tối thiểu | Một dòng `huong=rui_ro`, một dòng `huong=co_hoi`, `phan_khuc` có `KHCN` |

- **Phải có:** điểm đảo chiều (tái đàn ồ ạt → giá giảm); nông hộ thường không có chi lương, phải dùng tín hiệu khác.
- **Không được:** tính thiệt hại bằng tiền; khẳng định dịch lan sang tỉnh khác khi tin không nêu.
