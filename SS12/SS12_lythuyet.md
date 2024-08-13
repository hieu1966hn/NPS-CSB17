File: Là đơn vị lưu trữ thông tin trong hệ thống máy tính. File có thể chứa nhiều loại dữ liệu khác nhau gồm: văn bản, video, ảnh, âm thanh, ... Các file được tổ chức và lưu trữ trong các thư mục (Folder).

Liệt kê các đuôi file cơ bản: 
- .exe: file thực thi
- .doc/.pptx: Tài liệu
- .mp3: File âm thanh
- .mp4/.mov: File video
- .png/.jpg: file hình ảnh
- .xlxs: file bảng tính
- .inf: file thông tin

File path: Đường dẫn file được lưu trữ bên trong máy tính.


Mode file: read mode
- read(): đọc toàn bộ nội dung trong file
- read(n): Đọc n ký tự đầu tiên
- readline(): Đọc theo từng dòng

Delete mode: xóa file
- B1: import module os
- B2: hàm remove
- B2.1: rmdir()

Bài tập thực hành
Bài 1a: Ghi dữ liệu vào file
- Tạo 1 file văn bản có tên là: example.txt
- Ghi dòng chữ "Hello World!!!" vòa file này

Bài 1b: Đọc dữ liệu từ file
- Mở file example.txt đã tạo ở bài 1a
- Đọc và in ra nội dung của file này trên màn hình terminal.

Bài 2: Đếm số dòng trong file example.txt


Bài 3a: Đọc số nguyên từ file
- Tạo một file có tên là "numbers.txt" và ghi vào file này các số nguyên, mỗi số nằm trên 1 dòng.
- Viết chương trình để đọc các số từ file và tính tổng của chúng.

Bài 3b: Tính giá trị trung bình 
- Sử dụng file numbers.txt từ bài 3a. Viết chương trình để tính và in ra giá trị trung bình của các số.

Bài 4: Tìm và thay thế từ trong file
- Đọc nội dung của một file văn bản (sample.txt) có nội dung bên trong là: "Hello World"
- Tìm và thay thế một từ cụ thể trong nội dung. VD: Thay thế từ "Hello World" thành "Hi".
- Ghi nội dung đã thay thế vào một file mới.
- Viết dưới dạng hàm thay thế nội dung:
def repace_word_in_file(input_file, output_file, target_word, replacement_word):
