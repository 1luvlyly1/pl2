---
id: SEG-DNL
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [core/01_risk_codes.md, core/03_linkage_graph.md]
load_when: Sự kiện chạm DN lớn, ngành, thương mại quốc tế, BĐS, trái phiếu, hoặc lan qua L03, L04, L05, L08
version: v3.0
updated: 2026-11-02
---

# Phân khúc: Doanh nghiệp lớn (CIB)

> Gồm doanh nghiệp lớn và định chế tài chính. Mã phân khúc trong dòng nhãn và mã sản phẩm vẫn dùng `CIB`.

> Cấu trúc: (a) Chân dung → (b) Động lực rủi ro → (c) Bảng độ nhạy sản phẩm (kèm hành vi khuyến nghị) → (e) Lan ra phân khúc khác → (f) Danh mục sản phẩm & URL nguồn


## (a) Chân dung
- DN quy mô lớn, tập đoàn, FDI, định chế tài chính.
- Dư nợ tập trung lớn; dùng sản phẩm phức tạp (tài trợ thương mại, FX, phái sinh, trái phiếu); là **anchor** trong chuỗi cung ứng và là **CĐT BĐS / tổ chức phát hành trái phiếu** (cạnh `L04`, `L05`).

## (b) Động lực rủi ro chính
1. **Ngành** (BĐS, thép, dệt may, gỗ, thủy sản, hàng không, ô tô, tiêu dùng nhanh…)
2. **Thương mại quốc tế** – thuế quan, trừng phạt, đứt gãy vận tải (cạnh `L08`)
3. **Tỷ giá & lãi suất** – nợ ngoại tệ, vị thế phái sinh
4. **Pháp lý doanh nghiệp & lãnh đạo** – thanh tra, khởi tố, tranh chấp
5. **Thị trường vốn** – đáo hạn trái phiếu, khả năng huy động mới
6. **Rủi ro tập trung theo nhóm khách hàng liên quan**
7. **ESG** – quy định phát thải, CBAM, tín dụng xanh

## (c) Bảng độ nhạy sản phẩm CIB

