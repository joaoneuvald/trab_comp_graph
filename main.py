import glfw
from OpenGL.GL import *
from Ship import *
from Enemy import *
from Shot import *
import numpy as np

def check_collision():
    global shot, enemy
    if shot.fired and enemy.alive:
        if abs(shot.y - enemy.y) < 0.05 and abs(ship.x - enemy.x) < 0.2:
            enemy.alive = False
            shot.fired = False

def main():
    global window, ship, enemy, shot

    if not glfw.init():
        return

    width, height = 800, 600
    window = glfw.create_window(width, height, "Space Invaders", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    ship = Ship()
    enemy = Enemy()
    shot = Shot(ship.x)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            ship.move(-1)
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            ship.move(1)
        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            shot = Shot(ship.x)
            shot.fired = True
            
        shot.update()
        enemy.update()
        check_collision()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        ship.draw()
        enemy.draw()
        shot.draw(ship.x)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
