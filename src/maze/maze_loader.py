
class MazeLoader():

    def __init__(self, height, width, seed, MazeGenerator):
        self.maze_generator = MazeGenerator
        self.__maze = []
        self.__height = height
        self.__width = width
        self.__seed = seed

    def set_height(self, height):
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def set_seed(self, seed):
        self.__seed = seed

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def seed(self):
        return self.__seed

    @property
    def maze(self):
        return self.__maze

    # Generate the maze and check for all the errors inside it
    def generate_maze(self, seed: int = 0) -> list:
        maze_gen = self.maze_generator((self.width, self.height),
                                       seed=self.seed)
        maze_gen.generate(seed)
        self.__maze = maze_gen.maze
        return self.maze
