import time

import pygame
from minesweeper_board import Minesweeper

WIDTH = 20
HEIGHT = 20
MARGIN = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


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
                if minesweeper.board[row][column] == "flag":
                    minesweeper.board[row][column] = 0
                elif minesweeper.board[row][column] == 0:
                    minesweeper.board[row][column] = "flag"

                print("Click ", pos, "Grid coordinates: ", row, column)
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if minesweeper.board[row][column] != "flag":
                    if [row, column] in minesweeper.bombs:
                        print("Game over!")
                        game_is_end = True
                        for bomb in minesweeper.bombs:
                            minesweeper.board[bomb[0]][bomb[1]] = "bomb"
                    elif minesweeper.scores[row][column] != 0:
                        minesweeper.board[row][column] = minesweeper.scores[row][column]
                    elif minesweeper.scores[row][column] == 0:
                        data = minesweeper.check_to_show([row, column])
                        for cell in data:
                            minesweeper.board[cell[0]][cell[1]] = minesweeper.scores[cell[0]][cell[1]]
                        print("zero")

    scr.fill(BLACK)
    numbers = [i for i in range(100)]
    for row in range(10):
        for column in range(10):
            if minesweeper.board[row][column] == "flag":
                scr.blit(picture_flag, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
            elif minesweeper.board[row][column] == "bomb":
                scr.blit(picture_bomb, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
            elif minesweeper.board[row][column] == 0:
                pygame.draw.rect(scr, WHITE, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            else:
                value = minesweeper.board[row][column]
                font = pygame.font.Font(None, 20)
                text = font.render(f"{value}", True, BLACK, WHITE)
                text_rect = text.get_rect(center=((MARGIN + WIDTH) * column + MARGIN + WIDTH/2, (MARGIN + HEIGHT) * row + MARGIN+HEIGHT/2))
                scr.blit(text, text_rect)

    clock.tick(60)
    pygame.display.flip()
# pygame.quit()
