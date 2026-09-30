import pygame
from .screens import MainMenu, MazeRender, PauseScreen, VictoryScreen
from .screens import Instructions, GameOverScreen


class Window:
    """Window management placeholder."""

    def __init__(self, width=1100, height=1000, title="Pac-Man"):
        self.width = width
        self.height = height
        self.title = title

    def window_render(self, cells, pacgums):
        pygame.init()
        screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
        screen = pygame.display.set_mode(((screen_width * 0.6),
                                          (screen_height * 0.8)))
        game_rect = pygame.Rect(100, 100, screen.get_width() - 200,
                                screen.get_height() - 200)
        game_surface = pygame.Surface(game_rect.size)
        pygame.display.set_caption("Pac-Man")
        clock = pygame.time.Clock()
        state = "MAZE"
        pause_render = PauseScreen()
        maze_render = MazeRender()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if state == "PAUSE":
                            state = "MAZE"
                        elif state == "MAZE":
                            state = "PAUSE"
                            if event.type != pygame.K_SPACE:
                                pygame.event.wait()
                                pause_render.rendered = False
            if state == "MENU":
                MainMenu().render_menu(game_surface)
            elif state == "MAZE":
                maze_render.maze_render(cells, game_surface, pacgums)
            elif state == "PAUSE":
                pause_render.pause_render(game_surface)
            elif state == "VICTORY":
                VictoryScreen().victory_render(game_surface)
            elif state == "INSTRUCTIONS":
                Instructions().Instructions_render()
            elif state == "GAMEOVER":
                GameOverScreen().over_render()

            screen.blit(game_surface, game_rect.topleft)
            pygame.display.flip()
            clock.tick(60)
