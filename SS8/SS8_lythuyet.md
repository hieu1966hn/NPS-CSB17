Nội dung buổi 8
- Cách viết hàm và mục đích sử dụng hàm
- Phân biệt hàm print và hàm return
- Cách viết hàm thành module và import module


Hàm: là một đoạn code dùng để thực hiện một việc nào đó. Có 2 loại hàm: 
1. Hàm Built-in: print, len, append, ....
2. Hàm do người dùng viết: 

Cú pháp khai báo hàm:
def <ten_ham>():
    ... statement

Từ khóa "return" 
- Trả về một giá trị, nếu không có return thì hàm gọi luôn trả về giá trị "None".
- Khi từ khóa "return" được gọi sẽ kết thúc hàm ngay lập tức, phần code sau return sẽ không chạy.


Variable Scope:
- Global: Biến được tạo ngoài hàm, được sử dụng/duy trì trong toàn bộ chương trình. 
- Local: Là biến được tạo trong hàm. Có tác dụng trong hàm đó và biến mất sau khi hàm kết thúc.

Module: Các module (gần giống với hàm) giúp tổ chức mã nguồn một cách logic, làm cho mã nguồn dễ quản lý, bảo trì và tái sử dụng.


Bài tập viết hàm:
1. Viết hàm tìm số lớn hơn trong 2 số 
2. Định nghĩa hàm có thể chấp nhận input là số nguyên và in ra "Đây là một số chẵn" nếu nó chẵn. Ngược lại in ra "Đây là một số lẻ"
3. Viết hàm kiểm tra năm được truyền vào có phải là năm nhuận hay không? Yêu cầu kiểm tra năm đầu vào phải > 0.
4. Viết hàm tính tổng một array cho trước. Nếu trong array tồn tại phần tử không phải là "số" thì bỏ qua phần tử đó.
5. Viết một chương trình chấp nhập chuỗi từ người dùng nhập vào, phân tách nhau bởi dấu "," và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bởi dấu ","