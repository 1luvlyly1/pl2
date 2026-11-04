# Test case TC-18 đến TC-20 – Lăn cầu tuyết theo lớp, tin gian lận và phản ví dụ

Cách chạy như `tc_05_lan_cau_tuyet_a.md`.

## TC-18 Hộ kinh doanh mặt phố – quy định dồn lên, mặt bằng bị trả lan rộng

| Ngày | Tin (tóm tắt) | Nguyên nhân | Lớp | Nguồn |
|---|---|---|---|---|
| 21/12/2025 | Hà Nội siết tiếng ồn; công an phường yêu cầu quán cà phê, ăn uống dọn trước 22h | giờ hoạt động | Quy định | [Hà Nội Mới](https://hanoionline.vn/siet-quan-ly-tieng-on-tra-lai-su-yen-tinh-cho-dan-cu-246377332.htm) |
| 26/12/2025 | HKD lo khi bỏ thuế khoán, chuyển sang tự kê khai từ 2026 | thuế, hóa đơn | Quy định | [Thuế – Hải quan](https://thuehaiquan.tapchikinhtetaichinh.vn/go-kho-cho-ho-kinh-doanh-chuyen-doi-thue-khoan-sang-ke-khai-kien-nghi-tu-vtca-135298.html) |
| 11/04/2026 | Nghị định 87/2026 tăng phạt karaoke quá giờ, hiệu lực 15/05 | giờ hoạt động | Quy định | [Thư viện Pháp luật](https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/109850/nghi-dinh-87-2026-nd-cp-muc-xu-phat-kinh-doanh-karaoke-qua-gio-quy-dinh-tu-15-5-2026) |
| 29/04/2026 | Hộ nhỏ phản ánh khách không mua khi thiếu hóa đơn điện tử | thuế, hóa đơn | Quy định | [Thời báo Tài chính VN](https://thoibaotaichinhvietnam.vn/giai-phap-nao-de-han-che-tac-dung-phu-cua-hoa-don-196518.html) |
| 08/05/2026 | Mặt phố Hà Nội hạ nhiệt, trả mặt bằng; giá thuê giảm 10–30%; do chi phí và siết vỉa hè | chi phí thuê; vỉa hè | Triệu chứng | [Nhân Dân](https://nhandan.vn/kinh-doanh-mat-pho-ha-nhiet-post960678.html) |
| 08/06/2026 | Làn sóng trả mặt bằng TP.HCM, giá chào thuê thấp hơn 8–10% | TMĐT; vỉa hè | Triệu chứng | [VnExpress](https://vnexpress.net/lan-song-tra-mat-bang-keo-gia-thue-nha-pho-tp-hcm-lao-doc-5082897.html) |
| 12/07/2026 | Nhà mặt phố Hà Nội rao nhiều tháng vẫn ế dù giảm 20–30% | sức mua; TMĐT; vỉa hè | Triệu chứng | [Znews](https://znews.vn/nha-mat-pho-rao-nhieu-thang-van-e-khach-thue-post1668596.html) |
| 03/11/2026 | Mặt bằng TP.HCM bỏ trống trước cao điểm mua sắm | nhà bán lẻ dời khu; TMĐT | Triệu chứng | [Dân trí](https://dantri.com.vn/bat-dong-san/loat-mat-bang-cho-thue-o-tphcm-van-bo-trong-truoc-cao-diem-mua-sam-20261103171228309.htm) |

| Hạng mục | Kỳ vọng |
|---|---|
| Khóa cụm | `vai_tro=hkd_mat_pho` × `vung=do_thi_lon` × `nganh=I09/I10` |
| Ngày mở | **08/05/2026** (11/04 giờ hoạt động + 29/04 thuế + 08/05 chi phí thuê, vỉa hè) |
| Trạng thái 03/11/2026 | Đang diễn biến |
| Loại cụm | Lăn cầu tuyết theo lớp: quy định là nguyên nhân, trả mặt bằng là triệu chứng; hiển thị theo lớp |
| Agent cụm | Chuỗi: quy định → doanh thu HKD giảm → trả mặt bằng → giá thuê giảm → chủ nhà mất thu nhập → nhà phố làm TSBĐ giảm giá; hai nhóm khách: HKD (`HKD-LN-01` `HKD-LN-02` `HKD-REV-01`) và chủ nhà phố có vay thế chấp |
| Tín hiệu | `S02` `S03` theo tuyến phố; `S16`; LTV nhà phố theo tuyến |

- **Phải có:** nêu rõ không có quy định chung cấm HKD hoạt động sau 22h; phạm vi chỉ Hà Nội và TP.HCM theo tin.
- **Không được:** mở rộng sang tỉnh khác khi tin không nêu; đề xuất cắt hạn mức HKD đồng loạt.

## TC-19 Lừa đảo nhắm vào người trẻ – cụm tin gian lận

| Ngày | Tin (tóm tắt) | Kênh | Nguồn |
|---|---|---|---|
| 29/10/2026 | Công an cảnh báo trang web giả mạo VNeID | website giả mạo | [CafeF](https://cafef.vn/tat-ca-nguoi-dung-vneid-chu-y-thong-bao-nong-tu-cong-an-188261028133515035.chn) |
| 30/10/2026 | Người trẻ thành thạo thiết bị vẫn dễ bị thao túng; nhắc giả mạo bằng AI | giả mạo bằng AI | [CafeF](https://cafef.vn/lua-dao-cong-nghe-cao-nguoi-tre-thanh-thao-thiet-bi-van-de-bi-thao-tung-188261030094415724.chn) |
| 01/11/2026 | Công an TP.HCM cảnh báo lừa đảo nhắm học sinh, sinh viên; giả danh công an | cuộc gọi giả danh | [VietnamPlus](https://www.vietnamplus.vn/canh-bao-thu-doan-lua-dao-bat-coc-online-nham-vao-nguoi-tre-post1145526.vnp) |

| Hạng mục | Kỳ vọng |
|---|---|
| Khóa cụm | `phan_khuc=KHCN` × `kieu=mao_danh_co_quan_nha_nuoc` × `kenh=kenh_so` |
| Ngày mở | **01/11/2026** (cửa sổ 7 ngày) |
| Độ tuổi | Khớp 2/3 tin → **không** vào khóa; nêu là nhóm cần ưu tiên kiểm tra |
| Sản phẩm, ưu tiên | `CN-ACC-01` P1; `CN-DIG-01` P1 |
| Agent cụm | Mức nhận diện; tín hiệu `X01` (tài khoản sinh viên mới mở nhận nhiều nguồn), `X02`, `X03`; cảnh báo chủ động cho khách trẻ |

- **Phải có:** câu "chưa có số liệu nội bộ, cần truy vấn"; mức cụm "có thể".
- **Không được:** mô tả cách thực hiện thủ đoạn; đưa độ tuổi vào khóa; kết luận khách của ngân hàng đã bị lừa.

## TC-20 Người vay mua nhà – phản ví dụ

| Ngày | Tin (tóm tắt) | Nguyên nhân | Nguồn |
|---|---|---|---|
| 08/06/2026 | Lãi vay mua nhà từ ưu đãi 8–10% lên 13–15% khi hết ưu đãi; nhà đầu tư bán cắt lỗ | lãi suất thả nổi | [Doanh nghiệp Hội nhập](https://doanhnghiephoinhap.vn/lai-suat-vay-tang-cao-nha-dau-tu-bat-dong-san-chiu-ap-luc-ban-cat-lo-139106.html) |
| 27/07/2026 | Lãi vay mua nhà neo hai con số | lãi suất thả nổi | [Thời báo Tài chính VN](https://thoibaotaichinhvietnam.vn/lai-suat-vay-mua-nha-neo-hai-con-so-ky-vong-ha-nhiet-khong-de-201273-201273.html) |
| 04/08/2026 | Thả nổi 13–16%, gia đình cắt chi tiêu, bán lại hợp đồng | lãi suất thả nổi | [Tiền Phong](https://tienphong.vn/lai-suat-tha-noi-neo-cao-nguoi-mua-nha-chat-vat-xoay-xo-post1865018.tpo) |
| 27/08/2026 | Cảnh báo nợ nhóm 2 tăng đều ở cho vay cá nhân | lãi suất thả nổi | [VietnamFinance](https://vietnamfinance.vn/rui-ro-lon-dan-khi-lai-suat-tha-noi-vay-mua-nha-tang-cao-d149495.html) |

| Hạng mục | Kỳ vọng |
|---|---|
| Cụm | **Không mở** – 1 nguyên nhân dù tiêu chí nhóm trùng 4/4 |
| Xử lý | Mỗi tin chạy playbook tin đơn lẻ: `CN-LN-01` `CN-LN-02` P2 |
| Biến thể | Thêm tin "cắt giảm lao động ở đô thị lớn" ngày 01/09 → 2 nguyên nhân, chưa mở; thêm tiếp "giá căn hộ thứ cấp giảm" ngày 05/09 → 3 nguyên nhân còn hiệu lực (tin lãi suất 27/08 còn hiệu lực 14 ngày) → mở cụm 05/09 |
| Tín hiệu | Khoản vay hết ưu đãi theo tháng; `S05` `S06` `F03` |

- **Phải có:** giải thích vì sao nhiều bài không phải cụm.
- **Không được:** mở cụm với một nguyên nhân; dự báo lãi suất.
