class Character:
    image_s = []
    image_d = []
    image_a = []
    image_w = []

    image = None
    direction = 's'
    num = 0

    def __init__(self, filename):
        self.image_s = [
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_s0.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_s1.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_s2.png"), (cell_size * 8, cell_size * 8))
        ]

        self.image_d = [
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_d0.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_d1.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_d2.png"), (cell_size * 8, cell_size * 8))
        ]

        self.image_a = [
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_a0.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_a1.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_a2.png"), (cell_size * 8, cell_size * 8))
        ]

        self.image_w = [
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_w0.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_w1.png"), (cell_size * 8, cell_size * 8)),
            pygame.transform.scale(pygame.image.load(f"resources/characters/{filename}_w2.png"), (cell_size * 8, cell_size * 8))
        ]

        image = self.image_s[0]
        direction = 's'
        num = 0

        self.rect = image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        
class PlayerCharacter(Character):
    def walk(self, direction):
        new_rect = self.rect.copy()

        if direction == 'w':
            new_image = self.image_w
        elif direction == 'd':
            new_image = self.image_d
        elif direction == 'a':
            new_image = self.image_a
        else:
            new_image = self.image_s
