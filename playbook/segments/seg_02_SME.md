---
id: SEG-SME
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [core/01_risk_codes.md, core/03_linkage_graph.md]
load_when: Sự kiện chạm DN vừa và nhỏ, mua sắm công, hoặc lan qua L01, L02, L03, L07, L12
version: v3.0
updated: 2026-11-02
---

# Phân khúc: Doanh nghiệp vừa và nhỏ (SME)

> Cấu trúc: (a) Chân dung → (b) Động lực rủi ro → (c) Bảng độ nhạy sản phẩm (kèm hành vi khuyến nghị) → (e) Lan ra phân khúc khác → (f) Danh mục sản phẩm & URL nguồn


## (a) Chân dung
- Quy mô vừa/nhỏ, quản trị phụ thuộc chủ sở hữu (cạnh `L01` rất mạnh).
- Dùng gói BusinessOne / MerchantOne; vay dựa trên dữ liệu (Misa Lending, Hybrid, B1CP); tham gia mua sắm công.

## (b) Động lực rủi ro chính
1. **Dòng tiền ngắn hạn** – SME ít đệm thanh khoản; chậm thu tiền khách hàng là nguy cơ lớn nhất
2. **Phụ thuộc khách hàng/nhà cung cấp lớn** (cạnh `L03`)
3. **Chủ sở hữu** – biến cố cá nhân của chủ = biến cố DN
4. **Thuế, hóa đơn, kế toán** (dữ liệu từ phần mềm kế toán ảnh hưởng hạn mức vay)
5. **Thanh toán chậm từ ngân sách / chủ đầu tư công** (cạnh `L12`)
6. **Tỷ giá** với SME có nhập khẩu nguyên liệu
7. **Lừa đảo chiếm đoạt tài khoản DN, giả mạo email đối tác (BEC)**

## (c) Bảng độ nhạy sản phẩm SME

