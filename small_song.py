'''
Windows Only. Plays a song in major key or minor key. ctrl+C to kill the song.
'''
import winsound
import random

c_major = [261.626, 293.665, 329.628, 349.228, 391.995, 440.000, 493.883, 523.251]
c_minor = [261.626, 293.665, 311.127, 349.228, 391.995, 415.305, 466.164, 523.251]

choice = input("major or minor scale? ([M]/m): ") or 'M'
if choice in ['M', 'major']:
    for i in range(200):
        winsound.Beep(random.choice([int(round(note,0)) for note in c_major]), random.choice([250, 500, 1000]))
elif choice in ['m', 'minor']:
    for i in range(200):
        winsound.Beep(random.choice([int(round(note,0)) for note in c_minor]), random.choice([1000, 1500, 2000]))
