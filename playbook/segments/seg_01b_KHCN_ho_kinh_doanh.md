---
id: SEG-KHCN-HKD
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [core/01_risk_codes.md, core/03_linkage_graph.md]
load_when: Sự kiện chạm nhóm hộ kinh doanh của KHCN, sức mua địa phương, thuế HKD, hoặc lan qua L03, L06, L07
version: v3.0
updated: 2026-11-02
---

# Phân khúc KHCN – nhóm hộ kinh doanh (HKD)

> Hộ kinh doanh thuộc phân khúc **KHCN**. Tài chính của hộ và của chủ hộ không tách bạch, nên luôn đọc cùng `segments/seg_01a_KHCN_ca_nhan.md`. Mã sản phẩm `HKD-` giữ nguyên.

> Cấu trúc: (a) Chân dung → (b) Động lực rủi ro → (c) Bảng độ nhạy sản phẩm (kèm hành vi khuyến nghị) → (e) Lan ra phân khúc khác → (f) Danh mục sản phẩm & URL nguồn


## (a) Chân dung
- Chủ hộ là cá nhân, thường đồng thời là KHCN (một CIF hoặc hai CIF liên kết).
- Mô hình: tạp hóa, ăn uống, bán lẻ online, dịch vụ nhỏ; doanh thu nhận qua QR, Soundbox, POS, phần mềm bán hàng.
- Đang trong giai đoạn **chuyển đổi thuế** và có lộ trình **chuyển lên doanh nghiệp** (cạnh `L07`).

## (b) Động lực rủi ro chính
1. **Chi tiêu của KHCN tại địa bàn** (cạnh `L06`) – nguồn doanh thu trực tiếp
2. **Chính sách thuế/hóa đơn** cho HKD – thay đổi chi phí tuân thủ, minh bạch doanh thu
3. **Chuỗi cung ứng / nhà phân phối** (cạnh `L03`) – điều khoản công nợ, giá nhập
4. **Sức khỏe & biến cố của chủ hộ** – dừng kinh doanh ngay lập tức
5. **Thiên tai, dịch bệnh, giải tỏa mặt bằng, quy hoạch chợ**
6. **Cạnh tranh từ thương mại điện tử / chuỗi bán lẻ**
7. **Lừa đảo nhắm vào chủ shop** (QR giả, mạo danh cơ quan thuế)

## (c) Bảng độ nhạy sản phẩm HKD

