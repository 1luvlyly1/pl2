---
id: IND-11
code: I11
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về cước container, tuyến hàng hải gián đoạn, xung đột tại eo biển, giá dầu diesel, thuế quan (đẩy hàng trước hạn), sản lượng xuất nhập khẩu, hạ tầng cảng, đường cao tốc, thương mại điện tử, lừa đảo mạo danh giao hàng
version: v3.4
updated: 2026-11-04
---

# I11 – Logistics, vận tải, cảng, kho

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
Ngành gồm vận tải biển (phần lớn hàng xuất khẩu do hãng tàu nước ngoài chở), cảng (các cụm cảng nước sâu phía Bắc và phía Nam), vận tải đường bộ, kho bãi, giao nhận (forwarder), vận tải hàng không, giao hàng chặng cuối cho thương mại điện tử, và đường sắt, đường thủy nội địa với tỷ trọng nhỏ. Vùng chính là các hành lang cảng – khu công nghiệp ở phía Bắc và Đông Nam Bộ, cùng các cửa khẩu biên giới phía Bắc.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Khai thác cảng, kho, giao hàng | Công suất theo khối lượng xuất nhập khẩu; vay dài hạn cho hạ tầng |
| SME | Forwarder, vận tải container, kho lạnh | Forwarder ứng cước cho khách và bị chậm thu; vận tải chịu giá dầu; dễ bị email giả đổi tài khoản thanh toán |
| KHCN – hộ kinh doanh | Chủ xe tải, đầu kéo, xe ba gác | Biên mỏng, vay mua xe; giá dầu tăng là thiệt ngay vì cước nội địa điều chỉnh chậm |
| KHCN – cá nhân | Tài xế, shipper | Thu nhập theo chuyến; nhiều người vay mua xe; là đối tượng bị mạo danh trong lừa đảo giao hàng |

**Đặc thù quan trọng với ngân hàng:** doanh thu của ngành theo khối lượng hàng xuất nhập khẩu và thương mại điện tử, nên ngành là "nhiệt kế" của thương mại. Chi phí nhiên liệu chiếm tỷ trọng cao. Cước cao là hai chiều trong cùng một ngành: chủ hàng thiệt, forwarder và hãng tàu có biên cao hơn – nhưng cơ hội này thường ngắn.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Cước container quốc tế | Cước tăng làm chủ hàng xuất khẩu thiệt; forwarder, hãng tàu có biên cao hơn; cước giảm nhanh làm ai đã thuê tàu, container giá cao lỗ | Chủ hàng xuất khẩu | Vài tuần | `I03` `I05` `I07` |
| Tuyến hàng hải bị gián đoạn (xung đột, eo biển) | Tàu đi vòng, thời gian giao dài hơn, cước tăng, thiếu container rỗng | Chủ hàng, forwarder | Vài tuần | Xem `examples/ex_NW_01_xung_dot_trung_dong.md` |
| Giá dầu diesel | Chủ xe tải, hộ vận tải bị ép biên ngay vì cước nội địa điều chỉnh chậm | Hộ vận tải, tài xế | Ngay | `I12` |
| Khối lượng xuất nhập khẩu | Thuế quan, đơn hàng giảm làm kho, cảng giảm công suất; pha đẩy hàng trước hạn áp thuế tạo đỉnh tạm thời | Cảng, kho, forwarder | Một quý | – |
| Đầu tư hạ tầng (cao tốc, cảng) | Chiều tích cực: giảm chi phí, mở tuyến mới | DN cảng, vận tải | Dài | `I02` |
| Thương mại điện tử | Tăng thì giao hàng chặng cuối tăng | Shipper, DN giao hàng | Nhanh | `I09` |
| Biên mậu Trung Quốc | Đóng, siết làm xe ùn ở cửa khẩu | Hộ vận tải, thương lái | Ngay | `I07` |
| Bão lũ | Tuyến bị gián đoạn, cảng đóng | Vận tải vùng bão | Ngay | – |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Tài xế, shipper vay mua xe chịu áp lực khi giá dầu tăng hoặc ít chuyến. Shipper bị kẻ gian mạo danh, và người dân bị lừa qua tin nhắn giả đơn vị giao hàng.

