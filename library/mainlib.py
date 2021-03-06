# Imports
import pygame
import logging

# Log
log = logging.getLogger("Main Lib")

def drawWorld(data, x, y, bound, size, images, rot):
    for i in range(len(data)):
        for j in range(len(data)):
            if x == i and y == j:
                log.debug(f"Draw Player at Location {x} and {y}")
                if rot[0] == 1:
                    pygame.display.get_surface().blit(images[0], (bound+x*size+1, bound+y*size+1))
                elif rot[0] == -1:
                    pygame.display.get_surface().blit(images[2], (bound+x*size+1, bound+y*size+1))
                elif rot[1] == 1:
                    pygame.display.get_surface().blit(images[1], (bound+x*size+1, bound+y*size+1))
                elif rot[1] == -1:
                    pygame.display.get_surface().blit(images[3], (bound+x*size+1, bound+y*size+1))
                else:
                    pygame.display.get_surface().blit(images[0], (bound+x*size+1, bound+y*size+1))
            elif data[i][j] == 1:
                log.debug(f"Draw Obstacle at Location {i} and {j}")
                pygame.display.get_surface().blit(images[4], (bound+i*size+1, bound+j*size+1))
            elif data[i][j] == 2:
                log.debug(f"Draw House at Location {i} and {j}")
                pygame.display.get_surface().blit(images[5], (bound+i*size+1, bound+j*size+1))
            elif data[i][j] == 3:
                log.debug(f"Draw Box at Location {i} and {j}")
                pygame.display.get_surface().blit(images[6], (bound+i*size+1, bound+j*size+1))
            elif data[i][j] == 4:
                log.debug(f"Draw Flag at Location {i} and {j}")
                pygame.display.get_surface().blit(images[7], (bound+i*size+1, bound+j*size+1))


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


def playerObstacle(x, y, vel, data, boxes):
    try:
        if data[x+vel[0]][y+vel[1]] == 3:
            data[x+vel[0]][y+vel[1]] = 0
            boxes += 1
            log.debug(f"Boxes Collected: {boxes}")
            return vel, boxes
        elif data[x+vel[0]][y+vel[1]] == 2 and boxes >= 1:
            data[x+vel[0]][y+vel[1]] = 4
            boxes -= 1
            log.debug(f"Boxes Collected: {boxes}")
            log.debug(f"Goal!")
            return [0, 0], boxes
        elif data[x+vel[0]][y+vel[1]] >= 1:
            return [0, 0]
        else:
            return vel
    except Exception:
        return [0, 0]


def worldgen(data, boxCount, obstacleCount):
    import random
    types = [1, 2, 3,]
    for _ in range(obstacleCount):
        p = random.randint(0, boxCount-1)
        q = random.randint(0, boxCount-1)

        while data[p][q]!=0:
            p = random.randint(0, boxCount-1)
            q = random.randint(0, boxCount-1)
        objectType = types[random.randint(0, len(types)-1)]
        data[p][q] = objectType
        if objectType == 2:
            while data[p][q]!=0:
                p = random.randint(0, boxCount-1)
                q = random.randint(0, boxCount-1)
            data[p][q] = 3
        elif objectType == 3:
            while data[p][q]!=0:
                p = random.randint(0, boxCount-1)
                q = random.randint(0, boxCount-1)
            data[p][q] = 2
    return data
