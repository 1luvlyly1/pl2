# Test case TC-12 đến TC-14 – Suy luận nhiều bước qua nhiều nhóm khách

## TC-12 Chủ tịch tập đoàn bất động sản bị khởi tố (giả định)

- **Loại:** đa bước, mẫu cá nhân trước (`P2` lan truyền), 4 bước · Nguồn: giả định
- **Đầu vào:** Cơ quan điều tra khởi tố chủ tịch một tập đoàn bất động sản lớn về tội lừa dối khách hàng. Tập đoàn có nhiều dự án nhà ở đang mở bán và trái phiếu sắp đáo hạn trong 6 tháng tới.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu cá nhân trước; ô C nếu tin có hành vi bán tháo, ngược lại ô D |
| File | `segments/seg_03_DN_lon.md`, `seg_01a_KHCN_ca_nhan.md`, `industry/ind_01_bat_dong_san.md`, `core/06_ngan_hang.md` |
| Bước 1 (có khả năng cao) | Chủ tịch → tập đoàn (`L01`): mất người ra quyết định, rủi ro pháp lý dự án |
| Bước 2 (có thể) | Tập đoàn → người mua nhà dự án (`L04`, `CN-LN-01` P1); → trái chủ (`L05`, `CN-INV-01` P1, `CIB-INV-01` P1) |
| Bước 3 (có thể) | Tài khoản giữ hộ BĐS, bảo lãnh (`CIB-ACC-04` P1, `CIB-TF-04` P1); nhà thầu, SME trong chuỗi (`L03`, `SME-GTE-01`) |
| Bước 4 (giả thuyết) | Cấp ngân hàng: danh tiếng, khiếu nại iBond, nhà đầu tư (`L10`, `NH-RP-01`, `IR-`) |
| Tín hiệu kiểm tra | `S08` `S14` `S12`; DPD `CN-LN-01` theo dự án |
| Bài mẫu gần nhất | `examples/ex_P2_ca_nhan_truoc.md` |

- **Phải có:** mức chắc chắn giảm dần đúng 4 bước; hành vi khuyến nghị: dừng bán mới trái phiếu của tổ chức, RM gọi trái chủ, không thông tin sai lệch.
- **Không được:** nêu tên tập đoàn hay cá nhân; kết luận tội danh; đề xuất thu hồi đồng loạt khoản vay mua nhà.

## TC-13 Nhà máy điện tử FDI cắt 30% lao động (giả định)

- **Loại:** đa bước qua KCN · Nguồn: giả định
- **Đầu vào:** Một nhà máy điện tử vốn nước ngoài ở Bắc Ninh thông báo cắt giảm khoảng 30% lao động trong quý tới do đơn hàng điện thoại toàn cầu giảm.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu DN trước; ô D |
| File ngành | `ind_04_dien_tu.md` (bắt buộc); có thể `ind_09_ban_le_tmdt.md`, `ind_01_bat_dong_san.md` |
| Bước 1 | Nhà máy → công nhân (`L02`): `CIB-PAY-06` P1 (cắt giảm nhân sự); `CN-LN-06` `CN-CARD-01` `CN-LN-05` P2 |
| Bước 2 | Nhà cung cấp phụ trợ SME phụ thuộc một khách FDI (`SME-LN-01` P2); HKD quanh KCN (`L06`, `HKD-REV-01` `HKD-LN-01` P2) |
| Bước 3 | Chủ nhà trọ (KHCN) mất người thuê → khoản vay thế chấp nhà trọ (`CN-LN-02`, giả thuyết) |
| Tín hiệu kiểm tra | `S01` `S04` `S05` `S02` `S03` theo KCN |
| Hành vi khuyến nghị | RM liên hệ DN; rà khoản vay nhân viên DN đó; what-if 30% nhân sự nghỉ việc |
| Nhãn tối thiểu | `phan_khuc=CIB,KHCN,SME` |

- **Phải có:** dòng tiền của FDI thường qua ngân hàng nước ngoài, cơ hội và rủi ro chủ yếu ở chuỗi nhà cung cấp và người lao động; lao động thời vụ và nhà cung cấp cấp thấp bị chạm trước.
- **Không được:** suy ra quyết định của tập đoàn khác; đề xuất hạ hạn mức đồng loạt cho công nhân KCN.

## TC-14 Bão số 4 ở Bắc Ninh, Lạng Sơn, Quảng Ninh

- **Loại:** đa bước, thiên tai, hai pha · Nguồn thật: [AHA Centre, 22/08/2026](https://adinet.ahacentre.org/report/viet-nam-floods-landslides-and-strong-winds-in-northern-region-tropical-cyclone-narra-20260822)
- **Đầu vào:** Bão số 4 và mưa lớn gây ngập, sạt lở ở Bắc Ninh, Lạng Sơn, Quảng Ninh. Sơ bộ: 200 nhà hư hại hoặc tốc mái, 733 nhà ngập ở Lạng Sơn; 2.864 ha cây trồng ngập, hư hại; 603 điểm sạt lở, ngập gây ách tắc giao thông.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `TT`; mẫu cá nhân trước theo vùng; ô D |
| File ngành | `ind_07_nong_san.md`; `ind_02_xay_dung_vlxd.md` (pha sửa chữa); có thể `ind_04_dien_tu.md` (KCN Bắc Ninh) |
| Pha 1 – thiệt hại | Nông hộ, nhà ở: `CN-LN-08` P2, `CN-INS-03` P1 (claim theo địa bàn); `CN-PAY-02` P1 (máy dừng, nhu cầu tiền mặt) |
| Pha 2 – sửa chữa | HKD vật liệu, nhà thầu nhỏ tăng doanh thu (`HKD-LN-01`, `SME-LN-01`, cơ hội có thể) |
| Bước giả thuyết | Gián đoạn giao thông → nhà máy KCN Bắc Ninh chậm giao hàng (`CIB-LN-01`) |
| Tín hiệu kiểm tra | `S07` `S06` `S02` theo tỉnh; trạng thái CDM |
| Nhãn tối thiểu | Một dòng rủi ro `o=D`, một dòng cơ hội `o=A` mức `co_the` |

- **Phải có:** tách pha thiệt hại và pha sửa chữa; giới hạn tác động ở ba tỉnh được nêu.
- **Không được:** cộng thêm số liệu không có trong tin; khai thác hoàn cảnh khó khăn để bán sản phẩm (`RP`).
