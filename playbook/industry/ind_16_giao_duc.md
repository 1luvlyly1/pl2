---
id: IND-16
code: I16
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về tỷ lệ sinh, chính sách giáo dục, học phí, chương trình phổ thông, quy định trường tư và trung tâm, quy định học thêm, chính sách thị thực du học của nước ngoài, tỷ giá, dịch bệnh (đóng cửa trường), AI trong giáo dục
version: v3.4
updated: 2026-11-04
---

# I16 – Giáo dục

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Giáo dục công lập chiếm phần lớn. Trường tư thục và quốc tế (mầm non, phổ thông, đại học) tăng ở đô thị. Bên cạnh là trung tâm ngoại ngữ, luyện thi, kỹ năng; dịch vụ du học (Mỹ, Úc, Canada, Anh, Nhật Bản, Hàn Quốc và các nước khác); và giáo dục số.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Hệ thống trường tư, đại học tư | Vay để xây cơ sở; doanh thu theo số học sinh tuyển được |
| SME | Trung tâm, công ty tư vấn du học, công nghệ giáo dục | Chi phí thuê mặt bằng cố định; nhạy với quy định và cạnh tranh online; tư vấn du học phụ thuộc chính sách nước ngoài |
| KHCN – hộ kinh doanh | Nhóm trẻ, mầm non tư nhỏ, lớp học thêm, trung tâm nhỏ | Nhạy với số trẻ sinh ra theo địa bàn và quy định học thêm |
| KHCN – cá nhân | Phụ huynh, giáo viên, học sinh và sinh viên du học | Phụ huynh coi giáo dục là khoản chi cuối cùng bị cắt; du học tạo dòng chuyển tiền ra nước ngoài |

**Đặc thù quan trọng với ngân hàng:** học phí thu theo kỳ nên tạo dòng tiền vào theo mùa (tựu trường, đóng học phí đầu kỳ, mùa nộp hồ sơ du học). Vì phụ huynh cắt chi giáo dục sau cùng, việc phụ huynh bắt đầu cắt học phí là tín hiệu thu nhập đã yếu rõ. Du học nhạy với tỷ giá và chính sách thị thực nước ngoài, và chạm nhu cầu ngoại tệ ở cấp ngân hàng.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Tỷ lệ sinh, số trẻ theo địa bàn | Mầm non thiếu trẻ trước, phổ thông vài năm sau | Mầm non tư nhỏ | Rất dài | Tin `GT`, xem `examples/ex_NW_02_ty_le_sinh_giam.md` |
| Thu nhập phụ huynh | Chuyển từ trường quốc tế sang tư thục rẻ hơn, giảm học thêm | Trung tâm, trường tư cao cấp | Một năm học | – |
| Chính sách thị thực, giới hạn du học sinh ở nước ngoài | Giảm du học hoặc chuyển nước | Công ty tư vấn du học | Một đến hai mùa tuyển | – |
| USD và ngoại tệ mạnh | Chi phí du học tăng | Gia đình có con du học | Ngay | – |
| Quy định học thêm, trường tư, liên kết quốc tế | Trung tâm, lớp học thêm giảm | Hộ kinh doanh, SME giáo dục | Theo hiệu lực | – |
| Dịch bệnh | Đóng cửa trường, học online; trường tư nhỏ thiếu dòng tiền | Trường tư nhỏ | Ngay | `I15` |
| AI, giáo dục số | Mô hình trung tâm truyền thống thay đổi | Trung tâm | Dài | Tin `GT` |
| Đô thị hóa, di cư | Khu đô thị mới thiếu chỗ; vùng xuất cư thừa chỗ | Trường theo vùng | Dài | `I01` |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Phụ huynh vay để đóng học phí, du học khi thu nhập giảm. Chi phí du học tăng khi ngoại tệ mạnh. Giáo viên trường tư nhỏ mất việc khi trường đóng.

