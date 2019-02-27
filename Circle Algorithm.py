import pygame
from pygame.locals import *
import math
import sys
import time
from pygame import gfxdraw
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
pygame.display.flip()
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
pygame.display.set_caption('Scan-Converting Circle ')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
A=[168,218]
c=0
mx,my=1,1

def ROUND(n):
    return int(n+0.5)


def midpoint(x1, y1, x2, y2):
    #x1,y1 center
    dx = x2 - x1
    dy = y2 -y1
    r = dx ** 2 + dy ** 2
    r = math.pow(r, .5)
    r = int(r)
    x = 0
    y = r
    p = 1-r
    while x < y:

        if p<0:
            p = p + 2*x +3
        else:
            p = p + 2*(x-y)+5
            y = y-1
        x = x+ 1
        circle_draw(x,y,x1,y1)


def circle_draw(x,y,x1,y1):
    gfxdraw.pixel(screen, +ROUND(x) + x1, +ROUND(y) + y1, blue)
    gfxdraw.pixel(screen, +ROUND(y) + x1, +ROUND(x) + y1, blue)
    gfxdraw.pixel(screen, +ROUND(x) + x1, -ROUND(y) + y1, black)
    gfxdraw.pixel(screen, +ROUND(y) + x1, -ROUND(x) + y1, blue)
    gfxdraw.pixel(screen, -ROUND(x) + x1, -ROUND(y) + y1, blue)
    gfxdraw.pixel(screen, -ROUND(y) + x1, -ROUND(x) + y1, blue)
    gfxdraw.pixel(screen, -ROUND(x) + x1, +ROUND(y) + y1, black)
    gfxdraw.pixel(screen, -ROUND(y) + x1, +ROUND(x) + y1, red)

def bresenham(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1
    r = dx ** 2 + dy ** 2
    r = math.pow(r, .5)
    r = int(r)
    x1 = abs(x1)
    y1 = abs(y1)
    x = 0
    y = r
    d = 3 - 2 * r
    while x < y:

        gfxdraw.pixel(screen, +ROUND(x) + x1, +ROUND(y) + y1, blue)
        gfxdraw.pixel(screen, +ROUND(y) + x1, +ROUND(x) + y1, blue)
        gfxdraw.pixel(screen, +ROUND(x) + x1, -ROUND(y) + y1, black)
        gfxdraw.pixel(screen, +ROUND(y) + x1, -ROUND(x) + y1, blue)
        gfxdraw.pixel(screen, -ROUND(x) + x1, -ROUND(y) + y1, blue)
        gfxdraw.pixel(screen, -ROUND(y) + x1, -ROUND(x) + y1, blue)
        gfxdraw.pixel(screen, -ROUND(x) + x1, +ROUND(y) + y1, black)
        gfxdraw.pixel(screen, -ROUND(y) + x1, +ROUND(x) + y1, red)
        if d < 0:
            d = d+4*x+6
        else:
            d = d + 4*(x-y)+10
            y -= 1
        x += 1

    pygame.display.flip()


def input(x):
    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEMOTION:

                mx, my = pygame.mouse.get_pos()

                mx_str = 'pixel value = ( '+str(mx)+" , "+str(my)+" )"
                pygame.display.set_caption(mx_str)
                screen.fill((255, 255, 255))
                if x == 'midpoint':
                    midpoint(A[0], A[1], mx, my)
                elif x == 'bresenham':
                    bresenham(A[0],A[1],mx,my)
                elif x == 'all':
                    midpoint(A[0], A[1], mx, my)
                    bresenham(A[0], A[1], mx, my)
                dx = mx - A[0]
                dy = my - A[1]
                r = dx ** 2 + dy ** 2
                r = math.pow(r, .5)
                mx_str = 'Circle for Center  = ( ' + str(A[0]) + " , " + str(A[1]) + " ) , radius = "+str(r)+""
                pygame.display.get_caption()
                pygame.display.set_caption(mx_str)
                pygame.display.get_caption()
            if e.type == pygame.MOUSEBUTTONDOWN:
                    A[0] = mx
                    A[1] = my

        time.sleep(0.03)
        pygame.display.update()



#input('midpoint')
input('bresenham')
#input('all')