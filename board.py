import numpy as np

board_size = (6, 7)


class Board:
    def __init__(self):
        self.player = 1
        self.board = np.zeros(board_size, dtype=int)
        self.winner = None

    def drop(self, column):
        for r in range(board_size[0]):
            if self.board[r, column] == 0:
                self.board[r, column] = self.player
                return [r, column]
        return None

    def check_winner(self, position):
        directions = [np.array((0, 1)), np.array((1, 0)), np.array((1, 1)), np.array((-1, 1))]
        for direction in directions:
            counter = self.check_direction(position, direction) + self.check_direction(position, direction * (-1))
            if counter >= 5:
                self.winner = self.player
                return self.winner

    def check_direction(self, position, direction):
        distance = 1
        while distance < 5:
            new_pos = position + distance * direction
            if 0 <= new_pos[0] < board_size[0] and 0 <= new_pos[1] < board_size[1] and self.player == self.board[
                tuple(new_pos)]:
                distance += 1
            else:
                return distance
        return distance

    def next_move(self, col):
        position = self.drop(col)
        if position is None:
            return
        max_seq = self.check_winner(position)
        self.player = (self.player % 2) + 1

    def reset_board(self):
        self.board = np.zeros(board_size, dtype=int)
        self.winner = None

    def __repr__(self):
        return f"{self.board}"