Mức ưu tiên trong bảng (in đậm, khác với mẫu lan truyền `P1`–`P3`): **P1** tác động trong ≤ 7 ngày, chạm tiền của khách, thanh khoản, vận hành hoặc tuân thủ – xử lý trong ngày. **P2** tác động trong 1–3 tháng qua thu nhập, tỷ giá, lãi suất, chạm `CR` hoặc `LQ` – theo dõi hằng tuần. **P3** tác động chậm (trên 3 tháng), gián tiếp, hoặc chỉ ảnh hưởng doanh thu phí (`BR`), mức tương tác – ghi nhận, chỉ nêu khi đi cùng tin khác hoặc khi gom cụm. **(+)** là chiều cơ hội: **P2 (+)** cơ hội cần hành động trong 1–3 tháng; **P3 (+)** cơ hội chậm hoặc nhỏ, chỉ ghi nhận; cơ hội luôn kèm mặt trái theo `fear_greed/fg_01_dual_lens.md`. Ở cột tác động, **(+)** là tác động của các keyword cơ hội. Tin khớp nhiều keyword → lấy mức cao nhất. Cột hành vi khuyến nghị gồm việc con người cần làm và dữ liệu cần kiểm tra để chạy what-if, stress test; các con số trong kịch bản là tham số giả định, không phải dự báo.
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `HKD-ACC-01` | Tài khoản Hộ kinh doanh | `LQ` `CO` `FR` | **P1:** mạo danh cơ quan thuế, ngân hàng nhắm chủ hộ; tài khoản bị dùng làm trung gian<br>**P2:** bỏ thuế khoán, kê khai, hóa đơn điện tử; AML tách bạch dòng tiền<br>**P3:** sàn TMĐT khấu trừ thuế thay<br>**P2 (+):** quy định tách tài khoản HKD; HKD chuyển lên DN (`L07`) | **P1:** mất tiền, phong tỏa tài khoản (`X01`)<br>**P2:** doanh thu chảy về TK cá nhân thay TK HKD (`S16`); doanh thu về TK giảm<br>**P3:** đổi kênh bán hàng<br>**(+):** mở mới TK HKD, chuyển đổi lên DN | **Con người:** cảnh báo chủ hộ về mạo danh cơ quan thuế; hướng dẫn tách tài khoản, kê khai, hóa đơn; không phong tỏa diện rộng<br>**Dữ liệu, what-if:** tỷ lệ doanh thu về TK HKD so với TK cá nhân (`S16`); what-if: 30% hộ chuyển doanh thu về TK cá nhân sau đổi thuế |
| `HKD-REV-01` | Soundbox | `OR` `BR` | **P1:** sự cố mạng, thiết bị hàng loạt<br>**P2:** sức mua giảm; trả mặt bằng, giới hạn giờ hoạt động, siết vỉa hè<br>**P3:** QR miễn phí của đối thủ | **P1:** không nhận được tiền<br>**P2:** giảm số giao dịch/ngày, số người trả tiền (`S02` `S03`)<br>**P3:** rời bỏ thiết bị | **Con người:** kỹ thuật kiểm tra thiết bị theo cụm; RM thăm hộ có giao dịch giảm mạnh<br>**Dữ liệu, what-if:** số giao dịch/ngày, unique payers theo tuyến phố, MCC; what-if: doanh thu QR −30% ở một tuyến phố |
| `HKD-REV-02` | Liên kết phần mềm bán hàng (QR liên kết) | `OR` `BR` | **P1:** sự cố, lộ dữ liệu ở đối tác phần mềm (`L13`)<br>**P2:** đối tác đổi chính sách; hóa đơn điện tử từ máy tính tiền<br>**P3 (+):** quy định hóa đơn điện tử thúc đẩy số hóa | **P1:** mất dữ liệu doanh thu, gián đoạn nhận tiền<br>**P2:** chuyển sang đối tác khác<br>**(+):** kết nối mới tăng | **Con người:** liên hệ đối tác phần mềm khi có sự cố; thông báo hộ bị ảnh hưởng<br>**Dữ liệu, what-if:** số kết nối bị ngắt theo đối tác; what-if: một đối tác phần mềm lớn gián đoạn 48 giờ |
| `HKD-REV-03` | Nhận thanh toán thẻ: SoftPOS / SmartPOS / SoundPOS | `OR` `FR` `BR` | **P1:** gian lận thẻ tại điểm bán, lộ dữ liệu thẻ<br>**P2:** khách quốc tế giảm, sức mua giảm<br>**P3 (+):** khách du lịch tăng | **P1:** tra soát, chargeback (`X05`)<br>**P2:** doanh số thẻ giảm<br>**(+):** doanh số thẻ tăng | **Con người:** khóa nhận thẻ ở điểm bán nghi gian lận; hướng dẫn hộ xử lý tra soát<br>**Dữ liệu, what-if:** chargeback theo điểm bán; what-if: khách quốc tế −40% ở tỉnh du lịch |
| `HKD-LN-01` | Vay tín chấp kinh doanh ShopCash (hạn mức cấp sẵn) | `CR` | **P2:** doanh thu giảm (sức mua, thuế, mặt bằng, giờ hoạt động); dịch bệnh vật nuôi, giá nông sản giảm (với đại lý); biến cố chủ hộ<br>**P3 (+):** mùa Tết, mùa vụ nhập hàng | **P2:** sử dụng hạn mức tăng khi doanh thu giảm = tín hiệu căng thẳng (`S04`); DPD<br>**(+):** nhu cầu vốn mùa vụ, kèm rủi ro xin hạn mức ở giá đỉnh (`G05`) | **Con người:** RM gọi hộ dùng hết hạn mức khi doanh thu giảm; tư vấn giãn nợ; không cắt hạn mức đồng loạt<br>**Dữ liệu, what-if:** liên hệ doanh thu QR – sử dụng hạn mức theo hộ; what-if: doanh thu −30% trong 3 tháng ở một ngành hoặc tuyến phố |
| `HKD-LN-02` | Vay thế chấp kinh doanh ShopCredit | `CR` `CL` | **P2:** doanh thu giảm, trả mặt bằng; giá nhà phố, giá thuê mặt bằng giảm; lãi suất tăng | **P2:** DPD; TSBĐ là nhà ở/mặt bằng giảm giá (`CL`) | **Con người:** định giá lại TSBĐ nhà phố ở tuyến có nhiều mặt bằng bỏ trống; tư vấn cơ cấu<br>**Dữ liệu, what-if:** LTV theo tuyến phố, giá thuê; what-if: giá thuê −30%, giá nhà phố −20% |
| `HKD-LN-03` | Vay trả góp tín chấp cho chủ HKD | `CR` | **P2:** doanh thu giảm; chủ hộ ốm đau, biến cố | **P2:** DPD sớm | **Con người:** liên hệ sớm chủ hộ có biến cố<br>**Dữ liệu, what-if:** DPD theo ngành, địa bàn; what-if: doanh thu −30% |
| `HKD-CARD-01` | Thẻ thanh toán Techcombank Visa Seller | `FR` `BR` | **P1:** gian lận thẻ, lộ dữ liệu thẻ<br>**P2:** HKD thu hẹp, giá đầu vào tăng | **P1:** giao dịch trái phép, tra soát<br>**P2:** giảm chi tiêu nhập hàng = HKD thu hẹp | **Con người:** khóa thẻ nghi lộ dữ liệu; theo dõi hộ giảm nhập hàng<br>**Dữ liệu, what-if:** chi tiêu nhập hàng theo tháng; what-if: chi tiêu −40% |
| `HKD-DEP-01` | Tiền gửi HKD; Sinh lời tự động | `LQ` | **P2:** doanh thu giảm, cần vốn nhập hàng; giá vàng tăng (tiệm vàng giữ tiền mặt)<br>**P3 (+):** tiền về sau mùa vụ, mùa cao điểm | **P2:** số dư nhàn rỗi giảm<br>**(+):** số dư tăng (`O2`) | **Con người:** tư vấn quản lý dòng tiền mùa vụ<br>**Dữ liệu, what-if:** số dư theo hộ, mùa vụ; what-if: số dư −30% trước mùa Tết |
| `HKD-INS-01` | BH sức khỏe nhóm; BH toàn diện HKD & DN | `INS` | **P1:** cháy chợ, cháy nổ, bão lũ<br>**P2:** dịch bệnh | **P1:** claim tăng theo địa bàn<br>**P2:** claim sức khỏe tăng | **Con người:** hỗ trợ hồ sơ bồi thường sau cháy chợ, thiên tai<br>**Dữ liệu, what-if:** số hộ có bảo hiểm theo chợ, vùng; what-if: cháy một chợ lớn |
| `HKD-DIG-01` | Techcombank Mobile (cho HKD) | `OR` `FR` | **P1:** sự cố app; mạo danh, chiếm đoạt tài khoản | **P1:** mất doanh thu trực tiếp trong thời gian gián đoạn; mất tiền (`S13`) | **Con người:** thông báo sự cố; cảnh báo chiếm đoạt tài khoản<br>**Dữ liệu, what-if:** giao dịch thất bại theo giờ; what-if: app gián đoạn trong giờ cao điểm bán hàng |
| `HKD-SVC-01` | Dịch vụ qua CDM | `OR` | **P1:** sự cố máy, thiên tai, mất điện<br>**P2:** mùa cao điểm tiền mặt | **P1:** không nộp được tiền mặt doanh thu<br>**P2:** máy quá tải, cần tiếp quỹ | **Con người:** tăng tiếp quỹ, ưu tiên sửa máy ở khu chợ<br>**Dữ liệu, what-if:** nộp tiền CDM theo máy; what-if: 20% máy một tỉnh dừng |

