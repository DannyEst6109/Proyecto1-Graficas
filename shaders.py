from gl import color
import mate as mate
import random


def flat(renderer, **kwargs):
    A, B, C = kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    triangleNormal = kwargs['triangleNormal']

    b, g, r = b / 255, g / 255, r / 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    intensity = mate.pPunto(triangleNormal, renderer.directional_light)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def gourad(renderer, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    intensityA = mate.pPunto(nA, renderer.directional_light)
    intensityB = mate.pPunto(nB, renderer.directional_light)
    intensityC = mate.pPunto(nC, renderer.directional_light)

    intensity = intensityA * u + intensityB * v + intensityC * w

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def phong(renderer, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mate.pPunto(normal, renderer.directional_light)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0


def unlit(renderer, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    return r, g, b


def toon(renderer, **kwargs):
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    nA, nB, nC = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = (nX, nY, nZ)

    intensity = mate.pPunto(normal, renderer.directional_light)

    if intensity > 0.7:
        intensity = 1
    elif intensity > 0.3:
        intensity = 0.5
    else:
        intensity = 0.05

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0, 0, 0



def MotherRussia(renderer, **kwargs):

    color1 = 0,0.13,0.28
    color2 = 1,1,1
    color3 = 0.73,0.074,0.25

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    A, B, C = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    X = A[0] * u + B[0] * v + C[0] * w
    Y = A[1] * u + B[1] * v + C[1] * w
    Z = A[2] * u + B[2] * v + C[2] * w

    n = (X, Y, Z)

    l = mate.pPunto(n, renderer.directional_light)



    if l > 0.80:
        r, g, b = color1
    elif l > 0.60:
        r, g, b = color2
    elif l > 0.40:
        r, g, b = color3
    elif l > 0.20:
        r, g, b = color1
    elif l > 0.10:
        r, g, b = color2
    else:
        r, g, b = color2

    b *= l
    g *= l
    r *= l

    if l > 0:
        return r, g, b
    else:
        return 0, 0, 0


def ShuffleColor(renderer, **kwargs):

    color1 = 0,0.13,0.28
    color2 = 1,1,1
    color3 = 0.73,0.074,0.25
    color4 = 0,0,0
    color5 = 1,0,0
    color6 = 0,1,0
    color7 = 0,0,1

    color1a = 0.5,0.5,0.5
    color2a = 0.2,0.2,0.2
    color3a = 0.7,0.2,0.1
    color4a = 0,0.5,0.9
    color5a = 0.8,0,0.5
    color6a = 0.1,0.9,0.4

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    A, B, C = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    X = A[0] * u + B[0] * v + C[0] * w
    Y = A[1] * u + B[1] * v + C[1] * w
    Z = A[2] * u + B[2] * v + C[2] * w

    n = (X, Y, Z)

    l = mate.pPunto(n, renderer.directional_light)



    if l > 0.5:
        num = random.randint(1,6)
        if num == 1:
            r, g, b = color1
        elif num == 2:
            r, g, b = color2
        elif num == 3:
            r, g, b = color3
        elif num == 4:
            r, g, b = color4
        elif num == 5:
            r, g, b = color5
        elif num == 6:
            r, g, b = color6

    elif 0.5 >= l >= 0:
        num = random.randint(1, 6)
        if num == 1:
            r, g, b = color1a
        elif num == 2:
            r, g, b = color2a
        elif num == 3:
            r, g, b = color3a
        elif num == 4:
            r, g, b = color4a
        elif num == 5:
            r, g, b = color5a
        elif num == 6:
            r, g, b = color6a

    else:
        r, g, b = color7

    b *= l
    g *= l
    r *= l

    if l > 0:
        return r, g, b
    else:
        return 0, 0, 0





def NightVision(renderer, **kwargs):
    night = 110 / 255, 1, 65 / 255
    u, v, w = kwargs['baryCoords']
    tA, tB, tC = kwargs['texCoords']
    b, g, r = kwargs['color']
    A, B, C = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    if renderer.active_texture:
        tx = tA[0] * u + tB[0] * v + tC[0] * w
        ty = tA[1] * u + tB[1] * v + tC[1] * w
        texColor = renderer.active_texture.getColor(tx, ty)
    else:
        texColor = color(1, 1, 1)

    b *= texColor[0] / 255
    g *= texColor[1] / 255
    r *= texColor[2] / 255

    X = A[0] * u + B[0] * v + C[0] * w
    Y = A[1] * u + B[1] * v + C[1] * w
    Z = A[2] * u + B[2] * v + C[2] * w

    n = (X, Y, Z)

    l = mate.pPunto(n, renderer.directional_light)

    r = (night[0] + r) / 2
    g = (night[1] + g) / 2
    b = (night[2] + b) / 2

    if l > 0:
        return r, g, b
    else:
        return 93 / 255, 95 / 255, 0

def Guate(renderer, **kwargs):

    color1 = 0,163/255,224/255
    color2 = 1,1,1
    color3 = 0,163/255,224/255

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    A, B, C = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    X = A[0] * u + B[0] * v + C[0] * w
    Y = A[1] * u + B[1] * v + C[1] * w
    Z = A[2] * u + B[2] * v + C[2] * w

    n = (X, Y, Z)

    l = mate.pPunto(n, renderer.directional_light)



    if l > 0.80:
        r, g, b = color1
    elif l > 0.60:
        r, g, b = color2
    elif l > 0.40:
        r, g, b = color3
    elif l > 0.20:
        r, g, b = color1
    elif l > 0.10:
        r, g, b = color2
    else:
        r, g, b = color2

    b *= l
    g *= l
    r *= l

    if l > 0:
        return r, g, b
    else:
        return 0, 0, 0


def Shell(renderer, **kwargs):

    color1 = 255/255,102/255,255/255
    color2 = 192/255,192/255,192/255

    u, v, w = kwargs['baryCoords']
    b, g, r = kwargs['color']
    A, B, C = kwargs['normals']

    b /= 255
    g /= 255
    r /= 255

    X = A[0] * u + B[0] * v + C[0] * w
    Y = A[1] * u + B[1] * v + C[1] * w
    Z = A[2] * u + B[2] * v + C[2] * w

    n = (X, Y, Z)

    l = mate.pPunto(n, renderer.directional_light)



    if l > 0.80:
        r, g, b = color1
    elif l > 0.60:
        r, g, b = color2
    elif l > 0.40:
        r, g, b = color1
    elif l > 0.20:
        r, g, b = color2
    elif l > 0.10:
        r, g, b = color1
    else:
        r, g, b = color2

    b *= l
    g *= l
    r *= l

    if l > 0:
        return r, g, b
    else:
        return 0, 0, 0