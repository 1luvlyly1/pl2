# Test case TC-15 đến TC-17 – Lăn cầu tuyết: nhiều tin nhỏ trong một khoảng thời gian

Chạy từng tin qua playbook theo thứ tự ngày (mỗi tin ra dòng `[EXP]`), sau đó chạy bộ gom cụm với tham số mặc định của FSD (ngưỡng 3 nguyên nhân; mỗi tin còn hiệu lực theo loại nguyên nhân: thuế quan, cước, năng lượng, lãi suất 14 ngày; nông sản, dịch bệnh, quy định, mặt bằng, sức mua 30 ngày; tin `GL` 7 ngày), rồi chạy agent cụm.

## TC-15 Gỗ xuất khẩu sang Mỹ – nhiều nguyên nhân dồn vào một ngành

| Ngày | Tin (tóm tắt) | Nguyên nhân | Nguồn |
|---|---|---|---|
| 16/06/2026 | Xuất khẩu gỗ 5 tháng tăng 4,4% nhưng chịu áp lực phòng vệ thương mại và yêu cầu xanh của EU | thuế quan; quy định xanh EU | [VnEconomy](https://en.vneconomy.vn/wood-exports-maintain-growth-but-industry-still-faces-dual-pressure.htm) |
| 18/06/2026 | Cước container 40 feet tăng 23% trong một tuần; đồ gỗ, dệt may, da giày chịu ảnh hưởng | cước vận tải | [Báo Đầu tư](https://baodautu.vn/cuoc-van-tai-bien-tang-them-ap-luc-len-xuat-khau-d617862.html) |
| 19/06/2026 | Mỹ áp thuế lên tới 208,88% với gỗ dán | thuế quan | [Trung tâm WTO](https://trungtamwto.vn/chuyen-de/32735-my-danh-thue-hon-200-len-mat-hang-ty-usd-cua-viet-nam-xuat-khau-lap-tuc-giam-toc) |
| 20/06/2026 | Dự báo nửa cuối năm: rủi ro thuế Mỹ, chống phá rừng EU, chi phí logistics, tài chính | thuế quan; xanh EU; cước; lãi suất | [Mekong ASEAN](https://mekongasean.vn/du-bao-xuat-khau-go-nua-cuoi-nam-2026-56480.html) |
| 24/07/2026 | Thuế bổ sung Mục 301, Việt Nam 12,5%; gỗ chịu sức ép rõ | thuế quan | [Trung tâm WTO](https://trungtamwto.vn/hiep-dinh-khac/33123-viet-nam-ung-pho-ra-sao-truoc-chinh-sach-thue-quan-moi-cua-hoa-ky) |
| 12/08/2026 | Xuất khẩu đồ nội thất 7 tháng giảm 2,3%, sang Mỹ giảm khoảng 6% | xác nhận | [Trung tâm WTO](https://trungtamwto.vn/chuyen-de/33220-nganh-go-vuot-suc-ep-thue-huong-toi-muc-tieu-19-ty-usd) |

| Hạng mục | Kỳ vọng |
|---|---|
| Khóa cụm | `nganh=I05` × `vai_tro=dn_xuat_khau` × `thi_truong=my` |
| Ngày mở | **18/06/2026** (16/06 mới có 2 nguyên nhân) |
| Đếm | Tin 19/06 không tăng số đếm (thuế quan đã có); 20/06 thêm lãi suất → 4 |
| Loại cụm | `nhieu_nguyen_nhan`; tin 12/08 gắn nhãn xác nhận, không đếm |
| Agent cụm | Cộng dồn: đầu ra (thuế), vận chuyển (cước), tuân thủ, vốn → biên lợi nhuận bị ép từ nhiều phía; chuỗi DN gỗ → xưởng vệ tinh → công nhân → nông hộ trồng rừng |
| Nhãn cụm | `[CUM] khoa=nganh:I05+vai_tro:dn_xuat_khau+thi_truong:my \| loai=nhieu_nguyen_nhan \| so_nguyen_nhan=3 \| cua_so=14 \| mo=2026-06-18 \| huong=rui_ro \| phan_khuc=CIB,SME \| muc=co_the` |

- **Phải có:** "đọc riêng thì bỏ qua" cho ít nhất 3 tin; tiêu chí vùng chỉ là suy ra.
- **Không được:** mở cụm ngày 16/06; đếm 19/06 là nguyên nhân mới; tính tin 12/08 vào ngưỡng.

## TC-16 Nông hộ Tây Nguyên – khác ngành, cùng nhóm người

| Ngày | Tin (tóm tắt) | Nguyên nhân | Nguồn |
|---|---|---|---|
| 02/07/2026 | Giá tiêu giảm 2.000–4.000 đồng/kg ở Đắk Lắk, Gia Lai, Lâm Đồng; nông dân bán tháo | giá tiêu | [Doanh nghiệp Hội nhập](https://doanhnghiephoinhap.vn/gia-tieu-hom-nay-272026-ho-tieu-trong-nuoc-quay-dau-giam-manh-141762.html) |
| 10/07/2026 | Giá cà phê Tây Nguyên giảm 2.500 đồng/kg | giá cà phê | [Báo Lào Cai](https://baolaocai.vn/gia-ca-phe-hom-nay-107-giam-manh-tren-dien-rong-post903577.html) |
| 15/07/2026 | Giá tiêu tăng trở lại 140.000 đồng/kg | ngược chiều | [Doanh nghiệp Hội nhập](https://doanhnghiephoinhap.vn/gia-tieu-hom-nay-1572026-gia-tieu-tang-vot-tro-lai-moc-140000-dongkg-143214.html) |
| 18/07/2026 | Đắk Lắk: dịch tả lợn châu Phi ở 113 hộ, tiêu hủy hơn 8.500 con | dịch bệnh vật nuôi | [VOV](https://vov.vn/kinh-te/dak-lak-chu-dong-ung-pho-truoc-nguy-co-virus-moi-tren-dan-vat-nuoi-post1316200.vov) |
| 10/08/2026 | Xuất khẩu cà phê 7 tháng tăng lượng nhưng giảm khoảng 11% giá trị | xác nhận | [Trung tâm WTO](https://trungtamwto.vn/chuyen-de/33200-xuat-khau-ca-phe-truoc-nghich-ly-tang-luong-nhung-hut-gia-tri) |

| Hạng mục | Kỳ vọng |
|---|---|
| Khóa cụm | `vung=tay_nguyen` × `vai_tro=nong_ho` |
| Ngày mở | **18/07/2026** |
| Biến thể bắt buộc | Khóa theo ngành → **không** mở; ép cửa sổ 14 ngày cho mọi tin → **không** mở (tin 02/07 hết hiệu lực) |
| Tin ngược chiều | 15/07 gắn vào hồ sơ, không trừ số đếm; agent phải nhắc tới |
| Loại cụm | `cung_nhom_khac_nganh` |
| Agent cụm | Cộng dồn: cà phê, tiêu xen canh, chăn nuôi thêm cùng giảm → cách chia nhỏ rủi ro của nông hộ thất bại; chuỗi nông hộ → đại lý thu mua, vật tư bán chịu (`HKD-LN-01`) → HKD bán lẻ vùng → tiền gửi chi nhánh |
| Tín hiệu | `S06` `S04` `S02` `S07`; `X02` theo vùng |

- **Phải có:** tiêu chí "phân khúc KHCN" ghi là suy ra; mức cụm "có thể".
- **Không được:** gộp ba tin thành một nguyên nhân "nông nghiệp"; bỏ qua tin ngược chiều.

## TC-17 Hàng không và du lịch bay xa – một gốc, nhiều kênh

| Ngày | Tin (tóm tắt) | Kênh tác động | Nguồn |
|---|---|---|---|
| 24/03/2026 | Nhiên liệu bay tăng gần gấp ba; hãng Việt giảm chuyến, tăng phụ thu | chi phí nhiên liệu | [VTC News](https://vtcnews.vn/hang-khong-viet-chat-vat-giam-chuyen-tang-phu-thu-giua-cang-thang-nhien-lieu-ar1009129.html) |
| 24/03/2026 | Cục Hàng không cảnh báo nguy cơ thiếu nhiên liệu bay | nguồn cung nhiên liệu | [VietnamFinance](https://vietnamfinance.vn/hang-khong-viet-ung-pho-ra-sao-truoc-nguy-co-thieu-nhien-lieu-bay-d141985.html) |
| 26/03/2026 | Khoảng 1.000 chuyến dự kiến bị cắt; vé dịp 30/4 tăng; gia đình đổi sang điểm gần, đi ô tô | nhu cầu du lịch nội địa | [VnBusiness](https://vnbusiness.vn/gia-nhien-lieu-tang-hang-khong-thu-hep-hoat-dong-nguoi-dan-tinh-lai-ke-hoach-nghi-le-304.html) |
| 14/05/2026 | Vé neo cao; hãng nước ngoài cắt tuyến Đông Nam Á | khách quốc tế | [Doanh nghiệp Hội nhập](https://doanhnghiephoinhap.vn/gia-ve-may-bay-neo-muc-cao-ky-luc-du-lich-mua-he-2026-doi-mat-cu-soc-chi-phi-135644.html) |
| 28/06/2026 | Hãng bay quốc gia gánh thêm hơn 7.000 tỷ đồng chi phí nhiên liệu quý 2 | xác nhận | [Mekong ASEAN](https://mekongasean.vn/gia-nhien-lieu-tang-vietnam-airlines-ganh-them-hon-7000-ty-dong-chi-phi-trong-quy-2-56732.html) |

| Hạng mục | Kỳ vọng |
|---|---|
| Khóa cụm | `nganh=I10` × `vai_tro=hang_bay_dai_ly_ve` |
| Ngày mở | **26/03/2026** khi đếm theo kênh |
| Biến thể bắt buộc | Đếm theo `goc` (xung đột Trung Đông) → chỉ 1 → **không** mở |
| Loại cụm | `mot_goc_nhieu_kenh`; ghi `goc` chung |
| Agent cụm | Chuỗi hãng bay → đại lý vé (`CIB-SCF-01`) → lữ hành, khách sạn, HKD lưu trú ở điểm đến bay xa → lao động dịch vụ; cơ hội: du lịch gần đô thị, đi ô tô |
| Tín hiệu | `S11` đại lý vé; `S02` QR lưu trú, ăn uống theo tỉnh; giao dịch thẻ quốc tế |

- **Phải có:** giải thích vì sao đếm theo kênh chứ không theo gốc; tin xác nhận không đếm.
- **Không được:** nêu tên hãng bay trong kết luận cụm; dự báo giá nhiên liệu.
