import pygame
import pygame.midi as midi

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
    




def rightHandImprov():
    #print(midi.get_device_info(1)) #midi ID 1 is my midi controller keyboard
    #print(midi_in.read(1))
    midi_out.write(midi_in.read(1))
    pass