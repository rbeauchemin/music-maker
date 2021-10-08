'''
Windows Only. Plays a song in a selected key. ctrl+C to kill the song.
'''
import winsound
import time


ChromaticCircle = {'LowC': 262, 'LowC#': 277, 'LowD': 294, 'LowD#': 311, 'LowE': 330, 'LowF': 349,
                   'LowF#': 370, 'LowG': 392, 'LowG#': 415, 'LowA': 440, 'LowA#': 466, 'LowB': 494,
                   'HighC': 523, 'HighC#': 554,'HighD': 587, 'HighD#': 622, 'HighE': 659, 'HighF': 698,
                   'HighF#': 740, 'HighG': 784, 'HighG#': 831, 'HighA': 880, 'HighA#': 932, 'HighB': 988,
                   'REST': 0}

DMajor = ['LowD', 'LowE', 'LowF#', 'LowG', 'REST', 'LowA', 'LowB', 'LowC#', 'HighD']
CMajor = ['LowC', 'LowD', 'LowE', 'LowF', 'REST', 'LowG', 'LowA', 'LowB', 'HighC']
CMinor = ['LowC', 'LowD', 'LowD#', 'LowF', 'REST', 'LowG', 'LowG#', 'LowA#', 'HighC']

Tempo = [200, 100, 400]


def buildscale(scaleIn, noteDict):
    scaleOut = []
    for note in scaleIn:
        scaleOut.append(noteDict[note])
    return scaleOut


def step(tape, rule):
    rule_lookup = [c == '1' for c in '{:08b}'.format(rule)]
    newtape = [False] * len(tape)
    for i in range(len(tape)):
        s = tape[i - 1] * 4 + tape[i] * 2 + tape[(i + 1) % len(tape)]
        newtape[i] = rule_lookup[-1 - s]
    for i in range(len(tape)):
        tape[i] = newtape[i]


def music(rows, rule, scale, size=16):
    scale = buildscale(scale, ChromaticCircle)
    tape = [False] * size
    tape[size // 2] = True
    for _ in range(rows):
        display(tape)
        playmusic(tape, scale)
        step(tape, rule)


def display(tape):
    print(''.join('@' if b else ' ' for b in tape))


def playmusic(tape, scale, tempo=Tempo):
    note = sum(i for i in tape[5:-4])
    duration = sum(i for i in tape[1:3])
    if note == scale.index(0):
        time.sleep(tempo[duration] / 1000)
    else:
        winsound.Beep(scale[note], tempo[duration])


music(100, 86, CMinor)
