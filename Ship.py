from OpenGL.GL import *
import glfw

class Ship:
    def __init__(self):
        self.x = 0.0
        self.speed = 0.05

    def move(self, direction):
        self.x = direction * self.speed
        if self.x < -1.0:
            self.x = -1.0
        elif self.x > 1.0:
            self.x = 1.0

        """
        CARNIÇA QUE NÃO FUNCIONA
        glLoadIdentity()
        glTranslate(self.x * direction, 0, 0)"""
        

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(self.x - 0.05, -0.8)
        glVertex2f(self.x + 0.05, -0.8)
        glVertex2f(self.x, -0.7)
        glEnd()