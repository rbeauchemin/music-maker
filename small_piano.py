# -*- coding: ascii -*-
'''
Windows Only. Plays a song syncronously with only white keys. ctrl+C to kill.
'''
import curses
import winsound

c_major = {'c1':261.626, 'd':293.665, 'e':329.628, 'f':349.228, 'g':391.995, 'a':440.000, 'b':493.883, 'c2':523.251}
a = chr(219)

piano_vis = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
_________________________________________________
'''.format(a)
piano_vis_c1 = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|{0}{0}{0}{0}{0}|     |     |     |     |     |     |     |
|{0}{0}{0}{0}{0}|     |     |     |     |     |     |     |
|{0}{0}{0}{0}{0}|     |     |     |     |     |     |     |
|{0}{0}{0}{0}{0}|     |     |     |     |     |     |     |
|{0}{0}{0}{0}{0}|     |     |     |     |     |     |     |
|{0}{0}{0}{0}{0}|     |     |     |     |     |     |     |
|{0}{0}{0}{0}{0}|     |     |     |     |     |     |     |
_________________________________________________
'''.format(a)
piano_vis_d = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |{0}{0}{0}{0}{0}|     |     |     |     |     |     |
|     |{0}{0}{0}{0}{0}|     |     |     |     |     |     |
|     |{0}{0}{0}{0}{0}|     |     |     |     |     |     |
|     |{0}{0}{0}{0}{0}|     |     |     |     |     |     |
|     |{0}{0}{0}{0}{0}|     |     |     |     |     |     |
|     |{0}{0}{0}{0}{0}|     |     |     |     |     |     |
|     |{0}{0}{0}{0}{0}|     |     |     |     |     |     |
_________________________________________________
'''.format(a)
piano_vis_e = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |     |{0}{0}{0}{0}{0}|     |     |     |     |     |
|     |     |{0}{0}{0}{0}{0}|     |     |     |     |     |
|     |     |{0}{0}{0}{0}{0}|     |     |     |     |     |
|     |     |{0}{0}{0}{0}{0}|     |     |     |     |     |
|     |     |{0}{0}{0}{0}{0}|     |     |     |     |     |
|     |     |{0}{0}{0}{0}{0}|     |     |     |     |     |
|     |     |{0}{0}{0}{0}{0}|     |     |     |     |     |
_________________________________________________
'''.format(a)
piano_vis_f = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |     |     |{0}{0}{0}{0}{0}|     |     |     |     |
|     |     |     |{0}{0}{0}{0}{0}|     |     |     |     |
|     |     |     |{0}{0}{0}{0}{0}|     |     |     |     |
|     |     |     |{0}{0}{0}{0}{0}|     |     |     |     |
|     |     |     |{0}{0}{0}{0}{0}|     |     |     |     |
|     |     |     |{0}{0}{0}{0}{0}|     |     |     |     |
|     |     |     |{0}{0}{0}{0}{0}|     |     |     |     |
_________________________________________________
'''.format(a)
piano_vis_g = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |     |     |     |{0}{0}{0}{0}{0}|     |     |     |
|     |     |     |     |{0}{0}{0}{0}{0}|     |     |     |
|     |     |     |     |{0}{0}{0}{0}{0}|     |     |     |
|     |     |     |     |{0}{0}{0}{0}{0}|     |     |     |
|     |     |     |     |{0}{0}{0}{0}{0}|     |     |     |
|     |     |     |     |{0}{0}{0}{0}{0}|     |     |     |
|     |     |     |     |{0}{0}{0}{0}{0}|     |     |     |
_________________________________________________
'''.format(a)
piano_vis_a = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |     |     |     |     |{0}{0}{0}{0}{0}|     |     |
|     |     |     |     |     |{0}{0}{0}{0}{0}|     |     |
|     |     |     |     |     |{0}{0}{0}{0}{0}|     |     |
|     |     |     |     |     |{0}{0}{0}{0}{0}|     |     |
|     |     |     |     |     |{0}{0}{0}{0}{0}|     |     |
|     |     |     |     |     |{0}{0}{0}{0}{0}|     |     |
|     |     |     |     |     |{0}{0}{0}{0}{0}|     |     |
_________________________________________________
'''.format(a)
piano_vis_b = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |     |     |     |     |     |{0}{0}{0}{0}{0}|     |
|     |     |     |     |     |     |{0}{0}{0}{0}{0}|     |
|     |     |     |     |     |     |{0}{0}{0}{0}{0}|     |
|     |     |     |     |     |     |{0}{0}{0}{0}{0}|     |
|     |     |     |     |     |     |{0}{0}{0}{0}{0}|     |
|     |     |     |     |     |     |{0}{0}{0}{0}{0}|     |
|     |     |     |     |     |     |{0}{0}{0}{0}{0}|     |
_________________________________________________
'''.format(a)
piano_vis_c2 = '''
   C     D     E     F     G     A     B     C
_________________________________________________
|     |     |     |     |     |     |     |{0}{0}{0}{0}{0}|
|     |     |     |     |     |     |     |{0}{0}{0}{0}{0}|
|     |     |     |     |     |     |     |{0}{0}{0}{0}{0}|
|     |     |     |     |     |     |     |{0}{0}{0}{0}{0}|
|     |     |     |     |     |     |     |{0}{0}{0}{0}{0}|
|     |     |     |     |     |     |     |{0}{0}{0}{0}{0}|
|     |     |     |     |     |     |     |{0}{0}{0}{0}{0}|
_________________________________________________
'''.format(a)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

while True:
    stdscr.addstr(0,0,piano_vis)
    stdscr.refresh()
    entered = stdscr.getch()
    if entered == ord('a'):
        stdscr.addstr(0,0,piano_vis_c1)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['c1'])),200)
    elif entered == ord('s'):
        stdscr.addstr(0,0,piano_vis_d)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['d'])),200)
    elif entered == ord('d'):
        stdscr.addstr(0,0,piano_vis_e)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['e'])),200)
    elif entered == ord('f'):
        stdscr.addstr(0,0,piano_vis_f)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['f'])),200)
    elif entered == ord('j'):
        stdscr.addstr(0,0,piano_vis_g)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['g'])),200)
    elif entered == ord('k'):
        stdscr.addstr(0,0,piano_vis_a)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['a'])),200)
    elif entered == ord('l'):
        stdscr.addstr(0,0,piano_vis_b)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['b'])),200)
    elif entered == ord(';'):
        stdscr.addstr(0,0,piano_vis_c2)
        stdscr.refresh()
        winsound.Beep(int(round(c_major['c2'])),200)
    elif entered == ord('q'):
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()
        exit()
    else:
        pass
