from OpenGL.GL import *
from enum import Enum
from PIL import Image
import numpy as np

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
        
        image_path = "assets/sprite_ship_3.png"
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

    def move(self, direction: Direction):
        if direction == Direction.RIGHT and self.positionX < 0.9:
            self.positionX += self.moveSpeed
        elif direction == Direction.LEFT and self.positionX > -0.99:
            self.positionX -= self.moveSpeed
        self.center = self.positionX + 0.05
        glTranslate(self.positionX, self.positionY, 0)

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        
        glTexCoord2f(0.0, 1.0); glVertex3f(self.positionX, self.positionY, 0)
        glTexCoord2f(0.0, 0.0); glVertex3f(self.positionX, self.positionY + 0.1, 0)
        glTexCoord2f(1.0, 0.0); glVertex3f(self.positionX + 0.1, self.positionY + 0.1, 0)
        glTexCoord2f(1.0, 1.0); glVertex3f(self.positionX + 0.1, self.positionY, 0)
        
        glEnd()
        glDisable(GL_TEXTURE_2D)
