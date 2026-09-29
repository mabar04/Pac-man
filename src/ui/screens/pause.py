import pygame


class PauseScreen:
    """Pause screen placeholder."""
    def __init__(self):
        self.rendered = False

    def blur_surface(self, surface, scale=0.08):
        width, height = surface.get_size()

        small = pygame.transform.smoothscale(
            surface,
            (int(width * scale), int(height * scale))
        )

        blurred = pygame.transform.smoothscale(
            small,
            (width, height)
        )

        return blurred

    def pause_render(self, screen):
        if self.rendered is False:
            blurred = self.blur_surface(screen)
            screen.blit(blurred, (0, 0))
            text_font = pygame.font.SysFont("impact", 150, bold=90)
            text = text_font.render("PAUSE", True, (255, 136, 60))
            text_rect = text.get_rect(
                    center=screen.get_rect().center
            )
            screen.blit(text, text_rect)
            self.rendered = True
