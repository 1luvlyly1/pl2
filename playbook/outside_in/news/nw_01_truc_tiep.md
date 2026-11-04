---
id: NEWS-DIRECT
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [1, 2, 3, 4]
depends_on: [outside_in/news/nw_00_router.md, core/03_linkage_graph.md, fear_greed/fg_03_opportunity_map.md]
load_when: Tin nhóm TT – giá hàng hóa, vàng, năng lượng, tỷ giá, lãi suất, thương mại, vận tải, trừng phạt, chính sách trong nước, xung đột quân sự
version: v3.1
updated: 2026-11-03
---

# Tin tác động trực tiếp (TT)

## 1. Nguyên tắc: xếp khách theo vai trò trong chuỗi giá trị
Khi một mặt hàng hoặc biến số (giá vàng, giá dầu, tỷ giá) thay đổi, **cùng một tin có lợi cho vai trò này và hại cho vai trò khác**. Trước khi tra sản phẩm, xếp khách hàng vào 5 vai trò:

| Vai trò | Khi giá **tăng** | Khi giá **giảm** | Phân khúc thường gặp |
|---|---|---|---|
| **Người sản xuất, xuất khẩu** | Lợi: doanh thu tăng (Greed) | Thiệt: doanh thu giảm | DN lớn, SME, nông hộ (KHCN) |
| **Người dùng làm đầu vào** | Thiệt: chi phí tăng, biên lợi nhuận giảm | Lợi | SME, DN lớn, HKD |
| **Nhà phân phối, người giữ hàng tồn** | Lợi trên hàng tồn, nhưng cần nhiều vốn lưu động hơn | Thiệt: hàng tồn mất giá | SME, DN lớn, HKD, đại lý trong chuỗi |
| **Người tiêu dùng cuối** | Thiệt: chi tiêu bị co lại | Lợi | KHCN |
| **Người nắm giữ như tài sản** | Lợi: tài sản tăng giá, có thể chốt lời | Thiệt | KHCN (vàng, chứng khoán), DN có vị thế |

Thêm hai câu hỏi cho mọi tin giá:
- **Biến động bao lớn, kéo dài bao lâu?** Tăng vọt vài ngày khác xu hướng nhiều tháng. Tin không nêu thì ghi giả định.
- **Khách đã phòng ngừa chưa?** (hợp đồng kỳ hạn, hợp đồng giá cố định). Không biết thì đưa vào tín hiệu cần kiểm tra.

## 2. Bảy kênh truyền dẫn
> Kênh dưới đây cho biết biến số lan theo hướng nào. Để biết **ngành nào** bị chạm và ai trong ngành (người lao động, nông hộ, hộ kinh doanh, SME, DN lớn) gặp thách thức hay cơ hội gì, tra `industry/ind_00_index.md` mục 3 rồi nạp tối đa 3 file ngành.

Mỗi kênh liệt kê: ai thiệt, ai lợi, tác động cấp ngân hàng (`core/06_ngan_hang.md`), sản phẩm chính, điểm đảo chiều. Mã sản phẩm tra chi tiết trong file phân khúc.

### 2.1 Giá vàng
- **Thiệt:** tiền gửi của KHCN chảy sang vàng (`CN-DEP-01` `CN-ACC-03`); cấp ngân hàng mất huy động (`NH-LQ-01`), áp lực tiền mặt nếu người dân mua bằng tiền mặt (`NH-LQ-02`), áp lực tỷ giá nếu nhập khẩu vàng tăng (`NH-MR-01`).
- **Lợi:** KHCN đang giữ vàng có tài sản tăng; khi chốt lời có thể quay lại tiền gửi (`O2`). HKD kinh doanh vàng bạc có doanh thu tăng (`HKD-ACC-01`).
- **Lưu ý tuân thủ:** giao dịch tiền mặt lớn, chuyển tiền liên quan mua bán vàng (`NH-CO-01`).
- **Đảo chiều:** giá vàng quay đầu; người mua ở đỉnh bằng tiền vay có thể gặp khó trả nợ (`G01`).

### 2.2 Năng lượng (dầu, khí, điện)
- **Thiệt:** DN vận tải, hàng không, logistics, hóa chất, nhựa, thủy sản đánh bắt (DN lớn, SME; `CIB-LN-01` `CIB-SCF-01` đại lý vé, `SME-LN-*`); HKD vận tải nhỏ; KHCN chi phí đi lại tăng, chi tiêu giảm (`L06`).
- **Lợi:** DN khai thác, phân phối nhiên liệu (`CIB-LN-01` `CIB-TF-01`, `O1` `O3`).
- **Cấp ngân hàng:** lạm phát nhập khẩu → kỳ vọng lãi suất tăng (`NH-MR-02`), nhu cầu USD của nhà nhập khẩu (`NH-MR-01`).
- **Đảo chiều:** giá dầu hạ khi nguồn cung phục hồi; DN đã ký hợp đồng nhiên liệu giá cao bị kẹt.

