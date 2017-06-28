import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((640,400))

continuer = 1
while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = 0
