from gl import Renderer, V3, color
from obj import Texture
from shaders import *

width = 960
height = 460

rend = Renderer(width, height)

#rend.background = Texture("model.bmp")
#rend.glClearBackground()

modelo = 'craft.obj'
escala = V3(4,4,4)
traslacion = V3(2,0,-9)
rotacion = V3(0,0,0)

# Static
#for x in range(width):
#    for y in range(height):
#        if random.random() > 0.999:
#            rend.glPoint(x, y, color(1,1,1))

# Starfield
for x in range(width):
    for y in range(height):
        if random.random() > 0.996:
            size = random.randrange(0, 3)

            brightness = random.random() / 2 + 0.5

            starColor = color(brightness, brightness, brightness)

            if size == 0:
                rend.glPoint(x,y,starColor)

            elif size == 1:
                rend.glPoint(x,y,starColor)
                rend.glPoint(x+1,y,starColor)
                rend.glPoint(x+1,y+1,starColor)
                rend.glPoint(x,y+1,starColor)

            elif size == 2:
                rend.glPoint(x,y,starColor)
                rend.glPoint(x,y+1,starColor)
                rend.glPoint(x,y-1,starColor)
                rend.glPoint(x+1,y,starColor)
                rend.glPoint(x-1,y,starColor)

#nave
rend.active_texture = Texture('model.bmp')
rend.active_shader = Guate
rend.glLoadModelShade('nave.obj', V3(0.5,0.5,0.5), V3(-3,0,-8), V3(0,50,10))
rend.glFinish('output.bmp')

#Planeta1
rend.active_texture = Texture('model.bmp')
rend.active_shader = ShuffleColor
rend.glLoadModelShade('planeta.obj', V3(2,2,2), V3(5,0,-9), V3(0,0,0))
rend.glFinish('output.bmp')

#Planeta2
rend.active_texture = Texture('model.bmp')
rend.active_shader = MotherRussia
rend.glLoadModelShade('planeta.obj', V3(0.75,0.75,0.75), V3(7,2,-8), V3(0,0,0))
rend.glFinish('output.bmp')

#Stormtrooper
rend.active_texture = Texture('model.bmp')
rend.active_shader = Shell
rend.glLoadModelShade('stormtrooper.obj', V3(0.85,0.85,0.85), V3(-3.2,0,-8), V3(0,40,5))
rend.glFinish('output.bmp')

#Disparos Abajo
rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.2,0.1,0.2), V3(-1.9,-1,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.4,0.1,0.25), V3(-1.5,-1.1,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.3,0.1,0.3), V3(-1,-1.2,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(-0.5,-1,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(0.1,-0.9,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(0.7,-0.8,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(1.3,-0.9,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(1.9,-0.8,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(2.5,-0.9,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(3.1,-1,-9), V3(0,0,0))
rend.glFinish('output.bmp')

#Disparos Arriba
rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(-0.4,0.6,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(-0.4,0.6,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(0.2,0.5,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(0.8,0.6,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(1.4,0.7,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(2,0.6,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.5,0.1,0.4), V3(2.6,0.5,-9), V3(0,0,0))
rend.glFinish('output.bmp')

#Arbol
rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('tree.obj', V3(0.11,0.11,0.11), V3(5,2,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('tree.obj', V3(0.05,0.05,0.05), V3(3.5,1.3,-9), V3(0,0,30))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('tree.obj', V3(0.05,0.05,0.05), V3(7.7,0,-9), V3(-50,0,-100))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('tree.obj', V3(0.05,0.05,0.05), V3(6.8,-1.5,-9), V3(-50,0,-150))
rend.glFinish('output.bmp')
