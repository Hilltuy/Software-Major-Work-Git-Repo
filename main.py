import pygame
import pygame.midi as midi
from classes import Scale
import constantArraysAndDicts
import random
pygame.init()
midi.init()
mainClock = pygame.time.Clock()

SCREEN_WIDTH = 1600 
SCREEN_HEIGHT = 900

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)

midi_in = midi.Input(midi.get_default_input_id(),0)
midi_out = midi.Output(midi.get_default_output_id(),0)

gray = (100,100,100)      
green = (93, 227, 129)
orange = (227, 156, 93)
skyBlue = (93, 167, 227)
purple = (129, 0, 176)
darkRed = (84, 62, 62)

def modulateColour(colour,lightOrDark):
    if lightOrDark == 'Dark':
        colour = list(colour)
        for i in range(len(colour)):
            if colour[i] > 30:
                colour[i] -= 30
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
##'cc' is 'can click' abbreviated
# ccRHI = False
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
#         if event.type == pygame.MOUSEBUTTONDOWN and ccRHI:
#             runningMainMenu = False #kills main menu
#             runningRHI = True #Starts while loop for right hand improv app

#     pygame.display.update() 



runningMainMenu = True

ccRHI = False
runningRHIMenu = False

keySelected = 0
ccKeySelect = False

tonalitySelected = 0
ccTonalitySelect = False

octaveSelected = 3
ccOctaveSelect = False

repetitionsSelected = 4
ccRepetitionSelect = False

playSelected = False
ccPlaySelect = False

scaleKeyList = list(constantArraysAndDicts.keyDistancesFromC.keys())
modalitiesList = list(constantArraysAndDicts.degreeTonalityForModes.keys())

appRunning = True

rhiFinishedRunning = False

