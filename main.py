# Imports
import pygame
from random import randint as rand
import time
import sys
import logging
import argparse


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

x = 4
y = 4

run = True

# Const Variables
DIM = 700

boxCount = 10
windowborder = 20
boxSize = int(DIM/boxCount)

log.debug(f"All Variables set")

# Create the Window
win = pygame.display.set_mode((DIM+2*windowborder, DIM+2*windowborder))
log.debug(f"Creating Pygame Window")

# Create world data
log.debug(f"Calculating World...")
data = [[0]*boxCount for i in range(boxCount)]
data[2][1] = 1 #Testwerte
data[3][7] = 1
data[8][4] = 1
log.debug(f"World calculated!")

# Main Game Loop
log.info(f"Starting Game...")
while run:
    for i in pygame.event.get():
        # Quit Event
        if i.type == pygame.QUIT:
            log.info(f"Event Quit recognized")
            run = False


# End Logging
log.info(f"Shutting down...")
log.info(f"Execution Time: {time.time() - startTime}")

# End Application
log.info(f"Shutting down kernal")
sys.exit()
