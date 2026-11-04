# Định dạng dòng nhãn [FG] và cách đọc

Phiên bản v3.0 · 02/11/2026 · Dành cho đội kỹ thuật. Phía agent, định dạng được quy định ở `playbook/core/05_output_prose.md`.

## 1. Định dạng
Mỗi kết luận của agent kết thúc bằng 1–3 dòng, mỗi dòng một nhánh chính:

```
[FG] loai_tin=TT | o=B | tam_ly=tham | huong=co_hoi | phan_khuc=KHCN,CIB | muc=co_kha_nang_cao
```

| Trường | Giá trị hợp lệ | Ý nghĩa |
|---|---|---|
| `loai_tin` | `TT` `GT` `GL` `IO` | Nhóm tin của nhánh: trực tiếp, gián tiếp, gian lận/an ninh mạng, sự kiện inside-out |
| `o` | `A` `B` `C` `D`, hoặc hai ô `A,B` | Ô ma trận của nhánh |
| `tam_ly` | `so` `binh_thuong` `tham` `chua_ro` | Tâm lý khách hàng theo sự kiện |
| `huong` | `rui_ro` `co_hoi` `ca_hai` | Lăng kính của nhánh |
| `phan_khuc` | `KHCN` `SME` `CIB` `NH`, nối bằng dấu phẩy | Phân khúc của nhánh; `KHCN` gồm cả hộ kinh doanh; `NH` là cấp ngân hàng |
| `muc` | `co_kha_nang_cao` `co_the` `gia_thuyet` | Mức chắc chắn |

**Thay đổi so với v2.1:** thêm `loai_tin` ở đầu; bỏ `HKD` (gộp vào `KHCN`) và `NDT`; thêm `NH`.

## 2. Biểu thức kiểm tra
```
^\[FG\] loai_tin=(TT|GT|GL|IO) \| o=[ABCD](,[ABCD])? \| tam_ly=(so|binh_thuong|tham|chua_ro) \| huong=(rui_ro|co_hoi|ca_hai) \| phan_khuc=(KHCN|SME|CIB|NH)(,(KHCN|SME|CIB|NH))* \| muc=(co_kha_nang_cao|co_the|gia_thuyet)$
```

## 3. Quy tắc đọc
- Chỉ đọc các dòng bắt đầu bằng `[FG]` ở **cuối** output.
- Dòng sai định dạng: ghi log và **bỏ**, không đoán sửa. Theo dõi tỷ lệ dòng sai để chỉnh prompt.
- Quá 3 dòng: chỉ lấy 3 dòng đầu, ghi log.
- Không có dòng nào: sự kiện không được tính vào chỉ số tin tức.
- Cùng một sự kiện chạy lại nhiều lần: chỉ giữ lần mới nhất theo `event_id`.
- `NH` không phải phân khúc khách hàng: **không** tính vào chỉ số tin tức của KHCN, SME, CIB; chỉ tính vào chỉ số toàn hàng và thống kê theo nhóm tin.

## 4. Bảng lưu trữ gợi ý
Tách mỗi phân khúc thành một dòng riêng.

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `event_id` | text | Mã sự kiện do người dùng sàng lọc |
| `run_at` | timestamp | Thời điểm agent chạy |
| `branch_no` | int | Thứ tự dòng nhãn (1–3) |
| `loai_tin` | text | `TT`, `GT`, `GL`, `IO` |
| `o` | text | `A`, `B`, `C`, `D` hoặc `A,B` |
| `tam_ly` | text | |
| `huong` | text | |
| `phan_khuc` | text | Một giá trị mỗi dòng |
| `muc` | text | |
| `prose_ref` | text | Đường dẫn tới bài văn gốc |

## 5. Mã mẫu (Python)
```python
import re

SEG = r"(?:KHCN|SME|CIB|NH)"
FG = re.compile(
    r"^\[FG\] loai_tin=(?P<lt>TT|GT|GL|IO) \| o=(?P<o>[ABCD](?:,[ABCD])?) "
    r"\| tam_ly=(?P<tam_ly>so|binh_thuong|tham|chua_ro) "
    r"\| huong=(?P<huong>rui_ro|co_hoi|ca_hai) "
    r"\| phan_khuc=(?P<pk>" + SEG + r"(?:," + SEG + r")*) "
    r"\| muc=(?P<muc>co_kha_nang_cao|co_the|gia_thuyet)$"
)
O_SCORE = {"A": 1, "B": 2, "C": -2, "D": -1}
WEIGHT = {"co_kha_nang_cao": 1.0, "co_the": 0.6, "gia_thuyet": 0.3}


def parse_tags(output: str):
    """Trả về danh sách nhánh hợp lệ (mỗi phân khúc một dòng) và danh sách dòng lỗi."""
    rows, errors = [], []
    tail = [l.strip() for l in output.strip().splitlines()][-8:]
    tags = [l for l in tail if l.startswith("[FG]")][:3]
    for i, line in enumerate(tags, 1):
        m = FG.match(line)
        if not m:
            errors.append(line)
            continue
        cells = m["o"].split(",")
        score = sum(O_SCORE[c] for c in cells) / len(cells)
        for pk in m["pk"].split(","):
            rows.append({"branch_no": i, "loai_tin": m["lt"], "o": m["o"], "tam_ly": m["tam_ly"],
                         "huong": m["huong"], "phan_khuc": pk, "muc": m["muc"],
                         "score": score, "weight": WEIGHT[m["muc"]]})
    return rows, errors


def news_index(rows):
    """rows: các nhánh trong 30 ngày của một phân khúc (hoặc toàn hàng). Trả về 0–100 hoặc None."""
    w = sum(r["weight"] for r in rows)
    if w == 0:
        return None
    avg = sum(r["score"] * r["weight"] for r in rows) / w
    return max(0, min(100, round(50 + 25 * avg)))
```