Mức ưu tiên trong bảng (in đậm, khác với mẫu lan truyền `P1`–`P3`): **P1** tác động trong ≤ 7 ngày, chạm tiền của khách, thanh khoản, vận hành hoặc tuân thủ – xử lý trong ngày. **P2** tác động trong 1–3 tháng qua thu nhập, tỷ giá, lãi suất, chạm `CR` hoặc `LQ` – theo dõi hằng tuần. **P3** tác động chậm (trên 3 tháng), gián tiếp, hoặc chỉ ảnh hưởng doanh thu phí (`BR`), mức tương tác – ghi nhận, chỉ nêu khi đi cùng tin khác hoặc khi gom cụm. **(+)** là chiều cơ hội: **P2 (+)** cơ hội cần hành động trong 1–3 tháng; **P3 (+)** cơ hội chậm hoặc nhỏ, chỉ ghi nhận; cơ hội luôn kèm mặt trái theo `fear_greed/fg_01_dual_lens.md`. Ở cột tác động, **(+)** là tác động của các keyword cơ hội. Tin khớp nhiều keyword → lấy mức cao nhất. Cột hành vi khuyến nghị gồm việc con người cần làm và dữ liệu cần kiểm tra để chạy what-if, stress test; các con số trong kịch bản là tham số giả định, không phải dự báo.
**Quản trị hàng ngày**
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `CIB-PKG-01` | BusinessOne Connect / Plus / Premium | `BR` | **P3:** hoạt động DN giảm | **P3:** hạ gói | **Con người:** RM hỏi lý do hạ gói<br>**Dữ liệu, what-if:** số DN hạ gói |
| `CIB-DIG-01` | Techcombank Business; F@st EBank (đang chuyển đổi sang Techcombank Business); Chữ ký số | `OR` `FR` | **P1:** sự cố, giai đoạn chuyển đổi nền tảng, chiếm đoạt chữ ký số | **P1:** gián đoạn thanh toán quy mô lớn; chuyển tiền trái phép (`X03` `X04`) | **Con người:** kích hoạt quy trình sự cố, kênh dự phòng cho thanh toán lớn; kiểm soát chữ ký số<br>**Dữ liệu, what-if:** giao dịch lớn thất bại, thiết bị lạ; what-if: gián đoạn vào ngày chi lương, nộp thuế |
| `CIB-ACC-01` | Tài khoản thanh toán | `LQ` `CO` | **P1:** tin đồn ngân hàng; BEC<br>**P2:** dòng tiền giảm, AML | **P1:** số dư lớn rút đột ngột (`NH-LQ-01`)<br>**P2:** số dư giảm, giao dịch cần rà soát | **Con người:** RM gọi DN rút số dư lớn bất thường; cảnh báo BEC<br>**Dữ liệu, what-if:** số dư theo DN lớn nhất (tập trung); what-if: 5 DN lớn nhất rút 50% số dư |
| `CIB-ACC-02` | Tài khoản vốn | `CO` `MR` | **P2:** quy định FDI, ngoại hối<br>**P3 (+):** FDI tăng, dịch chuyển chuỗi cung ứng | **P2:** dòng vốn dừng<br>**(+):** dòng vốn mới (`O6`) | **Con người:** tư vấn quy định FDI, ngoại hối<br>**Dữ liệu, what-if:** dòng vốn theo quốc gia, ngành; what-if: FDI −30% |
| `CIB-ACC-03` | Tài khoản giữ hộ thương mại | `RP` `CO` | **P2:** tranh chấp M&A, mua bán | **P2:** tranh chấp giải ngân giữ hộ | **Con người:** pháp chế hỗ trợ tranh chấp<br>**Dữ liệu, what-if:** tài khoản giữ hộ đang tranh chấp |
| `CIB-ACC-04` | Tài khoản giữ hộ bất động sản | `RP` `CO` `CR` | **P1:** dự án dừng, chủ đầu tư vỡ nợ<br>**P2:** pháp lý dự án, tiến độ (cạnh `L04`) | **P1:** phong tỏa, tranh chấp với người mua nhà<br>**P2:** chậm giải ngân | **Con người:** rà dự án có tin xấu, chuẩn bị xử lý với người mua nhà (`L04`)<br>**Dữ liệu, what-if:** giá trị giữ hộ, số người mua theo dự án; what-if: dự án dừng 12 tháng |
| `CIB-PAY-01` | Thanh toán hàng hóa dịch vụ trong nước | `FR` `OR` | **P1:** BEC, sự cố | **P1:** chuyển nhầm/lừa đảo, thanh toán chậm (`X04`) | **Con người:** gọi xác nhận thanh toán lớn đi người thụ hưởng mới<br>**Dữ liệu, what-if:** `X04`; giá trị thanh toán theo đối tác |
| `CIB-PAY-02` | Chuyển tiền đi nước ngoài | `CO` `MR` | **P1:** trừng phạt<br>**P2:** AML, tỷ giá | **P1:** giao dịch bị giữ, rà soát (`NH-CO-01`)<br>**P2:** chi phí tăng | **Con người:** tạm giữ, rà soát giao dịch nghi trừng phạt; báo cáo tuân thủ<br>**Dữ liệu, what-if:** giao dịch theo quốc gia, đối tác; what-if: thêm quốc gia bị trừng phạt |
| `CIB-PAY-03` | Nộp ngân sách nhà nước | `CO` | **P2:** thuế, hải quan | **P2:** nộp chậm = dấu hiệu thiếu tiền (`S10`) | **Con người:** RM hỏi DN nộp chậm<br>**Dữ liệu, what-if:** nộp NSNN theo kỳ (`S10`) |
| `CIB-PAY-04` | Thẻ dành cho DN | `CR` `FR` | **P1:** gian lận thẻ<br>**P2:** dòng tiền DN giảm | **P1:** giao dịch trái phép<br>**P2:** dư nợ thẻ chậm trả | **Con người:** khóa thẻ nghi lộ dữ liệu; RM liên hệ DN chậm trả<br>**Dữ liệu, what-if:** dư nợ thẻ theo DN |
| `CIB-PAY-05` | Thanh toán hóa đơn | `OR` | **P2:** sản lượng giảm do mất đơn, thuế quan | **P2:** hóa đơn điện/cảng giảm = sản xuất/xuất khẩu giảm (`S10`) | **Con người:** RM hỏi DN có hóa đơn điện, cảng giảm mạnh<br>**Dữ liệu, what-if:** hóa đơn điện, cảng theo DN, ngành (`S10`); what-if: sản lượng ngành −20% |
| `CIB-PAY-06` | Thanh toán lương | `BR` | **P1:** cắt giảm nhân sự, đóng nhà máy<br>**P2:** mất đơn hàng, thuế quan<br>**P3 (+):** mở nhà máy mới | **P1:** cắt giảm nhân sự lan tới hàng nghìn KHCN (cạnh `L02`, `S01`)<br>**P2:** quỹ lương giảm<br>**(+):** tài khoản lương mới (`O2`) | **Con người:** RM gọi DN giảm quỹ lương; rà khoản vay của nhân viên DN đó; chuẩn bị gói hỗ trợ nhân viên; không thu hồi đồng loạt<br>**Dữ liệu, what-if:** số nhân viên, dư nợ KHCN gắn với DN (`L02`); what-if: DN cắt 20–30% nhân sự |
| `CIB-COL-01` | Thu hộ: TK định danh, POS, QR, Payment Gateway, tiền mặt tại quầy, tại địa điểm KH, qua quầy đối tác | `OR` `FR` `BR` | **P1:** sự cố cổng thanh toán<br>**P2:** doanh thu bán lẻ giảm | **P1:** gián đoạn thu hộ<br>**P2:** thu hộ giảm = doanh thu DN giảm | **Con người:** kích hoạt kênh thu dự phòng khi cổng lỗi<br>**Dữ liệu, what-if:** thu hộ theo DN, kênh; what-if: thu hộ −30% |
| `CIB-LIQ-01` | Báo cáo tổng hợp dòng tiền | – | Công cụ quan sát | Nguồn tín hiệu sớm |  |
| `CIB-DEP-01` | CCTG Bảo Lộc; Tiền gửi xanh | `LQ` `MR` | **P1:** tin đồn ngân hàng<br>**P2:** lãi suất, nhu cầu vốn, đáo hạn trái phiếu của DN | **P1:** rút tiền gửi lớn ảnh hưởng thanh khoản ngân hàng (`NH-LQ-01`)<br>**P2:** tất toán sớm | **Con người:** RM giữ liên lạc với DN có tiền gửi lớn sắp đáo hạn; kịch bản tin đồn<br>**Dữ liệu, what-if:** tiền gửi DN theo kỳ đáo hạn, tập trung; what-if: 3 DN lớn nhất rút toàn bộ |

