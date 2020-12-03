# Imports
import pygame
import logging

# Log
log = logging.getLogger("Main Lib")

def drawWorld(data, x, y, bound, size, images):
    for i in range(len(data)):
        for j in range(len(data)):
            if x == i and y == j:
                log.debug(f"Draw Player at Location {x} and {y}")
                # pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), (bound+x*size, bound+y*size, size, size))
                pygame.display.get_surface().blit(images[0], (bound+x*size, bound+y*size))
            elif data[i][j] >= 1:
                log.debug(f"Draw Obstacle at Location {i} and {j}")
                # pygame.draw.rect(pygame.display.get_surface(), (96, 96, 96), (bound+i*size, bound+j*size, size, size))
                pygame.display.get_surface().blit(images[1], (bound+i*size, bound+j*size))


def playerMovement(event, vel):
    if event.type == pygame.KEYDOWN:
        # Key Down for Momvement
        log.debug(f"Key Down Detected: {event.key}")
        if event.key == pygame.K_a:
            vel[0] = -1
        if event.key == pygame.K_d:
            vel[0] = 1
        if event.key == pygame.K_w:
            vel[1] = -1
        if event.key == pygame.K_s:
            vel[1] = 1

    log.debug(f"Player Movement Velocity: {vel}")

    return vel


def playerPosCheck(x, y, bound):
    log.debug(f"Checking Player position")
    if x >= bound-1:
        x = bound-1
        log.debug(f"Player on boundary! Setting position")
    elif x <= 0:
        x = 0
        log.debug(f"Player on boundary! Setting position")
    if y >= bound-1:
        y = bound-1
        log.debug(f"Player on boundary! Setting position")
    elif y <= 0:
        y = 0
        log.debug(f"Player on boundary! Setting position")

    return x, y


def playerObstacle(x, y, vel, data):
    try:
        if data[x+vel[0]][y+vel[1]] >= 1:
            return [0, 0]
        else:
            return vel
    except Exception:
        return [0, 0]


def worldgen(data, boxCount, obstacleCount):
    import random
    types = [1, 2, 3, 4, 5]
    for _ in range(obstacleCount):
        p = random.randint(0, boxCount-1)
        q = random.randint(0, boxCount-1)
        while data[p][q]!=0:
            p = random.randint(0, boxCount-1)
            q = random.randint(0, boxCount-1)
        data[p][q] = types[random.randint(0, len(types)-1)]
    return data
