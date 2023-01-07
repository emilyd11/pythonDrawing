import os
import time
from termcolor import colored
import math
import random 

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        if round(point[0]) < 0 or round(point[0]) >= self._x:
            # bounced off vertical wall 
            return True, "v"
        elif round(point[1]) < 0 or round(point[1]) >= self._y:
            # bounced off horizontal wall 
            return True, "h"
        else: 
            return False, ""


    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    #sets degrees for directional movement. thrown off a bit by rounding when pos is set. 

    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]
        self.direction = [0, 0]

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
       self.direction = [-1, 0]
       self.forward()

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)
    
    #SOLUTION CODE FROM COURSE VIDEO-- passing in a function
    #functionality to add: stop it from hitting a wall. 
    #currently there is no check to stop it from hitting walls.
    def plotX(self, function):
        for x in range(self.canvas._x):
            pos = [x, function(x)]
            self.draw(pos)

    #draws a square with sides of a specified length 
    def drawSquare(self, size):
        for i in range(size-1): 
            self.right()
        
        for i in range(size-1):
            self.down()

        for i in range(size-1):
            self.left()
        
        for i in range(size):
            self.up()
    
    def setPosition(self, pos):
        self.pos = pos
        
    def setDegrees(self, degrees):
        self.degrees = degrees
        rads = (self.degrees/180)*math.pi
        self.direction = [math.sin(rads), -math.cos(rads)]

    #moves the scribe forward; depends on what the direction is currently set to (bvariable of the scribe object)
    def forward (self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos)[0]:
            self.draw(pos)
        elif self.canvas.hitsWall(pos)[1] == "v":
            self.direction[0] = -1 * self.direction[0]
            pos = [self.pos[0] + 2*self.direction[0], self.pos[1]]
            self.draw(pos)
        elif self.canvas.hitsWall(pos)[1] == "h":
            self.direction[1] = -1 * self.direction[1]
            pos = [self.pos[0], self.pos[1] + 2 * self.direction[1]]
            self.draw(pos)


class RandomTerminalScribe(TerminalScribe):
    
    def setDegrees(self):
        self.degrees = random.randrange(0, 180, 1)
        rads = (self.degrees/180)*math.pi
        self.direction = [math.sin(rads), -math.cos(rads)]
    

# SOLUTION CODE FROM COURSE VIDEO-- defining a function 
#which we can pass in to perform some predetermined thing with the scribe.
def sine(x):
    return 5*math.sin(x/4) + 10

#TESTING 
canvas = Canvas(30, 30)

#practicing data structures (example code)
# note: a list of dictionaries is good when you are wanting to set several parameters 
'''scribes = [
    {'degrees': 30, 'position': [10, 5], 'instructions': [
        {'function': 'forward', 'duration': 5 }
        ]},
    {'degrees': 180, 'position': [15, 15], 'instructions': [
        {'function': 'forward', 'duration': 5 },
        {'function': 'down', 'duration': 2}
        ]}
    ]

for scribeData in scribes:
    scribeData['scribe'] = TerminalScribe(canvas)
    scribeData['scribe'].setDegrees(scribeData['degrees'])
    scribeData['scribe'].setPosition(scribeData['position'])

    # Flatten instructions: convert "{'left':10}" to ['left', 'left', 'left'... ] etc
    scribeData['instructions_flat'] = []
    for instruction in scribeData['instructions']:
        scribeData['instructions_flat'] = scribeData['instructions_flat'] + [instruction['function']]*instruction['duration']

# we don't want to start reading instructions that don't exist -> find what the longest instruction is so we can stop the loop 
maxInstructionLen = max([len(scribeData['instructions_flat']) for scribeData in scribes])

# reading the instructions (modified from solution code: you can't draw a square using the function from the set of the dictionary at this time)
for i in range(maxInstructionLen):
    for scribeData in scribes:
        if i < len(scribeData['instructions_flat']):
            if scribeData['instructions_flat'][i] == 'forward':
                scribeData['scribe'].forward()
            elif scribeData['instructions_flat'][i] == 'up':
                scribeData['scribe'].up()
            elif scribeData['instructions_flat'][i] == 'down':
                scribeData['scribe'].down()
            elif scribeData['instructions_flat'][i] == 'left':
                scribeData['scribe'].left()
            elif scribeData['instructions_flat'][i] == 'right':
                scribeData['scribe'].right()
            
'''
 
scribe = TerminalScribe(canvas)

scribe.setPosition = [0, 0]

scribe.forward()
scribe.forward()
scribe.forward()
scribe.forward()


'''scribe.setDegrees(150)
for i in range(500):
    scribe.forward() '''