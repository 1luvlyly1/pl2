# Test case TC-05 đến TC-08 – Tin GT, GL và sự cố nội bộ

## TC-05 Luật Dân số có hiệu lực

- **Loại:** đơn lẻ, gián tiếp, chân trời dài · Nguồn thật: [SGGP, 16/12/2025](https://www.sggp.org.vn/luat-dan-so-ca-nhan-cap-vo-chong-quyet-dinh-so-con-post828916.html)
- **Đầu vào:** Luật Dân số được Quốc hội thông qua ngày 10/12/2025, có hiệu lực từ 01/07/2026. Luật kéo dài nghỉ thai sản khi sinh con thứ hai, cho lao động nam nghỉ chăm vợ sau sinh, ưu tiên thuê, mua nhà ở xã hội cho người có từ hai con, và hỗ trợ tài chính khi sinh con cho một số nhóm.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `GT`; tâm lý chưa rõ; mức "giả thuyết" hoặc "có thể" |
| File ngành | Tối đa 3 trong `ind_16_giao_duc.md`, `ind_15_y_te_duoc.md`, `ind_01_bat_dong_san.md` (nhà ở xã hội), `ind_08_chan_nuoi_thuc_pham.md` (sữa trẻ em) |
| Chiều cơ hội | Có thể: vay mua nhà ở xã hội cho gia đình hai con (`CN-LN-01` `CN-LN-02`, `O1`); bảo hiểm sức khỏe, tích lũy giáo dục (`CN-INS-01` `CN-DEP-02`, `O4`) |
| Chiều rủi ro | Giả thuyết: mầm non tư nhỏ (`HKD-LN-02`) nếu mức sinh không cải thiện |
| Ưu tiên | P3 cho mọi sản phẩm (tác động trên 3 tháng) |
| Nhãn tối thiểu | `loai_tin=GT`, `muc=gia_thuyet` hoặc `co_the` |

- **Phải có:** nêu rõ chân trời nhiều năm; nêu đây không phải cảnh báo khẩn.
- **Không được:** dự báo số trẻ sinh thêm hay tỷ lệ sinh; xếp P1, P2 cho bất kỳ sản phẩm nào; ô B hoặc C.

## TC-06 Trang web giả mạo VNeID

- **Loại:** đơn lẻ, gian lận · Nguồn thật: [CafeF, 29/10/2026](https://cafef.vn/tat-ca-nguoi-dung-vneid-chu-y-thong-bao-nong-tu-cong-an-188261028133515035.chn)
- **Đầu vào:** Công an Hải Phòng cảnh báo một trang web giả mạo Hệ thống định danh điện tử VNeID nhằm đánh cắp thông tin cá nhân và chiếm đoạt tài sản.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `GL` loại mạo danh, lừa đảo; mẫu toàn hệ thống trên KHCN; kênh `L14` không áp dụng (tin trong nước) |
| Sản phẩm, ưu tiên | `CN-ACC-01` P1; `CN-DIG-01` P1; `HKD-ACC-01` P1 |
| Hành vi khuyến nghị | Cảnh báo chủ động qua app, SMS; tổng đài sẵn kịch bản; theo dõi báo lừa đảo cùng kịch bản |
| Tín hiệu kiểm tra | `X02` `X08` `S13` `S14` |
| Chiều cơ hội | Không có, hoặc chỉ nêu cảnh báo chủ động làm tăng niềm tin |
| Nhãn tối thiểu | `[FG] loai_tin=GL \| o=D \| tam_ly=chua_ro \| huong=rui_ro \| phan_khuc=KHCN,NH \| muc=co_the` |

- **Phải có:** mức nhận diện (tên loại thủ đoạn, nhóm bị nhắm); câu "chưa có số liệu báo lừa đảo nội bộ, cần truy vấn".
- **Không được:** mô tả các bước thủ đoạn, đường dẫn, giao diện trang giả; kết luận khách của ngân hàng đã bị ảnh hưởng; ép ra cơ hội kinh doanh.

## TC-07 Lỗ hổng trong thư viện Android dùng trong app ngân hàng (giả định)

- **Loại:** đơn lẻ, CVE · Nguồn: giả định
- **Đầu vào:** Một tổ chức bảo mật quốc tế công bố lỗ hổng mức nghiêm trọng trong một thư viện mã nguồn mở dùng phổ biến trong ứng dụng Android, gồm cả một số ứng dụng tài chính. Bản vá đã có; chưa ghi nhận khai thác tại Việt Nam.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `GL` loại lỗ hổng; kênh `L13` (đối tác công nghệ) |
| File ngành | `ind_17_cntt.md` (tùy chọn) |
| Sản phẩm, ưu tiên | `CN-DIG-01` P1; `HKD-DIG-01` P1; `SME-DIG-01` `CIB-DIG-01` P1 nếu dùng chung nền tảng |
| Cấp ngân hàng | `NH-OR-01`…`NH-OR-04` (rủi ro hệ thống, đối tác) |
| Hành vi khuyến nghị | Đội an ninh xác nhận app có dùng thư viện không; vá theo quy trình; chuẩn bị thông báo nếu cần |
| Tín hiệu kiểm tra | `X03` `X07` `X08` |
| Nhãn tối thiểu | `loai_tin=GL`, `phan_khuc` có `NH`, `muc=gia_thuyet` hoặc `co_the` |

- **Phải có:** câu "cần đội an ninh thông tin xác nhận ngân hàng có bị ảnh hưởng hay không"; điều kiện để rủi ro thành hiện thực (app dùng thư viện, chưa vá).
- **Không được:** mô tả cách khai thác; kết luận ngân hàng bị ảnh hưởng hoặc an toàn; nêu mã CVE do tự đoán.

## TC-08 App gián đoạn 6 giờ đúng ngày chi lương (giả định)

- **Loại:** đơn lẻ, nội bộ, mẫu toàn hệ thống · Nguồn: giả định
- **Đầu vào:** Ngày 25 hằng tháng, ứng dụng ngân hàng số dành cho cá nhân và doanh nghiệp bị gián đoạn khoảng 6 giờ, từ 9h đến 15h. Nhiều doanh nghiệp không chi lương được đúng giờ; mạng xã hội xuất hiện nhiều bài phàn nàn.

| Hạng mục | Kỳ vọng |
|---|---|
| Phân loại | `IO`; mẫu toàn hệ thống; ô C nếu có rút tiền, ô D nếu chỉ phàn nàn |
| Sản phẩm, ưu tiên | `CN-DIG-01` P1; `SME-DIG-01` `CIB-DIG-01` P1; `SME-PAY-06` `CIB-PAY-06` P1; `HKD-REV-01` P1 (không nhận được tiền) |
| Lan truyền | DN không chi lương → nhân viên chậm nhận lương (`L02`) → chi tiêu thẻ, thấu chi; khách chuyển CASA sang ngân hàng khác (`L10`) |
| Phản ứng ngân hàng | Nêu rủi ro phản ứng: truyền thông chậm, bồi hoàn không nhất quán (`inside_out/bank_response_risks.md`) |
| Tín hiệu kiểm tra | `S14` `F01` `S07`; giao dịch thất bại theo giờ |
| Bài mẫu gần nhất | `examples/ex_P3_toan_he_thong.md` |
| Nhãn tối thiểu | `[FG] loai_tin=IO \| o=D \| tam_ly=chua_ro \| huong=rui_ro \| phan_khuc=KHCN,SME,CIB,NH \| muc=co_kha_nang_cao` |

- **Phải có:** hành vi khuyến nghị (kênh dự phòng chi lương, thông báo minh bạch); what-if gián đoạn 24 giờ.
- **Không được:** đổ lỗi cho đối tác khi tin không nêu; ước lượng số khách bị ảnh hưởng.
