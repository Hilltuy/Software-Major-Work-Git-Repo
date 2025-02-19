import pygame
import pygame.midi as midi

pygame.init()
midi.init()
mainClock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 960

pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))



midiDataList = []
midi_in = midi.Input(midi.get_default_input_id()) #can change the number to the computer keyboard for working at school
#midi_out = midi.Output(midi.get_default_output_id(),0)
midi_out = midi.Output(5,0)
midi_out.set_instrument(0)

def rightHandImprov():
    #print(midi.get_device_info(1)) #midi ID 1 is my midi controller keyboard
    #print(midi_in.read(1)[0])
    midi_out.write(midi_in.read(1))
    pass
for i in range(-2, 8):
    print(str(midi.get_device_info(i))+": "+str(i))
running = True

while running:
    rightHandImprov()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    #mainClock.tick(360)

running = False







