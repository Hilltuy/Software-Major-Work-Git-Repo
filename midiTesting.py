import pygame
import pygame.midi as midi
import pygame.mixer as mixer

pygame.init()
midi.init()
mixer.init()
mainClock = pygame.time.Clock()
midi_in = midi.Input(1)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 960

pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
while running:
    midi.Output.write([[[144, 59, 66, 0], 1000]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    mainClock.tick(60)

running = False
