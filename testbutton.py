import random
import time  # these are importing everything I will need for my program.
import pygame

pygame.init()  # Initiates pygame so it runs.
display_width = 1600  # This sets the boundries of the pygame screen
display_height = 800
gamedisplay = pygame.display.set_mode((display_width, display_height))
white = (255, 255, 255)
black = (000, 000, 000)
grey = (169, 169, 169)
clock = pygame.time.Clock()
buttonheight = 100
buttonwidth = 250


class Button:
    x = 0


y = 0
height = 100
width = 250

body = None
text = "Maths"


def __init__(self):
    self.body = pygame.Rect(self.x, self.y, self.width, self.height)


def setText(self, textOfButton):
    self.text = textOfButton


def clicked(self):
    print("test")


def checkClicked(self):
    click = pygame.mouse.get_pressed()


x, y = 0, 1
click = 0
if pygame.mouse.get_pos()[x] > self.x and pygame.mouse.get_pos()[x] < self.x + self.width:
    if pygame.mouse.get_pos()[y] > self.y and pygame.mouse.get_pos()[y] < self.y + self.height:
        self.clicked()


def draw(self):
    smallText = pygame.font.Font('RINGM___.ttf', 20, )


TextSurf, TextRect = text_objectsW(self.text, smallText)
TextRect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))

pygame.draw.rect(gamedisplay, black, self.body)
gamedisplay.blit(TextSurf, TextRect)


# gamedisplay.blit(smallText.render(self.text, False, white), TextRect)


class mathsButton(Button):
    def __init__(self):

        self.x = 95


self.y = 400
self.text = "Maths"
super().__init__()


class historyButton(Button):
    def __init__(self):

        self.x = 690


self.y = 400
self.text = "History"
super().__init__()


class englishButton(Button):
    def __init__(self):

        self.x = 1255


self.y = 400
self.text = "English"
super().__init__()


def text_objectsB(text,
                  font):  # These 2 functions are the same with the colour of the text being the exception. its renders the text and its colour
    textSurface = font.render(text, True, black)


return textSurface, textSurface.get_rect()


def text_objectsW(text, font):
    textSurface = font.render(text, True, white)


return textSurface, textSurface.get_rect()

my_image = pygame.image.load('Background2.jpg').convert()
gamedisplay.blit(my_image, [0, 0])
intro = True
btnMaths = mathsButton()
btnHistory = historyButton()
btnEnglish = englishButton()


def main_menu():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        pygame.quit()


quit()
elif event.type == pygame.MOUSEBUTTONDOWN:
btnMaths.checkClicked()
btnHistory.checkClicked()
btnEnglish.checkClicked()
largetext = pygame.font.Font('RINGM___.ttf', 80)
TextSurf, TextRect = text_objectsB("Are you smarter than a 13 year old?", largetext)
TextRect.center = ((display_width / 2), (display_height / 6))
gamedisplay.blit(TextSurf, TextRect)
# button("Maths Quiz",95,400,black,grey,"Maths")
# button("English Quiz",675,400,black,grey,"English")
# button("History Quiz",1255,400,black,grey,"History")
btnMaths.draw()
btnHistory.draw()
btnEnglish.draw()
pygame.display.update()
clock.tick(60)