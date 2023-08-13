import pygame

from pygame.locals import *
from engine.movement import *
from engine.map import Map
from resources.constants import *

pygame.init()

running = True
fighting = False
menu_open = False

num = 0
direction = 's'

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    #if fighting:
        #window.fill((255, 255, 255))
#
        ## Draw an oval in the top right corner
        #pygame.draw.ellipse(window, (255, 0, 0), pygame.Rect(window_width - 100, 0, 100, 100))
#
        ## Draw an oval in the bottom left corner
        #pygame.draw.ellipse(window, (0, 0, 255), pygame.Rect(0, window_height - 100, 100, 100))
#
        #pygame.display.flip()
    #elif menu_open:
        #bg_rect_width = 150
        #bg_rect_height = 500
        #bg_rect_color = (0, 0, 0)
        #bg_rect_x = window_width - bg_rect_width
        #bg_rect_y = 0
        #pygame.draw.rect(window, bg_rect_color, (bg_rect_x, bg_rect_y, bg_rect_width, bg_rect_height))
#
#
        #rect_width = 140
        #rect_height = 490
        #rect_color = (255, 255, 255)
        #rect_x = window_width - rect_width - 5
        #rect_y = 5
        #pygame.draw.rect(window, rect_color, (rect_x, rect_y, rect_width, rect_height))
#
        #pygame.display.flip()
    #else:
    encounter, direction, num = ground_roam(direction, num)

    if encounter:
        print("fighting")
        fighting = True
        encounter = False

pygame.quit()