# Playbook Rủi ro & Cơ hội (Fear & Greed) – Techcombank

Phiên bản **v3.4** · Cập nhật 04/11/2026 · Danh mục sản phẩm chốt 26/10/2026 từ techcombank.com

Bộ tài liệu cho hệ thống multi-agent đọc sự kiện (đã được người dùng sàng lọc) và suy luận rủi ro, cơ hội lan tới từng nhóm khách hàng, sản phẩm và chính ngân hàng.

- **3 phân khúc:** KHCN (gồm nhóm cá nhân và nhóm hộ kinh doanh), SME, doanh nghiệp lớn (mã `CIB`).
- **Cấp ngân hàng:** tác động chạm thẳng vào hoạt động của ngân hàng (thanh khoản, tỷ giá, hệ thống, lỗ hổng CVE, gian lận, tuân thủ, danh tiếng, nhà đầu tư).
- **3 nhóm tin outside-in**, mỗi nhóm một cách suy luận:
  - `TT` – tác động trực tiếp: xung đột làm giá vàng, dầu tăng; giá hàng hóa; tỷ giá; lãi suất; thương mại; chính sách.
  - `GT` – tác động gián tiếp: tỷ lệ sinh, già hóa, đại dịch, khí hậu, đô thị hóa, công nghệ.
  - `GL` – gian lận, lừa đảo, an ninh mạng: thủ đoạn ở nước khác, làn sóng lừa đảo, lỗ hổng CVE, rò rỉ dữ liệu.
- **What-if có SQL** (mới ở v3.3): agent What-if (Opus) biến rủi ro đã suy luận thành kịch bản có số đo và SQL Databricks; biến số chỉ lấy từ danh mục feature của ngân hàng, thiếu thì khai báo `GAP`.
- **18 ngành Việt Nam** (mới ở v3.1): từ biến số bên ngoài (giá dầu, vàng, tỷ giá, thuế quan, thời tiết, dịch bệnh, chính sách…) tra ra ngành nào thiệt, ngành nào lợi; mỗi ngành một file mô tả thách thức và cơ hội cho cá nhân, hộ kinh doanh, SME, DN lớn.

## 1. Cấu trúc thư mục và ai dùng

```
(thư mục giải nén)
├── README.md                     ← file này
│
├── playbook/                     ← AGENT ĐỌC. Nạp vào kho tri thức / prompt của hệ thống
│   ├── 00_INDEX.md               ← agent luôn đọc đầu tiên; chỉ dẫn đọc file nào tiếp theo
│   ├── guardrails.md             ← 21 ràng buộc bắt buộc (quy tắc, lý do, cách áp dụng)
│   ├── core/                     ← nền tảng dùng chung
│   │   ├── 01…05                 ← mã rủi ro, khái niệm, 14 kênh liên kết, quy trình 6 bước, mẫu văn xuôi + nhãn [FG]
│   │   ├── 06_ngan_hang.md       ← cấp ngân hàng (NH-, IR-)
│   │   └── whatif_chung/         ← what-if dùng chung: quy tắc, danh mục feature (md + csv), ánh xạ tín hiệu → cột, công thức, quy ước SQL, khuôn đầu ra [WI]
│   ├── outside_in/               ← rủi ro từ bên ngoài
│   │   ├── news/                 ← bộ định tuyến tin và 3 file cho tin TT, GT, GL
│   │   └── whatif/               ← what-if cho rủi ro từ tin + examples/ (6 bài có SQL)
│   ├── inside_out/               ← rủi ro từ bên trong ngân hàng
│   │   ├── signals.md, bank_response_risks.md
│   │   └── whatif/               ← what-if cho sự kiện nội bộ + examples/ (4 bài có SQL)
│   ├── fear_greed/               ← hai lăng kính rủi ro/cơ hội, ma trận ô A–D, tín hiệu F/G, cơ hội O1–O6
│   ├── industry/                 ← ind_00_index (biến số → ngành, kèm cơ chế) + 18 file ngành ind_01…ind_18
│   ├── segments/                 ← KHCN (2 file: cá nhân, hộ kinh doanh), SME, doanh nghiệp lớn
│   └── examples/                 ← 10 bài mẫu văn xuôi có dòng nhãn [FG]
│
├── tests/                        ← 20 test case có đáp án kỳ vọng. Agent KHÔNG nạp
│
├── index_spec/                   ← ĐỘI DỮ LIỆU / KỸ THUẬT ĐỌC. Agent KHÔNG nạp
│   ├── fg_index_spec.md          ← cách tính chỉ số hành vi, dòng tiền thực, tin tức
│   ├── fg_tag_format.md          ← định dạng dòng nhãn [FG], biểu thức kiểm tra, mã Python đọc nhãn
│   ├── sample_data.json          ← dữ liệu mẫu đúng cấu trúc dashboard cần
│   ├── validate_whatif_sql.py    ← kiểm SQL what-if theo danh mục feature
│   └── spark_check_whatif_sql.py ← chạy thử SQL what-if trên Spark cục bộ với bảng dựng từ danh mục
│
└── tham_khao/                    ← NGƯỜI XEM
    ├── luong_chay_playbook.html          ← luồng chạy (bản v3.0)
    ├── dashboard_fear_greed_mau.html     ← dashboard chỉ số Fear & Greed (dữ liệu mẫu)
    ├── ban_do_co_hoi_outside_in.html     ← minh họa chiều cơ hội (bản v2)
    └── FSD_gom_cum_tin_hieu_outside_in.md ← FSD gom cụm tín hiệu theo thời gian, suy luận nhiều bước
```

