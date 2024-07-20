import pygame
from game2048 import Game2048

class GUI2048:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.screen = pygame.display.set_mode((400, 500))
        pygame.display.set_caption('2048 Game')
        self.font = pygame.font.Font(None, 55)
        self.running = True
        self.clock = pygame.time.Clock()
        self.colors = {
            0: (204, 192, 179),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
        }
        self.run_game()

    def draw_board(self):
        self.screen.fill((187, 173, 160))
        for i in range(self.game.size):
            for j in range(self.game.size):
                value = self.game.board[i][j]
                color = self.colors.get(value, (60, 58, 50))
                pygame.draw.rect(self.screen, color, (j * 100 + 20, i * 100 + 20, 80, 80))
                if value != 0:
                    text = self.font.render(str(value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(j * 100 + 60, i * 100 + 60))
                    self.screen.blit(text, text_rect)
        
        score_text = self.font.render(f"Score: {self.game.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 410))

    def draw_game_over(self):
        self.screen.fill((187, 173, 160))
        text = self.font.render("Game Over!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(200, 200))
        self.screen.blit(text, text_rect)

        restart_text = self.font.render("Press R to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(200, 300))
        self.screen.blit(restart_text, restart_rect)

        quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(200, 350))
        self.screen.blit(quit_text, quit_rect)

    def get_player_name(self):
        name = ""
        input_box = pygame.Rect(100, 150, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill((30, 30, 30))
            txt_surface = self.font.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            self.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(self.screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(30)

    def handle_game_over(self):
        while self.running:
            self.draw_game_over()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player_name = self.get_player_name()
                        if player_name:
                            self.game.save_leaderboard(player_name)
                        self.game = Game2048(difficulty=self.game.difficulty)
                        return
                    elif event.key == pygame.K_q:
                        player_name = self.get_player_name()
                        if player_name:
                            self.game.save_leaderboard(player_name)
                        self.running = False
                        return

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.game.move_down()
                    elif event.key == pygame.K_LEFT:
                        self.game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.game.move_right()
                    elif event.key == pygame.K_u:
                        self.game.undo()
                    self.game.add_new_tile()

            self.draw_board()
            pygame.display.flip()
            self.clock.tick(30)

            if not self.game.can_move():
                self.handle_game_over()

        pygame.quit()
