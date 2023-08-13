import pygame
import random
from pygame.locals import *
from resources.constants import *
from engine.map import get_character_rect, Map

map = Map(
        'dorm.txt',
        ['empty_dormroom_background'],
        ['empty_dormroom_foreground']
)

def ground_roam(direction = 's', num = 0):
    keys = pygame.key.get_pressed()
    encounter = False

    # Calculate the potential new position of the character
    new_character_rect = get_character_rect()
    speed = 16
    if keys[K_LSHIFT] or keys[K_RSHIFT]:
        speed = 48

    num = (num+1) % len(stepnum)

    if keys[K_UP]:
        new_character_rect.centery -= speed
        direction = 'w'
    elif keys[K_DOWN]:
        new_character_rect.centery += speed
        direction = 's'
    elif keys[K_LEFT]:
        new_character_rect.centerx -= speed
        direction = 'a'
    elif keys[K_RIGHT]:
        new_character_rect.centerx += speed
        direction = 'd'
    else:
        num = 0

    # Check for collision with barriers
    collision = False
    for row in range(len(map.map_data)):
        for col in range(len(map.map_data[0])):
            if map.map_data[row][col][0] == '#':
                barrier_rect = pygame.Rect(map.x(col), map.y(row), cell_size, cell_size)
                if new_character_rect.colliderect(barrier_rect):
                    collision = True
                    break
            if map.map_data[row][col] == '-':
                barrier_rect = pygame.Rect(map.x(col), map.y(row), cell_size, cell_size)
                if new_character_rect.colliderect(barrier_rect) and new_character_rect != character_rect:
                    encounter = has_encounter()
                    break
        if collision or encounter:
            break

    # Update the character's position if no collision occurred
    if not collision or encounter:
        map.redraw_map(new_character_rect, direction, num)

        return (encounter, direction, num)

    map.redraw_map(get_character_rect(), direction, 0)
        
    return (encounter, direction, 0)
