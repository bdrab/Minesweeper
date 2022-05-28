import time

import pygame
from minesweeper_board import Minesweeper

WIDTH = 20
HEIGHT = 20
MARGIN = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

window_size = [255, 255]


pygame.init()
clock = pygame.time.Clock()
scr = pygame.display.set_mode(window_size)

pygame.display.set_caption("Grid")



picture_flag = pygame.image.load("flag.jpg")
picture_flag = pygame.transform.scale(picture_flag, (20, 20))
scr.blit(picture_flag, (0, 0))

picture_bomb = pygame.image.load("bomb.jpeg")
picture_bomb = pygame.transform.scale(picture_bomb, (20, 20))
scr.blit(picture_bomb, (0, 0))

minesweeper = Minesweeper()
print(*minesweeper.scores, sep="\n")

game_is_end = False



while not game_is_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                minesweeper.flags[row][column] = not minesweeper.flags[row][column]
                print("Click ", pos, "Grid coordinates: ", row, column)
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if [row, column] in minesweeper.bombs:
                    print("Game over!")


    scr.fill(BLACK)



    for row in range(10):
        for column in range(10):
            if minesweeper.board[row][column]:
                scr.blit(picture_bomb, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
            elif minesweeper.flags[row][column]:
                scr.blit(picture_flag, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
            else:
                pygame.draw.rect(scr,
                                 WHITE,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
