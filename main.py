print("Preparing...")
#Config

timeToSolve = 12
timeBetweenMoves = 0

#Get cube state

from PIL import ImageGrab
import keyboard
from pykeyboard import PyKeyboard
k = PyKeyboard()
from time import sleep
import mouse
mouse.move(666,666)
mouse.click()

sleep(0.5)
keyboard.send(" ")
sleep(0.5)
px = ImageGrab.grab().load()
print("Grabbed image")

def gc(x, y):
    col = px[x, y]
    if col == (255, 255, 255):
        return 'U'
    elif col == (235, 61, 29):
        return 'R'
    elif col == (99, 216, 53):
        return 'F'
    elif col == (255, 254, 70):
        return 'D'
    elif col == (243, 175, 50):
        return 'L'
    elif col == (0, 16, 248):
        return 'B'
    else :
        print("Unknown color: ", col)
        return 'X'

#U face GOOD
U1 = gc(500, 330)
U2 = gc(660, 330)
U3 = gc(820, 330)
U4 = gc(460, 444)
U5 = 'U'
U6 = gc(862, 450)
U7 = gc(500, 600)
U8 = gc(660, 600)
U9 = gc(820, 600)
print("-----------------------------------------------------")
print('U face calculated')
print('colors: ' + U1, U2, U3, U4, U5, U6, U7, U8, U9)
print("-----------------------------------------------------")
#R face GOOD
R1 = gc(976, 656)
R2 = gc(950, 508)
R3 = gc(932, 384)
R4 = gc(953, 802)
R5 = 'R'
R6 = gc(908, 509)
R7 = gc(930, 926)
R8 = gc(908, 801)
R9 = gc(891, 657)
print('R face calculated')
print('colors: ' + R1, R2, R3, R4, R5, R6, R7, R8, R9)
print("-----------------------------------------------------")
#F face GOOD
F1 = gc(475, 700)
F2 = gc(650, 700)
F3 = gc(825, 700)
F4 = gc(500, 850)
F5 = 'F'
F6 = gc(825, 850)
F7 = gc(478, 980)
F8 = gc(659, 980)
F9 = gc(836, 980)
print('F face calculated')
print('colors: ' + F1, F2, F3, F4, F5, F6, F7, F8, F9)
print("-----------------------------------------------------")
#D face GOOD
D1 = gc(490, 927)
D2 = gc(660, 927)
D3 = gc(830, 927)
D4 = gc(552, 811)
D5 = 'D'
D6 = gc(827, 803)
D7 = gc(548, 707)
D8 = gc(664, 665)
D9 = gc(772, 713)
print('D face calculated')
print('colors: ' + D1, D2, D3, D4, D5, D6, D7, D8, D9)
print("-----------------------------------------------------")
#L face GOOD
L1 = gc(390, 383)
L2 = gc(370, 507)
L3 = gc(344, 655)
L4 = gc(412, 510)
L5 = 'L'
L6 = gc(370, 801)
L7 = gc(430, 655)
L8 = gc(412, 802)
L9 = gc(392, 927)
print('L face calculated')
print('colors: ' + L1, L2, L3, L4, L5, L6, L7, L8, L9)
print("-----------------------------------------------------")
#B face
B1 = gc(820, 385)
B2 = gc(660, 385)
B3 = gc(500, 385)
B4 = gc(820, 505)
B5 = 'B'
B6 = gc(500, 505)
B7 = gc(771, 609)
B8 = gc(666, 646)
B9 = gc(548, 598)
print('B face calculated')
print('colors: ' + B1, B2, B3, B4, B5, B6, B7, B8, B9)
print("-----------------------------------------------------")
print("Grabbed cube state")

#Find solution

print("Prepping to find solution...")
import twophase.solver as sv
cubestring = str(U1 + U2 + U3 + U4 + U5 + U6 + U7 + U8 + U9 + R1 + R2 + R3 + R4 + R5 + R6 + R7 + R8 + R9 + F1 + F2 + F3 + F4 + F5 + F6 + F7 + F8 + F9 + D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9 + B1 + B2 + B3 + B4 + B5 + B6 + B7 + B8 + B9)
if "X" in cubestring:
    print("Error: not all colors found")
    exit()
print("cubestring: ", cubestring)
print("Finished prep, starting search...")
solution = sv.solve(cubestring,0,timeToSolve)
print("Solution computed: \n" + solution)
solution = solution.split(' ')[:-1]

#Execute solution

class Keybinds:
    r = 'I' #good
    ri = 'K' #good
    u = 'J' #broken/MediaStop
    ui = 'F' #broken/Unknown
    f = 'H' #good
    fi = 'G' #broken/Unknown
    d = 'S' #good
    di = 'L' #good
    l = 'D' #broken/MediaMute
    li = 'E' #good
    b = 'W' #good
    bi = 'O' #good
    
def executeMove(move):
    if str(1) in move:
        if 'R' in move:
            keyboard.send(Keybinds.r)
        elif 'L' in move:
            k.tap_key(Keybinds.l)
        elif 'U' in move:
            k.tap_key(Keybinds.u)
        elif 'F' in move:
            keyboard.send(Keybinds.f)
        elif 'D' in move:
            keyboard.send(Keybinds.d)
        elif 'B' in move:
            keyboard.send(Keybinds.b)
    elif str(2) in move:
        if 'R' in move:
            keyboard.send(Keybinds.r)
            sleep(timeBetweenMoves)
            keyboard.send(Keybinds.r)
        elif 'L' in move:
            k.tap_key(Keybinds.l)
            sleep(timeBetweenMoves)
            k.tap_key(Keybinds.l)
        elif 'U' in move:
            k.tap_key(Keybinds.u)
            sleep(timeBetweenMoves)
            k.tap_key(Keybinds.u)
        elif 'F' in move:
            keyboard.send(Keybinds.f)
            sleep(timeBetweenMoves)
            keyboard.send(Keybinds.f)
        elif 'D' in move:
            keyboard.send(Keybinds.d)
            sleep(timeBetweenMoves)
            keyboard.send(Keybinds.d)
        elif 'B' in move:
            keyboard.send(Keybinds.b)
            sleep(timeBetweenMoves)
            keyboard.send(Keybinds.b)
    elif str(3) in move:
        if 'R' in move:
            keyboard.send(Keybinds.ri)
        elif 'L' in move:
            keyboard.send(Keybinds.li)
        elif 'U' in move:
            k.tap_key(Keybinds.ui)
        elif 'F' in move:
            k.tap_key(Keybinds.fi)
        elif 'D' in move:
            keyboard.send(Keybinds.di)
        elif 'B' in move:
            keyboard.send(Keybinds.bi)

for move in solution:
    executeMove(move)
    sleep(timeBetweenMoves)

print("Finished execution!")
    