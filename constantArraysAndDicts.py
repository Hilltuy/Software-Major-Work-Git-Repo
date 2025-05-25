import sys

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

AccidentalsIntegerNotation = {
    'Sharp':1,
    'Natural':0,
    'Flat':-1
}

degreeTonalityForModes = {
    'Major':['Major','Natural Minor','Natural Minor','Major','Major','Natural Minor','Diminished'],
    'Natural Minor':['Natural Minor','Diminished','Major','Natural Minor','Natural Minor','Major','Major'],
    'Diminished':['Diminished','Diminished','Diminished','Diminished','Diminished','Diminished','Diminished'],
    'Augmented':['Augmented','Augmented','Augmented','Augmented','Augmented','Augmented','Augmented'],
    'Harmonic Minor':['Natural Minor','Diminished','Augmented','Natural Minor','Major','Major','Diminished'],
    'Melodic Minor':['Natural Minor','Natural Minor','Augmented','Major','Major','Diminished','Diminished'],
}


print(sys.getsizeof(degreeTonalityForModes))