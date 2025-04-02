import pygame
import pygame.midi as midi
import pygame.mixer as mixer
import sqlite3
pygame.init()
midi.init()
mixer.init()

keyDistancesFromC = {
    'C':0,
    'C#':1,
    'D':2,
    'D#':3,
    'E':4,
    'F':5,
    'F#':6,
    'G':7,
    'G#':8,
    'A':9,
    'A#':10,
    'B':11,
}

conn = sqlite3.connect('modeDatabase.db')
def getScale(key,mode, octave):
    cursor = conn.execute("SELECT scale FROM modeTable WHERE mode == '{}';".format(mode))
    for row in cursor:
        stringMode = row[0]

    scaleValues = []
    doubleDigitLeftoverIndexes = []

    counter = -1 #counter used for indexing
    for char in stringMode:
        counter += 1

        if char.isdigit() and counter != (len(stringMode)-1): #ensures that character is not a comma and isnt at the end of the array
            print("character "+str(counter)+": "+str(stringMode[counter])) #for console debugging

            if stringMode[counter+1].isdigit(): #if it's a 2 digit number
                scaleValues.append(int(char+stringMode[counter+1])) #combine both digits into one integer and append to scaleValues
                doubleDigitLeftoverIndexes.append(len(scaleValues)) #notes the index in which there will be a double digit 'leftover'; where the algorithm iterates through the second digit of a 2 digit number
                #doubleDigitLeftoverIndexes is used by the next for loop to delete the lone one digit numbers that come from the 2 digit numbers already iterated over
        
            else: #if the character is a one digit number
                scaleValues.append(int(char)) #add normally

    scaleBefore = scaleValues.copy() #Stores the uncleaned version of the scaleValues array for comparing in the cleaning algorithm
    print("scale before: "+str(scaleBefore)) #for console debugging

    counter = -1 #counter reused for indexing
    if len(doubleDigitLeftoverIndexes) > 1: #cleaning is only necessary if there is more than one 2 digit number
        for i in doubleDigitLeftoverIndexes:
            counter += 1
            print("ddi: "+str(i)) #ddi = the index of a double digit leftover

            if i != len(scaleBefore) - 1: #if the index isnt at the end of the array, as there will not be leftovers at the end of the array
                print("does "+str(i)+" = "+str(len(scaleBefore) - 1),"scaleBefore = "+str(scaleBefore)) #for console debugging

                scaleValues.pop(i) #deletes leftover at index 'i'

                doubleDigitLeftoverIndexes[counter + 1] -= (counter + 1) #reduces index value by 1 because the length of the array has been lowered
                print("new DDIs: "+str(doubleDigitLeftoverIndexes)) #for console debugging
            
            print("new scale: "+str(scaleValues)) #console debugging

        print("scale after: "+str(scaleValues)) #for comparing the new cleaned array to the uncleaned array

    scaleInKey = scaleValues.copy()
    if key in keyDistancesFromC.keys():
        for i in range(len(scaleInKey)):
            scaleInKey[i] = int(scaleInKey[i] + keyDistancesFromC[key]) 
    
    for note in scaleInKey:
        note += 12 * octave

    print("Scale: {} {}".format(key,mode))
    for value in scaleInKey:
        print(midi.midi_to_ansi_note(value))

getScale('C','Natural Minor',3)



mainClock = pygame.time.Clock()
midi_in = midi.Input(1)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 960

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)
my_font = pygame.font.SysFont('Helvetica', 30)

running = True
while running:
    #midi.Output.write([[[144, 59, 66, 0], 1000]])
    text_surface = my_font.render('B Minor', (255, 0, 0), (0, 0, 0))
    SCREEN.blit(text_surface, (0,0))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    mainClock.tick(60)

running = False


print(midi.midi_to_ansi_note(0))

