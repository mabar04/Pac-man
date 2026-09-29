import pygame
from .screens import MainMenu, MazeRender, PauseScreen, VictoryScreen
from .screens import Instructions, GameOverScreen


class Window:
    """Window management placeholder."""

    def __init__(self, width=1100, height=1000, title="Pac-Man"):
        self.width = width
        self.height = height
        self.title = title

    def window_render(self, cells):
        pygame.init()
        screen = pygame.display.set_mode((1100, 1000))
        game_rect = pygame.Rect(50, 50, 1000, 900)
        game_surface = pygame.Surface(game_rect.size)
        pygame.display.set_caption("Pac-Man")
        clock = pygame.time.Clock()
        state = "MAZE"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if state == "PAUSE":
                            state = "MAZE"
                        else:
                            state = "PAUSE"
                            if event.type != pygame.K_SPACE:
                                pygame.event.wait()
                                PauseScreen().rendered = False
            if state == "MENU":
                MainMenu().render_menu(cells, game_surface)
            elif state == "MAZE":
                MazeRender().maze_render(cells, game_surface)
            elif state == "PAUSE":
                PauseScreen().pause_render(game_surface)
            elif state == "VICTORY":
                VictoryScreen().victory_render(game_surface)
            elif state == "INSTRUCTIONS":
                Instructions().Instructions_render()
            elif state == "GAMEOVER":
                GameOverScreen().over_render()

            screen.blit(game_surface, game_rect.topleft)
            pygame.display.flip()
            clock.tick(60)
