import pygame
from minesweeper import Minesweeper
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

CELL_SIZE = 20
WIDTH = CELL_SIZE
HEIGHT = CELL_SIZE
MARGIN = 5
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
BUTTON_HEIGHT = 2 * CELL_SIZE


board_size = 12
bomb_number = 20
time = 0
flag_counter = bomb_number
game_is_end = False
game_result = ""
WIN_WIDTH = CELL_SIZE * board_size + (board_size+1) * MARGIN
WIN_HEIGHT = CELL_SIZE * board_size + (board_size+1) * MARGIN + BUTTON_HEIGHT
window_size = [WIN_WIDTH, WIN_HEIGHT]

pygame.init()
clock = pygame.time.Clock()
scr = pygame.display.set_mode(window_size)
font = pygame.font.Font(None, CELL_SIZE + 5)
pygame.time.set_timer(pygame.USEREVENT, 1000)

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
scr.fill(BLACK)


def bomb_counter():
    bomb_counter_width = (board_size // 2) * CELL_SIZE + (board_size // 2 - 1) * MARGIN
    bomb_counter_rect = pygame.draw.rect(scr, WHITE, [MARGIN, MARGIN, bomb_counter_width, BUTTON_HEIGHT - MARGIN])
    text_bomb_counter = font.render(f"{flag_counter}", True, BLACK)
    text_rect_bomb_counter = text_bomb_counter.get_rect(center=(bomb_counter_rect.centerx, bomb_counter_rect.centery))
    scr.blit(text_bomb_counter, text_rect_bomb_counter)
    pygame.display.flip()


def timer(time_value):

    timer_width = (board_size // 2) * CELL_SIZE + (board_size // 2 - 1) * MARGIN
    timer_rect = pygame.draw.rect(scr, WHITE, [WIN_WIDTH - MARGIN - timer_width, MARGIN, timer_width, BUTTON_HEIGHT - MARGIN])
    text_timer = font.render(f"{time_value}", True, BLACK)
    text_rect_timer = text_timer.get_rect(center=(timer_rect.centerx, timer_rect.centery))
    scr.blit(text_timer, text_rect_timer)
    pygame.display.flip()
    return time_value + 1


mode_not_set = True

while True:
    scr.fill(BLACK)
    while mode_not_set:
        mode1_rect = pygame.draw.rect(scr, WHITE, [MARGIN, MARGIN, WIN_WIDTH - 2 * MARGIN, WIN_HEIGHT/3 - 2 * MARGIN])
        text_mode1_rect = font.render(f"Beginner", True, BLACK)
        text_rect_mode1 = text_mode1_rect.get_rect(center=(mode1_rect.centerx, mode1_rect.centery))
        scr.blit(text_mode1_rect, text_rect_mode1)
        pygame.display.flip()

        mode2_rect = pygame.draw.rect(scr, WHITE, [MARGIN, WIN_HEIGHT/3+ MARGIN, WIN_WIDTH - 2 * MARGIN, WIN_HEIGHT/3 - 2 * MARGIN])
        text_mode2 = font.render(f"Intermediate", True, BLACK)
        text_rect_mode2 = text_mode2.get_rect(center=(mode2_rect.centerx, mode2_rect.centery))
        scr.blit(text_mode2, text_rect_mode2)
        pygame.display.flip()

        mode3_rect = pygame.draw.rect(scr, WHITE, [MARGIN, 2*WIN_HEIGHT/3 +MARGIN, WIN_WIDTH - 2 * MARGIN, WIN_HEIGHT/3 - 2 * MARGIN])
        text_mode3 = font.render(f"Expert", True, BLACK)
        text_rect_mode3 = text_mode3.get_rect(center=(mode3_rect.centerx, mode3_rect.centery))
        scr.blit(text_mode3, text_rect_mode3)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_end = True
                mode_not_set = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()[1]
                    if mode1_rect.bottom > pos > mode1_rect.top:
                        board_size = 9
                        bomb_number = 10
                        mode_not_set = False
                    elif mode2_rect.bottom > pos > mode2_rect.top:
                        board_size = 16
                        bomb_number = 40
                        mode_not_set = False
                    elif mode3_rect.bottom > pos > mode3_rect.top:
                        board_size = 30
                        bomb_number = 80
                        mode_not_set = False

                    WIN_WIDTH = CELL_SIZE * board_size + (board_size + 1) * MARGIN
                    WIN_HEIGHT = CELL_SIZE * board_size + (board_size + 1) * MARGIN + BUTTON_HEIGHT
                    window_size = [WIN_WIDTH, WIN_HEIGHT]
                    scr = pygame.display.set_mode(window_size)
                    time = 0
                    flag_counter = bomb_number

    minesweeper = Minesweeper(board_size=board_size, bombs_number=bomb_number)
    scr.fill(BLACK)
    bomb_counter()
    timer(0)
    while not game_is_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_end = True
            elif event.type == pygame.USEREVENT:
                time = timer(time)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = (pos[1] - BUTTON_HEIGHT) // (HEIGHT + MARGIN)
                    if row >= 0:
                        if minesweeper.board[row][column] == "flag":
                            minesweeper.board[row][column] = "A"
                            flag_counter += 1
                            bomb_counter()
                        elif minesweeper.board[row][column] == "A":
                            flag_counter -= 1
                            minesweeper.board[row][column] = "flag"
                            bomb_counter()

                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (WIDTH + MARGIN)
                    row = (pos[1] - BUTTON_HEIGHT) // (HEIGHT + MARGIN)
                    if row >= 0:
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

        for row in range(minesweeper.board_size):
            for column in range(minesweeper.board_size):
                if minesweeper.board[row][column] == "flag":
                    scr.blit(picture_flag, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN + BUTTON_HEIGHT))
                elif minesweeper.board[row][column] == "bomb":
                    scr.blit(picture_bomb, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN + BUTTON_HEIGHT))
                elif minesweeper.board[row][column] == 0:
                    pygame.draw.rect(scr, WHITE, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN + BUTTON_HEIGHT, WIDTH, HEIGHT])

                elif minesweeper.board[row][column] == "A":
                    pygame.draw.rect(scr, GREY,
                                     [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN + BUTTON_HEIGHT, WIDTH, HEIGHT])

                else:
                    value = minesweeper.board[row][column]
                    scr.blit(number_pictures[value], ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN + BUTTON_HEIGHT))

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
        mode_not_set = True
        time = 0
    else:
        game_is_end = False
        pygame.quit()
        break
