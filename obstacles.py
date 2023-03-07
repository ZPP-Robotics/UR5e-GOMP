class Obstacle:
    def __init__(self):
        pass
    
    def convert(self):
        pass


class Box(Obstacle):
    def __init__(self, middle, height, width, depth):
        super().__init__()
        self.middle = middle
        self.height = height
        self.width = width
        self.depth = depth
    
    def convert(self):
        pass