**Vay**
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `CIB-LN-01` | Vay vốn lưu động: theo món, theo hạn mức, theo ngành, thấu chi | `CR` `CL` | **P2:** doanh thu, vòng quay hàng tồn giảm; thuế quan, giá hàng hóa, cước vận tải (xem file ngành)<br>**P3:** TSBĐ hàng tồn giảm giá | **P2:** DPD, xin cơ cấu<br>**P3:** LTV xấu đi | **Con người:** RM rà DN trong ngành bị chạm; tư vấn cơ cấu sớm; không cắt hạn mức đồng loạt<br>**Dữ liệu, what-if:** dư nợ theo ngành, thị trường, vòng quay hàng tồn; what-if: doanh thu ngành −20–30%, giá hàng tồn −20% |
| `CIB-LN-02` | Vay trung dài hạn: theo món, theo dự án, theo ngành, mua ô tô DN | `CR` `CL` `MR` | **P1:** dự án bị dừng, thu hồi<br>**P2:** lãi suất, tiến độ, pháp lý dự án | **P1:** dòng tiền trả nợ mất<br>**P2:** dự án chậm → dòng tiền trả nợ chậm | **Con người:** rà tiến độ, pháp lý dự án có tin xấu; chuẩn bị phương án tái cấu trúc<br>**Dữ liệu, what-if:** dòng tiền dự án; what-if: dự án chậm 12 tháng, lãi suất +2 điểm % |
| `CIB-SCF-01` | Tài trợ chuỗi cung ứng: kinh doanh ô tô; đại lý bán vé hàng không; vận chuyển hàng hóa hàng không; nhà phân phối Masan | `CR` | **P1:** anchor gặp sự cố: vỡ nợ, đình chỉ, bị điều tra<br>**P2:** nhu cầu cuối giảm: giá nhiên liệu bay, doanh số ô tô, tiêu dùng FMCG | **P1:** toàn bộ spoke bị ảnh hưởng đồng thời (cạnh `L03`, `S11`)<br>**P2:** spoke chậm trả dần | **Con người:** rà toàn bộ spoke khi anchor có tin xấu; liên hệ anchor; không cắt đồng loạt spoke<br>**Dữ liệu, what-if:** dư nợ spoke theo anchor, `S11`; what-if: anchor dừng thanh toán 60 ngày |

