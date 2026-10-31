# [LAB02]

## Câu hỏi 1: Vì sao phải đồng bộ `master` trước khi tạo Pull Request?

Trong quá trình phát triển, nhánh `master` có thể đã được cập nhật bởi các Pull Request khác, trong khi nhánh tính năng vẫn dựa trên phiên bản `master` cũ. Vậy nên cần đồng bộ nhánh làm việc với `master` mới nhất trước khi gửi Pull Request

Việc này giúp:
- Phát hiện sớm các xung đột giữa những thay đổi
- Kiểm tra khả năng tương thích của tính năng với phiên bản mới nhất
- Tránh đưa code lỗi hoặc chưa được tích hợp đầy đủ vào `master`
- Giúp quá trình review và merge diễn ra thuận lợi hơn


## Câu hỏi 2: Khi nào không được rebase?

Không nên rebase những nhánh đã được chia sẻ với người khác hoặc những nhánh mà người khác đang dựa vào để phát triển, vì rebase tạo ra các commit mới với SHA khác, làm thay đổi lịch sử commit

Điều này có thể khiến lịch sử giữa các bản sao repository không còn thống nhất và gây khó khăn khi đồng bộ

Đặc biệt, không nên tùy tiện rebase các nhánh dùng chung như `master` hoặc `release/*`. Rebase phù hợp hơn với nhánh cá nhân chưa được chia sẻ, khi muốn sắp xếp lại lịch sử commit trước khi tích hợp

## Câu hỏi 3: `feature/*` khác `topic/*` ra sao?

Hai loại nhánh đều được tạo ra để thực hiện công việc độc lập với `master`, nhưng khác nhau về mục đích:

- **`feature/*`**: Dùng để phát triển chức năng mới của phần mềm. Ví dụ: `feature/cart-print` dùng để bổ sung chức năng in giỏ hàng, `feature/search-by-title` dùng để tìm kiếm DVD theo tên
- **`topic/*`**: Dùng cho những công việc theo một chủ đề cụ thể, không nhất thiết là phát triển chức năng mới. Ví dụ: `topic/pr-template` dùng để tạo mẫu Pull Request, `topic/use-case-diagram` dùng để bổ sung tài liệu sơ đồ Use Case
- Việc phân chia này giúp nhận biết mục đích của từng nhánh, quản lý công việc rõ ràng và dễ theo dõi lịch sử phát triển.