import pygame
from ChessEngine import ChessEngine
from ChessAI import ChessAI

class ChessMain:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess Game")
        self.clock = pygame.time.Clock()
        self.engine = ChessEngine()
        self.ai = ChessAI(self.engine)
        self.valid_moves = []
        self.selected_square = None
        self.running = True

    def draw_board(self):
        colors = [pygame.Color(255, 255, 255), pygame.Color(169, 169, 169)]  # Màu trắng và xám
        for r in range(8):
            for c in range(8):
                color = colors[(r + c) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(c * 100, r * 100, 100, 100))

    def draw_pieces(self):
        for r in range(8):
            for c in range(8):
                piece = self.engine.board[r][c]
                if piece != ".":
                    self.screen.blit(pygame.image.load(f'images/{piece}.png'), (c * 100, r * 100))

    def handle_click(self, square):
        row, col = square
        if self.selected_square:
            start = self.selected_square
            end = square
            # Kiểm tra nếu nước đi là hợp lệ
            if end in self.engine.get_valid_moves(start[0], start[1]):
                self.engine.make_move(start, end)
                ai_move = self.ai.get_best_move(depth=3)  # Thay đổi độ sâu tại đây
                if ai_move:
                    self.engine.make_move(ai_move[0], ai_move[1])
                self.selected_square = None
        else:
            if self.engine.board[row][col][0] == 'w':  # Chỉ cho phép chọn quân trắng
                self.selected_square = square
            else:
                self.selected_square = None

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    square = (pos[1] // 100, pos[0] // 100)  # (row, col)
                    self.handle_click(square)

            self.draw_board()
            self.draw_pieces()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = ChessMain()
    game.run()
