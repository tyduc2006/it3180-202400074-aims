# [LAB03]

## Câu hỏi 1: Merge base là gì?

Merge base là commit chung gần nhất trong lịch sử của hai branch. Git sử dụng merge base làm điểm tham chiếu để xác định những thay đổi trên mỗi branch khi thực hiện merge.

Ví dụ: Hai branch `master` và `feature` cùng phát triển từ commit B. Sau đó, mỗi branch có những commit mới riêng. Khi merge, Git sử dụng commit B làm merge base để so sánh và kết hợp các thay đổi.

## Câu hỏi 2: Vì sao master/release/* phải dùng revert?

Các branch `master` và `release/*` thường là những branch đã được chia sẻ và có thể có nhiều người cùng làm việc. Vì vậy, cần hạn chế thay đổi lịch sử chung.

- **`git reset`:** Di chuyển con trỏ branch về commit cũ hơn, làm thay đổi lịch sử branch.
- **`git revert`:** Tạo một commit mới để đảo ngược thay đổi của commit trước đó mà vẫn giữ nguyên lịch sử.

Do đó, nên sử dụng `git revert` trên `master` và `release/*` vì nó giúp giữ lịch sử đã chia sẻ, tránh ảnh hưởng đến những người khác và dễ dàng đồng bộ giữa các thành viên.