Mức ưu tiên trong bảng (in đậm, khác với mẫu lan truyền `P1`–`P3`): **P1** tác động trong ≤ 7 ngày, chạm tiền của khách, thanh khoản, vận hành hoặc tuân thủ – xử lý trong ngày. **P2** tác động trong 1–3 tháng qua thu nhập, tỷ giá, lãi suất, chạm `CR` hoặc `LQ` – theo dõi hằng tuần. **P3** tác động chậm (trên 3 tháng), gián tiếp, hoặc chỉ ảnh hưởng doanh thu phí (`BR`), mức tương tác – ghi nhận, chỉ nêu khi đi cùng tin khác hoặc khi gom cụm. **(+)** là chiều cơ hội: **P2 (+)** cơ hội cần hành động trong 1–3 tháng; **P3 (+)** cơ hội chậm hoặc nhỏ, chỉ ghi nhận; cơ hội luôn kèm mặt trái theo `fear_greed/fg_01_dual_lens.md`. Ở cột tác động, **(+)** là tác động của các keyword cơ hội. Tin khớp nhiều keyword → lấy mức cao nhất. Cột hành vi khuyến nghị gồm việc con người cần làm và dữ liệu cần kiểm tra để chạy what-if, stress test; các con số trong kịch bản là tham số giả định, không phải dự báo.
**Tài khoản & Gói giải pháp**
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `SME-ACC-01` | Tài khoản doanh nghiệp | `LQ` `FR` `CO` | **P1:** email giả đối tác (BEC), chiếm quyền tài khoản<br>**P2:** dòng tiền giảm, bị chậm thanh toán; AML | **P1:** chuyển tiền nhầm cho đối tượng lừa đảo (`X04`)<br>**P2:** số dư giảm; giao dịch bất thường | **Con người:** cảnh báo BEC cho kế toán DN; gọi xác nhận khi đổi người thụ hưởng; rà giao dịch bất thường<br>**Dữ liệu, what-if:** đổi người thụ hưởng trước kỳ thanh toán lớn (`X04`); dòng tiền vào theo khách; what-if: dòng tiền vào −30% |
| `SME-ACC-02` | Tài khoản vốn | `CO` `MR` | **P2:** quy định đầu tư nước ngoài, ngoại hối; FDI rút<br>**P3 (+):** FDI tăng, dịch chuyển chuỗi cung ứng | **P2:** dòng vốn FDI/góp vốn dừng<br>**(+):** dòng vốn mới | **Con người:** giải thích quy định mới cho DN có vốn nước ngoài<br>**Dữ liệu, what-if:** dòng vốn góp theo quốc gia nhà đầu tư; what-if: FDI vào ngành −30% |
| `SME-ACC-03` | Tài khoản giữ hộ thương mại | `RP` `CO` | **P2:** tranh chấp hợp đồng mua bán, đối tác vỡ nợ | **P2:** tranh chấp giải ngân giữ hộ | **Con người:** pháp chế hỗ trợ khi có tranh chấp giữ hộ<br>**Dữ liệu, what-if:** số tài khoản giữ hộ đang tranh chấp |
| `SME-ACC-04` | Tài khoản giữ hộ bất động sản | `RP` `CO` | **P1:** dự án bị dừng, thanh tra<br>**P2:** pháp lý giao dịch BĐS | **P1:** phong tỏa<br>**P2:** tranh chấp | **Con người:** rà tài khoản giữ hộ ở dự án có tin xấu<br>**Dữ liệu, what-if:** giá trị giữ hộ theo dự án; what-if: dự án bị dừng |
| `SME-ACC-05` | Tài khoản ký quỹ | `CO` `MR` | **P2:** bảo lãnh bị gọi, giao dịch có điều kiện tranh chấp | **P2:** ký quỹ bị phong tỏa/giải tỏa đột ngột | **Con người:** rà điều kiện ký quỹ khi bảo lãnh bị gọi<br>**Dữ liệu, what-if:** ký quỹ theo khách, bảo lãnh tương ứng |
| `SME-PKG-01` | BusinessOne Plus / Connect / Premium | `BR` | **P3:** hoạt động DN giảm, cắt giảm chi phí | **P3:** hạ gói, đóng gói | **Con người:** RM hỏi lý do hạ gói (dấu hiệu thu hẹp)<br>**Dữ liệu, what-if:** số DN hạ gói theo ngành |
| `SME-PKG-02` | MerchantOne | `BR` `OR` | **P2:** doanh thu bán lẻ giảm, sức mua yếu (cạnh `L06`)<br>**P3 (+):** mùa mua sắm | **P2:** giảm giao dịch nhận tiền<br>**(+):** giao dịch tăng | **Con người:** tư vấn bán hàng đa kênh cho DN có giao dịch giảm<br>**Dữ liệu, what-if:** giao dịch nhận tiền theo MCC, địa bàn; what-if: −30% |
| `SME-REV-01` | SoftPOS; liên kết phần mềm bán hàng | `OR` `FR` | **P1:** gian lận thẻ, sự cố<br>**P2:** sức mua giảm | **P1:** chargeback, gián đoạn<br>**P2:** doanh số giảm | **Con người:** khóa điểm bán nghi gian lận<br>**Dữ liệu, what-if:** chargeback theo điểm bán |

