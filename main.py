import pygame
from constants import *
import map
display=pygame.display.set_mode((DISP_X,DISP_Y))
gameMap=map.Map(MAP_SIZE,TILE_SIZE,display,(46,46,46),(220,220,220))
#initially set the starting pos of the snake outside the loop here
gameMap.Spawn_snake()
while True:
    pygame.time.delay(50)
    clock=pygame.time.Clock()
    clock.tick()
    gameMap.Move_snake(pygame.key.get_pressed(),display,TILE_SIZE)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    gameMap.Show()
    pygame.display.update()