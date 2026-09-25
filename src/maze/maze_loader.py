from . import MazeGenerator


class MazeLoader():

    def __init__(self, height, width, seed):
        self.__height = height
        self.__width = width
        self.__seed = seed

    def set_height(self, height):
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def set_seed(self, seed):
        self.__seed = seed

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_seed(self):
        return self.__seed

    def generate_maze(self):
        return MazeGenerator((self.get_width(), self.get_height()),
                             seed=self.get_seed())
