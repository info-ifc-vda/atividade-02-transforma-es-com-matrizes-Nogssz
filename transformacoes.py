import glfw
from OpenGL.GL import *
import math

vertices = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

def init():
    glClearColor(0, 0, 0, 1)

    
def translacao(v, tx, ty):
    novo = []
    for x, y in v:
        novo.append([x + tx, y + ty])
    return novo

def escala(v, sx, sy):
    novo = []
    for x, y in v:
        novo.append([x * sx, y * sy])
    return novo

def reflexao(v):
    novo = []
    for x, y in v:

        novo.append([-x, y])
    return novo

def rotacao(v, angulo_graus):
    novo = []
    rad = math.radians(angulo_graus) 
    cos_a = math.cos(rad)
    sen_a = math.sin(rad)
    
    for x, y in v:
 
        nx = x * cos_a - y * sen_a
        ny = x * sen_a + y * cos_a
        novo.append([nx, ny])
    return novo



def render(v):    
    glBegin(GL_TRIANGLES)    
    for x, y in v:
        glVertex2f(x, y)                    
    glEnd()
    
def main():
    glfw.init() # inicializa biblioteca glfw
    window = glfw.create_window(800, 600, "Matrizes de Transformação", None, None)
    glfw.make_context_current(window) # cria o contexto
    init()
    
    v_translacao = translacao(vertices, -0.6, 0.2) 
    v_escala = translacao(escala(vertices, 0.5, 0.5), 0.6, 0.2) 
    v_reflexao = translacao(reflexao(vertices), -0.6, -0.6)     
    v_rotacao = translacao(rotacao(vertices, 45), 0.6, -0.6)   
    
    while not glfw.window_should_close(window): # roda enquanto não fecha a janela
        glfw.poll_events() # captura eventos
        glClear(GL_COLOR_BUFFER_BIT)
        
    
        render(vertices)
        
  
        render(v_translacao)
        render(v_escala)
        render(v_reflexao)
        render(v_rotacao)
        
        glfw.swap_buffers(window)
        
    glfw.terminate()
    
if __name__ == "__main__":
    main()