from OpenGL.GL import *
from Shot import *
import numpy as np
import glfw

def main():
    if not glfw.init():
        return

    janela = glfw.create_window(1000, 1000, "Minha janela", None, None)
    if not janela:
        glfw.terminate()
        return

    glfw.make_context_current(janela)

    while not glfw.window_should_close(janela):
        glfw.poll_events()
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        shot = Shot(0, 0.5)
        shot.draw()
        shot.move()
        glfw.swap_buffers(janela)

    glfw.destroy_window(janela)
    glfw.terminate()

if __name__ == "__main__":
    main()
    