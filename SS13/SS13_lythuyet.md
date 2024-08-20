Kiến thức:  
- Tìm hiểu về thư viện "pygame"
- Hàm init
- Cách vẽ các khối
- Hàm Rect()
- Hàm display()

Thư viện pygame: là bộ thư viện sử dụng để phát triển trò chơi trong Python. Nó cung cấp các chức năng để làm việc với đồ họa, âm thanh và các yếu tố khác của một trò chơi.

Để vẽ các khối, chúng ta cần cửa sổ để hiển thị chúng:

1. Tạo cửa sổ bằng hàm: display.set_model():
screen = pygame.display.set_mode((width, height))

2. Vẽ các khối với hàm: draw.rect() || x, y 
rect = pygame.Rect(x, y, width, height)

3. Để hiển thị những gì vừa vẽ, chúng ta cần cập nhật màn hình bằng hàm:
display.flip() hoặc display.update()

4. import sys
là module cung cấp các hàm và biến để tương tác với hệ thống Python.

Luyện tập: Thử vẽ khối
Đề bài: Hiển thị màn hình game có background là màu đen có chứa 1 khối hình chữ nhật màu đỏ.