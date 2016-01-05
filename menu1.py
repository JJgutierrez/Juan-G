#example# Highlight-able menu in Pygame
#
# To run, use:
#     python pygame-menu-mouseover.py
#
# You should see a window with three grey menu options on it.  Place the mouse
# cursor over a menu option and it will become white.

import pygame,sys

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
    


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 700))
menu_font = pygame.font.Font(None, 40)
pygame.mixer.music.load("Electrodoodle.mp3")
pygame.mixer.music.play(-1,0.0)
background = pygame.image.load("background.gif")
pygame.display.set_caption("Game of Lemons")
options = [Option("START", (357, 300)), Option("MULTIPLAYER", (310, 340)),
           Option("CREDITS", (340, 380)), Option("EXIT", (367,420))]
           
           
while True:
    done = False
    pygame.event.pump()
    screen.blit(background,(0,0))
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    pygame.display.update()
    


