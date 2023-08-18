import pygame
import os

pygame.init()
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BOTTOM_RECT = pygame.Rect(0, HEIGHT - 15, WIDTH, 15)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def draw_window():
    WIN.fill("white")
    pygame.draw.rect(WIN, BLACK, BOTTOM_RECT)
    pygame.display.flip()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
