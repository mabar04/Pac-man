import pygame


class MainMenu:
    """Main menu."""

    def __init__(self):
        self.title = "Pac-Man"
        self.selected_option = 0

    def render_menu(self):

        pygame.init()

        WIDTH = 1000
        HEIGHT = 800

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pac-Man")

        BLACK = (0, 0, 0)
        YELLOW = (255, 255, 0)
        LIGHT_BLUE = (50, 100, 220)
        GRAY = (156, 151, 151)
        LIGHT_ORANGE = (255, 139, 26)

        title_font = pygame.font.SysFont("Press Start 2P", 130)
        option_font = pygame.font.SysFont(
            "DejaVu Sans",
            40,
            bold=True
        )

        # -------------------------
        # Options
        # -------------------------

        options = [
            "START",
            "HIGHSCORE",
            "CHEAT MODE",
            "EXIT"
        ]

        # One rectangle for each option
        option_rects = []

        for i, option in enumerate(options):

            text = option_font.render(
                option,
                True,
                YELLOW
            )

            rect = text.get_rect(
                center=(
                    WIDTH // 2,
                    300 + i * 100
                )
            )

            # Add padding around the text
            rect.inflate_ip(80, 30)

            option_rects.append(rect)

        # -------------------------
        # Main loop
        # -------------------------

        running = True

        while running:

            # =========================
            # EVENTS
            # =========================

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self.selected_option -= 1

                        if self.selected_option < 0:
                            self.selected_option = 0

                    if event.key == pygame.K_DOWN:
                        self.selected_option += 1

                        if self.selected_option >= len(options):
                            self.selected_option = len(options) - 1

                    if event.key == pygame.K_RETURN:
                        print(
                            "Selected:",
                            options[self.selected_option]
                        )

            # =========================
            # BACKGROUND
            # =========================

            screen.fill(BLACK)

            pygame.draw.rect(
                screen,
                LIGHT_BLUE,
                (5, 5, WIDTH - 10, HEIGHT - 10)
            )

            pygame.draw.rect(
                screen,
                BLACK,
                (20, 20, WIDTH - 40, HEIGHT - 40)
            )

            # =========================
            # TITLE
            # =========================

            title = title_font.render(
                "PAC - MAN",
                True,
                YELLOW,
                LIGHT_ORANGE
            )
            title_rect = title.get_rect(
                center=(WIDTH // 2, 150)
            )
            screen.blit(title, title_rect)

            # =========================
            # OPTIONS
            # =========================

            for i, option in enumerate(options):

                rect = option_rects[i]

                # Selected option
                if i == self.selected_option:

                    # Option rectangle
                    pygame.draw.rect(
                        screen,
                        BLACK,
                        rect,
                        border_radius=10
                    )

                    text_color = YELLOW

                    # Triangle
                    triangle_x = rect.left - 35
                    triangle_y = rect.centery

                    pygame.draw.polygon(
                        screen,
                        YELLOW,
                        [
                            (triangle_x, triangle_y - 12),
                            (triangle_x + 20, triangle_y),
                            (triangle_x, triangle_y + 12)
                        ]
                    )

                else:
                    text_color = GRAY

                # Text
                text = option_font.render(
                    option,
                    True,
                    text_color
                )

                text_rect = text.get_rect(
                    center=rect.center
                )

                screen.blit(text, text_rect)

            # =========================
            # DISPLAY
            # =========================

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
