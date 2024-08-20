import pygame
import sys

### Khởi tạo game
pygame.init()

### Kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

## Đặt tên cửa sổ game
pygame.display.set_caption("Pong Game")


### Khởi tạo biến màu sắc
black = (0, 0, 0)
white = (255, 255, 255)

### Thông số của thanh điều khiển
paddle_width = 15
paddle_height = 100
paddle_speed = 7

### Vị trí của thanh điều khiển trên màn hình game
player1_x = 50
player1_y = screen_height // 2 - paddle_height // 2
player2_x = screen_width - 50 - paddle_width
player2_y = screen_height // 2 - paddle_height // 2

### Ball
ball_size = 20
ball_x = screen_width // 2 - ball_size // 2 ## chia 2 lấy phần nguyen
ball_y = screen_height // 2 - ball_size // 2 ## chia 2 lấy phần nguyen
ball_speed_x = 4
ball_speed_y = 4


### Score
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)


### Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ### Get keys pressed
    keys  = pygame.key.get_pressed()

    ### Move player 1
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_w] and player1_y > 0 :
        player1_y -= paddle_speed

    ### Move player 2
    if keys[pygame.K_DOWN] and player2_y > 0 :
        player2_y += paddle_speed
    if keys[pygame.K_UP] and player2_y < screen_height - paddle_height:
        player2_y -= paddle_speed
    
    ### Move Ball

    ### Ball collision with top and bottom (nghiên cứu thêm)

    ### Ball collision with paddles(thanh player 1, 2)

    ### Ball goes out of bounds


    ### fill screen
    screen.fill(black)

    ### Draw paddles and Ball
    player1 = pygame.draw.rect(screen, white, (player1_x, player1_y, paddle_width, paddle_height))
    player2 = pygame.draw.rect(screen, white, (player2_x, player2_y, paddle_width, paddle_height))
    ball = pygame.draw.rect(screen, white, (ball_x, ball_y, ball_size, ball_size))

    ### Draw scores

    ### Update display
    pygame.display.flip()

    ### Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
