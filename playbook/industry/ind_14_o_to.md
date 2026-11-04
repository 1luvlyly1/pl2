---
id: IND-14
code: I14
used_by: [Propagation, Product-Impact, Inside-out Monitor]
steps: [2, 3, 4]
depends_on: [industry/ind_00_index.md]
load_when: Tin về lệ phí trước bạ, thuế nhập khẩu ô tô, xe điện, chính sách hạn chế xe xăng, lãi suất vay mua xe, giá xăng, tiêu dùng nội địa, ưu đãi của hãng xe, giá xe cũ
version: v3.4
updated: 2026-11-04
---

# I14 – Ô tô, xe máy, xe điện

> Kiến thức nền định tính, không chứa số liệu. Mức phơi nhiễm của ngân hàng theo ngành cần truy vấn nội bộ.

## 1. Cấu trúc ngành ở Việt Nam
**Ô tô** gồm xe lắp ráp trong nước và xe nhập khẩu (nhiều từ ASEAN và Trung Quốc); xe điện tăng nhanh, có hãng trong nước; ô tô vẫn là tài sản có giá trị lớn với hộ gia đình. **Xe máy** là thị trường lớn, gần bão hòa ở đô thị; chính sách hạn chế xe xăng ở nội đô có thể thúc đẩy chuyển sang xe máy điện.

| Phân khúc | Ai tham gia | Vì sao nhạy cảm |
|---|---|---|
| DN lớn | Hãng lắp ráp, nhà nhập khẩu, hệ thống đại lý lớn | Cạnh tranh xe nhập; chi phí linh kiện nhập; chuyển đổi dây chuyền sang xe điện |
| SME | Đại lý, showroom xe cũ, garage | Tồn kho khi doanh số giảm hoặc hãng giảm giá; xe cũ mất giá |
| KHCN – hộ kinh doanh | Tiệm sửa xe, cửa hàng xe máy, phụ tùng, rửa xe | Garage xe xăng giảm việc khi xe điện tăng; cửa hàng xe máy theo thu nhập công nhân, nông hộ |
| KHCN – cá nhân | Người vay mua xe, tài xế công nghệ, taxi | Người chạy dịch vụ có thu nhập phụ thuộc giá xăng, phí nền tảng; xe mất giá nhanh |

**Đặc thù quan trọng với ngân hàng:** đại lý cần vốn lưu động lớn để nhập xe, thường qua chương trình tài trợ chuỗi do hãng giới thiệu (`L03`) – rủi ro tập trung theo hãng. Xe là tài sản bảo đảm mất giá nhanh, và cuộc đua giảm giá giữa các hãng làm giá trị tài sản bảo đảm của cả danh mục vay mua xe giảm cùng lúc. Nhu cầu nhạy với lãi suất, lệ phí, chính sách hãng.

## 2. Biến số nhạy cảm
| Biến số | Khi biến số xấu đi thì điều gì xảy ra | Ai bị chạm trước | Độ trễ | Ngành liên quan |
|---|---|---|---|---|
| Lệ phí trước bạ, thuế | Giảm lệ phí làm doanh số tăng mạnh trong thời gian áp dụng nhưng kéo cầu tương lai về hiện tại; hết ưu đãi thì doanh số giảm | Đại lý | Ngay | – |
| Lãi suất vay mua xe | Cầu giảm; người đã vay chịu áp lực trả nợ | Người vay, đại lý | Vài tháng | – |
| Chính sách xe điện, hạn chế xe xăng | Thúc đẩy xe điện; xe xăng cũ mất giá; garage truyền thống thiệt | Garage, người có xe xăng | Theo lộ trình | `I12` |
| Cuộc đua giảm giá giữa các hãng | Giá xe mới giảm kéo xe cũ và tài sản bảo đảm mất giá (`CL`) | Showroom xe cũ, ngân hàng | Nhanh | – |
| Giá xăng | Thu nhập tài xế công nghệ, taxi bị ép; cầu xe điện tăng | Tài xế vay mua xe | Nhanh | `I12` |
| Xe nhập giá rẻ | Cạnh tranh với xe lắp ráp; đại lý tồn kho | Hãng lắp ráp, đại lý | Vài tháng | – |
| Tiêu dùng nội địa | Người mua hoãn mua xe | Đại lý | Vài tháng | `I09` |
| USD mạnh | Xe nhập, linh kiện đắt hơn | Nhà nhập khẩu | Vài tháng | – |

## 3. Tác động theo đối tượng

### KHCN – cá nhân
**Thách thức.** Người vay mua xe để chạy dịch vụ chịu rủi ro thu nhập (giá xăng, cạnh tranh, phí nền tảng). Xe mất giá nhanh khi hãng giảm giá, làm phần đệm tài sản bảo đảm mỏng đi. Người mua ở cao điểm ưu đãi có thể vay vượt khả năng.