**Thương mại (Trade)**
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `CIB-TF-01` | Nhập khẩu: L/C nhập khẩu, nhờ thu | `CR` `MR` `CO` | **P1:** trừng phạt<br>**P2:** tỷ giá, giá hàng hóa tăng | **P1:** giao dịch bị dừng<br>**P2:** ngân hàng phải thanh toán thay khi DN thiếu tiền | **Con người:** rà L/C liên quan nước bị trừng phạt; RM liên hệ DN nhập khẩu khi tỷ giá tăng mạnh<br>**Dữ liệu, what-if:** L/C mở theo hàng hóa, quốc gia; what-if: giá hàng hóa +20%, USD/VND +5% |
| `CIB-TF-02` | Xuất khẩu: L/C xuất khẩu, nhờ thu, tài trợ thương mại | `CR` `CO` | **P1:** trừng phạt nước người mua<br>**P2:** thuế quan, phòng vệ thương mại, cước vận tải; chứng từ bất hợp lệ | **P1:** không thu được tiền<br>**P2:** hủy đơn, chậm thu tiền (`X06`) | **Con người:** kiểm tra chứng từ kỹ hơn; RM liên hệ DN xuất khẩu bị chạm thuế quan<br>**Dữ liệu, what-if:** L/C xuất khẩu theo thị trường, ngành; chứng từ bất hợp lệ (`X06`); what-if: mất 30% đơn hàng sang Mỹ |
| `CIB-TF-03` | Nội địa: L/C nội địa, tài trợ thương mại, tài trợ chuỗi cung ứng | `CR` `FR` | **P1:** gian lận chứng từ, hóa đơn khống<br>**P2:** chuỗi cung ứng đứt gãy | **P1:** tài trợ trên giao dịch không có thật (`X06`)<br>**P2:** chậm thanh toán trong chuỗi | **Con người:** rà chứng từ nghi trùng lặp; xác minh giao dịch hàng hóa<br>**Dữ liệu, what-if:** `X06`; đối chiếu hóa đơn điện tử; what-if: phát hiện một chuỗi giao dịch khống |
| `CIB-TF-04` | Bảo lãnh; L/C UPAS | `CR` `CO` | **P1:** chủ đầu tư vỡ nợ, bảo lãnh bị gọi hàng loạt<br>**P2:** vi phạm hợp đồng, tranh chấp | **P1:** ngân hàng phải trả thay<br>**P2:** bị gọi bảo lãnh | **Con người:** rà bảo lãnh liên quan chủ đầu tư có tin xấu<br>**Dữ liệu, what-if:** giá trị bảo lãnh theo chủ đầu tư, dự án; what-if: 10–20% bảo lãnh bị gọi |

