---
id: CORE-RISK-CODES
used_by: [ALL]
steps: [3, 6]
depends_on: []
load_when: Luôn nạp – mọi agent dùng chung mã loại rủi ro khi gắn rủi ro cho sản phẩm
version: v3.4
updated: 2026-11-04
---

# Mã loại rủi ro dùng chung

Mỗi sản phẩm chịu rủi ro trong bài viết được gắn một hoặc vài mã dưới đây. Mã giúp người đọc biết rủi ro thuộc bộ phận nào xử lý và giúp code gom chỉ số. Chọn mã theo **cơ chế gây thiệt hại**, không theo tên sản phẩm: cùng là khoản vay mua nhà, khách mất thu nhập là `CR`, giá nhà giảm làm tài sản bảo đảm mỏng đi là `CL`.

| Mã | Loại rủi ro | Định nghĩa | Thường xuất hiện khi | Tín hiệu kiểm chứng điển hình | Dễ nhầm với |
|---|---|---|---|---|---|
| `CR` | Tín dụng | Khả năng trả nợ của khách giảm, dẫn tới quá hạn và nợ xấu | Thu nhập hay doanh thu của khách giảm; khoản trả tăng do lãi suất; chi phí đầu vào của DN tăng | `S01` lương giảm, `S04` dùng hạn mức tăng, `S05` trả tối thiểu thẻ, quá hạn tăng | `CL`: khách vẫn trả được nhưng tài sản bảo đảm giảm giá là `CL`, không phải `CR` |
| `CL` | Tài sản bảo đảm | Giá trị hoặc khả năng bán của tài sản bảo đảm giảm, làm phần đệm của ngân hàng mỏng đi | Giá BĐS, ô tô, hàng tồn kho, nông sản giảm; tài sản khó bán do pháp lý dự án | LTV vượt ngưỡng, `F03` bán gấp tài sản để trả nợ | `CR`: hai loại thường đi cùng nhau ở pha suy giảm; nêu cả hai nếu có |
| `LQ` | Thanh khoản, huy động | Tiền gửi rời ngân hàng hoặc chuyển sang dạng kém ổn định, làm chi phí vốn tăng hoặc thiếu tiền mặt cục bộ | Kênh đầu tư khác hấp dẫn hơn (vàng, chứng khoán); tin đồn; đối thủ tăng lãi suất huy động | `S06` tất toán trước hạn, `S07` rút tiền mặt, `F01` chuyển tiền gửi đi, `F02` chuyển sang kỳ hạn ngắn | `MR`: lãi suất thị trường đổi là `MR`; tiền gửi chảy đi vì lãi suất đó là `LQ` |
| `MR` | Thị trường | Giá trị vị thế của ngân hàng hoặc của khách thay đổi theo lãi suất, tỷ giá, giá chứng khoán, trái phiếu, hàng hóa | Fed, NHNN đổi lãi suất; USD mạnh; giá dầu, vàng biến động mạnh | `S15` MTM âm trên vị thế ngoại tệ của khách; trạng thái ngoại tệ của ngân hàng | `CR`: khách DN lỗ tỷ giá rồi không trả được nợ thì ghi cả `MR` và `CR` |
| `OR` | Vận hành, hệ thống | Gián đoạn hoặc lỗi trong quy trình, hệ thống, mạng lưới làm khách không giao dịch được | Sự cố ngân hàng số, thẻ, POS, CDM; sự cố đối tác công nghệ (`L13`); thiên tai làm chi nhánh đóng cửa | `S14` khiếu nại theo chủ đề, nhật ký sự cố | `FR`: lỗ hổng bị khai thác để chiếm đoạt tiền là `FR` đi cùng `OR` |
| `FR` | Gian lận, lừa đảo | Tiền của khách hoặc ngân hàng bị chiếm đoạt, hoặc tài khoản ngân hàng bị dùng làm mắt xích chuyển tiền lừa đảo | Làn sóng lừa đảo mạo danh; thủ đoạn mới từ nước khác (`L14`); gian lận thẻ, chứng từ thương mại | `S13` đăng nhập lạ, `X01`–`X08` | `CO`: tài khoản bị thuê mượn vừa là `FR` vừa là `CO` |
| `CO` | Tuân thủ, pháp lý, phòng chống rửa tiền | Ngân hàng vi phạm hoặc phải thực hiện quy định mới; giao dịch đáng ngờ; trừng phạt quốc tế | Quy định mới của NHNN, thuế; danh sách trừng phạt; yêu cầu xác thực mới | Giao dịch bị chặn, báo cáo giao dịch đáng ngờ, `S16` doanh thu HKD về tài khoản cá nhân | `RP`: vi phạm bị công bố thì thêm `RP` |
| `RP` | Danh tiếng, hành vi bán hàng | Niềm tin của khách, công chúng, nhà đầu tư giảm do sự cố, khiếu nại, cách bán hàng | Tranh chấp sản phẩm đầu tư, bảo hiểm; khiếu nại tập thể; tin lan trên mạng xã hội | `S14` khiếu nại, `S08` bán lại sản phẩm đầu tư theo một tổ chức phát hành | `BR`: mất khách lâu dài do mất niềm tin là `RP` dẫn tới `BR` |
| `BR` | Doanh thu, kinh doanh của ngân hàng | Thu nhập phí và giao dịch của ngân hàng giảm dù khách không gặp rủi ro tín dụng | Khách giảm chi tiêu thẻ, QR; HKD chuyển sang nhận tiền ở ngân hàng khác; bán chéo giảm | `S02` doanh thu QR, `S03` số người trả tiền | Rủi ro này thường là mức **P3** trong bảng (c) |
| `INS` | Bồi thường bảo hiểm | Số yêu cầu bồi thường của sản phẩm bảo hiểm phân phối qua ngân hàng tăng | Dịch bệnh, thiên tai, tai nạn hàng loạt | Yêu cầu bồi thường theo địa bàn | `RP`: từ chối bồi thường gây tranh cãi dẫn tới `RP` |

## Cách dùng trong bài viết
- Mã đặt trong ngoặc sau cụm từ tiếng Việt, ví dụ "rủi ro tín dụng (`CR`) và tài sản bảo đảm (`CL`) của khoản vay mua nhà". Bỏ mã đi câu vẫn phải đọc hiểu được.
- Một sản phẩm có thể mang nhiều mã. Ghi mã chính trước; mã phụ chỉ ghi khi cơ chế khác hẳn.
- Rủi ro ở cấp ngân hàng (`NH-`, `IR-`) dùng cùng bộ mã; xem `core/06_ngan_hang.md`.
