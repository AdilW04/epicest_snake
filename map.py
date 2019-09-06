import tile
import snake
#note snake class takes mapArray,rearanges it to change its position and returns new map array
#eg: self._mapArray=self._snake.move_Snake(sfl._mapArray)once every iteration
class Map:
    def __init__(self,mapSize,tileSize,window,mapColor,snakeColor):
        self._color=mapColor
        self._snakeColor=snakeColor
        self._mapArray=self.Create_map(mapSize,window,tileSize)
        self._snake=snake.Snake(snakeColor,tileSize,window,self._mapArray)
        print(self._mapArray)
        for i in self._mapArray:
            for j in i:
              print(j.Get_pos())
            print("new lists")
    #TODO add change color function later
    def Spawn_snake(self):
        self._snake.Initial_spawn(self._mapArray)

    def Move_snake(self,keys,window,tileSize):
        self._snake.Update_direction(keys)
        self._mapArray=self._snake.move(self._mapArray,window,tileSize)

    def Create_map(self,mapSize,window,tileSize):
        out=[]
        for i in range(mapSize):
            out.append([])
        for i,x in zip(out,range(mapSize)):
            for j in range(mapSize):
                i.append(tile.Tile(window,self._color,(j*tileSize,x*tileSize),(tileSize,tileSize),x,j))

        return out
    def Show(self):
        for i in self._mapArray:
            for j in i:
                j.Show()