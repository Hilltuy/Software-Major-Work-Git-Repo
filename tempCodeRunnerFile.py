from classes import Scale
import pygame.midi as midi

midi.init()
#midi_out = midi.Output(midi.get_default_output_id(),0)


myScale = Scale("E","Major",3)
aScale = Scale('A','Major',4)

#print(myScale.get_notes())

print(aScale.get_notes())

myScale.playDegree(4,'Natural',3)