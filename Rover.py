import Grid

'''Grid import needed in order to access the grid objects boundry coordinates'''

'''The rover class allows for use of a rover object, to allow multiple potentially infinate
rovers to be used this class will only be instantiated once. The user will choose how many
rovers they want, and each one will be run in turn using the input provided by the user'''


class Rover():
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.startDirection = " "


    def setStart(self, roverStart):
        self.startX = int(roverStart[0])
        self.startY = int(roverStart[2])
        self.startDirection = roverStart[4]
        self.currentX = self.startX
        self.currentY = self.startY
        self.currentDirection = self.startDirection


    def execute(self, command_string):
        for command in command_string:
            if command == "L":
                self.turnLeft()

            elif command == "R":
                self.turnRight()

            elif command == "M":
                self.move()

            elif command == " ":
                pass

            else:
                print("Invalid command, try again")
                break

    def turnLeft(self):
        if self.currentDirection == "N":
            self.currentDirection = "W"
            
        elif self.currentDirection == "E":
            self.currentDirection = "N"
            
        elif self.currentDirection == "S":
            self.currentDirection = "E"
            
        else:
            self.currentDirection = "S"


    def turnRight(self):
        if self.currentDirection == "N":
            self.currentDirection = "E"
            
        elif self.currentDirection == "E":
            self.currentDirection = "S"
            
        elif self.currentDirection == "S":
            self.currentDirection = "W"
            
        else:
            self.currentDirection = "N"


    def move(self):
        if self.currentDirection == "N" and self.currentY <= Grid.grid.endY:
            self.currentY += 1
            
        elif self.currentDirection == "E" and self.currentX <= Grid.grid.endX:
            self.currentX += 1
          
        elif self.currentDirection == "S" and self.currentY >= Grid.grid.startY:
            self.currentY -=1
            
        elif self.currentDirection == "W" and self.currentX >= Grid.grid.startX:
            self.currentX -=1

        else:
            print("This will take the rover off the grid") 

            
    def returnCurrentPos(self):
        self.currentX = str(self.currentX)
        self.currentY = str(self.currentY)
        self.correntPos = f'{str(self.currentX)} {str(self.currentY)} {self.currentDirection}' #to be used later in the rover list
        print(f'Your current position is: {self.currentX},{self.currentY},{self.currentDirection}')

'''Empty rover object to be populated by user input of starting position and direction '''

currentRover = Rover()
    
