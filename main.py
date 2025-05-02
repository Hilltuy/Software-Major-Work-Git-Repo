import pygame
import pygame.midi as midi
from classes import Scale

pygame.init()
midi.init()
mainClock = pygame.time.Clock()

SCREEN_WIDTH = 1600 
SCREEN_HEIGHT = 900

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)


gray = (100,100,100)      

# defining a font  


def modulateColour(colour,lightOrDark):
    if lightOrDark == 'Dark':
        colour = list(colour)
        for i in range(len(colour)):
            if colour[i] > 70:
                colour[i] -= 70
        return tuple(colour)

    elif lightOrDark == 'Light':
        colour = list(colour)
        for i in range(len(colour)):
            if colour[i] < 185:
                colour[i] += 70
        return tuple(colour)
    
    elif lightOrDark == 'Normal':
        return tuple(colour)



# to easily write text onto screen
def text(text,color,font_size):
    smallfont = pygame.font.SysFont('Helvetica',font_size)  
    return smallfont.render(text, True, color)


def get_devices():
    for i in range(-2, 8):
        print(str(midi.get_device_info(i))+": "+str(i))

def drawButton(colour,width,height,x,y):
    return pygame.draw.rect(SCREEN,colour,[x,y, width, height])

get_devices()
CMajorScale = Scale('C','Major',4)
#CMajorScale.playDegree(2,natural,minor)

# canClickRHI = False
# runningMainMenu = True
# runningRHI = False

# while runningMainMenu == True:
     
#     # fills the SCREEN with a color  
#     SCREEN.fill((60,25,60))
    
#     mouse = pygame.mouse.get_pos()  
      
#     # if mouse is hovered on a button it  
#     # changes to lighter shade  
#     if SCREEN_WIDTH/2 - 200 <= mouse[0] <= SCREEN_WIDTH/2 + 200 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2 +75:  
#         pygame.draw.rect(SCREEN,color_light,[SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2, 400, 75])  
#         canClickRHI = True
#     else:  
#         pygame.draw.rect(SCREEN,color_dark,[SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2, 400, 75])  
#         canClickRHI = False
      
#     # # superimposing the text onto the button  
#     SCREEN.blit(text('Right Hand Improv Practice',color) , (SCREEN_WIDTH/2 -180,SCREEN_HEIGHT/2 +18.75))  
    

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         if event.type == pygame.MOUSEBUTTONDOWN and canClickRHI:
#             runningMainMenu = False #kills main menu
#             runningRHI = True #Starts while loop for right hand improv app

#     pygame.display.update() 

runningMainMenu = False
runningRHI = True

while runningRHI == True:
    mouse = pygame.mouse.get_pos()
    SCREEN.fill((20,25,20))

    SCREEN.blit(text('Right Hand Improv Setup',(255,255,255),64) , (SCREEN_WIDTH/2 - 280,80))


    #if hovering over button
    if SCREEN_WIDTH/2 - 200 <= mouse[0] <= SCREEN_WIDTH/2 + 200 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2 +75:  
        drawButton(modulateColour(gray,'Light'),400,75,SCREEN_WIDTH/2 - 200,SCREEN_HEIGHT/2)
    else:  
        drawButton(modulateColour(gray,'Normal'),400,75,SCREEN_WIDTH/2 - 200,SCREEN_HEIGHT/2)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 

    pygame.display.update()










