# Imports
import pygame
import logging

# Log
log = logging.getLogger("Main Lib")

def drawWorld(data, x, y, bound, size):
    for i in range(len(data)):
        for j in range(len(data)):
            if x == i and y == j:
                log.debug(f"Draw Player at Location {x} and {y}")
                pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), (bound+x*size, bound+y*size))
            elif data[i][j] == 1:
                log.debug(f"Draw Obstacle at Location {i} and {j}")
                pygame.draw.rect(pygame.display.get_surface(), (96, 96, 96), (bound+x*size, bound+y*size))