**Cơ hội.** Nhu cầu chuyển tiền du học, tài khoản ngoại tệ, thẻ cho du học sinh; tích lũy giáo dục, bảo hiểm cho con; phụ huynh thu nhập cao là khách hàng ưu tiên.

### KHCN – hộ kinh doanh
**Thách thức.** Nhóm trẻ, mầm non tư nhỏ thiếu trẻ ở vùng tỷ lệ sinh giảm; lớp học thêm chịu quy định.

**Cơ hội.** Khu đô thị mới thiếu trường; nhận học phí qua QR.

### SME
**Thách thức.** Trung tâm có chi phí thuê mặt bằng cố định, nhạy với quy định và cạnh tranh online; tư vấn du học phụ thuộc chính sách nước ngoài.

**Cơ hội.** Giáo dục số, kỹ năng nghề, đào tạo cho DN; chuyển tiền du học.

### DN lớn
**Thách thức.** Trường tư vay để xây cơ sở, nhạy với số học sinh tuyển được; cạnh tranh.

**Cơ hội.** Tầng lớp trung lưu tăng, nhu cầu chất lượng cao; trường ở khu đô thị mới; thu học phí tập trung.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay tiêu dùng `CN-LN-06`, thẻ `CN-CARD-01` để đóng học phí (thu nhập phụ huynh yếu) | Chuyển tiền quốc tế `CN-PAY-01`, tài khoản ngoại tệ `CN-ACC-02` (`O3`); tích lũy `CN-DEP-02`, bảo hiểm tích lũy `CN-INS-02` (`O2` `O4`) |
| HKD | ShopCredit `HKD-LN-02` của mầm non tư nhỏ (thiếu trẻ) | QR thu học phí `HKD-REV-02`, tài khoản hộ (`O3`) |
| SME | Vay `SME-LN-01` của trung tâm | Chuyển tiền đi nước ngoài `SME-PAY-07`, thu học phí (`O3`) |
| DN lớn | Vay đầu tư cơ sở `CIB-LN-02` (số học sinh thấp hơn kế hoạch) | Thu hộ học phí `CIB-COL-01`, chi lương `CIB-PAY-06`, tiền gửi theo mùa học phí `CIB-DEP-01` (`O3` `O2`) |
| Cấp ngân hàng | Nhu cầu ngoại tệ cho du học (`NH-MR-01`); tuân thủ mục đích chuyển tiền (`NH-CO-01`) | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| Giá trị chuyển tiền du học theo mùa; số tài khoản ngoại tệ mới | Nhu cầu du học | Chưa có |
| `S02` doanh thu QR thu học phí của hộ, SME giáo dục theo địa bàn | Số học sinh | Chưa có |
| Chi giáo dục từ tài khoản cá nhân | Phụ huynh cắt hoặc duy trì học phí | Có: chi giáo dục tháng gần nhất từ CASA cá nhân |
| `S04` thẻ, thấu chi phụ huynh tăng mùa tựu trường | Phụ huynh căng tiền | Có |
| `S01` chi lương giáo viên trường tư giảm người | Trường thu hẹp | Có |

Luôn ghi "cần truy vấn dư nợ giáo dục theo loại hình, số khách chuyển tiền du học".

## 6. Liên kết ngành
- **Song song – `I01` (khu đô thị mới, đất xây trường), `I17` (giáo dục số).**
- **Theo dân số – `I15` (cùng chịu tác động già hóa), `I08` (sữa trẻ em).**
- **Theo thu nhập – việc làm ở mọi ngành.**

## 7. Điểm đảo chiều và lưu ý
- Tin tỷ lệ sinh là `GT`: không cảnh báo khẩn, không ước lượng số trường bị ảnh hưởng.
- Chi tiêu giáo dục bị cắt sau cùng; khi phụ huynh bắt đầu cắt học phí, đó là tín hiệu thu nhập đã yếu rõ.
- Chính sách thị thực nước ngoài có thể đổi nhanh; chỉ nêu khi tin nêu.