### 2.3 Nông sản và phân bón
- Áp dụng bảng vai trò ở mục 1: nông hộ và DN xuất khẩu lợi khi giá tăng; DN chế biến trong nước, quán ăn, HKD thực phẩm thiệt.
- **Phân bón tăng** là chiều ngược: nông hộ (KHCN) và đại lý vật tư (HKD) thiệt trước, DN sản xuất phân bón lợi.
- **Sản phẩm:** `CIB-TF-02` `CIB-LN-01` `SME-LN-01` `HKD-LN-01` `CN-LN-08`; cơ hội tiền gửi sau mùa vụ `CN-DEP-01`.
- **Đảo chiều:** giá về mức bình quân; khoản vay mở rộng diện tích hoặc trữ hàng ở giá đỉnh (`G05`). Bài mẫu: `examples/ex_FG_01_ca_phe_o_B.md`.

### 2.4 Kim loại và vật liệu (thép, đồng, xi măng)
- **Thiệt:** nhà thầu xây dựng ký hợp đồng giá cố định (`SME-GTE-01` `CIB-TF-04`), người xây sửa nhà (`CN-LN-08`).
- **Lợi:** DN sản xuất, nhà phân phối có hàng tồn (`CIB-LN-01`, `CIB-SCF-01`).
- **Đảo chiều:** giá giảm làm nhà phân phối lỗ hàng tồn.

### 2.5 Tỷ giá và lãi suất quốc tế
- **USD mạnh lên:** DN nhập khẩu, DN có nợ ngoại tệ thiệt (`CIB-TF-01` `CIB-FX-01` `SME-PAY-04`); DN xuất khẩu lợi về doanh thu quy đổi. KHCN có chi phí du học, du lịch tăng (`CN-PAY-01`).
- **Cấp ngân hàng:** trạng thái ngoại tệ, chi phí vốn (`NH-MR-01` `NH-MR-02`); nhu cầu phái sinh phòng ngừa tăng (`CIB-CM-02`, `O3`).
- **Đảo chiều:** khách dùng phái sinh để đầu cơ thay vì phòng ngừa (`G06`).

### 2.6 Thương mại, vận tải và trừng phạt
- **Thuế quan, rào cản:** DN xuất khẩu vào thị trường bị áp thuế thiệt (bài mẫu `examples/ex_P1_doanh_nghiep_truoc.md`); DN ở nước cạnh tranh hoặc thay thế có thể lợi.
- **Tuyến hàng hải bị gián đoạn, cước và phí bảo hiểm hàng hải tăng:** thời gian giao hàng dài → vòng quay vốn chậm, nhu cầu vốn lưu động tăng (`CIB-LN-01` `CIB-TF-*` `SME-LN-*`).
- **Trừng phạt mới:** giao dịch với đối tác, quốc gia, tàu bị trừng phạt phải dừng (`NH-CO-01`, `CIB-PAY-02` `CN-PAY-01`); L/C liên quan có thể không thanh toán được.
- **Đảo chiều:** dỡ bỏ thuế quan hoặc trừng phạt; chuyển hướng thị trường.

### 2.7 Chính sách trong nước
- Lãi suất điều hành, hạn mức tín dụng, quy định về vàng, thuế với hộ kinh doanh, quy định xác thực giao dịch.
- Đọc theo mẫu P3 (`core/02_concepts_patterns.md`): chạm mọi phân khúc qua kênh `L09`, rồi xét từng phân khúc.
- Bài mẫu: `examples/ex_FG_03_lai_suat_giam_o_A_B.md`.

## 3. Xung đột quân sự và sự kiện địa chính trị
Đây là tin "gói nhiều kênh". Đi qua danh sách sau, mỗi mục chỉ giữ lại nếu sự kiện cho thấy có đường truyền:

1. **Năng lượng** (mục 2.2) – thường mạnh nhất và nhanh nhất.
2. **Vàng** (mục 2.1) – dòng tiền trú ẩn.
3. **Tỷ giá** (mục 2.5) – USD thường mạnh lên khi bất ổn.
4. **Vận tải và bảo hiểm hàng hải** (mục 2.6) – nếu xung đột gần tuyến hàng hải chính.
5. **Trừng phạt và tuân thủ** (mục 2.6) – danh sách đối tác, quốc gia bị hạn chế.
6. **Xuất khẩu sang khu vực xung đột** – đơn hàng, thu tiền, L/C.
7. **Người lao động và kiều hối** từ khu vực xung đột (`CN-PAY-01`, `CN-ACC-02`) – nếu có.
8. **Nhánh phụ `GL`:** tấn công mạng đi kèm, lừa đảo quyên góp hoặc đầu tư "hưởng lợi từ chiến tranh" – xem `outside_in/news/nw_03_gian_lan_an_ninh.md`.

Bài mẫu: `examples/ex_NW_01_xung_dot_trung_dong.md`.

## 4. Tín hiệu nội bộ hay dùng cho tin TT
| Câu hỏi | Tín hiệu |
|---|---|
| Tiền gửi có chảy sang vàng, chứng khoán không? | `G02` `F02` `S07` |
| DN nhập khẩu có cần thêm USD, vốn lưu động không? | L/C nhập khẩu, mua ngoại tệ, sử dụng hạn mức `S11` |
| DN xuất khẩu có thu tiền chậm không? | L/C xuất khẩu, chứng từ bất hợp lệ, `S10` |
| Thu nhập, chi tiêu KHCN có giảm không? | `S01` `S02` `S04` `S05` |
| Có giao dịch chạm đối tác bị trừng phạt không? | Rà soát `NH-CO-01` |
