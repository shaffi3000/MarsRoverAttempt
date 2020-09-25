
''' startX/startY and endX/endY lay out the boundries of the grid '''

class Grid():
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0

    def updateGridSize(self,endX,endY):
        self.startX = 0
        self.startY = 0
        self.endX = endX
        self.endY = endY

    def setGridUp(self, gridSize):
        self.endX = int(gridSize[0])
        self.endY = int(gridSize[2])


'''Creates a grid objects'''
grid = Grid()
