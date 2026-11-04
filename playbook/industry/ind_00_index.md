---
id: IND-INDEX
used_by: [Orchestrator, Propagation, Product-Impact]
steps: [1, 2, 3]
depends_on: [outside_in/news/nw_00_router.md, core/03_linkage_graph.md]
load_when: Mọi sự kiện có biến số bên ngoài (giá, tỷ giá, thuế quan, thời tiết, dịch bệnh, chính sách, công nghệ) – tra ngành bị tác động trước khi chọn file ngành
version: v3.4
updated: 2026-11-04
---

# Định tuyến ngành: biến số bên ngoài → ngành nào bị tác động

## 1. Module ngành dùng để làm gì
Tin bên ngoài thường chạm vào **một ngành** trước, rồi ngành truyền tác động tới chủ DN, người lao động, hộ kinh doanh và đối tác trong chuỗi. Module ngành giúp agent trả lời ba câu hỏi ở bước 1 và 2:
1. Biến số trong tin chạm **ngành nào**, theo chiều lợi hay thiệt, vì cơ chế gì?
2. Trong ngành đó, **ai** chịu tác động: KHCN cá nhân (người lao động, nông hộ, người tiêu dùng, nhà đầu tư), KHCN hộ kinh doanh, SME, DN lớn?
3. Mỗi nhóm gặp **thách thức** gì, có **cơ hội** gì, và dẫn tới sản phẩm ngân hàng nào?

Nguyên tắc dùng:
- **File ngành là kiến thức nền định tính, không phải dữ liệu.** Không suy ra số liệu, thị phần hay dư nợ theo ngành; mức phơi nhiễm của ngân hàng luôn ghi "cần truy vấn nội bộ".
- **Sự kiện được giao là nguồn duy nhất về diễn biến.** File ngành giải thích cơ chế truyền dẫn; không thêm diễn biến mà tin không nêu (ví dụ không nói "giá đã giảm tiếp" khi tin chỉ nói về một ngày).
- **Một ngành có thể vừa lợi vừa thiệt trong cùng một tin**, tùy vai trò trong chuỗi giá trị. Giá cà phê tăng có lợi cho nông hộ đang có hàng nhưng gây áp lực vốn cho đại lý thu mua phải ứng tiền nhiều hơn. Luôn đọc cả hai chiều.
- **Mức chắc chắn theo khoảng cách:** ngành bị chạm trực tiếp có thể ở mức "có khả năng cao"; ngành liên đới đi qua mục 6 của file ngành thường chỉ "có thể" hoặc "giả thuyết".

