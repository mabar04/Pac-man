import pygame
from .screens import __all__ as screens

class Window:
    """Window management placeholder."""

    def __init__(self, width=1100, height=1000, title="Pac-Man"):
        self.width = width
        self.height = height
        self.title = title

    def window_render(self):
        screen = pygame.display.set_mode((1100, 1000))
        clock = pygame.time.Clock()
        state = "MENU"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if state == "MENU":
                screens.
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (200, 100, 50, 50)
            )
            pygame.display.flip()
            clock.tick(60)