**Cơ hội.** Ưu đãi lệ phí và lãi suất kéo nhu cầu vay mua xe; chuyển sang xe điện cần vay và bảo hiểm.

### KHCN – hộ kinh doanh
**Thách thức.** Garage, tiệm sửa xe xăng giảm việc khi xe điện tăng; cửa hàng xe máy phụ thuộc thu nhập công nhân, nông hộ.

**Cơ hội.** Dịch vụ sửa xe điện, lắp sạc; mùa cao điểm cuối năm.

### SME
**Thách thức.** Đại lý tồn kho khi doanh số giảm hoặc hãng giảm giá; showroom xe cũ chịu xe mất giá.

**Cơ hội.** Mùa ưu đãi làm doanh số tăng, cần vốn nhập xe; mở đại lý xe điện.

### DN lớn
**Thách thức.** Cạnh tranh xe nhập; chi phí linh kiện nhập; chuyển đổi dây chuyền sang xe điện.

**Cơ hội.** Chính sách ưu đãi sản xuất trong nước; xe điện; đội xe cho DN vận tải, dịch vụ.

## 4. Sản phẩm ngân hàng liên quan
| Đối tượng | Phía rủi ro: sản phẩm và vì sao | Phía cơ hội: sản phẩm và điều kiện |
|---|---|---|
| KHCN | Vay mua ô tô `CN-LN-04` (`CR` khi thu nhập tài xế giảm, `CL` khi xe mất giá) | Vay mua xe mới (`O1`) với khả năng trả nợ rõ; bảo hiểm ô tô `CN-INS-03` (`O4`) |
| HKD | ShopCash `HKD-LN-01` của garage, cửa hàng xe máy | Vốn mở dịch vụ xe điện (`O1`), SoftPOS (`O3`) |
| SME | Vay `SME-LN-01` của đại lý nhỏ, showroom xe cũ | Vốn nhập xe mùa cao điểm (`O1`), thu hộ, thanh toán (`O3`) |
| DN lớn | Tài trợ chuỗi kinh doanh ô tô `CIB-SCF-01` (tập trung theo hãng), L/C nhập xe, linh kiện `CIB-TF-01` | Tài trợ đại lý, vay mua ô tô cho DN `CIB-LN-02`, phòng ngừa tỷ giá (`O1` `O3`) |
| Cấp ngân hàng | Giá trị tài sản bảo đảm là xe giảm theo cuộc đua giá (`CL`) | – |

## 5. Tín hiệu theo dõi
| Tín hiệu | Ý nghĩa với ngành này | Đo được bằng danh mục what-if |
|---|---|---|
| `S11` đại lý cùng một hãng chậm trả tài trợ chuỗi đồng loạt | Hãng có vấn đề hoặc tồn kho toàn hệ thống | Chưa có |
| `S05` người vay mua xe chuyển sang trả tối thiểu thẻ; quá hạn vay mua xe | Tài xế dịch vụ căng thu nhập | Có: thẻ và quá hạn theo khách có khoản vay mua xe (tên sản phẩm qua truy vấn khám phá) |
| Số hồ sơ vay mua xe trước khi hết ưu đãi lệ phí | Chiều cơ hội, cẩn trọng `G05` | Gần đúng: khoản vay mới theo tháng |
| `F03` bán gấp xe để trả nợ | Pha sợ | Gần đúng: tài sản biến mất giữa hai kỳ |
| LTV khoản vay mua xe | Đệm tài sản mỏng khi giá xe giảm | Có với giá trị tài sản bảo đảm theo loại tài sản (cần xác nhận cột giá trị) |

Luôn ghi "cần truy vấn dư nợ vay mua ô tô theo loại xe (xăng, điện), dư nợ tài trợ đại lý theo hãng".

## 6. Liên kết ngành
- **Thượng nguồn – `I02` (thép), `I13` (nhựa), `I04` (điện tử ô tô), nhập khẩu qua `I11`.**
- **Song song – `I12` (xăng, hạ tầng sạc).**
- **Khách hàng – `I11` vận tải, `I10` xe du lịch.**
- **Theo thu nhập – `I07` nông hộ mua xe khi được mùa.**

## 7. Điểm đảo chiều và lưu ý
- Ưu đãi lệ phí có thời hạn: doanh số tăng mạnh rồi giảm sau khi hết hạn; không coi đỉnh là xu hướng.
- Xe điện là cơ hội cho bên này và thách thức cho bên kia (garage xe xăng, xe cũ); nêu cả hai.
- Không suy ra giá xe hay chính sách của hãng cụ thể khi tin không nêu.
