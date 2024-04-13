from OpenGL.GL import *
from PIL import Image
from components.ship import Direction
import numpy as np

class Enemy:
    def __init__(self, lineIndex, columnIndex):
        self.positionX = columnIndex * 0.14 - 0.6
        self.positionY = 0.92 - lineIndex * 0.13
        self.speed = 0.001
        self.alive = True
        
        image_path = "assets/sprite_2.png"
        self.texture_id = self.load_texture(image_path)

    def load_texture(self, image_path):
        img = Image.open(image_path)
        img_data = np.array(list(img.getdata()), np.uint8)
        
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        
        return texture_id

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
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)
            
            glBegin(GL_QUADS)
            glColor3f(1.0, 1.0, 1.0)
            glTexCoord2f(0.0, 1.0); glVertex2f(self.positionX - 0.05, self.positionY + 0.05)
            glTexCoord2f(0.0, 0.0); glVertex2f(self.positionX - 0.05, self.positionY - 0.05)
            glTexCoord2f(1.0, 0.0); glVertex2f(self.positionX + 0.05, self.positionY - 0.05)
            glTexCoord2f(1.0, 1.0); glVertex2f(self.positionX + 0.05, self.positionY + 0.05)
            glEnd()
            glDisable(GL_TEXTURE_2D)
