import Rover, Rovers_List, Grid

'''Import class functionality for the Rover's, Rover List and Grid objects'''

'''again = True used to allow testing of multiple runs through the main program'''

def main():
    again = True

    while again == True:
        gridSize = input('What size grid would you like? Please give your X and Y cordinates in the following format:X Y \n')
        Grid.grid.setGridUp(gridSize)
        
        roverNums = int(input("How many rovers would you like to track?\n"))
        Rovers_List.roverL.maxSize = roverNums

        for i in range(1, Rovers_List.roverL.maxSize+1):
            print("This is rover number: ",i,"\n")
            roverStart = input('Where would you like this rover to start? Please give the X and Y Cordinates and the direction: \n')
            Rover.currentRover.setStart(roverStart.upper())
            commandString = input('Please provide the instructions for how you want the rover to move: \n')
            Rover.currentRover.execute(commandString.upper())
            Rover.currentRover.returnCurrentPos()

            Rovers_List.roverL.roverList.append([i, roverStart, commandString, Rover.currentRover.correntPos])


        againReply = input('Would you like another go, Y/N \n')
        if againReply.upper() == "Y" or againReply == "YES":
            again = True
        elif againReply.upper() == "N" or againReply == "NO":
            again = False
        else:
            print("That was not a correct value")

        
    roverOut = int(input("Press 1 to see all your rovers journeys, or 2 to select a specific rover to see \n"))

    if roverOut == 1:
        Rovers_List.roverL.displayRoverJourneys()
    elif roverOut == 2:
        roverReq = int(input("Which rover would you like to see: \n"))
        Rovers_List.roverL.displayIndRover(roverReq)    
    else:
        print("Please choose a valid option")

'''Calling main function'''        

main()




    
