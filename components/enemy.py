from OpenGL.GL import *
from components.ship import Direction

class Enemy:
    def __init__(self, lineIndex, columnIndex):
        self.positionX = columnIndex * 0.14 - 0.6
        self.positionY = 0.92 - lineIndex * 0.13
        self.speed = 0.001
        self.alive = True

    def move(self, direction: Direction, descend: bool = False):
        if self.alive:
            if direction == Direction.RIGHT:
                self.positionX += self.speed
            elif direction == Direction.LEFT:
                self.positionX -= self.speed
            
            if descend:
                self.positionY -= 0.1

            glTranslate(self.positionX, self.positionY,0)


    def draw(self):
        if self.alive:
            glBegin(GL_TRIANGLES)
            glColor3f(0.0, 1.0, 0.0)
            glVertex2f(self.positionX, self.positionY + 0.05)
            glVertex2f(self.positionX - 0.05, self.positionY - 0.05)
            glVertex2f(self.positionX + 0.05, self.positionY - 0.05)
            glEnd()