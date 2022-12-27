import os
import time
from termcolor import colored
import math

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

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

    #sets degrees for directional movement. thrown off a bit by rounding when pos is set. 
    def setDegrees(self, degrees):
        rads = (degrees/180)*math.pi
        self.direction = [math.sin(rads), -math.cos(rads)]

    #moves the scribe forward; depends on what the direction is currently set to (bvariable of the scribe object)
    def forward (self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)




canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

scribe.drawSquare(5)

scribe.down()
scribe.down()
scribe.down()

scribe.setDegrees(45)
for i in range(3):
  scribe.forward()