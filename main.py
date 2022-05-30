import pygame
from minesweeper import Minesweeper



from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window



CELL_SIZE = 20


WIDTH = CELL_SIZE
HEIGHT = CELL_SIZE
MARGIN = 5
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
WHITE = (255, 255, 255)


board_size = 10
bomb_number = 10
game_is_end = False
game_result = ""
window_size = [CELL_SIZE*board_size + (board_size+1)*MARGIN, CELL_SIZE*board_size + (board_size+1)*MARGIN]

pygame.init()
clock = pygame.time.Clock()
scr = pygame.display.set_mode(window_size)

pygame.display.set_caption("Grid")


picture_flag = pygame.image.load("images/flag.jpg")
picture_flag = pygame.transform.scale(picture_flag, (CELL_SIZE, CELL_SIZE))

picture_bomb = pygame.image.load("images/bomb.jpeg")
picture_bomb = pygame.transform.scale(picture_bomb, (CELL_SIZE, CELL_SIZE))

picture_1 = pygame.image.load("images/1.jpg")
picture_1 = pygame.transform.scale(picture_1, (CELL_SIZE, CELL_SIZE))

picture_2 = pygame.image.load("images/2.jpg")
picture_2 = pygame.transform.scale(picture_2, (CELL_SIZE, CELL_SIZE))

picture_3 = pygame.image.load("images/3.jpg")
picture_3 = pygame.transform.scale(picture_3, (CELL_SIZE, CELL_SIZE))

picture_4 = pygame.image.load("images/4.jpg")
picture_4 = pygame.transform.scale(picture_4, (CELL_SIZE, CELL_SIZE))

picture_5 = pygame.image.load("images/5.jpg")
picture_5 = pygame.transform.scale(picture_5, (CELL_SIZE, CELL_SIZE))

picture_6 = pygame.image.load("images/6.jpg")
picture_6 = pygame.transform.scale(picture_6, (CELL_SIZE, CELL_SIZE))

picture_7 = pygame.image.load("images/7.jpg")
picture_7 = pygame.transform.scale(picture_7, (CELL_SIZE, CELL_SIZE))

picture_8 = pygame.image.load("images/8.jpg")
picture_8 = pygame.transform.scale(picture_8, (CELL_SIZE, CELL_SIZE))

number_pictures = {
    1: picture_1,
    2: picture_2,
    3: picture_3,
    4: picture_4,
    5: picture_5,
    6: picture_6,
    7: picture_7,
    8: picture_8
}

while True:
    minesweeper = Minesweeper(board_size=board_size, bombs_number=bomb_number)
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
                        minesweeper.board[row][column] = "A"
                    elif minesweeper.board[row][column] == "A":
                        minesweeper.board[row][column] = "flag"

                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if minesweeper.board[row][column] != "flag":
                        if [row, column] in minesweeper.bombs:
                            game_is_end = True
                            game_result = "LOSE"
                            for bomb in minesweeper.bombs:
                                minesweeper.board[bomb[0]][bomb[1]] = "bomb"
                        elif minesweeper.scores[row][column] != 0:
                            minesweeper.board[row][column] = minesweeper.scores[row][column]
                        elif minesweeper.scores[row][column] == 0 and minesweeper.board[row][column] != 0:
                            data = minesweeper.check_to_show([row, column])
                            for cell in data:
                                minesweeper.board[cell[0]][cell[1]] = minesweeper.scores[cell[0]][cell[1]]

        scr.fill(BLACK)
        for row in range(minesweeper.board_size):
            for column in range(minesweeper.board_size):
                if minesweeper.board[row][column] == "flag":
                    scr.blit(picture_flag, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
                elif minesweeper.board[row][column] == "bomb":
                    scr.blit(picture_bomb, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))
                elif minesweeper.board[row][column] == 0:
                    pygame.draw.rect(scr, WHITE, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                elif minesweeper.board[row][column] == "A":
                    pygame.draw.rect(scr, GREY,
                                     [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                else:
                    value = minesweeper.board[row][column]
                    scr.blit(number_pictures[value], ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN))

        win_list = []
        win = True
        for row in range(minesweeper.board_size):
            for column in range(minesweeper.board_size):
                if minesweeper.board[row][column] == "A" or minesweeper.board[row][column] == "flag":
                    win_list.append([row, column])
        for bomb in minesweeper.bombs:
            if bomb not in win_list:
                win = False
                break

        if len(win_list) == len(minesweeper.bombs) and win:
            game_result = "WIN"
            game_is_end = True

        clock.tick(60)
        pygame.display.flip()

    user_choice = ""
    if game_result == "WIN":
        user_choice = messagebox.askyesno("You win!", "Would you like to play again?")
    elif game_result == "LOSE":
        user_choice = messagebox.askyesno("Game over!", "Would you like to play again?")

    if user_choice:
        game_is_end = False
        game_result = ""
    else:
        game_is_end = False
        pygame.quit()
        break
