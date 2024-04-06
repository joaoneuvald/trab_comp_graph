from OpenGL.GL import *
import glfw

class Enemy:
    def __init__(self):
        self.x = 0.0
        self.y = 0.8
        self.speed = 0.02
        self.alive = True

    def update(self):
        if self.alive:
            self.x += self.speed
            if self.x > 1.0 or self.x < -1.0:
                self.speed = -self.speed

    def draw(self):
        if self.alive:
            glBegin(GL_TRIANGLES)
            glColor3f(0.0, 1.0, 0.0)
            glVertex2f(self.x, self.y + 0.1)
            glVertex2f(self.x - 0.1, self.y - 0.1)
            glVertex2f(self.x + 0.1, self.y - 0.1)
            glEnd()