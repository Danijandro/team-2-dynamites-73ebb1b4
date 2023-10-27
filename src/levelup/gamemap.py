
from levelup.position import Position

class GameMap:
        starting_position = Position(0,0)
        positions = []

        numPositions =100;
       
        def move_south(self,position: Position) -> Position:
                newY =position.y - 1
                if(self.validate_new_cordinate(newY)):
                    return Position(position.x,newY)
                else:
                    print("you cannot move to that direction")
                    return position   

        def move_north(self,position: Position) -> Position:
                newY = position.y + 1
                if(self.validate_new_cordinate(newY)):
                 return Position(position.x,newY)
                else:
                 return position  

        def move_west(self,position: Position) -> Position:
                newX = position.x - 1
                if(self.validate_new_cordinate(newX)):
                 return Position(newX,position.y)
                else:
                 return position  


        def move_east(self,position: Position) -> Position:
                newX = position.x + 1
                if(self.validate_new_cordinate(newX)):
                 return Position(newX,position.y)
                else:
                 return position   
                    
        def validate_new_cordinate(self,newValue) -> bool:
                return newValue>=0 and newValue< self.numPositions

        def calculateposition(self,currrentPostion:Position,direction) -> Position:
           if direction == 1:
             return self.move_north(currrentPostion)
           elif direction == 2:
             return self.move_south(currrentPostion)
           elif direction == 3:
              return self.move_west(currrentPostion)    
           elif direction == 4:
              return self.move_east(currrentPostion)    

