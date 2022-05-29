import random
indexes = [[0, 0], [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


class Minesweeper:
    def __init__(self):
        self.board = []
        self.bombs = []
        self.scores = []
        self.__prepare_board()
        self.set_bombs()

    def __prepare_board(self):
        for row in range(10):
            self.board.append([])
            self.scores.append([])
            for column in range(10):
                self.board[row].append("A")
                self.scores[row].append(0)

    def set_bombs(self):
        while not len(self.bombs) == 10:
            value = random.randint(0, 9)
            value2 = random.randint(0, 9)

            if [value, value2] not in self.bombs:
                self.bombs.append([value, value2])

        for bomb in self.bombs:
            for index in indexes:
                row = bomb[0] + index[0]
                column = bomb[1] + index[1]
                if not (row > 9 or row < 0 or column > 9 or column < 0):
                    if [row, column] not in self.bombs:
                        self.scores[row][column] += 1

    def score_print(self):
        for row in range(10):
            for column in range(10):
                self.board[row][column] = self.scores[row][column]

    def check_to_show(self, cell):
        cell_to_return = []
        cell_to_check = [cell]
        cell_checked = []

        while len(cell_to_check):
            # TODO: add condition while checking. Now it shows all board.
            for data in cell_to_check.copy():
                for index in indexes:
                    row = data[0] + index[0]
                    column = data[1] + index[1]
                    if not (row > 9 or row < 0 or column > 9 or column < 0):
                        if [row, column] not in cell_checked:
                            cell_to_check.append([row, column])
                            cell_checked.append([row, column])
                            cell_to_return.append([row, column])
                cell_to_check.remove(data)

        return cell_to_return
