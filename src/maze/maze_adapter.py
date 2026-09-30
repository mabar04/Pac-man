from .cell import Cell
from .maze_loader import MazeLoader


class MazeAdapter():

    def __init__(self, maze):
        self.mazeLoader: MazeLoader = maze
        self.cells: list[Cell] = []

    def create_cells(self):
        for height_coord in self.mazeLoader.maze:
            cell_list = []
            for width_coord in height_coord:
                cell = Cell()
                cell.create_cell(width_coord)
                cell_list.append(cell)
            self.cells.append(cell_list)

    def get_cell(self, w_index, h_index):
        return self.cells[h_index, w_index]

    def is_wall(self, w_index, h_index, position):
        if position == "top":
            return self.cells[h_index, w_index].top_wall
        elif position == "bottom":
            return self.cells[h_index, w_index].bottom_wall
        elif position == "right":
            return self.cells[h_index, w_index].right_wall
        elif position == "left":
            return self.cells[h_index, w_index].left_wall

    def is_inside(self, w_index, h_index):
        if (0 <= h_index < self.mazeLoader.height
                and 0 <= w_index < self.mazeLoader.width):
            return True
        return False

    def get_neighbors(self, w_index, h_index):
        neighbors: list[tuple] = []

        if (self.is_inside(w_index, h_index - 1)
                and not self.is_wall(w_index, h_index, "top")):
            neighbors.append((w_index, h_index - 1))

        if (self.is_inside(w_index, h_index + 1)
                and not self.is_wall(w_index, h_index, "bottom")):
            neighbors.append((w_index, h_index + 1))

        if (self.is_inside(w_index - 1, h_index)
                and not self.is_wall(w_index, h_index, "left")):
            neighbors.append((w_index - 1, h_index))

        if (self.is_inside(w_index + 1, h_index)
                and not self.is_wall(w_index, h_index, "right")):
            neighbors.append((w_index + 1, h_index))

        return neighbors

    def get_all_walkable(self):
        walkable_cells = []
        for cell_row in self.cells:
            for cell in cell_row:
                bool_array = [cell.bottom_wall, cell.left_wall,
                              cell.right_wall, cell.top_wall]
                player_spawn_x, player_spawn_y = self.player_spawn()
                if (not all(bool_array) and cell !=
                        self.cells[player_spawn_y][player_spawn_x]):
                    walkable_cells.append(cell)
        return walkable_cells

    def ghost_spawns(self):
        return [(0, 0), (0, self.mazeLoader.height - 1),
                (self.mazeLoader.width - 1, 0),
                (self.mazeLoader.width,  self.mazeLoader.height)]

    def player_spawn(self):
        return (self.mazeLoader.width // 2, self.mazeLoader.height // 2)