**Vì sao tách `index_spec/` ra ngoài `playbook/`:** agent chỉ cần viết dòng nhãn đúng định dạng (đã có trong `playbook/core/05_output_prose.md`). Công thức tính chỉ số là việc của code; để chung, agent có thể nạp nhầm và tự chấm điểm.

## 2. Triển khai từng bước

### Bước 1 – Đưa playbook vào hệ thống agent
- Chép nguyên thư mục `playbook/`, **giữ nguyên cấu trúc thư mục con**: các file tham chiếu nhau bằng đường dẫn tương đối.
- Không gộp các file; mỗi file giữ quanh 12 KB để agent đọc được.

### Bước 2 – Cấu hình từng agent
Theo `playbook/00_INDEX.md` mục 3. Tóm tắt:

| Agent | Luôn nạp | Nạp thêm khi cần |
|---|---|---|
| Orchestrator | `00_INDEX.md`, `core/04`, `guardrails.md`, `outside_in/news/nw_00_router.md` | – |
| Propagation | `core/02`, `core/03`, `fear_greed/fg_01`, `outside_in/news/nw_00_router.md` | **Một** file nhóm tin, file phân khúc, `industry/ind_00_index.md` + **tối đa 3** file ngành, 1 bài mẫu |
| Product-Impact | `core/01`, `fear_greed/fg_03` | Tối đa 3 file phân khúc; `core/06_ngan_hang.md` khi chạm cấp ngân hàng; mục 4 file ngành |
| Inside-out Monitor | `inside_out/signals.md`, `fear_greed/fg_02`, `inside_out/bank_response_risks.md` | Cột hành vi khuyến nghị trong bảng (c) file phân khúc; tín hiệu `X01`–`X08` với tin `GL`; mục 5 file ngành |
| Critic | `guardrails.md`, `core/05`, `fear_greed/fg_01` | 1 bài mẫu, ghi chú các agent trước |
| What-if (Opus), chạy sau Critic | `guardrails.md`, `core/whatif_chung/wc_00`…`wc_05` | `outside_in/whatif/oi_wi_00_index.md` (rủi ro từ tin) hoặc `inside_out/whatif/io_wi_00_index.md` (sự kiện nội bộ); `wc_01b` khi chạm SME, CIB; 1 bài mẫu của cửa vào đó |

