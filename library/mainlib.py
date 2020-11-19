# Imports
import pygame
import logging

# Log
log = logging.getLogger("Main Lib")

def drawWorld(data, x, y, bound, size):
    for i in range(len(data)):
        for j in range(len(data)):
            if x == i and y == j:
                pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), (bound+x*size, bound+y*size))
            elif data[i][j] == 1:
                pygame.draw.rect(pygame.display.get_surface(), (96, 96, 96), (bound+x*size, bound+y*size))