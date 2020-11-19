import pygame
from random import randint as rand
import time
import sys


x = 4
y = 4

DIM = 700

n = 10
b = 20
s = int(DIM/n)

win = pygame.display.set_mode((DIM+2*b, DIM+2*b))
