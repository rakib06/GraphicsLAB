# Mid-point circle drawing algorithm.
# Requires pygame: http://pygame.org

from pygame import gfxdraw
import sys,pygame
pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
pygame.display.flip()

def circle(radius,offset):
    x,y = 0,radius
    plotCircle(x,y,radius,offset)

def symmetry_points(x,y,offset):
    gfxdraw.pixel(screen,x+offset,y+offset,(255,0,0))
    gfxdraw.pixel(screen,-x+offset,y+offset,(255,0,0))
    gfxdraw.pixel(screen,x+offset,-y+offset,(255,0,0))
    gfxdraw.pixel(screen,-x+offset,-y+offset,(255,0,0))
    gfxdraw.pixel(screen,y+offset,x+offset,(255,0,0))
    gfxdraw.pixel(screen,-y+offset,x+offset,(255,0,0))
    gfxdraw.pixel(screen,y+offset,-x+offset,(255,0,0))
    gfxdraw.pixel(screen,-y+offset,-x+offset,(255,0,0))
    pygame.display.flip()

def plotCircle(x,y,radius,offset):
    d = 3 - 2 * radius
    symmetry_points(x,y,radius+offset)
    while x < y:
        if d < 0:
            d += 4*x + 6
        else:
            d += 4*(x-y) + 10
            y -= 1
        x += 1
        symmetry_points(x,y,radius+offset)


circle(100,100) # circle(radius,<offset from edge>)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()