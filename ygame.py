import pygame
import sys

pygame.init()

# Настройки экрана и цветов
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping-Pong mäng")

light_green = (153, 255, 153)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

# Мяч
ball_size = 20
ball_x = screen_width // 2 - ball_size // 2
ball_y = 0  # Мяч падает сверху, стартует с верха экрана
ball_speed_x = 9
ball_speed_y = 8

# Ракетка снизу
paddle_width = 120
paddle_height = 20
paddle_y = screen_height - paddle_height  # внизу экрана
paddle_x = screen_width // 2 - paddle_width // 2
paddle_speed = 7

# Счёт
score = 0

running = True
game_over = False

while running:
    screen.fill(light_green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Управление ракеткой с клавиатуры
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT]:
            paddle_x += paddle_speed

        # Ограничение ракетки по краям экрана
        if paddle_x < 0:
            paddle_x = 0
        elif paddle_x + paddle_width > screen_width:
            paddle_x = screen_width - paddle_width

        # Движение мяча
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Отскок мяча от левой, правой и верхней стен
        if ball_x <= 0 or ball_x + ball_size >= screen_width:
            ball_speed_x = -ball_speed_x
        if ball_y <= 0:
            ball_speed_y = -ball_speed_y

        # Проверка, если мяч упал ниже экрана — минус очко и сброс мяча
        if ball_y > screen_height:
            score -= 1
            ball_x = screen_width // 2 - ball_size // 2
            ball_y = 0  # мяч снова падает сверху
            ball_speed_y = 8

        # Проверка столкновения мяча с ракеткой
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
        if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
            ball_speed_y = -ball_speed_y
            score += 1

        # Проверка победы/поражения
        if score <= -10:
            game_over = True
            result_text = "Kaotasid!"
        elif score >= 15:
            game_over = True
            result_text = "Võitsid!"

        # Отрисовка мяча и ракетки
        pygame.draw.rect(screen, black, ball_rect)
        pygame.draw.rect(screen, red, paddle_rect)

        # Отображаем счёт
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

    else:
        # Если игра окончена, выводим сообщение в центре
        text = big_font.render(result_text, True, red)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
