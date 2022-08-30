from gl import Renderer, V3, color
from obj import Texture
from shaders import *

width = 960
height = 540


rend = Renderer(width, height)

modelo = 'craft.obj'
escala = V3(4,4,4)
traslacion = V3(2,0,-9)
rotacion = V3(0,0,0)


rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('nave.obj', V3(0.5,0.5,0.5), V3(2,0,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = ShuffleColor
rend.glLoadModelShade('model.obj', V3(1,1,1), V3(2,1.5,-8), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = MotherRussia
rend.glLoadModelShade('planeta.obj', V3(1,1,1), V3(-4,0.5,-8), V3(0,0,0))
rend.glFinish('output.bmp')



rend.active_texture = Texture('model.bmp')
rend.active_shader = Guate
rend.glLoadModelShade('planeta.obj', V3(0.75,0.75,0.75), V3(-1.5,0.5,-8), V3(0,0,0))
rend.glFinish('output.bmp')


rend.active_texture = Texture('model.bmp')
rend.active_shader = Shell
rend.glLoadModelShade('stormtrooper.obj', V3(0.75,0.75,0.75), V3(-1.5,0.5,-8), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.2,0.2,0.2), V3(-3,0,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.2,0.2,0.2), V3(-3,-1,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.2,0.2,0.2), V3(-3.2,-0.5,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.2,0.2,0.2), V3(-2.7,-1,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.2,0.2,0.2), V3(-2.3,-1,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.2,0.2,0.2), V3(-1.9,-1.2,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.25,0.25,0.25), V3(-1.5,-1.2,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.3,0.3,0.3), V3(-1,-1.2,-9), V3(0,0,0))
rend.glFinish('output.bmp')

rend.active_texture = Texture('model.bmp')
rend.active_shader = NightVision
rend.glLoadModelShade('model3.obj', V3(0.4,0.4,0.4), V3(-0.5,-0.8,-9), V3(0,0,0))
rend.glFinish('output.bmp')

#rend.active_texture = Texture('model.bmp')
#rend.active_shader = ShuffleColor
#rend.glLoadModelShade(modelo, escala, traslacion, rotacion)
#rend.glFinish('output.bmp')

