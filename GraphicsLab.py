import pygame
from pygame.locals import *

import sys
import time
from pygame import gfxdraw
pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
pygame.display.flip()
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
def ROUND(n):
    return int(n+0.5)

'''    if 0 < m < 1 and dx > 0 and dy > 0:
        d = 2 * dy - dx

        for x in range(x1, x2):
            x += 1
            if d < 0:
                d = d + 2 * dy
            else:
                y += 1
                d = d + 2 * (dy - dx)

            gfxdraw.pixel(screen, x, y, blue)
    if 0 < m <1 and dx <0 and dy <0:
        dx = abs(dx)
        dy = abs(dy)
        s1=-1
        s2=-1
        d = 2 * dy - dx

        for x in range(x1, x2):
            x -= 1
            if d < 0:
                d = d + 2 * dy
            else:
                y -= 1
                d = d + 2 * (dy - dx)

            gfxdraw.pixel(screen, x, y, blue)

    elif -1 < m < 0 and dx < 0 and dy > 0:
        d = 2 * dy - dx

        for x in range(x1, x2):
            x -= 1
            if d < 0:
                d = d + 2 * dy
            else:
                y += 1
                d = d + 2 * (dy - dx)
            gfxdraw.pixel(screen, x, y, red)

    elif -1 < m < 0 and dy < 0 and dx > 0:
        d = 2 * abs(dy) - dx

        for x in range(x1, x2):
            x += 1
            if d < 0:
                d = d + 2 * abs(dy)
            else:
                y -= 1
                d = d + 2 * (abs(dy) - dx)

            gfxdraw.pixel(screen, x, y, red)


'''

def bresenham(x1, y1, x2, y2):

    x = x1
    y = y1

    if x2 == x1:
        x2 += 1
    if y2 ==y1:
        y2 += 1
    dy = abs(y2-y1)
    dx = abs(x2-x1)
    sx = (x2-x1)/dx
    sy = (y2-y1)/dy
    sx = int(sx)
    sx = int(sx)
    m = dy/dx

    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        change = 1
    else:
        change = 0
    d = 2*dy - dx
    ds = 2*dy
    dt = 2*(dy-dx)

    gfxdraw.pixel(screen, x, y, blue)

    for i in range(1, dx):
        if d < 0:
            if change == 1:
                d = d + ds
                y = y + sy
            else:
                x = x + sx
                d = d + ds

        else:
            y = y + sy
            x = x + sx
            d = d + dt
        x = int(x)
        y = int(y)

        gfxdraw.pixel(screen, x, y, blue)



def dda(x1, y1, x2, y2):
    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
        temp2 = y1
        y1 = y2
        y2 = temp2

    x, y = x1, y1
    if x2 == x1:
        x2 += 1
    m=(y2-y1)/(x2-x1)
    if m == 0:
        m += 1
    length = (x2 - x1) if (x2 - x1) > (y2 - y1) else (y2 - y1)
    dx = (x2 - x1) / float(length)
    dy = (y2 - y1) / float(length)

    gfxdraw.pixel(screen, ROUND(x), ROUND(y), green)

    for i in range(length):
        x += dy/m
        y += dx*m
        gfxdraw.pixel(screen, ROUND(x), ROUND(y), green)
    pygame.display.flip()


def name():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    name = ""
    font = pygame.font.Font(None, 10)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name = ""
            elif evt.type == QUIT:
                return
        screen.fill((255, 255, 255))
        block = font.render(name, True, (255, 0, 0))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()


def directLine(x1,y1,x2,y2):
    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
        temp2 = y1
        y1 = y2
        y2 = temp2
    #x,y = x1,y1
    x=x1
    y=y1
    if x2==x1:
        x2=x2+1
    m=float((y2-y1)/(x2-x1))
    b=float(y1-m*x1)
    gfxdraw.pixel(screen, x, y, red)
    if(m<=1):
        for x in range(x1,x2):
            y=m*x+b
            gfxdraw.pixel(screen,ROUND(x),ROUND(y),red)
    else:
        for y in range(y1,y2):
            x=(y-b)/m
            gfxdraw.pixel(screen, ROUND(x),y, red)
    pygame.display.flip()


#gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Scan-Converting Line ')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
A=[200,200]
c=0
mx,my=1,1
while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEMOTION:

            mx, my = pygame.mouse.get_pos()

            mx_str = 'pixel value = ( '+str(mx)+" , "+str(my)+" )"
            pygame.display.set_caption(mx_str)

            #directLine(A[0], A[1],mx, my)
            screen.fill((255, 255, 255))
            #dda(A[0], A[1], mx, my)
            bresenham(A[0],A[1],mx,my)
            mx_str = 'Line for Pixel  = ( ' + str(A[0]) + " , " + str(A[1]) + " ) and ("+str(mx)+" , "+str(my)+" )"
            pygame.display.get_caption()
            pygame.display.set_caption(mx_str)
            pygame.display.get_caption()
        if e.type == pygame.MOUSEBUTTONDOWN:
                A[0]=mx
                A[1]=my

    time.sleep(0.03)
    pygame.display.update()


def mousebuttondown():
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(pos):
            button.call_back()


button_01 = Button("Direct Line", (60, 30), directLine())
button_03= Button("Bresenham", (60, 70), my_fantastic_function, bg=(255, 0, 20))
button_02 = Button("DDA", (60, 110), DDA, bg=(50, 200, 20))
buttons = [button_01, button_02, button_03]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown()

    for button in buttons:
        button.draw()

    pygame.display.flip()
    pygame.time.wait(40)