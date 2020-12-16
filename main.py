# Imports
import pygame
from random import randint as rand
import time
import sys
import logging
import argparse

# Imports
from library.mainlib import *


# Saving time to calculate time needed
startTime = time.time()

# Argparser
parser = argparse.ArgumentParser()
parser.version = "1.0"

parser.add_argument("--version", action="version")
parser.add_argument("-v", action="store_true",
                    help="Verbose")

args = vars(parser.parse_args())

# Verbose
log_format = "%(asctime)s [%(name)s][%(levelname)s]: %(message)s"

if args["v"]:
    logging.basicConfig(level=logging.DEBUG, format=log_format,
                        filename="log.log", filemode="w")
else:
    logging.basicConfig(level=logging.INFO, format=log_format,
                        filename="log.log", filemode="w")

log = logging.getLogger()

log.info("Logging Initialized")

# Pygame Initialization
try:
    pygame.init()
    log.info("Pygame Initialized")
except Exception as e:
    log.cirtical("Error while initializing pygame")
    log.critical(f"{e}")

x = 4
y = 4

run = True

# Const Variables
DIM = 700

boxCount = 10
windowborder = 20
boxSize = int(DIM/boxCount)

obstacleCount = 20

rotation = 0

imageURL = [
            "images/right.png",
            "images/down.png",
            "images/left.png",
            "images/up.png",
            "images/boulder.png",
           ]

log.info(f"Loading Images...")
images = [pygame.transform.scale(pygame.image.load(i), (boxSize, boxSize)) for i in imageURL]
log.info(f"Successfully loaded images")

log.debug(f"All Variables set")

# Create the Window
win = pygame.display.set_mode((DIM+2*windowborder, DIM+2*windowborder))
log.debug(f"Creating Pygame Window")

# Create world data
log.debug(f"Calculating World...")
data = [[0]*boxCount for i in range(boxCount)]
data = worldgen(data, boxCount, obstacleCount)
log.debug(f"World calculated!")
log.debug(f"World: {data}")

while data[y][x] != 0:
    x = rand(0, boxCount)
    y = rand(0, boxCount)

vel = [0, 0]

rot = [0, 0]

# ---------------------------------

def redraw():
    global x, y, data, vel, DIM, boxCount, windowborder, boxSize, run, images, rot
    log.debug(f"Window Design...")
    # Background Design
    win.fill((94, 94, 94))
    pygame.draw.rect(win, (255, 255, 255), (windowborder, windowborder, DIM, DIM))
    log.debug(f"Drawing Lines...")
    for i in range(boxCount):
        for _ in range(boxCount):
            pygame.draw.line(win, (90, 90, 90), (i*boxSize+windowborder, windowborder), (i*boxSize+windowborder, DIM+windowborder))
            pygame.draw.line(win, (90, 90, 90), (windowborder, i*boxSize+windowborder), (DIM+windowborder, i*boxSize+windowborder))

    for i in pygame.event.get():
        # Quit Event
        if i.type == pygame.QUIT:
            log.info(f"Event Quit recognized")
            run = False

        vel = playerMovement(i, vel)
        vel = playerObstacle(x, y, vel, data)

    x += vel[0]
    y += vel[1]

    x, y = playerPosCheck(x, y, boxCount)

    if vel != [0, 0]:
        rot = vel

    drawWorld(data, x, y, windowborder, boxSize, images, rot)

    vel = [0, 0]

    pygame.display.update()
    pygame.time.delay(50)


# --------------------------------

# Main Game Loop
log.info(f"Starting Game...")
while run:
    redraw()


# End Logging
log.info(f"Shutting down...")
log.info(f"Execution Time: {time.time() - startTime}")

# End Application
log.info(f"Shutting down kernal")
sys.exit()
