from ChessEngine import ChessEngine

class ChessAI:
    def __init__(self, engine):
        self.engine = engine

    def minimax(self, depth, maximizing_player):
        if depth == 0:
            return self.engine.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            for r in range(8):
                for c in range(8):
                    if self.engine.board[r][c][0] == 'w':
                        valid_moves = self.engine.get_valid_moves(r, c)
                        for move in valid_moves:
                            start = (r, c)
                            end = move
                            self.engine.make_move(start, end)
                            eval = self.minimax(depth - 1, False)
                            self.engine.undo_move(start, end)
                            max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for r in range(8):
                for c in range(8):
                    if self.engine.board[r][c][0] == 'b':
                        valid_moves = self.engine.get_valid_moves(r, c)
                        for move in valid_moves:
                            start = (r, c)
                            end = move
                            self.engine.make_move(start, end)
                            eval = self.minimax(depth - 1, True)
                            self.engine.undo_move(start, end)
                            min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self, depth):
        best_move = None
        best_value = float('-inf')

        for r in range(8):
            for c in range(8):
                if self.engine.board[r][c][0] == 'w':
                    valid_moves = self.engine.get_valid_moves(r, c)
                    for move in valid_moves:
                        start = (r, c)
                        end = move
                        self.engine.make_move(start, end)
                        move_value = self.minimax(depth - 1, False)
                        self.engine.undo_move(start, end)

                        if move_value > best_value:
                            best_value = move_value
                            best_move = (start, end)

        return best_move
