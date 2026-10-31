# [LAB01]

## Câu hỏi 1: cấu hình --global được lưu ở đâu? Khác gì so với --local?
+ Cấu hình --global được lưu trong file .gitconfig ở thư mục home của người dùng 
+ Cấu hình --local được lưu trong file
+ --global là cấu hình chung cho user, còn --local là cấu hình riêng cho từng repository (Có phạm vi áp dụng lên repository hiện tại). Khi hai cấu hình trùng một khóa (Có phạm vi áp dụng lên toàn bộ repository), --local được ưu tiên hơn --global


## Câu hỏi 2: Vì sao dùng git mv? release/lab01 có phải baseline? Vì sao không commit thẳng master dù làm một mình?
+ Vì git mv thuận tiện hơn mv. Nếu dùng mv dvd.py aims/dvd.py thì Git sẽ  phát hiện file bị xóa ở vị trí cũ và xuất hiện ở vị trí mới và ta phải git add -A để đưa thay đổi vào staging. Nếu dùng git mv dvd.py aims/dvd.py thì Git di chuyển file và đưa thay đổi vào staging ngay. Còn nếu sử dụng cách xóa rồi tạo mới thì sẽ dễ gây ra nguy cơ mất dữ liệu và có quá nhiều thao tác không cần thiết
+ Branch release/lab01: Chỉ là 1 nhánh phục vụ cho việc phát triển hoặc duy trì phiên bản Lab 01 thôi chứ chưa chắc đã là baseline (Nhưng nó cũng có thể có khả năng làm baseline trong tương lai)
+ Có thể làm thế khi làm việc một mình do khi commit xong mà bị lỗi thì cũng k làm ảnh hưởng đến ai cả vì nhóm có mỗi mình nhưng nên tạo branch riêng để có thể chứa những thay đổi mới, có thể kiểm thử những ý tưởng mới và sửa lỗi nó mà không làm ảnh hưởng đến master, khi đã ổn thì mới merge và chúng ta cũng nên tập thói quen đó do những project sau này sẽ cần làm với đội nhóm chứ không phải lúc nào cũng có thể làm cá nhân