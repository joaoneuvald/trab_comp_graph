import glfw
from OpenGL.GL import *
from components.ship import *
from components.enemy import *
from components.shot import Shot
import numpy as np
import time

def check_collision():
    global shots, enemies
    for shot in shots:
        shotRemoved = False
        for line in enemies:
            for enemy in line:
                if enemy.alive:
                    if (shot.positionY >= enemy.positionY - 0.05 or shot.positionY <= enemy.positionY) and (shot.positionX >= enemy.positionX - 0.05 and shot.positionX <= enemy.positionX + 0.05):
                        enemy.alive = False
                        shots.remove(shot)
                        shotRemoved = True
                        break
                # if abs(shot.positionY - enemy.positionY) < 0.05 and abs(shot.positionX - enemy.positionX) < 0.2:
                #     enemy.alive = False
                #     shots.remove(shot)
            if shotRemoved:
                break

def checkEndGame():
    global enemies
    for line in enemies:
        for enemy in line:
            if enemy.alive and enemy.positionY <= -0.85:
                print("Game Over")
                glfw.terminate()
                exit()
                
def main():
    global window, ship, enemy, shots, enemies
    enemies = [[], [], []]

    if not glfw.init():
        return

    width, height = 800, 800
    window = glfw.create_window(width, height, "Space Invaders", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    for i in range(3):
        enemies[i] = []
        for j in range(10):
            enemies[i].append(Enemy(i, j))

    ship = Ship()
    enemy = Enemy(0,0)
    shots = [Shot(ship.positionX, ship.shotOutY)]
    lastShot = time.time()

    enemyDirection = Direction.RIGHT
    while not glfw.window_should_close(window):
        enemyDescend = False

        if(enemies[0][len(enemies[0])-1].positionX >= 0.95):
            enemyDirection = Direction.LEFT
            enemyDescend = True
        elif(enemies[0][0].positionX <= -0.95):
            enemyDirection = Direction.RIGHT
            enemyDescend = True
    
        glfw.poll_events()

        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            ship.move(Direction.LEFT)
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            ship.move(Direction.RIGHT)
        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            if(time.time() - lastShot > 1):
                shots.append(Shot(ship.center, ship.shotOutY))
                lastShot = time.time()
        if glfw.get_key(window,glfw.KEY_ESCAPE) == glfw.PRESS:
            break;
            
        check_collision()
        checkEndGame()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glLoadIdentity()
        ship.draw()

        for shot in shots:
            shot.draw()
            shot.move()
            glLoadIdentity()
            if shot.positionY >= 1:
                shots.remove(shot)

        for enemyArray in enemies:
            for enemy in enemyArray:
                enemy.draw()
                enemy.move(enemyDirection, enemyDescend)
                glLoadIdentity()
        
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
