# Bộ test case playbook – mục lục và cách chấm

Phiên bản v3.2 · 04/11/2026 · 20 test case

> **Agent KHÔNG nạp thư mục này.** Test case chứa đáp án kỳ vọng; nạp vào agent sẽ làm lộ đáp án. Bài mẫu few-shot cho agent vẫn nằm ở `playbook/examples/`.

## 1. Mục đích
Kiểm tra hệ thống multi-agent chạy đúng playbook sau mỗi lần sửa playbook hoặc đổi mô hình:
- xếp đúng nhóm tin, mẫu lan truyền, ô A–D;
- chọn đúng file ngành, sản phẩm và mức ưu tiên P1–P3 theo bảng (c) của file phân khúc;
- suy luận nhiều bước với mức chắc chắn giảm dần theo số bước;
- với chuỗi tin: gom cụm đúng khóa, đúng ngày mở, không mở cụm khi chỉ có một nguyên nhân;
- giữ ràng buộc an toàn (không bịa số, tin `GL` chỉ ở mức nhận diện, không đề xuất siết đồng loạt).

## 2. Danh sách

| Mã | Tên | Loại | Nhóm tin | Nguồn | File |
|---|---|---|---|---|---|
| TC-01 | Thuế 208,88% với gỗ dán | Đơn lẻ, DN trước | TT | Thật 19/06/2026 | `tc_01_don_le.md` |
| TC-02 | Lãi suất huy động bình quân lên 6,46% | Đơn lẻ, toàn hệ thống | TT | Thật 09/10/2026 | `tc_01_don_le.md` |
| TC-03 | Giá vàng lập đỉnh, xếp hàng mua | Đơn lẻ, ô B | TT | Giả định | `tc_01_don_le.md` |
| TC-04 | Tin đồn thanh khoản ngân hàng khác | Đơn lẻ, ô C | TT | Giả định | `tc_01_don_le.md` |
| TC-05 | Luật Dân số có hiệu lực | Đơn lẻ, dài hạn | GT | Thật, hiệu lực 01/07/2026 | `tc_02_GT_GL_IO.md` |
| TC-06 | Trang web giả mạo VNeID | Đơn lẻ, gian lận | GL | Thật 29/10/2026 | `tc_02_GT_GL_IO.md` |
| TC-07 | Lỗ hổng thư viện Android dùng trong app ngân hàng | Đơn lẻ, CVE | GL | Giả định | `tc_02_GT_GL_IO.md` |
| TC-08 | App gián đoạn 6 giờ đúng ngày chi lương | Đơn lẻ, nội bộ | IO | Giả định | `tc_02_GT_GL_IO.md` |
| TC-09 | Eo biển Hormuz gần như đóng | Đa bước, nhiều ngành | TT | Thật 02/03/2026 | `tc_03_da_buoc_a.md` |
| TC-10 | Thuế bổ sung Mục 301 mức 12,5% | Đa bước, giới hạn 3 file ngành | TT | Thật, hiệu lực 24/07/2026 | `tc_03_da_buoc_a.md` |
| TC-11 | Dịch tả lợn châu Phi ở Đắk Lắk | Đa bước, hai chiều | TT | Thật 18/07/2026 | `tc_03_da_buoc_a.md` |
| TC-12 | Chủ tịch tập đoàn BĐS bị khởi tố | Đa bước, cá nhân trước, 4 bước | TT | Giả định | `tc_04_da_buoc_b.md` |
| TC-13 | Nhà máy điện tử FDI cắt 30% lao động | Đa bước, KCN | TT | Giả định | `tc_04_da_buoc_b.md` |
| TC-14 | Bão số 4 ở Bắc Ninh, Lạng Sơn, Quảng Ninh | Đa bước, thiên tai | TT | Thật 22/08/2026 | `tc_04_da_buoc_b.md` |
| TC-15 | Gỗ xuất khẩu sang Mỹ | Lăn cầu tuyết, nhiều nguyên nhân | TT | Thật 06–08/2026 | `tc_05_lan_cau_tuyet_a.md` |
| TC-16 | Nông hộ Tây Nguyên | Lăn cầu tuyết, khác ngành cùng nhóm | TT | Thật 07–08/2026 | `tc_05_lan_cau_tuyet_a.md` |
| TC-17 | Hàng không, du lịch bay xa | Lăn cầu tuyết, một gốc nhiều kênh | TT | Thật 03–06/2026 | `tc_05_lan_cau_tuyet_a.md` |
| TC-18 | Hộ kinh doanh mặt phố | Lăn cầu tuyết theo lớp | TT | Thật 12/2025–11/2026 | `tc_06_lan_cau_tuyet_b.md` |
| TC-19 | Lừa đảo nhắm vào người trẻ | Lăn cầu tuyết, tin gian lận | GL | Thật 10–11/2026 | `tc_06_lan_cau_tuyet_b.md` |
| TC-20 | Người vay mua nhà | Phản ví dụ: một nguyên nhân | TT | Thật 06–08/2026 | `tc_06_lan_cau_tuyet_b.md` |

## 3. Cách chạy
1. **Tin đơn lẻ, đa bước (TC-01 đến TC-14):** dán phần "Đầu vào" làm sự kiện, chạy quy trình 6 bước như vận hành thật.
2. **Lăn cầu tuyết (TC-15 đến TC-20):** chạy từng tin theo thứ tự ngày; sau đó chạy bộ gom cụm (theo FSD gom cụm tín hiệu) với tham số mặc định; cuối cùng chạy agent cụm trên hồ sơ cụm nếu cụm mở.
3. Lưu bài văn xuôi, các dòng nhãn và ghi chú của từng agent để chấm.

## 4. Cách chấm
Mỗi test case có ba phần chấm:

| Phần | Cách chấm | Trọng số |
|---|---|---|
| **Kỳ vọng chính** (bảng "Kỳ vọng") | Mỗi dòng đạt / không đạt. Chấp nhận cách diễn đạt khác nếu đúng ý | 60% |
| **Phải có** | Mỗi ý thiếu trừ điểm tương ứng | 25% |
| **Không được** | Vi phạm bất kỳ ý nào → test case **trượt**, bất kể điểm khác | Điều kiện loại |

- Đạt test case: ≥ 80% điểm và không vi phạm mục "Không được".
- Đạt bộ test: ≥ 17/20 test case đạt, và **mọi** test case tin `GL` (TC-06, TC-07, TC-19) đạt.
- Dòng nhãn `[FG]` phải khớp biểu thức kiểm tra trong `index_spec/fg_tag_format.md`; giá trị ô và mức chắc chắn được phép lệch một bậc nếu bài viết giải thích hợp lý.
- Với lăn cầu tuyết: ngày mở cụm phải **đúng ngày**; khóa cụm phải chứa đủ các tiêu chí ghi trong kỳ vọng.

## 5. Ghi chú
- Ca "thật" dùng tin đã kiểm tra ngày đăng; nội dung "Đầu vào" là tóm tắt bài, không phải trích nguyên văn.
- Mức ưu tiên lấy theo bảng (c) trong `playbook/segments/`. Khi bảng (c) đổi, cập nhật lại cột ưu tiên ở các test case liên quan.
- Ca lăn cầu tuyết dùng dòng `[EXP]` và `[CUM]` theo FSD gom cụm; hai dòng này sẽ có hiệu lực khi module gom cụm được đưa vào playbook.