### Bước 3 – Đầu vào và đầu ra
- **Đầu vào:** nội dung một sự kiện đã sàng lọc. Agent xếp tin vào `TT` / `GT` / `GL` chỉ để chọn cách suy luận, không để loại tin.
- **Đầu ra:** một bài văn xuôi 350–650 từ (7 đoạn, có cả rủi ro và cơ hội), kết thúc bằng 1–3 dòng nhãn, ví dụ:
  ```
  [FG] loai_tin=TT | o=D | tam_ly=chua_ro | huong=rui_ro | phan_khuc=CIB,SME,KHCN,NH | muc=co_kha_nang_cao
  ```

### Bước 4 – Lưu dòng nhãn
- Dùng biểu thức và mã mẫu trong `index_spec/fg_tag_format.md`.
- Dòng sai định dạng: ghi log và bỏ, không đoán sửa.
- `NH` (cấp ngân hàng) không tính vào chỉ số của KHCN, SME, CIB; chỉ tính vào chỉ số toàn hàng.

### Bước 5 – Tính chỉ số (khi đã có dữ liệu)
- Làm theo `index_spec/fg_index_spec.md`: chỉ số hành vi (7 thành phần), dòng tiền thực (4 thành phần), tin tức (từ dòng nhãn).
- Cần ít nhất 12 tháng lịch sử cho hai chỉ số đầu.

### Bước 6 – Đưa chỉ số hành vi vào agent làm bối cảnh (không bắt buộc)
- Orchestrator thêm một dòng kèm sự kiện: `Bối cảnh: chỉ số hành vi KHCN = 78 (Tham lam cực độ)`.
- **Không bao giờ** truyền chỉ số tin tức vào agent.

### Bước 7 – What-if và SQL
- Đầu vào agent What-if: bài văn xuôi + dòng `[FG]` (và `[CUM]` nếu có) với rủi ro từ tin, hoặc mô tả sự kiện nội bộ. Đầu ra: file markdown 8 phần theo `playbook/core/whatif_chung/wc_05_dau_ra.md`, gồm truy vấn khám phá, truy vấn chính và dòng nhãn `[WI]` (trường `cua=OI` hoặc `cua=IO`).
- Trước khi chạy trên Databricks:
  ```
  python3 index_spec/validate_whatif_sql.py --catalog playbook/core/whatif_chung/feature_catalog.csv output.md
  pip install pyspark   # cần Java 17+
  python3 index_spec/spark_check_whatif_sql.py --smoke --catalog playbook/core/whatif_chung/feature_catalog.csv output.md
  ```
- Chạy truy vấn khám phá trước, điền giá trị mã vào tham số (`:province_list`, `:gso_list`…), rồi chạy truy vấn chính. Tham số ghi "giả định" cần người phụ trách rủi ro duyệt.
- Danh mục feature đổi: sửa `playbook/core/whatif_chung/feature_catalog.csv`, sinh lại `wc_01a`/`wc_01b`, chạy lại hai script trên mọi bài mẫu.

### Bước 8 – Hiển thị
- Mở `tham_khao/dashboard_fear_greed_mau.html` bằng trình duyệt. Dữ liệu nằm trong khối `<script type="application/json" id="data">` cuối file; thay bằng nội dung `sample_data.json` hoặc output thật.

## 3. Lưu ý
- Mọi ví dụ và số liệu mẫu là **giả định**, không phản ánh dữ liệu hay khách hàng thực.
- File ngành là **kiến thức nền định tính**: không có số liệu, không có tên công ty. Mức phơi nhiễm của Techcombank theo ngành luôn cần truy vấn nội bộ. Khi chính sách thay đổi, cập nhật mục 2 và mục 7 của file ngành.
- Mã ngành `I01`–`I18` chỉ dùng giữa các agent, không đưa vào dòng nhãn `[FG]` (định dạng nhãn không đổi so với v3.0).
- Với tin `GL`, agent chỉ mô tả ở mức nhận diện, không mô tả cách khai thác hay thủ đoạn chi tiết, và không kết luận hệ thống ngân hàng bị ảnh hưởng hay an toàn khi chưa có xác nhận của đội an ninh thông tin.
- Chỉ số Fear & Greed là chỉ số nội bộ để đọc tâm lý khách hàng, **không phải dự báo thị trường**.
- Trang HTML cần mạng để tải font; khi offline vẫn hiển thị đúng tiếng Việt.