## 2. Danh sách 18 ngành
| Mã | File | Phạm vi | Khách hàng điển hình |
|---|---|---|---|
| `I01` | `ind_01_bat_dong_san.md` | Nhà ở, khu công nghiệp, nghỉ dưỡng, môi giới | DN lớn là chủ đầu tư, SME môi giới và nhà thầu, KHCN người mua nhà và nhà đầu tư |
| `I02` | `ind_02_xay_dung_vlxd.md` | Xây dựng, thép, xi măng, vật liệu | DN lớn sản xuất vật liệu, SME nhà thầu, hộ kinh doanh cửa hàng vật liệu |
| `I03` | `ind_03_det_may_da_giay.md` | Dệt, may, da giày, túi xách | DN lớn và FDI, SME gia công, công nhân |
| `I04` | `ind_04_dien_tu.md` | Điện tử, linh kiện, bán dẫn, công nghiệp hỗ trợ | DN FDI, SME phụ trợ, công nhân khu công nghiệp |
| `I05` | `ind_05_go_noi_that.md` | Gỗ, đồ gỗ, nội thất xuất khẩu và nội địa | DN lớn, SME, hộ kinh doanh làng nghề, nông hộ trồng rừng |
| `I06` | `ind_06_thuy_san.md` | Tôm, cá tra, hải sản đánh bắt, chế biến | DN lớn chế biến, nông hộ nuôi trồng, ngư dân |
| `I07` | `ind_07_nong_san.md` | Cà phê, gạo, tiêu, điều, cao su, trái cây | Nông hộ, đại lý thu mua là hộ kinh doanh, DN xuất khẩu |
| `I08` | `ind_08_chan_nuoi_thuc_pham.md` | Chăn nuôi, thức ăn chăn nuôi, thực phẩm, đồ uống, hàng tiêu dùng nhanh | DN lớn, trang trại, nhà phân phối, đại lý |
| `I09` | `ind_09_ban_le_tmdt.md` | Bán lẻ hiện đại, tạp hóa, chợ, thương mại điện tử | Hộ kinh doanh, SME, chuỗi bán lẻ, người bán online |
| `I10` | `ind_10_du_lich_hang_khong.md` | Du lịch, lưu trú, ăn uống, hàng không, lữ hành | Hộ kinh doanh ăn uống và lưu trú, SME lữ hành, DN lớn |
| `I11` | `ind_11_logistics.md` | Vận tải bộ, biển, hàng không; cảng; kho; giao hàng | SME, hộ kinh doanh xe tải, DN lớn cảng và kho |
| `I12` | `ind_12_nang_luong.md` | Dầu khí, xăng dầu, điện, năng lượng tái tạo | DN lớn, cửa hàng xăng dầu, SME lắp đặt điện mặt trời |
| `I13` | `ind_13_hoa_chat_phan_bon.md` | Phân bón, hóa chất, nhựa, bao bì | DN lớn, SME nhựa, đại lý vật tư nông nghiệp |
| `I14` | `ind_14_o_to.md` | Ô tô, xe máy, xe điện, đại lý, sửa chữa | DN lắp ráp, đại lý trong chương trình tài trợ chuỗi, hộ kinh doanh sửa xe, KHCN vay mua xe |
| `I15` | `ind_15_y_te_duoc.md` | Bệnh viện, phòng khám, dược, thiết bị y tế, nhà thuốc | DN lớn, SME phân phối, hộ kinh doanh nhà thuốc, KHCN y bác sĩ |
| `I16` | `ind_16_giao_duc.md` | Trường tư, mầm non, trung tâm, du học, giáo dục số | SME, hộ kinh doanh, KHCN phụ huynh và giáo viên |
| `I17` | `ind_17_cntt.md` | Phần mềm, thuê ngoài, viễn thông, trung tâm dữ liệu | DN lớn, SME công nghệ, KHCN thu nhập cao |
| `I18` | `ind_18_vang_trang_suc.md` | Vàng miếng, vàng nhẫn, trang sức, tiệm vàng | Hộ kinh doanh tiệm vàng, DN kinh doanh vàng, KHCN giữ vàng |

## 3. Ma trận biến số → ngành (khi biến số **tăng** hoặc xấu đi)
Khi biến số giảm, đảo chiều hai cột thiệt và lợi. Ngành in đậm chịu tác động mạnh hoặc nhanh nhất. Cột "Cơ chế chính" giải thích vì sao, để agent kiểm tra ngành có thật sự khớp với tin không.

