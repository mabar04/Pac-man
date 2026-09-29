import pygame
from ...maze.cell import Cell


class MazeRender():

    @classmethod
    def calculate_cell_size(cls, maze_width, maze_height, cells):
        cell_height = maze_height // len(cells)
        cell_width = maze_width // len(cells[0])
        return (cell_width, cell_height)

    @classmethod
    def maze_render(cls, cells: list[list[Cell]], screen):

        WIDTH = screen.get_width()
        HEIGHT = screen.get_height()
        screen.fill((0, 0, 0))
        cell_width, cell_height = cls.calculate_cell_size(WIDTH, HEIGHT,
                                                          cells)
        LIGHT_BLUE = (50, 100, 220)
        YELLOW = (255, 255, 0)
        start_width = 0
        start_height = 0
        for cell_array in cells:
            start_width = 0
            for cell in cell_array:
                if cell.top_wall is True:
                    pygame.draw.line(screen, LIGHT_BLUE,
                                     (start_width, start_height),
                                     (start_width + cell_width,
                                      start_height), 3)
                if cell.left_wall is True:
                    pygame.draw.line(screen, LIGHT_BLUE,
                                     (start_width, start_height),
                                     (start_width,
                                      start_height + cell_height),
                                     3)
                if cell.bottom_wall is True:
                    pygame.draw.line(screen, LIGHT_BLUE,
                                     (start_width, start_height
                                      + cell_height),
                                     (start_width + cell_width,
                                      start_height + cell_height),
                                     3)
                if cell.right_wall is True:
                    pygame.draw.line(screen, LIGHT_BLUE,
                                     (start_width + cell_width,
                                      start_height),
                                     (start_width + cell_width,
                                      start_height + cell_height),
                                     3)
                if all([cell.top_wall, cell.left_wall,
                        cell.bottom_wall, cell.right_wall]) is True:
                    pygame.draw.rect(
                        screen,
                        YELLOW,
                        (start_width, start_height, cell_width,
                            cell_height)
                    )
                start_width = start_width + cell_width
            start_height += cell_height
