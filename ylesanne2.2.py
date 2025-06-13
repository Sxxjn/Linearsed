import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
ekraan = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruudustik värvidega")

def joonista_ruudustik(ekraan, ruudu_laius, ruudu_korgus, read, veerud, joone_varv, taustavarv):
    for rida in range(read):
        for veerg in range(veerud):
            x = veerg * ruudu_laius
            y = rida * ruudu_korgus
            ruut = pygame.Rect(x, y, ruudu_laius, ruudu_korgus)
            pygame.draw.rect(ekraan, taustavarv, ruut)      # täitevärv (taust)
            pygame.draw.rect(ekraan, joone_varv, ruut, 1)    # äär

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        ekraan.fill((153, 255, 153))  

        must = (0, 0, 0)
        valge = (255, 255, 255)
        lGreen = (153, 255, 153)
        red = (255, 0, 0)

        # Joonista ruudustik — valge täitevärv ja mustad jooned
        joonista_ruudustik(ekraan, 20, 20, 24, 32, red, lGreen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()