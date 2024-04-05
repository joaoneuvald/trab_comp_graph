from OpenGL.GL import *

class Shot:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.move_speed = 0.05

    def move(self):
        while (self.position_y <= 1000):
            glTranslate(self.position_x, self.position_y + 0.025)


    def draw(self):
        glBegin(GL_LINES)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.position_x, self.position_y, 0)
        glColor3f(0.15, 1, 0.15)
        glVertex3f(self.position_x, self.position_y + 0.05, 0)
        glEnd()