import pygame


class PauseScreen:
    """Pause screen placeholder."""
    rendered = False

    @classmethod
    def blur_surface(cls, surface, scale=0):
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

    @classmethod
    def pause_render(cls, screen):
        if not cls.rendered:
            blurred = cls.blur_surface(screen)
            screen.blit(blurred, (0, 0))
            text_font = pygame.font.SysFont("impact", 100)
            text = text_font.render("PAUSE", True, (150, 255, 255))
            text_rect = text.get_rect(
                    center=screen.get_rect().center
            )
            screen.blit(text, text_rect)
            cls.rendered = True
