import pygame, sys, math
from pygame.locals import *

GAMEWORLD = ((
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0),
             (
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1))

WINDOWX = 600  # width of game window
WINDOWY = 600  # height of game window
FRAMEX = 60  # number of displayed cells in x-axis
FRAMEY = len(GAMEWORLD)  # number of displayed cells in y-axis
CELLX = math.ceil(WINDOWX // FRAMEX)  # width of a cell
CELLY = math.ceil(WINDOWY // FRAMEY)  # height of a cell
BALLRADIUS = CELLY / 2
GLIDERWIDTH = CELLX * 5
GLIDERHEIGHT = 5

FRAMERATE = 60
ALLRESTRICTEDX = []
ALLRESTRICTEDY = []
GLIDEDONX = []
GLIDEDONY = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BALLCOLOR = GREEN
BACKGROUND = BLACK

# navigation
xVELOCITY = 2
STATIC = WINDOWX / 2
MAXDISPLACEMENT = len(GAMEWORLD[0]) - FRAMEX
GRAVITY = 1  # acceleration due to gravity
RIGHT = 'right'
LEFT = 'left'
BOTH = 'both'


def main():
    pygame.init()

    # Fundamentals
    global GAMEWINDOW, FPSCLOCK
    FPSCLOCK = pygame.time.Clock()
    GAMEWINDOW = pygame.display.set_mode((WINDOWX, WINDOWY))
    pygame.display.set_caption('Basic Platformer')

    # Movement variables
    global ballx, bally, screenDisplacement, angularDisplacement  # coordinates of centre of ball
    global glideAmplitude, isGliding
    ballx = BALLRADIUS
    bally = BALLRADIUS
    moveRight = False
    moveLeft = False
    isGliding = False
    screenDisplacement = 0
    angularDisplacement = [0, 180]
    glideAmplitude = CELLX * 5

    # Gravity and jump variables
    global time, landed, ydisplacement, isJumping
    isJumping = False
    landed = False
    time = 0
    ydisplacement = 0

    for x in range(MAXDISPLACEMENT + 1):
        getRestricted(x)

    # Start Animation
    while not landed:
        gravity()
        drawWorld()
        drawBall(ballx, bally)
        FPSCLOCK.tick(FRAMERATE)
        pygame.display.update()

    # Game Loop
    while True:
        pygame.display.set_caption('Basic Platformer')
        # movement
        adjustX(BOTH)
        gravity()
        if moveRight:
            movex(RIGHT)
        if moveLeft:
            movex(LEFT)
        if isJumping:
            jump()
        if isGliding:
            glide(glideType)
            #isGliding = False


        # event handlers
        for event in pygame.event.get():

            # Quit Event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # x Movement
            if event.type == KEYDOWN and event.key == K_RIGHT:
                moveRight = True
            if event.type == KEYUP and event.key == K_RIGHT:
                moveRight = False
            if event.type == KEYDOWN and event.key == K_LEFT:
                moveLeft = True
            if event.type == KEYUP and event.key == K_LEFT:
                moveLeft = False
            if event.type == KEYDOWN and event.key == K_UP:
                isJumping = True

        # move glider
        for i in range(len(angularDisplacement)):
            angularDisplacement[i] = (angularDisplacement[i] + 0.05) % 360

        # update Screen
        drawWorld()
        drawBall(ballx, bally)
        FPSCLOCK.tick(FRAMERATE)
        pygame.display.update()


def drawWorld():
    GLIDEDONX.clear()
    GAMEWINDOW.fill(BACKGROUND)
    for x in range(FRAMEX):
        for y in range(FRAMEY):
            if GAMEWORLD[y][x + screenDisplacement] == 1:
                drawCell(x, y)
            elif GAMEWORLD[y][x + screenDisplacement] == 2:
                drawGlider(x, y, angularDisplacement[0], 2)
            elif GAMEWORLD[y][x + screenDisplacement] == 3:
                drawGlider(x, y, angularDisplacement[1], 3)

def drawGlider(x, y, angle, glidetype):
    global isGliding, ballx, glideType
    left, top = getLeftTop(x, y)
    displacement = math.sin(angle)
    displacement = displacement * glideAmplitude
    left = left + displacement

    for X in range(int(left), int(left) + GLIDERWIDTH + 1):
        section = []
        for Y in range(top, top + GLIDERHEIGHT + 1):
            section.append([X, Y, glidetype])
        GLIDEDONX.append(section)

    for Y in range(top, top + GLIDERHEIGHT + 1):
        section = []
        for X in range(int(left), int(left) + GLIDERWIDTH + 1):
            section.append([X, Y])
            GLIDEDONY.append(section)
    pygame.draw.rect(GAMEWINDOW, WHITE, (left, top, GLIDERWIDTH, GLIDERHEIGHT))

def glide(glidetype):
    global ballx, isGliding
    if glidetype == 2:
        ballDisplacement = (math.sin(angularDisplacement[0]) - math.sin(angularDisplacement[0] - 0.05)) * glideAmplitude
        ballx = ballx + ballDisplacement
    elif glidetype == 3:
        ballDisplacement = (math.sin(angularDisplacement[1]) - math.sin(angularDisplacement[1] - 0.05)) * glideAmplitude
        ballx = ballx + ballDisplacement
    isGliding = False


def drawCell(x, y):
    left, top = getLeftTop(x, y)
    pygame.draw.rect(GAMEWINDOW, WHITE, (left, top, CELLX, CELLY))


def getRestricted(Displacement):
    global RESTRICTEDX
    global RESTRICTEDY
    RESTRICTEDX = []
    RESTRICTEDY = []
    tempRESTRICTEDX = []
    tempRESTRICTEDY = []

    # Get the left, top coordinate of every restricted cell
    for x in range(FRAMEX):
        for y in range(FRAMEY):
            if GAMEWORLD[y][x + Displacement] == 1:
                left, top = getLeftTop(x, y)

                # Get all coordinate pairs occupied by every cell and add them to a temporary list
                for X in range(left, left + CELLX + 1):
                    section = []
                    for Y in range(top, top + CELLY + 1):
                        section.append([X, Y])
                    tempRESTRICTEDX.append(section)

                for Y in range(top, top + CELLY + 1):
                    section = []
                    for X in range(left, left + CELLX + 1):
                        section.append([X, Y])
                    tempRESTRICTEDY.append(section)

    # Group all coordinate pairs with similar x  values
    groupRestricted(WINDOWX, 0, tempRESTRICTEDX)

    # Group all coordinate pairs with similar x  values
    groupRestricted(WINDOWY, 1, tempRESTRICTEDY)


    splitGroups(RESTRICTEDX, 1)
    splitGroups(RESTRICTEDY, 0)


def groupRestricted(numOfGroups, pos, tempRESTRICTED):

    global RESTRICTEDX
    global RESTRICTEDY
    for i in range(numOfGroups + 1):
        section = []
        for X in tempRESTRICTED:
            if X[0][pos] == i:
                section += X
        if len(section) == 0:
            continue
        if pos == 0:
            RESTRICTEDX.append(section)
        elif pos == 1:
            RESTRICTEDY.append(section)


def splitGroups(RESTRICTED, pos):
    # for every group, split group if there is occurrence of two adjacent y coords with difference greater than 1.
    # e.g (not exact implementation as in code) [1,2,7,8,10] = [1,2], [7,8], [10]
    global ALLRESTRICTEDX, ALLRESTRICTEDY
    for X in RESTRICTED:
        altered = False
        start = 0
        initial = X[0][pos]
        for Y in X:
            if Y[pos] - initial > 1:
                altered = True
                column = X[start:X.index(Y)]
                RESTRICTED.insert(RESTRICTED.index(X), column)
                start = X.index(Y)
            initial = Y[pos]
        if altered:
            column = X[start:]
            RESTRICTED.insert(RESTRICTED.index(X), column)
            RESTRICTED.remove(X)
    if pos == 0:
        ALLRESTRICTEDY.append(RESTRICTED)
    elif pos == 1:
        ALLRESTRICTEDX.append(RESTRICTED)


def drawBall(x, y):
    pygame.draw.circle(GAMEWINDOW, BALLCOLOR, (x, y), BALLRADIUS)


def getLeftTop(x, y):
    left = x * CELLX
    top = y * CELLY
    return left, top


def gravity():
    global bally
    global time
    global landed
    global isJumping
    global glideType, isGliding

    if not isJumping:

        initialDisplacement = -GRAVITY * (
                time ** 2)  # ydisplacement equals minus acceleration due to gravity multiplied time squared
        time += 0.3
        finalDisplacement = -GRAVITY * (
                time ** 2)  # ydisplacement equals minus acceleration due to gravity multiplied time squared
        ydisplacement = finalDisplacement - initialDisplacement

        initialBottomCoord = bally + BALLRADIUS
        bally = bally - ydisplacement
        bottomCoord = bally + BALLRADIUS
        for X in ALLRESTRICTEDX[screenDisplacement]:  # check if bottom coordinates of ball is in a restricted area
            if int(ballx) == X[0][0] and initialBottomCoord <= X[0][1] <= bottomCoord:
                landed = True
                time = 0  # reset time to 0
                bottomCoord = X[0][
                    1]  # adjust bottom coordinates to surface of restricted zone
                bally = bottomCoord - BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate
        for X in GLIDEDONX:  # check if bottom coordinates of ball is in a restricted area
            if int(ballx) == X[0][0] and initialBottomCoord <= X[0][1] <= bottomCoord:
                landed = True
                isGliding = True
                glideType = X[0][2]
                time = 0  # reset time to 0
                bottomCoord = X[0][
                    1]  # adjust bottom coordinates to surface of restricted zone
                bally = bottomCoord - BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate

def movex(direction):
    global ballx, screenDisplacement
    leftx = ballx - BALLRADIUS
    rightx = ballx + BALLRADIUS

    if direction == 'right':
        if ballx > STATIC and screenDisplacement != MAXDISPLACEMENT:
            screenDisplacement += 1
        elif rightx < WINDOWX:
            ballx += xVELOCITY
        adjustX(RIGHT)



    elif direction == 'left':
        if ballx < STATIC and screenDisplacement != 0:
            screenDisplacement -= 1
        elif leftx > 0:
            ballx -= xVELOCITY
        adjustX(LEFT)


def adjustX(direction):
    global ballx, isJumping, time
    leftx = ballx - BALLRADIUS
    rightx = ballx + BALLRADIUS
    if direction == 'right' or direction == 'both':
        for X in ALLRESTRICTEDY[screenDisplacement]:
            if [math.ceil(rightx), int(bally)] in X:
                rightx = X[0][0]
                ballx = rightx - BALLRADIUS
                isJumping = False
                time = 0
            if rightx > WINDOWX:
                ballx = WINDOWX - BALLRADIUS
                isJumping = False
                time = 0


    if direction == 'left' or direction == 'both':
        for X in ALLRESTRICTEDY[screenDisplacement]:
            if [math.floor(leftx), int(bally)] in X:
                leftx = X[len(X) - 1][0]
                ballx = leftx + BALLRADIUS
                isJumping = False
                time = 0
            if leftx < 0:
                ballx = 0 + BALLRADIUS
                isJumping = False
                time = 0


def jump():
    global time, bally, isJumping, isGliding, glideType
    initialDisplacement = -GRAVITY*(time ** 2) + 20 * time
    time += 0.3
    finalDisplacement = -GRAVITY*(time ** 2) + 20 * time
    ydisplacement = finalDisplacement - initialDisplacement
    isAscending = ydisplacement >= 0
    isDescending = ydisplacement <= 0

    initialTopCoord = bally - BALLRADIUS
    initialBottomCoord = bally + BALLRADIUS

    bally = bally - ydisplacement

    topCoord = bally - BALLRADIUS
    bottomCoord = bally + BALLRADIUS

    if isAscending:  # if ball is moving upwards
        for X in ALLRESTRICTEDX[screenDisplacement]:
            if int(ballx) == X[0][0] and initialTopCoord >= X[len(X) - 1][1] >= topCoord:
                time = 0  # reset time
                topCoord = X[len(X) - 1][1]
                bally = topCoord + BALLRADIUS
                isJumping = False
        for X in GLIDEDONX:  # check if bottom coordinates of ball is in a restricted area
            if int(ballx) == X[0][0] and initialTopCoord >= X[len(X) - 1][1] >= topCoord:
                isJumping = False
                time = 0  # reset time to 0
                topCoord = X[len(X) - 1][1]
                bally = topCoord + BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate

    if isDescending:  # if ball is moving downwards
        for X in ALLRESTRICTEDX[screenDisplacement]:
            if int(ballx) == X[0][0] and initialBottomCoord <= X[0][1] <= bottomCoord:
                time = 0  # reset time
                bottomCoord = X[0][1]
                bally = bottomCoord - BALLRADIUS
                isJumping = False
        for X in GLIDEDONX:  # check if bottom coordinates of ball is in a restricted area
            if int(ballx) == X[0][0] and initialBottomCoord <= X[0][1] <= bottomCoord:
                isJumping = False
                isGliding = True
                glideType = X[0][2]
                time = 0  # reset time to 0
                bottomCoord = X[0][
                    1]  # adjust bottom coordinates to surface of restricted zone
                bally = bottomCoord - BALLRADIUS  # get corresponding center coordinate from adjusted bottom coordinate


if __name__ == '__main__':
    main()