**Cơ hội.** Thương mại điện tử tăng kéo thu nhập shipper tăng; tuyến mới cần tuyển tài xế.

### KHCN – hộ kinh doanh
**Thách thức.** Chủ xe tải nhỏ có biên mỏng, đang vay mua xe; giá dầu tăng là thiệt ngay.

**Cơ hội.** Đầu tư công, khu công nghiệp mới làm tăng nhu cầu chở vật liệu, hàng hóa.

### SME
**Thách thức.** Forwarder ứng cước cho khách rồi bị chậm thu; vận tải container chịu giá dầu; bị email giả yêu cầu đổi tài khoản thanh toán.

**Cơ hội.** Cước cao làm doanh thu forwarder tăng; kho lạnh cho nông sản, thủy sản; vốn mua xe, đầu kéo mới.

### DN lớn
**Thách thức.** Cảng giảm công suất khi xuất nhập khẩu giảm; đầu tư hạ tầng vay dài hạn chịu lãi suất.

**Cơ hội.** FDI và thương mại tăng; trung tâm logistics mới; vay dự án hạ tầng.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay mua ô tô `CN-LN-04`, vay tiêu dùng `CN-LN-06` của tài xế, shipper (thu nhập theo chuyến); gian lận (`FR`) mạo danh giao hàng | Thẻ, tài khoản (`O3`), bảo hiểm (`O4`) theo nhu cầu thật |
| HKD | ShopCredit `HKD-LN-02` của chủ xe tải (giá dầu ép biên) | Vốn mua xe, vốn lưu động (`O1`), QR (`O3`) |
| SME | Vay `SME-LN-01`, thẻ DN `SME-PAY-02` trả nhiên liệu | Vốn lưu động (`O1`), chuyển tiền quốc tế `SME-PAY-07`, ngoại tệ `SME-PAY-04` (`O3`) |
| DN lớn | Vay dự án `CIB-LN-02`, vốn lưu động `CIB-LN-01` | Tài trợ vận chuyển hàng không `CIB-SCF-01`, bảo lãnh `CIB-TF-04`, thu hộ `CIB-COL-01` (`O1` `O3`) |
| Cấp ngân hàng | Tin nhắn mạo danh giao hàng (`FR`, `X08`) | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S10` hóa đơn cảng, phí hạ tầng cảng biển của khách xuất nhập khẩu | Khối lượng hàng qua cảng | Chưa có |
| `S04` hạn mức của hộ vận tải tăng khi giá dầu tăng | Hộ vận tải thiếu tiền nhiên liệu | Có với thẻ, thấu chi cá nhân của chủ hộ |
| Dòng ra ngoại tệ trả cước tăng | Chiều cơ hội cho forwarder | Gần đúng: tỷ lệ giao dịch ngoại tệ của DN |
| `X04` đổi tài khoản thụ hưởng trước kỳ thanh toán; `X08` tin nhắn mạo danh giao hàng | Lừa đảo | Chưa có |

Luôn ghi "cần truy vấn dư nợ vận tải theo loại hình, số khoản vay mua xe tải".

## 6. Liên kết ngành
- **Đầu vào – `I12` nhiên liệu.**
- **Khách hàng của ngành – `I03` `I04` `I05` `I06` `I07` xuất khẩu, `I09` thương mại điện tử:** khối lượng của họ là doanh thu của logistics.
- **Song song – `I02` hạ tầng, `I14` xe tải và đầu kéo.**

## 7. Điểm đảo chiều và lưu ý
- Cước cao là cơ hội cho forwarder nhưng thường ngắn; khi cước giảm nhanh, ai ký thuê tàu, container giá cao sẽ lỗ.
- Tin xung đột hàng hải tác động qua ba kênh cùng lúc – cước, thời gian giao hàng, giá dầu; nêu cả ba.
- Với tin gian lận mạo danh giao hàng, chỉ mô tả ở mức nhận diện.
