
from levelup.coordinate import Coordinate

class GameMap:
        starting_position = Coordinate(0,0)
        positions = []

        numPositions =100;
       
        def move_south(self,coordinate: Coordinate) -> Coordinate:
                newY =coordinate.y - 1
                if(self.validate_new_cordinate(newY)):
                    return Coordinate(coordinate.x,newY)
                else:
                    print("you cannot move to that direction")
                    return coordinate   

        def move_north(self,coordinate: Coordinate) -> Coordinate:
                newY = coordinate.y + 1
                if(self.validate_new_cordinate(newY)):
                 return Coordinate(coordinate.x,newY)
                else:
                 return coordinate  

        def move_west(self,coordinate: Coordinate) -> Coordinate:
                newX = coordinate.x - 1
                if(self.validate_new_cordinate(newX)):
                 return Coordinate(newX,coordinate.y)
                else:
                 return coordinate  


        def move_east(self,coordinate: Coordinate) -> Coordinate:
                newX = coordinate.x + 1
                if(self.validate_new_cordinate(newX)):
                 return Coordinate(newX,coordinate.y)
                else:
                 return coordinate   
                    
        def validate_new_cordinate(self,newValue) -> bool:
                return newValue>=0 and newValue< self.numPositions

        def calculateCordinates(self,currrentPostion:Coordinate,direction) -> Coordinate:
           if direction == 1:
             return self.move_north(currrentPostion)
           elif direction == 2:
             return self.move_south(currrentPostion)
           elif direction == 3:
              return self.move_west(currrentPostion)    
           elif direction == 4:
              return self.move_east(currrentPostion)    

