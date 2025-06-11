import pygame

pygame.init()

# Окно и цвета
ekraan = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 1.3")
valge = (255, 255, 255)
must = (0, 0, 0)

# Фон
taust = pygame.image.load("bar.png")
taust = pygame.transform.scale(taust, (640, 480))
ekraan.blit(taust, (0, 0))

# Медведь
bear = pygame.image.load("bear.png")
bear = pygame.transform.scale(bear, (150, 150))
ekraan.blit(bear, (400, 180))

# Облачко
speech = pygame.image.load("speech1.png")
speech = pygame.transform.scale(speech, (250, 100))
ekraan.blit(speech, (400, 100))

# Шрифт побольше
font = pygame.font.SysFont('Arial', 18)

# Текст для вывода (две строки)
rida1 = "Tere!"
rida2 = "Mina olen Ruslan!"

# Рендер текста
tekst1 = font.render(rida1, True, must)
tekst2 = font.render(rida2, True, must)

# Позиция облачка и его размеры
speech_x, speech_y = 460, 100
speech_w, speech_h = 100, 100

# Центрируем первую строку по ширине и смещаем чуть выше центра облачка
rect1 = tekst1.get_rect(center=(speech_x + speech_w // 2, speech_y + speech_h // 2 - 10))

# Вторую строку центрируем по ширине и чуть ниже первой
rect2 = tekst2.get_rect(center=(speech_x + speech_w // 2, speech_y + speech_h // 2 + 15))

# Рисуем текст на экране
ekraan.blit(tekst1, rect1)
ekraan.blit(tekst2, rect2)

pygame.display.flip()

# Цикл программы
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()
