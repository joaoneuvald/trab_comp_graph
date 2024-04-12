from OpenGL.GL import *
from enum import Enum

class Direction(Enum):
    RIGHT = 1
    LEFT = 2

class Ship:
    def __init__(self):
        self.positionX = -0.05
        self.positionY = -0.95
        self.moveSpeed = 0.01
        self.center = self.positionX + 0.05
        self.shotOutY = -0.9

    def move(self, direction: Direction):
        if direction == Direction.RIGHT and self.positionX < 0.9:
            self.positionX += self.moveSpeed
        elif direction == Direction.LEFT and self.positionX > -0.99:
            self.positionX -= self.moveSpeed
        self.center = self.positionX + 0.05
        glTranslate(self.positionX, self.positionY, 0)


    def draw(self):
        glBegin(GL_LINE_LOOP)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX, self.positionY, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX, self.positionY + 0.03, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX + 0.04, self.positionY + 0.03, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX + 0.04, self.positionY + 0.04, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX + 0.06, self.positionY + 0.04, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX + 0.06, self.positionY + 0.03, 0)        
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX + 0.1, self.positionY + 0.03, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX + 0.1, self.positionY, 0)
        glEnd()