from classes import Scale
import random 
from pygame import time

#myScale.playDegree(2,'Natural')

key = input("What key would you like to play in?")
tonality = input("In which tonality?")
octave = ''
while octave.isdigit() == False:
    octave = input("In which octave?")
octave = int(octave)

myScale = Scale(key,tonality,octave)
for i in range(20):
    myScale.playDegree(random.randint(1,7),'Natural')
    print("clean ansi: "+myScale.cleanAnsi(myScale.get_notes()[random.randint(0,len(myScale.get_notes())-1)]))
    time.delay(1000)
    #make time customizable