import pygame


class Window:
    """Window management placeholder."""

    def __init__(self, width=800, height=600, title="Pac-Man"):
        self.width = width
        self.height = height
        self.title = title

    def window_render(self):
        screen = pygame.display.set_mode((1000, 800))
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (200, 100, 50, 50)
            )
            pygame.display.flip()
            clock.tick(60)
