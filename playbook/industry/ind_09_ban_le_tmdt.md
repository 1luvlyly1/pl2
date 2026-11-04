---
id: IND-09
code: I09
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về tiêu dùng nội địa, lạm phát, thuế và hóa đơn với hộ kinh doanh, quy định giờ kinh doanh, thương mại điện tử, hàng nhập giá rẻ xuyên biên giới, lừa đảo mua sắm online, mặt bằng bán lẻ, mùa lễ Tết, thu nhập công nhân
version: v3.4
updated: 2026-11-04
---

# I09 – Bán lẻ và thương mại điện tử

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Bán lẻ có ba kênh. **Kênh truyền thống** (chợ, tạp hóa, cửa hàng nhỏ) vẫn chiếm phần lớn và chủ yếu là hộ kinh doanh. **Kênh hiện đại** (chuỗi siêu thị, cửa hàng tiện lợi, điện máy, dược phẩm, thời trang) do DN lớn vận hành. **Thương mại điện tử** và bán qua mạng xã hội, livestream có rất nhiều người bán nhỏ là hộ kinh doanh hoặc cá nhân. Thanh toán chuyển dịch nhanh sang QR, thẻ, ví.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Chuỗi bán lẻ | Cạnh tranh giá, chi phí thuê mặt bằng, biên mỏng |
| SME | Cửa hàng, nhà phân phối, người bán online có quy mô | Tồn kho khi tiêu dùng yếu; phí sàn tăng; cạnh tranh với hàng nhập giá rẻ |
| KHCN – hộ kinh doanh | Tạp hóa, sạp chợ, cửa hàng mặt phố, người bán online | Không có đệm vốn; chi phí tuân thủ thuế, hóa đơn; thuê mặt bằng theo giá cố định |
| KHCN – cá nhân | Người tiêu dùng (đầu ra của ngành); người bán online cá nhân | Thu nhập quyết định doanh thu ngành; bị lừa mua sắm online |

**Đặc thù quan trọng với ngân hàng:** dòng tiền QR của hộ kinh doanh là nơi tác động tiêu dùng hiện ra sớm nhất trong dữ liệu ngân hàng. Chính sách thuế với hộ kinh doanh (bỏ thuế khoán, tự kê khai, hóa đơn điện tử) và quy định quản lý đô thị (giờ hoạt động, vỉa hè) đang thay đổi, có thể làm doanh thu giảm mà không phải do tiêu dùng yếu. Hộ kinh doanh mặt phố thuê mặt bằng chịu áp lực kép khi doanh thu giảm mà giá thuê chưa giảm theo; làn sóng trả mặt bằng là triệu chứng, không phải nguyên nhân. Mùa vụ: Tết, các dịp khuyến mãi cuối năm, mùa tựu trường.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Thu nhập, việc làm, niềm tin tiêu dùng | Doanh thu giảm, hộ kinh doanh chịu trước vì không có đệm (`L06`) | Hộ kinh doanh | Một đến hai tháng | `I03` `I04` |
| Lạm phát, giá xăng | Chi tiêu chuyển sang hàng thiết yếu, hàng không thiết yếu giảm | Cửa hàng hàng không thiết yếu | Vài tuần | `I12` |
| Chính sách thuế, hóa đơn với hộ kinh doanh | Chi phí tuân thủ tăng; một số hộ ngừng kinh doanh hoặc chuyển dòng tiền sang tài khoản cá nhân; khách cần hóa đơn bỏ hộ nhỏ | Hộ kinh doanh nhỏ | Theo hiệu lực | Cơ hội chuyển đổi lên DN (`L07`) |
| Quy định giờ hoạt động, tiếng ồn, vỉa hè ở đô thị | Doanh thu buổi tối, doanh thu từ không gian vỉa hè giảm ở khu vực áp dụng | Hộ ăn uống, bán lẻ mặt phố | Theo hiệu lực | `I10` |
| Giá thuê mặt bằng | Doanh thu giảm mà giá thuê chưa giảm làm hộ trả mặt bằng; chủ nhà mất thu nhập cho thuê | Hộ mặt phố, chủ nhà phố | Vài tháng | `I01` |
| Thuế, quản lý người bán trên sàn | Người bán nhỏ rời sàn hoặc chuyển kênh | Người bán online | Theo hiệu lực | – |
| Hàng nhập giá rẻ xuyên biên giới | Người bán, nhà sản xuất trong nước mất khách | Người bán online, SME | Nhanh | `I03` |
| Khách du lịch | Khách tăng kéo bán lẻ ở khu du lịch, trung tâm thương mại | Cửa hàng khu du lịch | Theo mùa | `I10` |
| Lãi suất, tín dụng tiêu dùng | Lãi thấp kéo mua trả góp điện máy, điện thoại | Chuỗi điện máy | Vài tháng | – |
| Lừa đảo mua sắm online | Mất niềm tin, tranh chấp | Người mua, người bán online | Nhanh | Tin `GL` |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Người mua online bị lừa đảo, mua phải hàng giả. Chi tiêu thẻ, trả góp vượt khả năng ở mùa mua sắm. Người bán online cá nhân chịu chi phí thuế, phí sàn tăng.

