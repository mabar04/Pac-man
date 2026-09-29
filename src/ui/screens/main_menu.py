import pygame
from .maze_render import MazeRender


class MainMenu:
    """Main menu."""

    def render_menu(self, screen):

        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()

        BLACK = (0, 0, 0)
        YELLOW = (245, 226, 17)
        LIGHT_BLUE = (50, 100, 220)
        GRAY = (156, 151, 151)
        LIGHT_ORANGE = (255, 139, 26)
        