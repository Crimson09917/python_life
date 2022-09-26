import pygame
from pygame.locals import *
from sys import exit

from board import Board
from board import Cell

drag = False
windowWidth = 1600
windowHeight = 800
timer = 0
stop = True

window = pygame.display.set_mode((windowWidth, windowHeight))

board = Board()

mainLoop = True
while mainLoop:
    pygame.time.delay(1)
    timer += 1
    window.fill((0, 0, 0))
    board.draw(window)

    if not stop and timer % 10 == 0:
        board.iterate()

    keys = pygame.key.get_pressed()
    clicks = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                mainLoop = False
            if event.key == K_SPACE:
                stop = not stop
            # if event.key == K_EQUALS:
            #     board.changeDimension(window, "UP")
            # if event.key == K_MINUS:
            #     board.changeDimension(window, "DOWN")

        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
            button = event.button

        if event.type == pygame.MOUSEBUTTONUP:
            drag = False

        if drag:
            board.click(button, pygame.mouse.get_pos())

    pygame.display.flip()
print(board.iterate())
pygame.quit()
exit()
