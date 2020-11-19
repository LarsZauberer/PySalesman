import pygame
from random import randint as rand
import time
import sys


x = 4
y = 4

DIM = 700

boxCount = 10
windowborder = 20
boxSize = int(DIM/boxCount)

win = pygame.display.set_mode((DIM+2*windowborder, DIM+2*windowborder))

data = [[0]*boxCount for i in range(boxCount)]
data[2][1] = 1 #Testwerte
data[3][7] = 1
data[8][4] = 1

run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

sys.exit()
