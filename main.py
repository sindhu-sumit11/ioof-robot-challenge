import Robot

def main():
    
    isRobotPlaced = False
    rob = Robot.robot()
    file = open('input.txt', 'r')

    lines = file.readlines()    
   
    for line in lines:
        placeCommand = False
        
        for command in line.split():
            pos = [0,0, 'NORTH']
            index = 0
            
            if command == 'PLACE' and placeCommand == False:
                placeCommand = True
            
            elif placeCommand == True:
                for s in command.split(','):
                    if index < 2:
                        pos[index] = int(s)
                        index = index + 1
                    elif index == 2:
                        pos[index] = s
                        
                placeCommand = False
                if rob.place(pos) == True:
                    isRobotPlaced = True
         #       else:
         #           isRobotPlaced = False
            
            
            elif placeCommand == False and isRobotPlaced == True:
                if command == 'MOVE':
                    rob.move()
                elif command == 'LEFT':
                    rob.left()
                elif command == 'RIGHT':
                    rob.right()
                elif command == 'REPORT':
                         rob.report()
            
           # elif isRobotPlaced == False and command == 'REPORT':
           #     print('Robot has not been placed or pickedup')
                    
                    



main()
    
    

    
