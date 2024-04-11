from OpenGL.GL import *

class Shot:
    def __init__(self, position_x, position_y):
        print(position_x, position_y)
        self.positionX = position_x
        self.positionY = position_y
        self.moveSpeed = 0.0001

    def move(self):
        if self.positionY < 1.0:
            self.positionY += self.moveSpeed
            #glTranslate(self.positionX, self.positionY, 0)


    def draw(self):
        glBegin(GL_LINE_LOOP)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX, self.positionY, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.positionX, self.positionY + 0.05, 0)
        glEnd()