class SpacialHashGrid:
    def __init__(self,cell_size):
        self.cellSize = cell_size
        self.objects = []
    def __hash__(self,object):
        return int(object.x/self.cellSize),int(object.y/self.cellSize)
    def add(self,object):
        x,y = self.__hash__(object)
        self.contents[y][x] = object
        