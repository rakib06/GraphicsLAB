import sys, pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
pygame.display.flip()

white = (255, 0, 0)


def ROUND(n):
    return int(n + 0.5)


def bresenham(x1, y1, x2, y2):
    _2dy = 2 * (y2 - y1)
    _2dx = 2 * (x2 - x1)
    dy=y2-y1
    dx=x2-x1
    m=(y2-y1)/(x2-x1)
    _p = _2dy - (x2 - x1)
    dT=2*(dy-dx)
    x = x1
    y = y1
    x=x1
    y = y1
    if(m<=1):
        for x in range(x1, x2+1):
            gfxdraw.pixel(screen,x,y, white)
            _p = _p + _2dy
            if _p >= 0:
                y = y + 1
                _p = _p+dT
            else:
                _p=_p+_2dy
        pygame.display.flip()
    else:
        for y in range(y1, y2+1):
            gfxdraw.pixel(screen,x,y, white)
            _p = _p + _2dx
            if _p >= 0:
                x = x + 1
                _p = _p+dT
            else:
                _p=_p+_2dx
        pygame.display.flip()
input1 = input("Initial point (x1,y1):  ").split(" ")
x1 = int(input1[0])
y1 = int(input1[1])

input2 = input("Finishing point (x2,y2): ").split(" ")
x2: int = int(input2[0])
y2 = int(input2[1])
if x1>x2:
    temp = x1
    x1 = x2
    x2 = temp
    temp2=y1
    y1=y2
    y2=temp2
pygame.mouse.get_pos
pygame.mouse.set_visible
#bresenham(x1, y1, x2, y2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