**Cơ hội.** Ưu đãi thẻ, hoàn tiền mùa mua sắm; thu nhập phụ từ bán online.

### KHCN – hộ kinh doanh
**Thách thức.** Doanh thu giảm khi tiêu dùng yếu và mất khách vào chuỗi, sàn. Chi phí tuân thủ thuế, hóa đơn tăng. Hộ mặt phố ở đô thị lớn chịu thêm quy định giờ hoạt động, vỉa hè và giá thuê; khi nhiều áp lực dồn lại, hộ trả mặt bằng. Tài khoản người bán có thể bị chiếm đoạt.

**Cơ hội.** Số hóa (QR, phần mềm bán hàng) làm dòng tiền minh bạch, mở đường vay theo doanh thu; chuyển đổi lên DN; mùa Tết cần vốn nhập hàng.

### SME
**Thách thức.** Tồn kho khi tiêu dùng yếu; cạnh tranh giá với hàng nhập; phí sàn tăng.

**Cơ hội.** Mở cửa hàng, kênh online nhiều sàn; vốn lưu động mùa cao điểm; nhận thanh toán đa kênh.

### DN lớn
**Thách thức.** Cạnh tranh giá, chi phí thuê mặt bằng, biên lợi nhuận mỏng.

**Cơ hội.** Chiếm thị phần từ kênh truyền thống; mở rộng chuỗi ở tỉnh; chi lương, thu hộ lớn.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Thẻ tín dụng `CN-CARD-01`, trả góp `CN-LN-06`, MyCash `CN-LN-05` (chi tiêu vượt khả năng); gian lận (`FR`) mua sắm online | Chi tiêu thẻ (`O3`), ưu đãi `CN-LOY-01` |
| HKD | ShopCash `HKD-LN-01`; doanh thu QR `HKD-REV-01` `HKD-REV-02` giảm; vay thế chấp nhà phố của chủ nhà cho thuê | Vay theo dòng tiền (`O1`) khi dòng tiền ổn định; Soundbox, SoftPOS `HKD-REV-03`, tài khoản hộ `HKD-ACC-01` (`O3` `O6`) |
| SME | Vay `SME-LN-01`, Misa Lending `SME-LN-02` | MerchantOne `SME-PKG-02`, SoftPOS `SME-REV-01` (`O3`), vốn mùa Tết (`O1`) |
| DN lớn | Vốn lưu động `CIB-LN-01` | Thu hộ `CIB-COL-01`, chi lương `CIB-PAY-06`, thẻ DN (`O3` `O2`) |
| Cấp ngân hàng | Doanh thu phí QR, thẻ giảm (`BR`); tài khoản trung gian cho lừa đảo (`FR`) | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S02` doanh thu QR, POS theo ngành điểm bán và địa bàn; `S03` số người trả tiền | Sức mua và lượng khách | Chưa có – đây là thiếu hụt lớn nhất cho ngành này |
| `S16` doanh thu hộ kinh doanh chảy về tài khoản cá nhân | Phản ứng với chính sách thuế, không phải tiêu dùng yếu | Chưa có |
| `S04` `S05` thẻ, thấu chi cá nhân sau mùa mua sắm | Chi tiêu vượt khả năng | Có |
| LTV khoản vay thế chấp nhà phố theo tuyến | Giá thuê, giá nhà phố giảm khi trả mặt bằng lan rộng | Gần đúng: theo tỉnh và loại tài sản, không có tuyến phố |
| `X01` tài khoản mới nhận tiền nhiều nguồn rồi chuyển đi; `X02` báo lừa đảo mua sắm | Lừa đảo | Chưa có |

Luôn ghi "cần truy vấn số hộ kinh doanh bán lẻ theo ngành điểm bán, xu hướng doanh thu QR theo quý".

## 6. Liên kết ngành
- **Thượng nguồn – `I08` (hàng tiêu dùng nhanh), `I03` (thời trang), `I04` (điện máy, điện thoại).**
- **Song song – `I11` (giao hàng chặng cuối), `I10` (bán lẻ du lịch, ăn uống), `I17` (nền tảng), `I01` (mặt bằng nhà phố).**
- **Đầu vào thu nhập – việc làm ở `I03` `I04` (khu công nhân).**

## 7. Điểm đảo chiều và lưu ý
- Thay đổi thuế có thể làm doanh thu QR giảm mà không phải do tiêu dùng yếu; phân biệt bằng `S16`.
- Quy định về giờ hoạt động hay vỉa hè thường áp dụng theo từng địa phương; không mở rộng sang tỉnh khác khi tin không nêu, và không viết thành "cấm hộ kinh doanh hoạt động" khi quy định chỉ áp cho một số loại hình.
- Trả mặt bằng hàng loạt là triệu chứng của nhiều nguyên nhân dồn lại; khi gặp, tìm các nguyên nhân (quy định, thuế, sức mua, thương mại điện tử) thay vì coi là nguyên nhân.
- Không mô tả thủ đoạn lừa đảo chi tiết (`guardrails.md` mục 15).
