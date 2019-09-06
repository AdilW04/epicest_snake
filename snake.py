import tile
import pygame
import tile
from constants import *
class Snake:
    def __init__(self,color,tileSize,window,map):
        #self._snakePart=tile.SnakePart(map[0][0].Get_x(),map[0][0].Get_y(),map[0][0].Get_i(),map[0][0].Get_j(),color,(tileSize,tileSize),window)
        self._snakeParts=[tile.SnakeHead(map[10][10].Get_x(),map[10][10].Get_y(),map[10][10].Get_i(),map[10][10].Get_j(),color,(tileSize,tileSize),window)]
        self._direction="RIGHT"


    def Update_direction(self,keys):#takes in that massive list of key bindings
        #might change to switch case
        print(self._direction)
        if keys[pygame.K_w]:
            if self._direction!="DOWN":
                self._direction="UP"
        if keys[pygame.K_s]:
            if self._direction!="UP":
                self._direction="DOWN"
        if keys[pygame.K_d]:
            if self._direction!="LEFT":
                self._direction="RIGHT"
        if keys[pygame.K_a]:
            if self._direction!="RIGHT":
               self._direction="LEFT"
        else:
            pass

    def Initial_spawn(self,map):
        for i in self._snakeParts:
            #remove tile
            #tile=map[i.Get_i()][i.Get_j()]
            map[i.Get_i()].remove(map[i.Get_i()][i.Get_j()])
            #inserting snake part
            map[i.Get_i()].insert(i.Get_j(),i)
    # rearange,Then give new indexes
    def move(self,map,window,tileSize):
        for i in self._snakeParts:
            #removes snake part
            map[i.Get_i()].remove(map[i.Get_i()][i.Get_j()])

            #insert tile
            map[i.Get_i()].insert(i.Get_j(), tile.Tile(window, BG_COLOR, i.Get_pos(), [tileSize,tileSize],i.Get_i(),i.Get_j()))
            #TODO finish move method
            #update position within list
            if self._direction=="UP":
                i.Set_i(i.Get_i()-1)
            if self._direction=="DOWN":
                i.Set_i(i.Get_i()+1)
            if self._direction=="LEFT":
                i.Set_j(i.Get_j()-1)
            if self._direction=="RIGHT":
                i.Set_j(i.Get_j()+1)
            #actually inserting the snake part into the list here:
            #remove tile
            map[i.Get_i()].remove(map[i.Get_i()][i.Get_j()])
            #insert snakepart
            print(i.Get_i())
            print(i.Get_j())
            if i.Get_i()<0:
                raise IndexError("list index out of range")
            elif i.Get_j()<0:
                raise IndexError("list index out of range")
            else:
                map[i.Get_i()].insert(i.Get_j(),i)
            print(i.Get_pos())
            #rmbr 2 return map
            return map