**Nguồn vốn (Treasury & Markets)**
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `CIB-FX-01` | Giao dịch ngoại tệ: giao ngay, kỳ hạn, hoán đổi | `MR` `CR` (đối tác) | **P1:** cú sốc tỷ giá đột ngột<br>**P2:** biến động tỷ giá | **P1:** lỗ vị thế lớn của khách → rủi ro đối tác (`S15`)<br>**P2:** lỗ vị thế, yêu cầu ký quỹ | **Con người:** RM liên hệ khách có vị thế lỗ lớn; kiểm tra ký quỹ<br>**Dữ liệu, what-if:** giá trị thị trường vị thế (`S15`); what-if: USD/VND ±5% |
| `CIB-CM-01` | Phái sinh lãi suất | `MR` `CR` | **P2:** thay đổi lãi suất | **P2:** giá trị thị trường âm lớn với khách (`S15`) | **Con người:** RM liên hệ khách có giá trị âm lớn<br>**Dữ liệu, what-if:** `S15`; what-if: lãi suất ±2 điểm % |
| `CIB-CM-02` | Phái sinh tỷ giá | `MR` `CR` | **P1:** cú sốc tỷ giá<br>**P2:** tỷ giá biến động | **P1:** giá trị thị trường âm lớn, rủi ro đối tác (`S15`)<br>**P2:** vị thế vượt nhu cầu phòng ngừa (`G06`) | **Con người:** kiểm tra vị thế vượt nhu cầu phòng ngừa (`G06`)<br>**Dữ liệu, what-if:** `S15`; what-if: USD/VND ±5% |
| `CIB-CM-03` | Sản phẩm cấu trúc | `MR` `RP` | **P1:** khách lỗ lớn, khiếu nại<br>**P2:** biến động thị trường | **P1:** tranh chấp về tính phù hợp sản phẩm (`RP`)<br>**P2:** giá trị sản phẩm giảm | **Con người:** rà hồ sơ đánh giá tính phù hợp sản phẩm của khách<br>**Dữ liệu, what-if:** giá trị sản phẩm theo khách; what-if: thị trường biến động mạnh 2 lần độ lệch chuẩn |
| `CIB-INV-01` | Trái phiếu doanh nghiệp (phát hành/thu xếp) | `CR` `RP` `CO` | **P1:** đáo hạn không trả được, vỡ nợ<br>**P2:** quy định phát hành | **P1:** lan sang nhà đầu tư cá nhân qua iBond (cạnh `L05`)<br>**P2:** khó phát hành, thu xếp | **Con người:** dừng thu xếp, phân phối mới của tổ chức có tin xấu; phối hợp kênh iBond chuẩn bị xử lý trái chủ cá nhân (`L05`)<br>**Dữ liệu, what-if:** lịch đáo hạn trái phiếu theo tổ chức; số trái chủ cá nhân; what-if: tổ chức lớn nhất không trả đúng hạn |
| `CIB-INS-01` | Bảo hiểm phi nhân thọ cho DN | `INS` | **P1:** cháy nổ, thiên tai<br>**P2:** gián đoạn kinh doanh | **P1:** claim lớn<br>**P2:** claim gián đoạn | **Con người:** hỗ trợ hồ sơ bồi thường<br>**Dữ liệu, what-if:** giá trị bảo hiểm theo vùng, ngành; what-if: thiên tai lớn ở một KCN |

