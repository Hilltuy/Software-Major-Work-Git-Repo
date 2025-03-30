import pygame
import pygame.midi as midi
import pygame.mixer as mixer
import sqlite3
pygame.init()
midi.init()
mixer.init()

conn = sqlite3.connect('modeDatabase.db')

cursor = conn.execute("SELECT scale FROM modeTable WHERE mode == 'Major';")
for row in cursor:
    stringMode = row[0]

scaleValues = []
counter = -1
for char in stringMode:
    counter += 1
    if char.isdigit():
        print("character "+str(counter)+": "+str(stringMode[counter]))
        if stringMode[counter+1].isdigit():
            scaleValues.append(char+stringMode[counter+1])
        else:
            scaleValues.append(char)

print(scaleValues)

# for value in scaleValues:
#     print(midi.midi_to_ansi_note(value))




# mainClock = pygame.time.Clock()
# midi_in = midi.Input(1)

# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 960

# pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# running = True
# while running:
#     midi.Output.write([[[144, 59, 66, 0], 1000]])
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

#     pygame.display.update()
#     mainClock.tick(60)

# running = False


print(midi.midi_to_ansi_note(0))