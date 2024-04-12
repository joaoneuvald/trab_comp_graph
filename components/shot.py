from OpenGL.GL import *


class Shot:
    def __init__(self, position_x, position_y):
        print(position_x, position_y)
        self.positionX = position_x
        self.positionY = position_y
        self.moveSpeed = 0.01

    def move(self):
        if self.positionY < 1.0:
            self.positionY += self.moveSpeed
            glTranslate(self.positionX, self.positionY, 0)

    def draw(self):
            glBegin(GL_TRIANGLES)
            glColor3f(1.0, 0.0, 0.0)
            glVertex2f(self.positionX, self.positionY)
            glVertex2f(self.positionX + 0.01, self.positionY + 0.05)
            glVertex2f(self.positionX - 0.01, self.positionY + 0.05)
            glVertex2f(self.positionX, self.positionY)
            glEnd()