## (e) Lan ra phân khúc khác

| Hướng lan | Kênh | Cơ chế | Độ trễ | Tín hiệu kiểm chứng | Chiều cơ hội |
|---|---|---|---|---|---|
| → KHCN nhân viên | `L02` | Cắt giảm quy mô lớn → hàng nghìn KHCN mất hoặc giảm thu nhập cùng lúc | 1–2 tháng | `S01` `S04` `S05` | Nhà máy mới → tài khoản lương, thẻ, vay tiêu dùng |
| → KHCN lãnh đạo, cổ đông Private | `L01` | Lãnh đạo bị điều tra, bán cổ phần, giải chấp → tài sản cá nhân và khoản vay cá nhân | Ngay | Chuyển nhượng cổ phần lớn; `S12` | – |
| → KHCN người mua nhà | `L04` | Chủ đầu tư chậm tiến độ, pháp lý → khoản vay mua nhà dự án | 1–6 tháng | DPD `CN-LN-01` theo dự án | Tháo gỡ pháp lý → giải ngân mới |
| → KHCN trái chủ, nhà đầu tư quỹ | `L05` | Chậm trả trái phiếu → bán lại iBond, NAV quỹ giảm, khiếu nại | Ngày – tuần | `S08` | – |
| → SME, HKD trong chuỗi | `L03` | Anchor gặp khó → spoke, đại lý, nhà cung cấp cùng chậm trả | 1–2 tháng | `S11` | Anchor mở rộng → đơn hàng spoke tăng |
| → Cấp ngân hàng | `L10` | Rủi ro tập trung lớn → chất lượng tài sản, xếp hạng, nhà đầu tư; tiền gửi lớn rút đột ngột (`core/06_ngan_hang.md`) | Ngày – quý | `NH-LQ-01`; tập trung dư nợ theo nhóm khách | – |

Mức chắc chắn giảm theo số bước lan (`core/04_reasoning_procedure.md`); mỗi hướng lan ghi rõ độ trễ và tín hiệu kiểm chứng khi đưa vào bài viết.

## (f) Danh mục sản phẩm & URL nguồn (chốt 26/10/2026)

Nguồn: https://techcombank.com/khach-hang-doanh-nghiep

- **Quản trị hàng ngày:** Gói BusinessOne (Connect/Plus/Premium) · Techcombank Business · F@st EBank (đang chuyển đổi) · Chữ ký số · TK thanh toán · TK vốn · Giữ hộ thương mại · Giữ hộ BĐS · Thanh toán trong nước · Chuyển tiền nước ngoài · Nộp NSNN · Thẻ DN · Hóa đơn · Lương · Thu hộ (TK định danh, POS, QR, Payment Gateway, tiền mặt tại quầy / tại địa điểm KH / qua đối tác) · Báo cáo tổng hợp dòng tiền · CDM · Tổng đài · CCTG Bảo Lộc · Tiền gửi xanh
- **Vay:** Vốn lưu động (theo món, hạn mức, theo ngành, thấu chi) · Trung dài hạn (theo món, theo dự án, theo ngành, mua ô tô DN) · Tài trợ chuỗi cung ứng (kinh doanh ô tô, đại lý bán vé hàng không, vận chuyển hàng hóa hàng không, nhà phân phối Masan)
- **Thương mại:** L/C nhập khẩu · Nhờ thu NK · L/C xuất khẩu · Nhờ thu XK · Tài trợ thương mại · L/C nội địa · Tài trợ chuỗi cung ứng nội địa · Bảo lãnh · L/C UPAS
- **Nguồn vốn:** FX giao ngay · Kỳ hạn · Hoán đổi · Phái sinh lãi suất · Phái sinh tỷ giá · Sản phẩm cấu trúc · Trái phiếu doanh nghiệp
- **Bảo hiểm:** Bảo hiểm phi nhân thọ cho DN