## (e) Lan ra phân khúc khác

| Hướng lan | Kênh | Cơ chế | Độ trễ | Tín hiệu kiểm chứng | Chiều cơ hội |
|---|---|---|---|---|---|
| → KHCN (chính chủ hộ) | Hop 0 | Rủi ro HKD là rủi ro cá nhân chủ hộ: vay tiêu dùng, mua nhà, thẻ của chủ hộ | Ngay | DPD khoản vay cá nhân chủ hộ; `S04` | Doanh thu tốt → chủ hộ gửi tiết kiệm, mua nhà |
| → Chủ nhà cho thuê mặt bằng (KHCN) | Trả mặt bằng | HKD trả mặt bằng → chủ nhà mất thu nhập cho thuê, giá thuê giảm, nhà phố làm TSBĐ giảm giá | 1–6 tháng | DPD khoản vay thế chấp nhà phố; giá thuê theo tuyến phố | – |
| → Nhà phân phối, DN lớn | `L03` (ngược) | HKD giảm nhập hàng, chậm công nợ → nhà phân phối trong chuỗi SCF | 1–2 tháng | `S11`; chi tiêu Visa Seller | HKD mở rộng → đơn hàng nhà phân phối tăng |
| → SME | `L07` | HKD chuyển lên DN mang theo rủi ro tín dụng cũ, hoặc né chuyển đổi bằng cách dùng TK cá nhân | Theo chính sách thuế | `S16` | Khách SME mới (`O6`) |
| → Người làm thuê của HKD (KHCN) | `L02` (quy mô nhỏ) | Hộ cắt giảm người làm thuê; thu nhập thường trả tiền mặt nên khó thấy | 1–2 tháng | Ít dữ liệu; theo dõi qua QR khu vực | – |
| → Cấp ngân hàng | `L10` | Doanh thu QR giảm diện rộng → phí `BR`; tài khoản HKD bị lợi dụng → `FR` `CO` | Tuần | `X01`; doanh thu phí QR | – |

Mức chắc chắn giảm theo số bước lan (`core/04_reasoning_procedure.md`); mỗi hướng lan ghi rõ độ trễ và tín hiệu kiểm chứng khi đưa vào bài viết.

## (f) Danh mục sản phẩm & URL nguồn (chốt 26/10/2026)

Nguồn: https://techcombank.com/ho-kinh-doanh-va-doanh-nghiep-nho/ho-kinh-doanh

- Tài khoản Hộ kinh doanh
- Quản lý doanh thu: Soundbox · Liên kết phần mềm bán hàng · (SoftPOS/SmartPOS/SoundPOS theo chương trình ưu đãi)
- Vay: ShopCash (tín chấp) · ShopCredit (thế chấp) · Vay trả góp tín chấp cho chủ HKD
- Techcombank Mobile · Thẻ thanh toán Techcombank Visa Seller · Tiền gửi (Sinh lời tự động)
- Bảo hiểm: Bảo hiểm sức khỏe nhóm · Bảo hiểm toàn diện
- Dịch vụ khác: CDM · Đặt lịch hẹn
- Lộ trình: Chuyển đổi HKD lên doanh nghiệp
