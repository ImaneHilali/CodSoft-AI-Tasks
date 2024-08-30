import random

class TicTacToeGame:
    def __init__(self):
        self.board_state = [' ' for _ in range(9)]
        self.active_player = 'X'

    def display_board(self):
        print(f"{self.board_state[0]} | {self.board_state[1]} | {self.board_state[2]}")
        print("---+---+---")
        print(f"{self.board_state[3]} | {self.board_state[4]} | {self.board_state[5]}")
        print("---+---+---")
        print(f"{self.board_state[6]} | {self.board_state[7]} | {self.board_state[8]}")

    def is_move_legal(self, position):
        return self.board_state[position] == ' '

    def execute_move(self, position):
        if self.is_move_legal(position):
            self.board_state[position] = self.active_player
            self.active_player = 'O' if self.active_player == 'X' else 'X'
            return True
        return False

    def has_winner(self):
        winning_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for pattern in winning_patterns:
            if self.board_state[pattern[0]] == self.board_state[pattern[1]] == self.board_state[pattern[2]] != ' ':
                return True
        return False

    def optimal_move(self, depth, maximizing_player):
        if self.has_winner():
            return -1 if maximizing_player else 1
        if not any(space == ' ' for space in self.board_state):
            return 0

        if maximizing_player:
            highest_score = -float('inf')
            for idx in range(9):
                if self.is_move_legal(idx):
                    self.board_state[idx] = 'O'
                    score = self.optimal_move(depth + 1, False)
                    self.board_state[idx] = ' '
                    highest_score = max(highest_score, score)
            return highest_score

        else:
            lowest_score = float('inf')
            for idx in range(9):
                if self.is_move_legal(idx):
                    self.board_state[idx] = 'X'
                    score = self.optimal_move(depth + 1, True)
                    self.board_state[idx] = ' '
                    lowest_score = min(lowest_score, score)
            return lowest_score

    def alphabeta_search(self, depth, maximizing_player, alpha, beta):
        if self.has_winner():
            return -1 if maximizing_player else 1
        if not any(space == ' ' for space in self.board_state):
            return 0

        if maximizing_player:
            best_score = -float('inf')
            best_position = -1
            for idx in range(9):
                if self.is_move_legal(idx):
                    self.board_state[idx] = 'O'
                    score = self.alphabeta_search(depth + 1, False, alpha, beta)
                    self.board_state[idx] = ' '
                    if score > best_score:
                        best_score = score
                        best_position = idx
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return best_position if depth == 0 else best_score

        else:
            best_score = float('inf')
            best_position = -1
            for idx in range(9):
                if self.is_move_legal(idx):
                    self.board_state[idx] = 'X'
                    score = self.alphabeta_search(depth + 1, True, alpha, beta)
                    self.board_state[idx] = ' '
                    if score < best_score:
                        best_score = score
                        best_position = idx
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return best_position if depth == 0 else best_score

    def revert_move(self, position):
        self.board_state[position] = ' '

    def start_game(self):
        while True:
            self.display_board()
            user_input = input("Choose your move (1-9): ")
            user_position = int(user_input) - 1
            if not self.execute_move(user_position):
                print("Invalid move. Please try again.")
                continue
            if self.has_winner():
                self.display_board()
                print("Congratulations, you win!")
                break
            if all(space != ' ' for space in self.board_state):
                self.display_board()
                print("It's a draw!")
                break
            # AI's turn to play
            ai_position = self.alphabeta_search(0, True, -float('inf'), float('inf'))
            self.execute_move(ai_position)
            if self.has_winner():
                self.display_board()
                print("AI wins this round!")
                break
            if all(space != ' ' for space in self.board_state):
                self.display_board()
                print("It's a draw!")
                break

if __name__ == "__main__":
    game_instance = TicTacToeGame()
    game_instance.start_game()
