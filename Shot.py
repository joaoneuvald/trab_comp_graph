from OpenGL.GL import *
import glfw

class Shot:
    def __init__(self, x):
        self.x = x
        self.y = -1.0
        self.speed = 0.1
        self.fired = False

    def update(self):
        if self.fired:
            self.y += self.speed
            
            if self.y > 1.0:
                self.fired = False
                self.y = -1.0
"""
            while (self.position_y <= 1000):
            glTranslate(self.position_x, self.position_y + 0.025)"""

            glTranslate(self.x, self.y, 0)

    def draw(self, x):
        self.x = x
        if self.fired:
            glBegin(GL_QUADS)
            glColor3f(1.0, 0.0, 0.0)
            glVertex2f(self.x, self.y)
            glVertex2f(self.x + 0.01, self.y + 0.05)
            glVertex2f(self.x - 0.01, self.y + 0.05)
            glVertex2f(self.x, self.y)
            glEnd()
