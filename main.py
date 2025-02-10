import pygame

pygame.init()

mainClock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 960

pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    mainClock.tick(60)

running = False