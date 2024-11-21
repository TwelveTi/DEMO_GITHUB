class ChessEngine:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_turn = True

    def make_move(self, start, end):
        r1, c1 = start
        r2, c2 = end
        self.board[r2][c2] = self.board[r1][c1]
        self.board[r1][c1] = "."
        self.white_turn = not self.white_turn

    def get_valid_moves(self, row, col):
        piece = self.board[row][col]
        moves = []
        if piece != ".":
            color = piece[0]
            # Logic cho quân Tốt
            if piece[1].lower() == 'p':
                direction = 1 if color == 'b' else -1
                # Di chuyển thẳng
                if 0 <= row + direction < 8 and self.board[row + direction][col] == '.':
                    moves.append((row + direction, col))
                # Di chuyển bắt chéo
                if 0 <= row + direction < 8:
                    if col - 1 >= 0 and self.board[row + direction][col - 1][0] != color:
                        moves.append((row + direction, col - 1))
                    if col + 1 < 8 and self.board[row + direction][col + 1][0] != color:
                        moves.append((row + direction, col + 1))
            # Logic cho các quân khác có thể thêm vào đây (như mã, xe, tượng, hậu, vua)
        return moves

    def evaluate_board(self):
        score = 0
        for row in self.board:
            for piece in row:
                if piece != '.':
                    if piece[0] == 'w':  # Quân trắng
                        score += 1  # Giá trị tích cực cho quân trắng
                    else:  # Quân đen
                        score -= 1  # Giá trị tiêu cực cho quân đen
        return score

    def undo_move(self, start, end):
        r1, c1 = start
        r2, c2 = end
        self.board[r1][c1] = self.board[r2][c2]
        self.board[r2][c2] = "."
        self.white_turn = not self.white_turn