**Thanh toán**
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `SME-PAY-01` | Thanh toán tiền hàng hóa, dịch vụ | `FR` `OR` | **P1:** BEC, đổi tài khoản thụ hưởng; sự cố | **P1:** chuyển nhầm/lừa đảo (`X04`); thanh toán chậm | **Con người:** gọi xác nhận giao dịch lớn đi người thụ hưởng mới; hướng dẫn quy trình hai người duyệt<br>**Dữ liệu, what-if:** `X04`, thời gian từ đổi thụ hưởng tới thanh toán; what-if: một chiến dịch BEC nhắm DN xuất khẩu |
| `SME-PAY-02` | Thẻ tín dụng DN (Visa Business Platinum) | `CR` `FR` | **P1:** lộ dữ liệu thẻ<br>**P2:** dòng tiền DN giảm | **P1:** giao dịch gian lận<br>**P2:** dư nợ thẻ tăng, chậm trả | **Con người:** khóa thẻ nghi lộ dữ liệu; RM liên hệ DN chậm trả<br>**Dữ liệu, what-if:** dư nợ thẻ DN theo ngành; what-if: dòng tiền DN −30% |
| `SME-PAY-03` | Thẻ thanh toán DN | `FR` | **P1:** gian lận thẻ, lộ dữ liệu thẻ | **P1:** giao dịch trái phép, tra soát | **Con người:** khóa thẻ nghi lộ dữ liệu<br>**Dữ liệu, what-if:** giao dịch gian lận theo cụm |
| `SME-PAY-04` | Giao dịch ngoại tệ | `MR` `CO` | **P2:** tỷ giá, USD tăng; quy định ngoại hối<br>**P3 (+):** USD tăng với DN xuất khẩu | **P2:** chi phí nhập khẩu tăng<br>**(+):** doanh thu xuất khẩu quy đổi tăng, nhu cầu bán ngoại tệ (`O3`) | **Con người:** tư vấn phòng ngừa tỷ giá gắn với hợp đồng thương mại thật<br>**Dữ liệu, what-if:** trạng thái ngoại tệ theo DN, ngành; what-if: USD/VND +5% |
| `SME-PAY-05` | Thanh toán hóa đơn | `OR` | **P1:** sự cố<br>**P3:** đổi nhà cung cấp dịch vụ | **P1:** hóa đơn trễ hạn<br>**P3:** giảm giao dịch | **Con người:** thông báo sự cố<br>**Dữ liệu, what-if:** tỷ lệ giao dịch lỗi |
| `SME-PAY-06` | Thanh toán lương | `CR` (gián tiếp) `BR` | **P1:** DN chậm hoặc giảm lương<br>**P2:** thuế quan, mất đơn, đơn hàng giảm<br>**P3 (+):** tuyển dụng mới | **P1:** trả lương trễ/giảm = DN căng thẳng, lan sang nhân viên (tín hiệu then chốt cạnh `L02`, `S01`)<br>**P2:** quỹ lương giảm dần<br>**(+):** tài khoản lương mới | **Con người:** RM gọi DN trả lương trễ hoặc giảm người; rà khoản vay của nhân viên DN đó; không thu hồi đồng loạt<br>**Dữ liệu, what-if:** lô lương theo DN (`S01`); số nhân viên có khoản vay; what-if: DN giảm 30% nhân sự |
| `SME-PAY-07` | Chuyển tiền đi nước ngoài | `CO` `MR` | **P1:** trừng phạt<br>**P2:** AML, tỷ giá | **P1:** giao dịch bị giữ lại<br>**P2:** rà soát, chi phí tăng | **Con người:** tạm giữ, rà soát giao dịch nghi trừng phạt<br>**Dữ liệu, what-if:** giao dịch theo quốc gia; what-if: thêm quốc gia bị trừng phạt |
| `SME-PAY-08` | Chuyển tiền nộp ngân sách nhà nước | `CO` | **P2:** thay đổi thuế, hóa đơn<br>**P3:** lịch nộp thuế | **P2:** nộp thuế chậm = dấu hiệu thiếu tiền (`S10`)<br>**P3:** giao dịch dồn kỳ | **Con người:** RM hỏi DN nộp thuế chậm (dấu hiệu thiếu tiền); hướng dẫn quy định thuế mới<br>**Dữ liệu, what-if:** nộp NSNN theo kỳ (`S10`) |

