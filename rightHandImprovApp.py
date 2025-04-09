import pygame
import pygame.midi as midi
import pygame.mixer as mixer
import sqlite3
import pygame.time as time

pygame.init()
midi.init()

midiDataList = []
midi_in = midi.Input(midi.get_default_input_id()) #can change the number to the computer keyboard for working at school
midi_out = midi.Output(midi.get_default_output_id(),0)
#midi_out = midi.Output(5,0)
midi_out.set_instrument(0)

def generateChords(key, tonality):
    if key == 0:
        #choose random notes
        pass

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
    
    # for note in scaleInKey:
    #     print("note before: "+str(note))
    #     note = note + (12 * octave)
    #     print("note after: "+str(note))

    for index in range(len(scaleInKey)):
        scaleInKey[index] = scaleInKey[index] + (12 * (octave + 1))

    #print(scaleInKey)

    return scaleInKey


    print("Scale: {} {}, Octave {}".format(key,mode,octave))
    for value in scaleInKey:
        print(midi.midi_to_ansi_note(value))




    for note in scaleInKey:

        midi_out.note_on(note,100,0) #plays all notes of the scale

def playDegree(degree,accidental,tonality):
    pass


def rightHandImprov():
    #print(midi.get_device_info(1)) #midi ID 1 is my midi controller keyboard
    #print(midi_in.read(1))
    #midi_out.write(midi_in.read(1))
    print(midi_in.read(1))
    pass


