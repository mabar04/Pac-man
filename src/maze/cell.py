class Cell():

    def __init__(self):
        self.top_wall = False
        self.right_wall = False
        self.bottom_wall = False
        self.left_wall = False

    def create_cell(self, coord):
        if coord >= 8:
            self.left_wall = True
            coord -= 8
        if coord >= 4:
            self.bottom_wall = True
            coord -= 4
        if coord >= 2:
            self.right_wall = True
            coord -= 2
        if coord >= 1:
            self.top_wall = True
            coord -= 1
