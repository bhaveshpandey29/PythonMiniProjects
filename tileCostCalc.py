#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

print("Welcome to the tiles calculation surface system".center(100,"*"))
print("\n\n")
#Details of the floor
width = float(input("\t\t\t\tPlease enter the width of the floor: "))
height = float(input("\t\t\t\tPlease enter the height of the floor: "))
#Details of tiles
tile_width = float(input("\t\t\t\tPlease enter the width of the tile: "))
tile_height = float(input("\t\t\t\tPlease enter the height of the tile: "))
cost_one_tile = int(input("\t\t\t\tPlease enter the cost of one tile: "))
try:
    class costCalc():
        #Calculate total cost of the tile
        def totalCostOfTile(self,width,height,tile_width,tile_height,cost_one_tile):
            self.__width = width
            self.__height = height
            self.__tile_width = tile_width
            self.__tile_height = tile_height
            self.__cost_one_tile = cost_one_tile
            
            # Calculations

            self.__areaOfSurface = (self.__width*self.__height)
            self.__areaOfOneTile = (self.__tile_height*self.__tile_width)
            self.__totalTile = (self.__areaOfSurface/self.__areaOfOneTile)
            self.__totalCost = (self.__totalTile*self.__cost_one_tile)
            return self.__totalTile,self.__totalCost

    tc  = costCalc()
    totalCost = tc.totalCostOfTile(width,height,tile_width,tile_height,cost_one_tile)
    print(f"\n\t\t\t\tTotal cost of {totalCost[0]} tiles is {totalCost[1]} USD\n\n")
    print("Thank you for using our system".center(100,"*"))
except Exception as e:
    raise e