**Tiền gửi, Ngân hàng số, Vay, Bảo lãnh, Bảo hiểm**
| Mã | Sản phẩm | Rủi ro chính | Nhạy với sự kiện | Chiều tác động khi sự kiện xấu | Hành vi khuyến nghị khi xảy ra |
|---|---|---|---|---|---|
| `SME-DEP-01` | Tiền gửi có kỳ hạn / linh hoạt | `LQ` | **P2:** cần vốn lưu động, đơn hàng giảm<br>**P3:** lãi suất | **P2:** tất toán sớm<br>**P3:** kỳ hạn ngắn lại | **Con người:** tư vấn vốn lưu động thay vì tất toán khi phù hợp<br>**Dữ liệu, what-if:** tất toán sớm theo ngành; what-if: 20% tiền gửi SME rút trong 1 tháng |
| `SME-DEP-02` | Chứng chỉ tiền gửi Bảo Lộc | `LQ` `MR` | **P1:** tin đồn về ngân hàng<br>**P2:** lãi suất | **P1:** yêu cầu bán lại<br>**P2:** không mua mới | **Con người:** kịch bản trả lời tin đồn<br>**Dữ liệu, what-if:** yêu cầu bán lại theo ngày |
| `SME-DIG-01` | Techcombank Business; F@st EBank | `OR` `FR` | **P1:** sự cố, chiếm quyền truy cập; giai đoạn chuyển đổi nền tảng | **P1:** không chi lương/thanh toán đúng hạn; chuyển tiền trái phép (`X03`) | **Con người:** thông báo sự cố; hỗ trợ chi lương thay thế; cảnh báo chiếm quyền truy cập<br>**Dữ liệu, what-if:** đăng nhập thiết bị, IP lạ (`X03`); what-if: nền tảng gián đoạn vào ngày chi lương |
| `SME-LN-01` | Giải pháp tín dụng linh hoạt (Hybrid) | `CR` `CL` | **P2:** doanh thu giảm do thuế quan, giá đầu vào, cước vận tải, sức mua (xem file ngành)<br>**P3:** TSBĐ giảm giá | **P2:** DPD<br>**P3:** LTV xấu đi | **Con người:** RM rà DN trong ngành bị chạm (file ngành); tư vấn cơ cấu sớm; không cắt hạn mức đồng loạt<br>**Dữ liệu, what-if:** dư nợ theo ngành, thị trường xuất khẩu; what-if: doanh thu ngành −20–30%, lãi suất +2 điểm % |
| `SME-LN-02` | Tín dụng kết nối Misa Lending | `CR` `OR` | **P1:** sự cố, lộ dữ liệu ở đối tác dữ liệu (`L13`)<br>**P2:** dữ liệu kế toán bị thao túng | **P1:** gián đoạn xét duyệt<br>**P2:** hạn mức dựa trên dữ liệu sai lệch | **Con người:** tạm dùng thẩm định thủ công khi đối tác dữ liệu có sự cố<br>**Dữ liệu, what-if:** đối chiếu dữ liệu kế toán với dòng tiền thực qua tài khoản; what-if: dữ liệu sai lệch 20% |
| `SME-LN-03` | Giải pháp tín dụng B1CP | `CR` | **P2:** dòng tiền giảm | **P2:** DPD | **Con người:** RM rà dòng tiền DN<br>**Dữ liệu, what-if:** dòng tiền vào/ra; what-if: −30% |
| `SME-GTE-01` | Bảo lãnh mua sắm công | `CR` `CO` | **P1:** điều tra sai phạm đấu thầu<br>**P2:** chậm giải ngân vốn đầu tư công (cạnh `L12`)<br>**P3 (+):** đầu tư công tăng | **P1:** bị yêu cầu thực hiện bảo lãnh<br>**P2:** nhà thầu thiếu vốn, gia hạn bảo lãnh<br>**(+):** nhu cầu bảo lãnh tăng (`O3`) | **Con người:** rà bảo lãnh của nhà thầu dự án bị điều tra; liên hệ chủ đầu tư công<br>**Dữ liệu, what-if:** giá trị bảo lãnh theo dự án, chủ đầu tư; what-if: 10% bảo lãnh bị gọi |
| `SME-INS-01` | BH sức khỏe nhóm; BH toàn diện | `INS` | **P1:** cháy nổ, thiên tai<br>**P2:** dịch bệnh | **P1:** claim lớn<br>**P2:** claim sức khỏe tăng | **Con người:** hỗ trợ hồ sơ bồi thường<br>**Dữ liệu, what-if:** hợp đồng theo khu công nghiệp, vùng; what-if: cháy một khu xưởng |

