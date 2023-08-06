import pygame
from pygame.locals import *

cell_size = 20  # Adjust cell size as needed
barrier_color = (255, 0, 0)  # Red color for barriers
walkable_color = (255, 255, 255)  # White color for walkable areas
grass_color = (0, 255, 0)  # White color for grass areas

character_image_s = [
    pygame.transform.scale(pygame.image.load("resources/character_s0.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_s1.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_s2.png"), (cell_size * 8, cell_size * 8))
]

character_image_d = [
    pygame.transform.scale(pygame.image.load("resources/character_d0.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_d1.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_d2.png"), (cell_size * 8, cell_size * 8))
]

character_image_a = [
    pygame.transform.scale(pygame.image.load("resources/character_a0.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_a1.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_a2.png"), (cell_size * 8, cell_size * 8))
]

character_image_w = [
    pygame.transform.scale(pygame.image.load("resources/character_w0.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_w1.png"), (cell_size * 8, cell_size * 8)),
    pygame.transform.scale(pygame.image.load("resources/character_w2.png"), (cell_size * 8, cell_size * 8))
]

stepnum = [
    0,0,0,
    1,1,1,
    0,0,0,
    2,2,2
] 

menu_key = K_c