| Biến số | Ngành thường **thiệt** | Ngành thường **lợi** | Cơ chế chính |
|---|---|---|---|
| Giá dầu | **I10** **I11**, I13, I06 (đánh bắt), I08, I02 | **I12** (khai thác; phân phối có hàng tồn) | Nhiên liệu là chi phí lớn của hàng không, vận tải, tàu cá; dầu là nguyên liệu hóa chất, nhựa. Qua lạm phát, giá dầu kéo sức mua tiêu dùng (`I09`) giảm sau vài tháng |
| Giá khí, than, giá điện bán lẻ | **I02** (thép, xi măng), **I13**, I03 (nhuộm), I04 | I12 (bên bán, nếu giá bán được điều chỉnh) | Ngành tiêu hao nhiều năng lượng bị ép biên lợi nhuận ngay; giá điện bán lẻ do Nhà nước điều chỉnh nên độ trễ theo quyết định |
| Giá vàng | I18 (trang sức: sức mua giảm), cấp ngân hàng (huy động) | **I18** (có hàng tồn, vàng miếng), KHCN đang giữ vàng | Giá vàng tăng nóng kéo tiền gửi ra mua vàng (`NH-LQ-01`); tiệm vàng có hàng tồn lãi nhưng khách mua trang sức giảm. Đọc cùng `core/06_ngan_hang.md` |
| USD mạnh, VND mất giá | Nhập khẩu ròng: **I12** (xăng dầu), I13, I08 (thức ăn chăn nuôi), I14, I15, I16 (du học); DN nợ USD (I10, I12) | Xuất khẩu ròng có đầu vào trong nước: **I06** **I07** I05; I10 (khách quốc tế thấy rẻ hơn) | Ngành mua đầu vào bằng USD và bán bằng VND bị ép; ngành bán bằng USD và mua bằng VND hưởng chênh lệch. I03, I04 xuất khẩu nhưng nhập nhiều đầu vào nên tác động ròng nhỏ |
| Lãi suất cho vay trong nước | **I01**, **I02**, I14, I09 (trả góp), I12 (năng lượng tái tạo đòn bẩy cao) | Ít ngành lợi trực tiếp | Ngành dùng nhiều vốn vay và bán hàng trả góp chịu cả chi phí vốn lẫn cầu giảm. Lãi suất giảm thì đảo chiều và dễ kéo pha tham ở `I01` |
| Thuế quan Mỹ, rào cản nhập khẩu | **I03** **I04** **I05** **I06**, I07, I02 (thép), I12 (tấm pin) | I11 ngắn hạn (đẩy hàng trước khi áp thuế) | Hàng xuất sang Mỹ mất lợi thế giá, người mua chuyển đơn; SME gia công bị cắt trước DN lớn. Kèm điều tra chống lẩn tránh xuất xứ |
| Chống bán phá giá, chống trợ cấp | **I02** (thép), **I06** (tôm, cá tra), I05, I04 (pin mặt trời) | Đối thủ trong nước khi Việt Nam áp thuế lên hàng nhập | Hai chiều: nước khác áp lên hàng Việt Nam làm DN xuất khẩu thiệt; Việt Nam áp lên hàng nhập giúp nhà sản xuất trong nước |
| Quy định xanh EU (chống phá rừng, điều chỉnh carbon biên giới) | **I07** (cà phê, cao su), **I05**, I02 (thép, xi măng), I13 (phân bón) | DN đã truy xuất được nguồn gốc | Chi phí chứng minh nguồn gốc và phát thải; nông hộ không có giấy tờ đất rõ bị loại khỏi chuỗi. Tác động theo lộ trình, độ trễ dài |
| Thẻ vàng chống khai thác bất hợp pháp (IUU) | **I06** (đánh bắt, chế biến hải sản) | Không | Hải sản đánh bắt khó vào EU; ngư dân, chủ tàu, cảng cá là KHCN và hộ kinh doanh |
| Nhu cầu Trung Quốc mạnh | – | **I07** (trái cây, cao su, gạo), I06, **I10** (khách), I13 | Trung Quốc là thị trường lớn của nông sản và nguồn khách du lịch. Khi Trung Quốc yếu và dư cung, hàng giá rẻ tràn sang làm **I02** I03 **I09** thiệt |
| Giá nông sản thế giới | **I08** (ngô, đậu tương làm thức ăn), DN đồ uống dùng nguyên liệu, đại lý thu mua (cần nhiều vốn hơn) | **I07** (nông hộ, DN xuất khẩu), I13 (cầu phân bón tăng) | Người bán hưởng giá cao; người mua làm nguyên liệu và đại lý phải ứng tiền bị ép. Xem `examples/ex_FG_01_ca_phe_o_B.md` |
| Hạn mặn, El Niño, bão lũ | **I07** **I06** I08, I12 (thủy điện), I10, I11, I01 (vùng ngập) | I02 (sửa chữa sau bão), I13 (vụ sau), I12 (nhiệt điện bù) | Mất mùa, mất vật nuôi, đứt giao thông theo vùng; pha sửa chữa sau thiên tai tạo cầu vật liệu. Luôn ghi rõ vùng và mùa vụ |
| Dịch bệnh ở người | **I10**, I09 (cửa hàng), I16, I03, I11 | **I15**, I09 (thương mại điện tử), I17, I08 (hàng thiết yếu) | Đóng cửa, hạn chế đi lại làm dịch vụ tiếp xúc mất doanh thu; ba pha theo `outside_in/news/nw_02_gian_tiep.md` |
| Dịch bệnh vật nuôi, thủy sản | **I08** (chăn nuôi), **I06** (nuôi tôm) | Nguồn đạm thay thế, thuốc thú y | Tiêu hủy đàn, mất vụ nuôi; nông hộ chăn nuôi là KHCN có khoản vay sản xuất |
| Khách quốc tế, nới thị thực | – | **I10**, I09, I01 (nghỉ dưỡng), I18 | Khách tăng kéo doanh thu lưu trú, ăn uống, bán lẻ; nhạy với tin chính trị và hàng không |
| Đầu tư công giải ngân | – | **I02**, I01 (đất ven hạ tầng), I11 | Dự án hạ tầng tạo cầu vật liệu và nhà thầu; thanh toán chậm từ ngân sách là rủi ro qua `L12` |
| Chính sách BĐS, pháp lý dự án, bảng giá đất | **I01**, I02, I05 (nội thất nội địa) | I01 khi tháo gỡ pháp lý | Pháp lý tắc làm vốn bị chôn; bảng giá đất tăng làm chi phí tiền sử dụng đất tăng. Kéo theo tài sản bảo đảm (`CL`) toàn hệ thống |
| FDI, dịch chuyển chuỗi cung ứng | I03 (cạnh tranh lao động) | **I04**, **I01** (khu công nghiệp), I02, I11, I12 | Nhà máy mới cần đất, nhà xưởng, điện, vận tải; lao động khu công nghiệp là KHCN nhận lương |
| Tiêu dùng nội địa mạnh | – | **I09**, I08, I14, I10, I15, I18 | Tiêu dùng yếu thì đảo chiều, hộ kinh doanh chịu trước vì không có đệm vốn |
| Thu nhập công nhân giảm, cắt giảm lao động | **I09** (quanh khu công nghiệp), I01 (nhà trọ), I14 (xe máy) | – | Thường đến sau khi đơn hàng `I03` `I04` giảm một đến hai kỳ lương |
| Tỷ lệ sinh giảm, già hóa | **I16** (mầm non), I08 (sữa trẻ em) | **I15**, I08 (dinh dưỡng người già) | Thay đổi cấu trúc nhiều năm; nhóm tin `GT`, không cảnh báo khẩn |
| AI, tự động hóa, số hóa | I17 (thuê ngoài cấp thấp), I09 (cửa hàng truyền thống) | **I17**, I04 (bán dẫn), I12 (điện cho trung tâm dữ liệu) | Việc làm đơn giản bị thay thế dần; nhu cầu hạ tầng số tăng. Nhóm tin `GT`, chân trời dài |
| Cước vận tải biển, tuyến hàng hải gián đoạn | **I05** **I03** I07, I06 (hàng lạnh), DN nhập khẩu nguyên liệu | I11 (hãng tàu, giao nhận được giá cước cao nhưng ít hàng hơn) | Hàng cồng kềnh, giá trị thấp mất biên lợi nhuận nhanh nhất; thường đi kèm giá dầu khi do xung đột |
| Giá thép, vật liệu xây dựng | **I02** (nhà thầu ký giá cố định), I01 | I02 (nhà sản xuất có hàng tồn) | Cùng ngành nhưng khác vai trò: người làm theo hợp đồng giá cố định thiệt, người có hàng tồn lợi |
| Thuế hộ kinh doanh, hóa đơn điện tử, kê khai | **I09** **I10** (ăn uống), I18, I14 (sửa xe) | Hộ chuyển đổi lên DN (`L07`) | Chi phí tuân thủ và doanh thu khai báo thay đổi; hộ nhỏ có thể mất khách khi thiếu hóa đơn. Xem `segments/seg_01b_KHCN_ho_kinh_doanh.md` |
| Chính sách xe (lệ phí, xe điện, hạn chế xe xăng) | I14 (xe xăng, sửa chữa) | I14 (xe điện, hạ tầng sạc), I12 | Cầu chuyển giữa loại xe; hộ sửa xe xăng mất dần khách |
| Đấu thầu thuốc, bảo hiểm y tế, giá dịch vụ y tế | I15 (tùy chiều chính sách) | I15 | Thanh toán bảo hiểm y tế chậm làm bệnh viện, nhà phân phối thiếu vốn lưu động |