## (e) Lan ra phân khúc khác

| Hướng lan | Kênh | Cơ chế | Độ trễ | Tín hiệu kiểm chứng | Chiều cơ hội |
|---|---|---|---|---|---|
| → KHCN chủ DN | `L01` | Chủ DN rút tiết kiệm, tăng thấu chi cá nhân để bơm cho DN; bảo lãnh cá nhân bị gọi | Ngay – 1 tháng | `S12` `S06` | – |
| → KHCN nhân viên | `L02` | Chậm lương, cắt giảm nhân sự → vay tiêu dùng, thẻ của nhân viên | 1–2 tháng | `S01` `S04` `S05` | Tuyển dụng → tài khoản lương mới |
| → HKD | `L03` `L06` | SME chậm trả nhà cung cấp HKD; SME bán lẻ giảm kéo theo hộ quanh đó | 1–2 tháng | `S02` | SME tăng trưởng → đơn hàng HKD tăng |
| → DN lớn | `L03` | SME là spoke trong chuỗi SCF: SME chậm trả anchor, hoặc anchor gặp khó kéo SME | 1–2 tháng | `S11` | Anchor mở rộng → SME có thêm đơn |
| → Nhà nước, mua sắm công | `L12` | Chậm giải ngân đầu tư công → bảo lãnh bị gọi, nhà thầu thiếu vốn; nộp NSNN chậm | 1–3 tháng | `S10` | Đầu tư công tăng → nhu cầu bảo lãnh, vốn lưu động |
| → Cấp ngân hàng | `L10` | Lừa đảo BEC, tài khoản DN bị lợi dụng; nợ xấu SME tập trung theo ngành | Tuần – tháng | `X04` `X01` | – |

Mức chắc chắn giảm theo số bước lan (`core/04_reasoning_procedure.md`); mỗi hướng lan ghi rõ độ trễ và tín hiệu kiểm chứng khi đưa vào bài viết.

## (f) Danh mục sản phẩm & URL nguồn (chốt 26/10/2026)

Nguồn: https://techcombank.com/ho-kinh-doanh-va-doanh-nghiep-nho/doanh-nghiep-nho

- Tài khoản: Tài khoản DN · Tài khoản vốn · Giữ hộ thương mại · Giữ hộ BĐS · Ký quỹ
- Gói giải pháp: BusinessOne Plus · BusinessOne Connect · BusinessOne Premium · MerchantOne
- Quản lý doanh thu: SoftPOS · Liên kết phần mềm bán hàng
- Thanh toán: Hàng hóa dịch vụ · Thẻ tín dụng DN (Visa Business Platinum) · Thẻ thanh toán DN · Giao dịch ngoại tệ · Thanh toán hóa đơn · Thanh toán lương · Chuyển tiền đi nước ngoài · Nộp NSNN
- Tiền gửi: Có kỳ hạn · Linh hoạt · CCTG Bảo Lộc
- Ngân hàng số: Techcombank Business · F@st EBank
- Vay: Tín dụng linh hoạt (Hybrid) · Kết nối Misa Lending · B1CP
- Bảo lãnh: Bảo lãnh mua sắm công
- Bảo hiểm: Sức khỏe nhóm · Toàn diện
- Dịch vụ khác: CDM · Đặt lịch hẹn
