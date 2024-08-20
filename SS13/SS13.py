import pygame

#### Khởi tạo các module cần thiết của pygame với hàm init:
pygame.init()


#### Tạo một cửa số có kích thước: 800, 600
screen = pygame.display.set_mode((800, 600))

### Đặt tên cho cửa sổ hiển thị
pygame.display.set_caption("Vẽ hình chữ nhật với pygame")

### Định nghĩa màu sắc (R, G, B)
white = (255, 255, 255)
red = (255, 0, 0)

### Vẽ một hình chữ nhật màu đỏ
rect = pygame.Rect(0, 0, 200, 150)
pygame.draw.rect(screen, red, rect)

### Cập nhật màn hình để hiển thị hình chữ nhật
pygame.display.update()

### Đợi người dùng thoát ra khỏi cửa sổ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

### Thoát pygame
pygame.quit()