while appRunning == True:

    while runningMainMenu == True:
        
        # fills the SCREEN with a color  
        SCREEN.fill((60,25,60))
        
        mouse = pygame.mouse.get_pos()  
        
        # if mouse is hovered on a button it  
        # changes to lighter shade  
        if SCREEN_WIDTH/2 - 200 <= mouse[0] <= SCREEN_WIDTH/2 + 200 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2 +75:  
            drawButton(modulateColour(green,'Normal'),400, 75,SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2)
            ccRHI = True
        else:  
            drawButton(modulateColour(green,'Dark'),400, 75,SCREEN_WIDTH/2 - 200, SCREEN_HEIGHT/2)
            ccRHI = False
        
        # # superimposing the text onto the button  
        SCREEN.blit(text('Right Hand Improv Practice',(255,255,255),30) , (SCREEN_WIDTH/2 -180,SCREEN_HEIGHT/2 +18.75))  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and ccRHI:
                runningMainMenu = False #kills main menu
                runningRHIMenu = True #Starts while loop for right hand improv app

        pygame.display.update() 


    while runningRHIMenu == True:
        mouse = pygame.mouse.get_pos()
        SCREEN.fill((20,25,20))

        #KEY selection button
        if SCREEN_WIDTH/2 - 300 <= mouse[0] <= SCREEN_WIDTH/2 -200 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2 +100:  
            drawButton(modulateColour(green,'Light'),100,100,SCREEN_WIDTH/2 - 300,SCREEN_HEIGHT/2)
            ccKeySelect = True
        else:
            ccKeySelect = False
            drawButton(modulateColour(green,'Normal'),100,100,SCREEN_WIDTH/2 - 300,SCREEN_HEIGHT/2)

        #TONALITY selection button
        if SCREEN_WIDTH/2 - 100 <= mouse[0] <= SCREEN_WIDTH/2 - 0 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2 +100:  
            drawButton(modulateColour(orange,'Light'),100,100,SCREEN_WIDTH/2 - 100,SCREEN_HEIGHT/2)
            ccTonalitySelect = True
        else: 
            ccTonalitySelect = False
            drawButton(modulateColour(orange,'Normal'),100,100,SCREEN_WIDTH/2 - 100,SCREEN_HEIGHT/2)

        #OCTAVE selection button
        if SCREEN_WIDTH/2 + 100 <= mouse[0] <= SCREEN_WIDTH/2 + 200 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2 +100:  
            drawButton(modulateColour(skyBlue,'Light'),100,100,SCREEN_WIDTH/2 + 100,SCREEN_HEIGHT/2)
            ccOctaveSelect = True
        else: 
            ccOctaveSelect = False
            drawButton(modulateColour(skyBlue,'Normal'),100,100,SCREEN_WIDTH/2 + 100,SCREEN_HEIGHT/2)

        #REPETITIONS selection button
        if SCREEN_WIDTH/2 + 300 <= mouse[0] <= SCREEN_WIDTH/2 + 400 and SCREEN_HEIGHT/2 <= mouse[1] <= SCREEN_HEIGHT/2 +100:  
            drawButton(modulateColour(purple,'Light'),100,100,SCREEN_WIDTH/2 + 300,SCREEN_HEIGHT/2)
            ccRepetitionSelect = True
        else: 
            ccRepetitionSelect = False
            drawButton(modulateColour(purple,'Normal'),100,100,SCREEN_WIDTH/2 + 300,SCREEN_HEIGHT/2)


        #PLAY button
        if SCREEN_WIDTH/2 + -150 <= mouse[0] <= SCREEN_WIDTH/2 + 250 and SCREEN_HEIGHT/2 + 250 <= mouse[1] <= SCREEN_HEIGHT/2 +400:  
            drawButton(modulateColour(darkRed,'Dark'),400,150,SCREEN_WIDTH/2 -150,SCREEN_HEIGHT/2 +250)
            ccPlaySelect = True
        else: 
            ccPlaySelect = False
            drawButton(modulateColour(darkRed,'Normal'),400,150,SCREEN_WIDTH/2-150,SCREEN_HEIGHT/2 +250)


        #Title
        SCREEN.blit(text('Right Hand Improvisation Setup',(255,255,255),64) , (SCREEN_WIDTH/2 - 360,80))

        #KEY selection button TEXT
        SCREEN.blit(text(scaleKeyList[keySelected],(255,255,255),64) , (SCREEN_WIDTH/2 - 282,385))   

        #TONALITY selection button TEXT
        SCREEN.blit(text(modalitiesList[tonalitySelected],(255,255,255),50 - (len(modalitiesList[tonalitySelected])*2)) , (SCREEN_WIDTH/2 - 100,400))  

        #OCTAVE selection button TEXT
        SCREEN.blit(text(str(octaveSelected),(255,255,255),48), (SCREEN_WIDTH/2 + 140,385))

        #REPETITIONS selection button TEXT
        SCREEN.blit(text(str(repetitionsSelected),(255,255,255),48), (SCREEN_WIDTH/2 + 340,385))

        #PLAY button TEXT
        SCREEN.blit(text('Play with Setup',(255,255,255),50) , (SCREEN_WIDTH/2 - 120,SCREEN_HEIGHT/2 +300))

        for event in pygame.event.get():
            #if KEY button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN and ccKeySelect:
                if keySelected < len(scaleKeyList)-1:
                    keySelected += 1
                else:
                    keySelected = 0

            #if TONALITY button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN and ccTonalitySelect:
                if tonalitySelected < len(modalitiesList)-1:
                    tonalitySelected += 1
                else:
                    tonalitySelected = 0

            #if OCTAVE button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN and ccOctaveSelect:
                if octaveSelected < 7:
                    octaveSelected += 1
                else:
                    octaveSelected = 3

            #if REPETITION button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN and ccRepetitionSelect:
                if repetitionsSelected < 48:
                    repetitionsSelected += 1
                else:
                    repetitionsSelected = 1

            #if PLAY button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN and ccPlaySelect:
                if playSelected == False:
                    runningRHIMenu = False
                    playSelected = True

            elif event.type == pygame.QUIT:
                pygame.quit() 

        pygame.display.update()


    currentScale = Scale(scaleKeyList[keySelected],modalitiesList[tonalitySelected],octaveSelected)
    currentChordDisplay = ''
    chordsList = []

    for i in range(repetitionsSelected):
        currentDegree = random.randint(1,len(currentScale.get_notes()) - 1)
        #sets the tonality of the current chord being played
        #currentChord = currentScale.playDegree(currentDegree,'Natural')
        chordsList.append(currentDegree)

    print('degree list: '+str(chordsList))
            
    chordCount = -1
    #pygame.USEREVENT represents the first event slot, pygame.USEREVENT + 1 would represent the second slot.
    pygame.time.set_timer(pygame.USEREVENT,1000)

    currentDegreeTonality = ''
    nextDegreeTonality = ''
    while playSelected == True:
        mouse = pygame.mouse.get_pos()
        SCREEN.fill((20,25,20))
        #actual improvisation app

        midi_out.write(midi_in.read(1))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 

            elif event.type == pygame.USEREVENT:
                chordCount += 1
                if chordCount + 1 < repetitionsSelected:
                    currentScale.playDegree(chordsList[chordCount],'Natural')


                    #uses mode dictionary to display the correct tonality (major, minor, etc) for the current chord. - '- 1' is added to convert 1-based number system to zero-based for python's array indexing 
                    currentDegreeTonality = constantArraysAndDicts.degreeTonalityForModes[modalitiesList[tonalitySelected]][chordsList[chordCount] - 1]
                    currentChordDisplay = str(currentScale.cleanAnsi((currentScale.get_notes()[chordsList[chordCount] - 1]))+" "+currentDegreeTonality)

                    #Same process as above, but finding the correct tonality for the chord after the current one
                    nextDegreeTonality =  constantArraysAndDicts.degreeTonalityForModes[modalitiesList[tonalitySelected]][chordsList[chordCount + 1] - 1]
                    nextChordDisplay = str(currentScale.cleanAnsi((currentScale.get_notes()[chordsList[chordCount + 1] - 1]))+" "+nextDegreeTonality)


                    # #randomly selects a chord degree to play from the scale
                    # currentDegree = random.randint(1,len(currentScale.get_notes()) - 1)
                    # #sets the tonality of the current chord being played
                    # currentDegreeTonality = constantArraysAndDicts.degreeTonalityForModes[modalitiesList[tonalitySelected]][currentDegree - 1]
                    # #print('current degree: '+str(currentDegree))
                    # #print("current tonality: "+modalitiesList[tonalitySelected])
                    # currentScale.playDegree(currentDegree,'Natural')
                else:
                    playSelected = False
                    rhiFinishedRunning = True



        if len(currentChordDisplay) > 0:
            SCREEN.blit(text(currentChordDisplay,(255,255,255),48),(SCREEN_WIDTH/2 - 120,SCREEN_HEIGHT/2))

        if len(currentChordDisplay) > 0:  
            SCREEN.blit(text('Next chord: '+nextChordDisplay,skyBlue,34),(SCREEN_WIDTH/2 - 150,SCREEN_HEIGHT/2 +110))

        SCREEN.blit(text('Bar count: '+str(chordCount + 1)+'/'+str(repetitionsSelected),(255,255,255),34),(SCREEN_WIDTH/2 - 800,SCREEN_HEIGHT/2 -450))

        pygame.display.update()

    ccRHIPlayAgain = False
    ccBackToMain = False

    while rhiFinishedRunning == True:
        mouse = pygame.mouse.get_pos()
        SCREEN.fill((20,25,20))    
        SCREEN.blit(text('Repetitions Completed!',(255,255,255),68),(SCREEN_WIDTH/2 -280,SCREEN_HEIGHT/2 - 150))

        #PLAY AGAIN button
        if SCREEN_WIDTH/2 + -170 <= mouse[0] <= SCREEN_WIDTH/2 + 230 and SCREEN_HEIGHT/2 + 50 <= mouse[1] <= SCREEN_HEIGHT/2 +200:  
            drawButton(modulateColour(orange,'Dark'),400,150,SCREEN_WIDTH/2 -170,SCREEN_HEIGHT/2 +50)
            ccRHIPlayAgain = True
        else: 
            ccRHIPlayAgain = False
            drawButton(modulateColour(orange,'Normal'),400,150,SCREEN_WIDTH/2-170,SCREEN_HEIGHT/2 +50)

        #BACK TO MENU button
        if SCREEN_WIDTH/2 + -170 <= mouse[0] <= SCREEN_WIDTH/2 + 230 and SCREEN_HEIGHT/2 + 250 <= mouse[1] <= SCREEN_HEIGHT/2 +400:  
            drawButton(modulateColour(darkRed,'Dark'),400,150,SCREEN_WIDTH/2 -170,SCREEN_HEIGHT/2 +250)      
            ccBackToMain = True
        else: 
            drawButton(modulateColour(darkRed,'Normal'),400,150,SCREEN_WIDTH/2-170,SCREEN_HEIGHT/2 +250)
            ccBackToMain = False


        #PLAY AGAIN text
        SCREEN.blit(text('Back to Setup',(255,255,255),50) , (SCREEN_WIDTH/2 - 120,SCREEN_HEIGHT/2 +100))

        #MAIN MENU text
        SCREEN.blit(text('Back to Main Menu',(255,255,255),40) , (SCREEN_WIDTH/2 - 150,SCREEN_HEIGHT/2 +300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #run setup again
            elif event.type == pygame.MOUSEBUTTONDOWN and ccRHIPlayAgain:
                if runningRHIMenu == False:
                    rhiFinishedRunning = False
                    runningRHIMenu = True

            #back to main menu
            elif event.type == pygame.MOUSEBUTTONDOWN and ccBackToMain:
                if runningMainMenu == False:
                    rhiFinishedRunning = False
                    runningMainMenu = True

        pygame.display.update()






