---
id: WC-05-DAU-RA
used_by: [What-if, Critic]
steps: [whatif-6]
depends_on: [core/whatif_chung/wc_00_quy_tac.md]
load_when: Luôn nạp khi viết đầu ra what-if, cho cả cửa outside-in và inside-out
version: v3.4
updated: 2026-11-04
---

# Khuôn đầu ra what-if

Đầu ra là một file markdown cho mỗi rủi ro được chọn, gồm 8 phần theo thứ tự. Văn xuôi ngắn ở phần 1 và 7; các phần còn lại dạng bảng hoặc khối SQL.

## 1. Rủi ro gốc
2–3 câu. Cửa outside-in: rủi ro nào từ bài playbook (dẫn mã sản phẩm, mức **P**, mức chắc chắn) và vì sao đáng đo. Cửa inside-out: sự kiện nội bộ là gì (tín hiệu đang xấu đi, quyết định ngân hàng đang cân nhắc, sự cố), ai bị chạm và câu hỏi mà người ra quyết định cần trả lời.

## 2. Kịch bản
| Mục | Nội dung |
|---|---|
| Quần thể | Bộ lọc bằng lời + cột dùng |
| Cú sốc | Biến nào đổi; tham số |
| Công thức | Viết bằng ký hiệu (mẫu ở `wc_03` mục 4) |
| Mức độ | Cơ sở, vừa, nặng (± ngược) |
| Biến kết quả | Cột đo hậu quả |

## 3. Biến số
| Biến | Bảng.cột | Cờ | Vai trò | Ghi chú |
|---|---|---|---|---|

Mỗi dòng một cột danh mục. Cờ lấy từ `wc_01a`/`wc_01b` (`F` `?` `A`).

## 4. Tham số
| Tham số | Giá trị vừa | Giá trị nặng | Nguồn |
|---|---|---|---|

Nguồn: `tin dd/mm/yyyy` kèm câu trích ngắn, hoặc `giả định: lý do`.

## 5. Thiếu dữ liệu và cần xác nhận
- `GAP` – tín hiệu playbook không đo được, cột đề xuất bổ sung.
- Cần xác nhận – cột cờ `?`/`A`, giả định nối khóa, ý nghĩa mã.

## 6. SQL
Khối SQL thứ nhất: truy vấn khám phá. Khối SQL thứ hai: truy vấn chính. Đầu khối chính là chú thích tham số (`wc_04` mục 4).

## 7. Cách đọc kết quả và hành động
- Kết quả trông thế nào thì nghĩa là gì (ví dụ "nhóm có tỷ lệ DSR > `:dsr_limit` tăng mạnh nhất ở mức vừa → ưu tiên RM"). Không đoán con số.
- Nối lại với cột "Hành vi khuyến nghị khi xảy ra" của file phân khúc.

## 8. Dòng nhãn
Kết thúc bằng một dòng `[WI]` cho mỗi kịch bản:
```
[WI] cua=<OI|IO> | rui_ro=<mã sản phẩm> | kich_ban=<tên_ngắn> | quan_the=<mô tả lọc> | soc=<tham số=giá trị vừa/nặng> | cong_thuc=<mẫu> | bang=<bảng chính> | gap=<mã tín hiệu thiếu hoặc none> | xac_nhan=<số mục cần xác nhận> | muc=<co_kha_nang_cao|co_the|gia_thuyet>
```

| Trường | Ý nghĩa |
|---|---|
| `cua` | `OI` rủi ro từ tin bên ngoài; `IO` rủi ro từ bên trong ngân hàng |
| `rui_ro` | Mã sản phẩm hoặc năng lực ngân hàng (`NH-`) bị đo, cách nhau bằng dấu phẩy |
| `soc` | Tên tham số và giá trị mức vừa/mức nặng; kịch bản chỉ đo quy mô thì ghi `none` |
| `gap` | Mã tín hiệu hoặc thông tin chưa có dữ liệu; đủ dữ liệu thì ghi `none` |
| `xac_nhan` | Số mục trong phần "Cần xác nhận" |
| `muc` | Mức chắc chắn, không cao hơn mức của nhận định playbook tương ứng |