## 4. Tin `GT` và `GL` → ngành
- **`GT`** (dân số, đại dịch, khí hậu, đô thị hóa, AI): dùng ma trận trên nhưng giữ chân trời dài; chỉ chọn ngành có cơ chế rõ, không kể hết các ngành có thể liên quan.
- **`GL`** (gian lận, lừa đảo, lỗ hổng phần mềm): ngành là **bề mặt tấn công**, không phải nơi chịu rủi ro tín dụng. Chỉ mô tả ở mức nhận diện:
  - `I09` `I11`: mạo danh giao hàng, cửa hàng online giả, chiếm tài khoản người bán;
  - `I10`: đặt phòng, vé, tour giả; `I01`: dự án không có thật, nhận đặt cọc trái phép;
  - `I18`: giao dịch tiền mặt lớn, vàng giả, rửa tiền qua vàng; `I17`: lỗ hổng ở nhà cung cấp phần mềm (`L13`);
  - `I03` `I05` `I06`: email giả người mua nước ngoài yêu cầu đổi tài khoản nhận tiền, chứng từ giả (`X04` `X06`).

## 5. Cách chọn file ngành (bước 1–2)
1. Sau khi `outside_in/news/nw_00_router.md` xếp nhóm tin, liệt kê **biến số** trong tin: giá gì, chính sách gì, ở đâu, áp lên ai.
2. Tra mục 3 để có danh sách ngành thiệt và ngành lợi; đọc cột cơ chế để loại ngành không khớp với tin.
3. Nạp **tối đa ba file ngành**, ưu tiên theo thứ tự: ngành chịu tác động mạnh hoặc nhanh nhất; ngành có cả chiều lợi và thiệt; ngành có nhiều khách KHCN hoặc hộ kinh doanh trong chuỗi.
4. Ngành liên đới không nạp; chỉ nêu qua mục 6 của file ngành đã nạp, ở mức "có thể" hoặc "giả thuyết".
5. Product-Impact dùng mục 4 của file ngành để chọn mã sản phẩm, rồi kiểm lại tên trong file phân khúc.
6. Inside-out Monitor lấy mục 5 của file ngành làm danh sách tín hiệu cần truy vấn; cột "Đo được" cho biết tín hiệu nào what-if dùng được ngay.

