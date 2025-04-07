import pygame
import pygame.midi as midi
import rightHandImprovApp 
pygame.init()
midi.init()
mainClock = pygame.time.Clock()

SCREEN_WIDTH = 1200 
SCREEN_HEIGHT = 960

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)





def get_devices():
    for i in range(-2, 8):
        print(str(midi.get_device_info(i))+": "+str(i))


get_devices()
CMajorScale = rightHandImprovApp.getScale('C','Major',4)
#CMajorScale.playDegree(2,natural,minor)


# running = True
# while running:
#     rightHandImprovApp.rightHandImprov()
    
    

    
#     pygame.display.update() 
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

# running = False







