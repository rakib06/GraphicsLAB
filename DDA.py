import sys, pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
pygame.display.flip()

white = (255, 0, 0)


def ROUND(n):
    return int(n + 0.5)


def dda(x1, y1, x2, y2):
    x, y = x1, y1
    m=(y2-y1)/(x2-x1)
    length = (x2 - x1) if (x2 - x1) > (y2 - y1) else (y2 - y1)
    dx = (x2 - x1) / float(length)
    dy = (y2 - y1) / float(length)

    gfxdraw.pixel(screen, ROUND(x), ROUND(y), white)

    for i in range(length):
        x += dy/m
        y += dx*m
        gfxdraw.pixel(screen, ROUND(x), ROUND(y), white)
    pygame.display.flip()


input0 = input("Initial point (x1,y1):  ").split(" ")
x1 = int(input0[0])
y1 = int(input0[1])

input1 = input("Finishing point (x2,y2): ").split(" ")
x2: int = int(input1[0])
y2 = int(input1[1])
if x1 > x2:
    temp = x1
    x1 = x2
    x2 = temp
    temp2 = y1
    y1 = y2
    y2 = temp2
dda(x1, y1, x2, y2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
