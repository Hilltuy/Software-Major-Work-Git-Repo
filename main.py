import pygame
import pygame.midi as midi

pygame.init()
midi.init()
mainClock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 960

pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

midiDataList = []
midi_in = midi.Input(1) #can change the number to the computer keyboard for working at school
def rightHandImprov():
    print(midi.get_device_info(1)) #midi ID 1 is my midi controller keyboard
    midiDataList.append(midi.Input.read(midi_in,1)) #reads in the midi input data
    print(midiDataList) #displays the midiDataList table to prove that information is coming in

running = True
while running:
    rightHandImprov()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    mainClock.tick(60)

running = False







