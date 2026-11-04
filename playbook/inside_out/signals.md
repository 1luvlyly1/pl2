---
id: IO-SIGNALS
used_by: [Inside-out Monitor, Product-Impact]
steps: [4]
depends_on: [core/03_linkage_graph.md]
load_when: Liệt kê tín hiệu nội bộ (S01–S16) cần truy vấn để xác nhận/bác bỏ giả thuyết
version: v3.4
updated: 2026-11-04
---

# Inside-out: thư viện tín hiệu nội bộ

| ID | Tín hiệu | Nguồn dữ liệu | Báo trước điều gì | Phân khúc | Đo được bằng danh mục what-if |
|---|---|---|---|---|---|
| `S01` | Lô chi lương trễ / giảm tổng quỹ / giảm số người | Thanh toán lương | DN căng dòng tiền; nhân viên sắp giảm thu nhập | SME, CIB → KHCN | Có |
| `S02` | Doanh thu QR/Soundbox/POS giảm theo địa bàn, MCC | Quản lý doanh thu HKD/SME | Sức mua địa phương giảm | KHCN – hộ kinh doanh, SME | Chưa có (thay thế bằng dòng vào DN) |
| `S03` | Unique payers giảm | Giao dịch nhận tiền | Mất khách | KHCN – hộ kinh doanh | Chưa có |
| `S04` | Sử dụng hạn mức MyCash/thẻ/ShopCash tăng nhanh | Hệ thống thẻ/thấu chi | Căng thẳng thanh khoản cá nhân/hộ | KHCN, HKD | Có |
| `S05` | Chuyển từ trả toàn bộ sang trả tối thiểu thẻ tín dụng | Hệ thống thẻ | Sắp DPD | KHCN | Có |
| `S06` | Tất toán tiết kiệm trước hạn, vay cầm cố tiền gửi tăng | Core banking | Cần tiền gấp | KHCN, SME | Có (phần tất toán) |
| `S07` | Rút tiền mặt CDM tăng đột biến | CDM | Hoảng loạn/tin đồn | Tất cả | Chưa có |
| `S08` | Bán lại iBond/rút iFund theo một tổ chức phát hành/ngành | Hệ thống đầu tư | Mất niềm tin vào issuer/ngành | KHCN Priority | Gần đúng |
| `S09` | Hủy bảo hiểm sớm, ngừng đóng phí | Đối tác bảo hiểm | Thu nhập giảm hoặc khủng hoảng niềm tin | KHCN | Gần đúng |
| `S10` | Nộp NSNN trễ, hóa đơn điện/cảng giảm | Thanh toán | Sản xuất/xuất khẩu giảm | SME, CIB | Chưa có |
| `S11` | Spoke SCF cùng anchor đồng loạt chậm trả | Tài trợ chuỗi cung ứng | Anchor gặp vấn đề | CIB → SME, hộ kinh doanh | Chưa có |
| `S12` | Chủ DN rút tiết kiệm cá nhân & DN tăng sử dụng hạn mức cùng lúc | Liên kết CIF (`L01`) | Chủ đang bơm tiền cứu DN | SME, CIB ↔ KHCN | Chưa có |
| `S13` | Đăng nhập lạ, đổi thiết bị, người thụ hưởng mới giá trị lớn | Ngân hàng số | Lừa đảo/chiếm đoạt | Tất cả | Chưa có |
| `S14` | Khiếu nại tăng theo chủ đề | CRM, tổng đài | Rủi ro danh tiếng | Tất cả | Chưa có |
| `S15` | Giá trị thị trường âm lớn trên vị thế FX/phái sinh của khách | Treasury | Rủi ro đối tác | CIB | Chưa có |
| `S16` | Doanh thu HKD chảy về TK cá nhân thay vì TK HKD | Giao dịch | Né thuế / rủi ro AML | KHCN – hộ kinh doanh | Chưa có |

Cột "Đo được": cột cụ thể và cách đọc ở `core/whatif_chung/wc_02_signal_map.md`. Tín hiệu "Chưa có" vẫn được nêu trong bài playbook như việc cần truy vấn, nhưng what-if phải ghi `GAP`. Khi một tín hiệu đo được đang xấu đi và cần dự phóng, dùng `inside_out/whatif/io_wi_00_index.md` (bài mẫu `io_wi_ex_01_tra_toi_thieu_the.md`).
