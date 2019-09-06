import pygame
class Tile:
    #size and position given by map obj
    def __init__(self,window,colour,position,size,i,j):
        self._xPos=position[0]
        self._yPos=position[1]
        self._rect=pygame.draw.rect(window,colour,(self._xPos,self._yPos,size[0],size[1]))
        self._size=size
        self._colour=colour
        self._window=window
        self._i=i
        self._j=j
    def Get_rect(self):
        return self._rect
    def Show(self):
        pygame.draw.rect(self._window,self._colour,(self._xPos,self._yPos,self._size[0],self._size[1]))
    def Get_pos(self):
        return [self._xPos,self._yPos]
    Get_x=lambda self:self._xPos
    Get_y=lambda self:self._yPos
    def Get_i(self):
        return self._i
    def Get_j(self):
        return self._j


class SnakePart(Tile):
    #the map class above gives it its x and y and i and j and color through a for loop or some sort of algorithm
    def __init__(self,x,y,i,j,color,size,window):
        #What is i and j?,explained
        #eg:[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        #i=list inside the list above(y)
        #j=element,(rect) inside i(x)
        #i and j are whole number indexes NOT rects
        super().__init__(window,color,(x,y),size,i,j)
        self._xPos=x
        self._yPos=y
        self._color=color
        self._size=size
    #TODO first have it so that it displays a snake head on the middle tile in the screen, just put one snake part and replace a tile with a snake head object
    #called by map class every time something moves
    def Set_j(self,new):
        self._j=new
        self._xPos=self._j*self._size[0]
    def Set_i(self,new):
        self._i=new
        self._yPos=self._i*self._size[0]

class SnakeHead(SnakePart):
    def __init__(self,x,y,i,j,color,size,window):
        super().__init__(x,y,i,j,color,size,window)