from constantArraysAndDicts import keyDistancesFromC
from constantArraysAndDicts import degreeTonalityForModes
from constantArraysAndDicts import AccidentalsIntegerNotation
import sqlite3
import pygame.midi as midi
midi.init()
midi_out = midi.Output(midi.get_default_output_id(),0)
midi_out.set_instrument(10)
#midi_in = midi.Input(midi.get_default_input_id(),0)

class Scale():
    def __init__(self, key = str, mode = str, octave = int):
        self.notes = self.setScale(key,mode,octave)
        self.key = key
        self.mode = mode
        self.octave = octave
    
    def setScale(self,key,mode, octave):
        conn = sqlite3.connect('modeDatabase.db')
        cursor = conn.execute("SELECT scale FROM modeTable WHERE mode == '{}';".format(mode))
        for row in cursor:
            stringMode = row[0]

        scaleValues = []
        doubleDigitLeftoverIndexes = []

        counter = -1 #counter used for indexing
        for char in stringMode:
            counter += 1

            if char.isdigit() and counter != (len(stringMode)-1): #ensures that character is not a comma and isnt at the end of the array
                #print("character "+str(counter)+": "+str(stringMode[counter])) #for console debugging

                if stringMode[counter+1].isdigit(): #if it's a 2 digit number
                    scaleValues.append(int(char+stringMode[counter+1])) #combine both digits into one integer and append to scaleValues
                    doubleDigitLeftoverIndexes.append(len(scaleValues)) #notes the index in which there will be a double digit 'leftover'; where the algorithm iterates through the second digit of a 2 digit number
                    #doubleDigitLeftoverIndexes is used by the next for loop to delete the lone one digit numbers that come from the 2 digit numbers already iterated over
            
                else: #if the character is a one digit number
                    scaleValues.append(int(char)) #add normally

        scaleBefore = scaleValues.copy() #Stores the uncleaned version of the scaleValues array for comparing in the cleaning algorithm
        #print(doubleDigitLeftoverIndexes)
        #print("scale before: "+str(scaleBefore)) #for console debugging

        counter = -1 #counter reused for indexing
        if len(doubleDigitLeftoverIndexes) > 1: #cleaning is only necessary if there is more than one 2 digit number
            for i in doubleDigitLeftoverIndexes:
                counter += 1
                #print("ddi: "+str(i)) #ddi = the index of a double digit leftover

                if i != len(scaleBefore) - 1: #if the index isnt at the end of the array, as there will not be leftovers at the end of the array
                    #print("does "+str(i)+" = "+str(len(scaleBefore) - 1),"scaleBefore = "+str(scaleBefore)) #for console debugging

                    scaleValues.pop(i) #deletes leftover at index 'i'

                    doubleDigitLeftoverIndexes[counter + 1] -= (counter + 1) #reduces index value by 1 because the length of the array has been lowered
                    #print("new DDIs: "+str(doubleDigitLeftoverIndexes)) #for console debugging
                
                #print("new scale: "+str(scaleValues)) #console debugging

           # print("scale after: "+str(scaleValues)) #for comparing the new cleaned array to the uncleaned array

        scaleInKey = scaleValues.copy()
        if key in keyDistancesFromC.keys():
            for i in range(len(scaleInKey)):
                scaleInKey[i] = int(scaleInKey[i] + keyDistancesFromC[key]) 
                scaleInKey[i] = scaleInKey[i] + (12 * (octave + 1))
        
        # for note in scaleInKey:
        #     print("note before: "+str(note))
        #     note = note + (12 * octave)
        #     print("note after: "+str(note))

        #print(scaleInKey)

        return scaleInKey

    def cleanAnsi(self,midiNote):
        ansi = midi.midi_to_ansi_note(midiNote)
        for i in range(len(ansi)):
            if ansi[i].isdigit():
                print("ansi char: "+ansi[i])
                cleanAnsi = ansi.replace(ansi[i],'')
        return cleanAnsi

    def playDegree(self,degree=int,accidental=str):
        #if type(tonality) == str:
        #    pass
        chord = []
        rootNote = self.notes[(degree-1)+AccidentalsIntegerNotation[accidental]] #sets root note of degree
        rootAnsi = self.cleanAnsi(rootNote)

        rootNoteScale = self.setScale(rootAnsi,degreeTonalityForModes[self.mode][degree - 1],self.octave + 1)
        print(midi.midi_to_ansi_note(rootNote) + degreeTonalityForModes[self.mode][degree - 1] + str((self.octave + 1)))
        print(rootNoteScale)
        
        diadNote = rootNoteScale[2]
        triadNote = rootNoteScale[4]
        print('\n'+midi.midi_to_ansi_note(diadNote)+midi.midi_to_ansi_note(triadNote))
        chord.extend([rootNote,diadNote,triadNote])
        print(chord)
        for note in chord:
            print(midi.midi_to_ansi_note(note))
            midi_out.note_on(note,80)
        return chord

    def get_notes(self):
        return self.notes

    def playerInput(self):
        midi_out.write(midi_in.read(1))
