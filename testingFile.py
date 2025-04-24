import classes
from classes import Scale
import random 
from pygame import time

myScale = Scale('A#','Major',3)

#myScale.playDegree(2,'Natural')

for i in range(4):
    degree = random.randint(1,7)
    myScale.playDegree(degree,'Natural')