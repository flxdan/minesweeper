# Author: Daniel Felix
# Description: A text based minesweeper game

import random


class Board:
    def __init__(self, version):
        if version == "original":
            self.board = [[0 for x in range(8)] for x in range(8)]
        elif version == "player":
            self.board = [["-" for x in range(8)] for x in range(8)]

    def print_board(self):
        column_header = "  "
        for i in range(8):
            column_header = column_header + str(i + 1) + " "
        print(column_header)

        num = 1
        for cell in self.board:
            print(str(num) + " " + " ".join(str(cell) for cell in cell))
            num += 1

    def get_board(self):
        return self.board

    def set_cell_value(self, row, column, val):
        self.board[row][column] = val

    def get_cell_value(self, row, column):
        return self.board[row][column]

    def get_game_status(self):
        for row in self.board:
            for cell in row:
                if cell == "-":
                    return True
        return False

    def set_cells(self):
        for num in range(6):
            x = random.randint(0, 8 - 1)
            y = random.randint(0, 8 - 1)
            self.board[x][y] = 'M'

            if (0 <= x <= 7) and (0 <= y <= 6):
                if self.board[x][y + 1] != 'M':
                    self.board[x][y + 1] += 1  # right cell

            if (0 <= x <= 7) and (1 <= y <= 7):
                if self.board[x][y - 1] != 'M':
                    self.board[x][y - 1] += 1  # left cell

            if (1 <= x <= 7) and (0 <= y <= 7):
                if self.board[x - 1][y] != 'M':
                    self.board[x - 1][y] += 1  # top cell

            if (0 <= x <= 6) and (0 <= y <= 7):
                if self.board[x + 1][y] != 'M':
                    self.board[x + 1][y] += 1  # bottom cell

            if (1 <= x <= 7) and (1 <= y <= 7):
                if self.board[x - 1][y - 1] != 'M':
                    self.board[x - 1][y - 1] += 1  # upper left

            if (1 <= x <= 7) and (0 <= y <= 6):
                if self.board[x - 1][y + 1] != 'M':
                    self.board[x - 1][y + 1] += 1  # upper right

            if (0 <= x <= 6) and (0 <= y <= 6):
                if self.board[x + 1][y + 1] != 'M':
                    self.board[x + 1][y + 1] += 1  # lower right

            if (0 <= x <= 6) and (1 <= y <= 7):
                if self.board[x + 1][y - 1] != 'M':
                    self.board[x + 1][y - 1] += 1  # lower left


def find_zeros(row, column, player_board, values_board, visited):
    # If the cell already not visited
    if [row, column] not in visited:

        # Mark the cell visited
        visited.append([row, column])

        if values_board.get_cell_value(row, column) == 0:
            # Display it to the user
            player_board.set_cell_value(row, column, values_board.get_cell_value(row, column))

            # Recursive calls for the neighboring cells
            if row > 0:
                find_zeros(row - 1, column, player_board, values_board, visited)
            if row < 7:
                find_zeros(row + 1, column, player_board, values_board, visited)
            if column > 0:
                find_zeros(row, column - 1, player_board, values_board, visited)
            if column < 7:
                find_zeros(row, column + 1, player_board, values_board, visited)
            if row > 0 and column > 0:
                find_zeros(row - 1, column - 1, player_board, values_board, visited)
            if row > 0 and column < 7:
                find_zeros(row - 1, column + 1, player_board, values_board, visited)
            if row < 7 and column > 0:
                find_zeros(row + 1, column - 1, player_board, values_board, visited)
            if row < 7 and column < 7:
                find_zeros(row + 1, column + 1, player_board, values_board, visited)

        if values_board.get_cell_value(row, column) != 0:
            player_board.set_cell_value(row, column, values_board.get_cell_value(row, column))


def main():
    print("Welcome to a game of Minesweeper!")
    print("There are 6 mines in this 8x8 board")

    minesweeper_board = Board("original")

    current_board = Board("player")

    minesweeper_board.set_cells()

    current_board.print_board()

    while current_board.get_game_status():
        row = int(input("Enter the cell row: "))
        column = int(input("Enter the cell column: "))
        flag = input("Place flag (Y/N)? ")
        row -= 1
        column -= 1

        if row + 1 < 0 or row + 1 > 8 or column + 1 < 0 or column + 1 > 8 or flag not in ["Y", "y", "n", "N"]:
            print("Error: Check inputs")
            row = int(input("Enter the cell row: "))
            column = int(input("Enter the cell column: "))
            flag = input("Place flag (Y/N)? ")
            row -= 1
            column -= 1

        if flag.upper() == "Y":
            current_board.set_cell_value(row, column, "F")
            print("")
            current_board.print_board()
        elif minesweeper_board.get_cell_value(row, column) == "M":
            print("")
            print("You landed on a mine!")
            print("Minesweeper values:")
            minesweeper_board.print_board()
            print("Game Over!")

            next_turn = input("Play again (Y/N)? ")
            if next_turn.upper() == "Y":
                main()
            else:
                break
        else:
            if minesweeper_board.get_cell_value(row, column) != 0:
                current_board.set_cell_value(row, column, minesweeper_board.get_cell_value(row, column))
            elif minesweeper_board.get_cell_value(row, column) == 0:
                visited = []
                find_zeros(row, column, current_board, minesweeper_board, visited)
            print("")
            current_board.print_board()

    if not current_board.get_game_status():
        print("Congratulations, you won!")
        next_turn = input("Play again (Y/N)? ")
        if next_turn.upper() == "Y":
            main()


if __name__ == '__main__':
    main()
