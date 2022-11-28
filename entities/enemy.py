import pygame
from   initial_screen import screen, deminsions
width = deminsions[0]
height = deminsions[1]
generate_enemies=0


class Lazer_e(pygame.sprite.Sprite):
    def __init__(self):
        super(Lazer_e, self).__init__()
        self.sprite = pygame.Surface((45,10))
        self.sprite.fill((0,205,0))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    def update(self, dir):
        """
        1: left
        2: right
        3: up
        4: down
        """
        if 1:
            self.rect.centerx -= 4

        elif 2:
            self.rect.centerx += 4

        elif 3:
            self.rect.centery -= 4

        elif 4:
            self.rect.centery += 4

class Lazer_m(pygame.sprite.Sprite):
    def __init__(self):
        super(Lazer_m, self).__init__()
        self.sprite = pygame.Surface((60,9))
        self.sprite.fill((255,255,0))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    def update(self, dir):
        """
        1: left
        2: right
        3: up
        4: down
        """
        if 1:
            self.rect.centerx -= 4

        elif 2:
            self.rect.centerx += 4

        elif 3:
            self.rect.centery -= 4

        elif 4:
            self.rect.centery += 4

class Lazer_H(pygame.sprite.Sprite):
    def __init__(self):
        super(Lazer_H, self).__init__()
        self.sprite = pygame.Surface((55,10))
        self.sprite.fill((255,0,0))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    def update(self, dir):
        """
        1: left
        2: right
        3: up
        4: down
        """
        if 1:
            self.rect.centerx -= 4

        elif 2:
            self.rect.centerx += 4

        elif 3:
            self.rect.centery -= 4

        elif 4:
            self.rect.centery += 4
