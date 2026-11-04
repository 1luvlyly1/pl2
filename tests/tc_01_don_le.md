# Test case TC-01 đến TC-04 – Tin đơn lẻ nhóm TT

## TC-01 Thuế 208,88% với gỗ dán

- **Loại:** đơn lẻ, mẫu DN trước (`P1` lan truyền) · Nguồn thật: [Trung tâm WTO, 19/06/2026](https://trungtamwto.vn/chuyen-de/32735-my-danh-thue-hon-200-len-mat-hang-ty-usd-cua-viet-nam-xuat-khau-lap-tuc-giam-toc)
- **Đầu vào:** Mỹ áp thuế chống bán phá giá và chống trợ cấp lên tới 208,88% với gỗ dán Việt Nam. Xuất khẩu gỗ sang Mỹ 5 tháng đầu năm 2026 giảm 6,5%; Mỹ vẫn chiếm 49,2% kim ngạch. Cơ quan thương mại Mỹ còn điều tra Mục 301 với đồ nội thất nhập khẩu.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu DN trước; ô D; tâm lý chưa rõ |
| File ngành | `industry/ind_05_go_noi_that.md` (bắt buộc); có thể thêm `ind_11_logistics.md` |
| Đối tượng chạm đầu | DN lớn và SME xuất khẩu gỗ sang Mỹ |
| Sản phẩm, ưu tiên | `CIB-TF-02` P2 (thuế quan, hủy đơn); `CIB-LN-01` P2; `SME-LN-01` P2; `SME-PAY-06` / `CIB-PAY-06` theo dõi lương |
| Chuỗi nhiều bước | DN gỗ → xưởng vệ tinh, làng nghề (`HKD-LN-02`, có thể) → công nhân (`L02`, `CN-LN-06`, có thể) → nông hộ trồng rừng (giả thuyết) |
| Tín hiệu kiểm tra | `S01` `S10`; tiền về từ người mua nước ngoài; `X04` |
| Chiều cơ hội | Có thể: DN chuyển thị trường EU, Nhật cần tài trợ xuất khẩu, phòng ngừa tỷ giá (`O1` `O3`) |
| Nhãn tối thiểu | `[FG] loai_tin=TT \| o=D \| tam_ly=chua_ro \| huong=rui_ro \| phan_khuc=CIB,SME,KHCN \| muc=co_kha_nang_cao` |

- **Phải có:** nêu thuế chỉ áp cho gỗ dán, chưa phải toàn ngành; nêu độ trễ tới công nhân 1–2 tháng; câu "cần truy vấn dư nợ ngành gỗ".
- **Không được:** ước lượng số DN hay số công nhân bị ảnh hưởng; nêu tên DN; đề xuất siết hạn mức toàn ngành gỗ.

## TC-02 Lãi suất huy động bình quân lên 6,46%

- **Loại:** đơn lẻ, toàn hệ thống (`P3` lan truyền), hai chiều · Nguồn thật: [Tạp chí Kinh tế – Tài chính, 09/10/2026](https://tapchikinhtetaichinh.vn/lai-suat-ty-gia-hom-nay-lai-huy-dong-binh-quan-len-6-46-nam-usd-ngan-hang-giam-gia-169067.html)
- **Đầu vào:** Lãi suất huy động bình quân với khoản gửi mới đạt 6,46%/năm tại 30/09/2026, tăng 1,22 điểm % so với cuối 2025; nhiều ngân hàng trả từ 7% cho kỳ hạn 12 tháng. NHNN giữ nguyên lãi suất điều hành 9 tháng. Tỷ giá trung tâm 25.629 đồng/USD.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu toàn hệ thống; hai nhánh: rủi ro ô D, cơ hội ô A |
| Bên lợi | KHCN có tiền gửi (`CN-DEP-01`, `CN-DEP-04`, `O2`) |
| Bên thiệt | Người vay thả nổi (`CN-LN-01` `CN-LN-02` P2); DN đòn bẩy cao (`CIB-LN-02`); cấp ngân hàng: chi phí vốn, cạnh tranh huy động (`NH-LQ-01`) |
| Chuỗi nhiều bước | Lãi huy động tăng → lãi cho vay tăng (có thể) → người vay hết ưu đãi chịu áp lực → giá BĐS, TSBĐ (giả thuyết) |
| Sản phẩm, ưu tiên | `CN-ACC-03` P2 (đối thủ tăng lãi suất); `CN-DEP-01` P2 |
| Tín hiệu kiểm tra | `F01` `F02`; danh sách khoản vay hết ưu đãi theo tháng; `S05` |
| Nhãn tối thiểu | Hai dòng: `o=D` `huong=rui_ro` và `o=A` `huong=co_hoi`, `phan_khuc` có `KHCN` và `NH` |

- **Phải có:** cả hai lăng kính; nêu rủi ro phản ứng của ngân hàng (chạy đua lãi suất theo phản xạ, `inside_out/bank_response_risks.md`).
- **Không được:** dự báo lãi suất tương lai bằng con số; khuyến nghị khách gửi hay rút tiền.

## TC-03 Giá vàng lập đỉnh, người dân xếp hàng mua (giả định)

- **Loại:** đơn lẻ, ô B (tham lam) · Nguồn: giả định
- **Đầu vào:** Giá vàng miếng trong nước lập đỉnh mới trong tuần thứ hai liên tiếp. Nhiều cửa hàng vàng ở Hà Nội và TP.HCM có người xếp hàng từ sáng sớm; một số người cho biết rút tiết kiệm để mua.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu cá nhân trước; ô B; tâm lý tham |
| File ngành | `ind_18_vang_trang_suc.md`; `core/06_ngan_hang.md` |
| Sản phẩm, ưu tiên | `CN-DEP-01` P2 (vàng tăng nóng); `CN-PAY-02` P2 (rút tiền mặt mua vàng); `CN-LN-05` `CN-LN-07` P2 (vay để mua, `G01` `G02`) |
| Cấp ngân hàng | `NH-LQ-01` `NH-LQ-02`; giao dịch tiền mặt lớn `NH-CO-01` |
| Chuỗi nhiều bước | Tiền gửi → vàng → HKD tiệm vàng (`HKD-ACC-01`, `HKD-SVC-01`) doanh thu tăng → điểm đảo chiều: giá quay đầu, người mua bằng tiền vay chịu lỗ |
| Tín hiệu kiểm tra | `G01` `G02` `S06` `S07`; `X01` (sàn vàng không phép) |
| Nhãn tối thiểu | `[FG] loai_tin=TT \| o=B \| tam_ly=tham \| huong=ca_hai \| phan_khuc=KHCN,NH \| muc=co_kha_nang_cao` |

- **Phải có:** điểm đảo chiều; mặt trái của cơ hội huy động lại khi khách chốt lời.
- **Không được:** dự báo giá vàng; khuyến nghị mua hay bán vàng; gọi đây là ô A (tin mô tả rõ hành vi đổ xô).

## TC-04 Tin đồn thanh khoản ở một ngân hàng khác (giả định)

- **Loại:** đơn lẻ, ô C (sợ hãi) · Nguồn: giả định
- **Đầu vào:** Trên mạng xã hội lan truyền tin một ngân hàng thương mại khác gặp khó khăn thanh khoản. Tại hai tỉnh, người dân xếp hàng rút tiền ở ngân hàng đó; NHNN chưa có thông báo.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; ô C; tâm lý sợ; lan qua tin đồn (lây lan tâm lý giữa KHCN) |
| Sản phẩm, ưu tiên | `CN-PAY-02` P1 (rút tiền ồ ạt); `CN-ACC-01` P1 (tin đồn thanh khoản); `CN-DEP-01` P1 |
| Cấp ngân hàng | `NH-LQ-01` `NH-LQ-02` `NH-RP-01` |
| Chiều cơ hội | Tiền tìm nơi an toàn chuyển đến (`O6`), mức "có thể" |
| Hành vi khuyến nghị | Tăng tiếp quỹ CDM ở hai tỉnh; kịch bản trả lời tin đồn; what-if rút gấp 3 trong 48 giờ |
| Tín hiệu kiểm tra | `S07` `F01` `S14` theo địa bàn |
| Nhãn tối thiểu | Hai dòng `o=C`: `huong=rui_ro` và `huong=co_hoi` |

- **Phải có:** điều kiện không lợi dụng khó khăn của bên khác khi nêu `O6`; rủi ro tin đồn lây sang chính ngân hàng.
- **Không được:** nêu tên ngân hàng; khẳng định tin đồn đúng hay sai; đề xuất quảng cáo kéo khách từ ngân hàng bị đồn.
