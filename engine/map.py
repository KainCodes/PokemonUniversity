import pygame
from resources.constants import *
map_data = []
    
background_image = None
foreground_image = None
background_rect = None
foreground_rect = None
window_width = 0
window_height = 0

def set_map(filename):
    global background_image, foreground_image, background_rect, foreground_rect, map_data, window_width, window_height

    map_data = []

    with open(f"./maps/{filename}", "r") as file:
        for line in file:
            map_data.append(list(line.strip().split(',')))
    
    background = map_data.pop(0)[0]

    window_width = len(map_data[0]) * cell_size  # Adjust cell size as needed
    window_height = len(map_data) * cell_size  # Adjust cell size as needed

    background_image = pygame.transform.scale(pygame.image.load(f"resources/{background}_background.png"), (window_width, window_height))
    foreground_image = pygame.transform.scale(pygame.image.load(f"resources/{background}_foreground.png"), (window_width, window_height))

    background_rect = background_image.get_rect()
    background_rect.centerx = window_width // 2
    background_rect.centery = window_height // 2

    foreground_rect = background_image.get_rect()
    foreground_rect.centerx = window_width // 2
    foreground_rect.centery = window_height // 2

set_map("test_map.txt")

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Map Game")

for row in range(len(map_data)):
    for col in range(len(map_data[0])):
        if map_data[row][col] == '#':
            pygame.draw.rect(window, barrier_color, (col * cell_size, row * cell_size, cell_size, cell_size))
        elif map_data[row][col] == '.':
            pygame.draw.rect(window, walkable_color, (col * cell_size, row * cell_size, cell_size, cell_size))

character_rect = character_image_s[0].get_rect()
character_rect.centerx = window_width // 2
character_rect.centery = window_height // 2

def get_character_rect():
    return character_rect.copy()

def redraw_map(new_character_rect, direction, num):
    global character_rect
    character_rect = new_character_rect
    draw_background(map_data)
    draw_character(direction, num)
    draw_foreground(map_data)

    pygame.display.flip()
    return 

def draw_background(map_data):
    window.blit(background_image, background_rect)

    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == '#1':
                pygame.draw.rect(window, barrier_color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif map_data[row][col] == '-':
                pygame.draw.rect(window, grass_color, (col * cell_size, row * cell_size, cell_size, cell_size))

    return

def draw_foreground(map_data):
    window.blit(foreground_image, foreground_rect)
    
    return

def draw_character(direction, num):
    if direction == 'w':
        character_image = character_image_w
    elif direction == 'd':
        character_image = character_image_d
    elif direction == 'a':
        character_image = character_image_a
    else:
        character_image = character_image_s

    image = character_image[stepnum[num]]
    window.blit(image, character_rect)

def has_encounter():
    return random.randint(0, 500) <= 1