## 4. Lịch sử phiên bản
| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| v1.2 | 26/10/2026 | Playbook rủi ro, đầu ra văn xuôi, bỏ sàng lọc sự kiện |
| v2.0 | 02/11/2026 | Hai lăng kính Fear & Greed, ma trận ô A–D, tín hiệu F/G, bản đồ cơ hội |
| v2.1 | 02/11/2026 | Dòng nhãn `[FG]`, bối cảnh chỉ số hành vi, `index_spec/`, dashboard mẫu |
| v3.0 | 02/11/2026 | 3 phân khúc (KHCN gồm hộ kinh doanh, SME, DN lớn) + cấp ngân hàng; module tin `news/` với nhóm `TT`, `GT`, `GL`; kênh `L13` `L14`; tín hiệu `X01`–`X08`; nhãn thêm `loai_tin`; 4 bài mẫu mới |
| v3.1 | 03/11/2026 | Module ngành `industry/`: file định tuyến biến số → ngành và 18 file ngành Việt Nam (`I01`–`I18`); nối vào `00_INDEX` (mục 4d), `core/04`, `outside_in/news/nw_01`, `outside_in/news/nw_02`. Trang luồng chạy giữ nguyên bản v3.0 |
| v3.4 | 04/11/2026 | Sắp xếp lại thư mục: `bank/` → `core/06_ngan_hang.md`; `news/` → `outside_in/news/`; what-if tách `core/whatif_chung/` (dùng chung), `outside_in/whatif/` và `inside_out/whatif/` (mỗi phần có examples); 4 bài mẫu what-if inside-out mới. Viết lại guardrails (21 ràng buộc), core 01–06 và 19 file ngành thành câu mô tả cơ chế thay cho từ khóa |
| v3.3 | 04/11/2026 | Module `whatif/`: danh mục 260 cột từ file feature của ngân hàng, ánh xạ tín hiệu → cột (`GAP` khi thiếu), phương pháp kịch bản, quy ước SQL Databricks, khuôn đầu ra và nhãn `[WI]`; 6 bài mẫu `outside_in/whatif/examples/`; 2 script kiểm tra SQL trong `index_spec/` |
| v3.2 | 04/11/2026 | Bảng (c) 4 file phân khúc: keyword theo ưu tiên P1–P3, cột hành vi khuyến nghị (con người, what-if, stress test); bỏ mục (d); mục (e) thành bảng hướng lan; thư mục `tests/` với 20 test case; FSD gom cụm trong `tham_khao/` |

**Chạy test:** xem `tests/tc_00_index.md`. Không nạp `tests/` vào agent: test case chứa đáp án kỳ vọng.

**Đổi đường dẫn ở v3.4:** `bank/ngan_hang.md` → `core/06_ngan_hang.md`; `news/nw_*.md` → `outside_in/news/nw_*.md`; `whatif/wi_0*` → `core/whatif_chung/wc_0*`; `examples/whatif/wi_ex_*` → `outside_in/whatif/examples/oi_wi_ex_*`. Mã sản phẩm, mã tín hiệu, định dạng nhãn `[FG]` không đổi.

**Đổi tên file so với v2.1:** `seg_01_KHCN` → `seg_01a_KHCN_ca_nhan`; `seg_02_HKD` → `seg_01b_KHCN_ho_kinh_doanh`; `seg_03_SME` → `seg_02_SME`; `seg_04_CIB` → `seg_03_DN_lon`; `seg_05_NDT` → bỏ, nội dung chuyển vào `core/06_ngan_hang.md`. Mã sản phẩm (`CN-`, `HKD-`, `SME-`, `CIB-`, `IR-`) giữ nguyên.