## 6. Ngành đi vào văn xuôi thế nào
- **Đoạn 2** (bên thiệt, bên lợi đầu tiên): gọi tên ngành và vai trò trong chuỗi bằng lời, không ghi mã `I`.
- **Đoạn 3, 4**: tách theo đối tượng – người lao động, nông hộ, hộ kinh doanh, SME, DN lớn – lấy từ mục 3 của file ngành.
- **Đoạn 6**: luôn có câu "cần truy vấn dư nợ, số khách theo ngành".
- Mã `I01`–`I18` chỉ dùng trong ghi chú giữa các agent, **không** đưa vào dòng nhãn `[FG]`.

## 7. Khuôn chung mỗi file ngành
1. **Cấu trúc ngành ở Việt Nam** – chuỗi giá trị, ai tham gia ở từng phân khúc và vì sao họ nhạy cảm, vùng, đặc thù quan trọng với ngân hàng.
2. **Biến số nhạy cảm** – bảng: biến số, điều gì xảy ra khi biến số xấu đi, ai bị chạm trước, độ trễ, ngành liên quan.
3. **Tác động theo đối tượng** – KHCN cá nhân, KHCN hộ kinh doanh, SME, DN lớn; mỗi nhóm có thách thức và cơ hội viết thành câu nêu cơ chế.
4. **Sản phẩm ngân hàng liên quan** – bảng: đối tượng, sản phẩm phía rủi ro và vì sao, sản phẩm phía cơ hội và điều kiện.
5. **Tín hiệu theo dõi** – bảng: tín hiệu, ý nghĩa với ngành, đo được bằng danh mục what-if hay chưa.
6. **Liên kết ngành** – thượng nguồn, hạ nguồn, song song; mỗi liên kết một câu cơ chế.
7. **Điểm đảo chiều và lưu ý** – điều kiện làm chiều tác động đảo lại, điều agent không được suy đoán.

Bảo trì: không ghi tên công ty, không ghi số liệu. Khi chính sách thay đổi, cập nhật mục 2 và mục 7 của file ngành và tăng `version`.
