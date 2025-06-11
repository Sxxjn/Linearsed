import pygame

pygame.init()
ekraan = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees – Ruslan Gergankin")
valge = (255, 255, 255)
must = (0, 0, 0)
orange = (255, 165, 0)
punane = (255, 0, 0)
ekraan.fill(must)

# Снежные шары
pygame.draw.circle(ekraan, valge, (150, 220), 40)  
pygame.draw.circle(ekraan, valge, (150, 150), 30)  
pygame.draw.circle(ekraan, valge, (150, 100), 20)   

# Глаза
pygame.draw.circle(ekraan, must, (142, 95), 3)
pygame.draw.circle(ekraan, must, (158, 95), 3)

# Нос 
pygame.draw.circle(ekraan, orange, (150, 102), 3)
 

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()
