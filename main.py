import pygame
import pygame.midi as midi
from classes import Scale
pygame.init()
midi.init()
mainClock = pygame.time.Clock()

SCREEN_WIDTH = 1600 
SCREEN_HEIGHT = 900

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)

# white color  
color = (255,255,255)  
  
# light shade of the button  
color_light = (170,170,170)  
  
# dark shade of the button  
color_dark = (100,100,100)      

# defining a font  
smallfont = pygame.font.SysFont('Helvetica',35)  
  
# rendering a text written in  
# this font  
text = smallfont.render('Right Hand Improv Practice' , True , color)  


def get_devices():
    for i in range(-2, 8):
        print(str(midi.get_device_info(i))+": "+str(i))


get_devices()
CMajorScale = Scale('C','Major',4)
#CMajorScale.playDegree(2,natural,minor)

canClickRHI = False
running = True
while running:
     
    # fills the SCREEN with a color  
    SCREEN.fill((60,25,60))
    
    mouse = pygame.mouse.get_pos()  
      
    # if mouse is hovered on a button it  
    # changes to lighter shade  
    if SCREEN_WIDTH/2 <= mouse[0] <= SCREEN_WIDTH/2+140 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2+40:  
        pygame.draw.rect(SCREEN,color_light,[SCREEN_WIDTH/2 - 200,SCREEN_HEIGHT/2,400,75])  
        canClickRHI = True
        if canClickRHI and pygame.MOUSEBUTTONDOWN:
            #play right hand improv app
            pass
    else:  
        pygame.draw.rect(SCREEN,color_dark,[SCREEN_WIDTH/2 - 200,SCREEN_HEIGHT/2,400,75])  
        canClickRHI = False
      
    # superimposing the text onto our button  
    SCREEN.blit(text , (SCREEN_WIDTH/2 -200,SCREEN_HEIGHT/2))  
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update() 


running = False







