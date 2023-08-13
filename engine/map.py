import pygame
from resources.constants import *
map_data = []
    
background_image = None
foreground_image = None
background_rect = None
foreground_rect = None
window_width = 0
window_height = 0

class Map():
    mapBackgrounds = []
    mapForegrounds = []
    map_data = []
    background_rect = None
    foreground_rect = None
    width = 0
    height = 0

    def __init__(self, mapFile, backgrounds, foregrounds):
        self.mapBackgrounds = []
        self.mapForegrounds = []
        self.map_data = []

        with open(f"./resources/maps/{mapFile}", "r") as file:
            for line in file:
                self.map_data.append(list(line.strip().split(',')))

        self.width = len(self.map_data[0]) * cell_size  # Adjust cell size as needed
        self.height = len(self.map_data) * cell_size  # Adjust cell size as needed
        
        for filename in backgrounds:
            image = pygame.transform.scale(
                pygame.image.load(f"resources/maps/{filename}.png"), 
                (self.width, self.height)
            )

            self.mapBackgrounds.append(image)

        for filename in foregrounds:
            image = pygame.transform.scale(
                pygame.image.load(f"resources/maps/{filename}.png"), 
                (self.width, self.height)
            )

            self.mapForegrounds.append(image)

        self.background_rect = self.mapBackgrounds[0].get_rect()
        self.background_rect.centerx = centerx
        self.background_rect.centery = centery

        self.foreground_rect = self.mapForegrounds[0].get_rect()
        self.foreground_rect.centerx = centerx
        self.foreground_rect.centery = centery

    def redraw_map(self, new_character_rect, direction, num):
        global character_rect
        character_rect = new_character_rect
        
        self.draw_background()
        draw_character(direction, num)
        self.draw_foreground()

        pygame.display.flip()
        return 

    def draw_background(self):
        for image in self.mapBackgrounds:
            window.blit(image, self.background_rect)

        for row in range(len(self.map_data)):
            for col in range(len(self.map_data[0])):
                if self.map_data[row][col] == '#1':
                    pygame.draw.rect(window, barrier_color, (self.x(col), self.y(row), cell_size, cell_size))
                elif self.map_data[row][col] == '-':
                    pygame.draw.rect(window, grass_color, (self.x(col), self.y(row), cell_size, cell_size))

        return

    def draw_foreground(self):
        for image in self.mapForegrounds:
            window.blit(image, self.foreground_rect)
        
        return
    
    def x(self, col):
        return col * cell_size + centerx - (self.width / 2)
    
    def y(self, row):
        return row * cell_size + centery - (self.height / 2)

#window_width = len(map_data[0]) * cell_size  # Adjust cell size as needed
#window_height = len(map_data) * cell_size  # Adjust cell size as needed
pygame.display.set_caption("Map Game")

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
centerx = window.get_rect().centerx
centery = window.get_rect().centery

character_rect = character_image_s[0].get_rect()
character_rect.centerx = centerx
character_rect.centery = centery

def get_character_rect():
    return character_rect.copy()

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