'''The RoverList class allows storage of all rovers run, and to provide the scope to have unlimited rovers. '''

class RoversList():
    def __init__(self):
        self.roverList = []
        self.minSize = 0
        self.maxSize = 0
        self.currentRover = 0
        self.roverRemaining = self.maxSize - self.minSize
        self.roversDone = len(self.roverList)
        


    def displayRoverJourneys(self):
        for rover in self.roverList:
            roverNum, roverStart, roverInstructions, roverEnd = rover
            print(f'Rover{roverNum} started at co-ordinates {roverStart}, the intructions given were {roverInstructions} so it ended at co-ordinates {roverEnd}. \n')

    def displayIndRover(self, roverReq):
        for rover in self.roverList:
            x = 0
            roverNum, roverStart, roverInstructions, roverEnd = rover
            if roverNum == roverReq:
                print(f'Rover{roverNum} started at co-ordinates {roverStart}, the intructions given were {roverInstructions} so it ended at co-ordinates {roverEnd}. \n')
                break
            else:
                if x < len(self.roverList):
                    pass
                else:
                    print("Rover could not be found")


'''Creates a rovers list object'''

roverL = RoversList()
