import pygame
from   initial_screen          import screen, deminsions
from   entities.background     import bg
store=bg._STORE
width = deminsions[0]
height = deminsions[1]


class Lazer(pygame.sprite.Sprite):
    def __init__(self):
        super(Lazer, self).__init__()
        self.sprite = pygame.Surface((45,10))
        self.sprite.fill((255, 0, 255))
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


class Lazer_e(pygame.sprite.Sprite):
    def __init__(self):
        super(Lazer_e, self).__init__()
        self.sprite = pygame.Surface((45,10))
        self.sprite.fill((0,205,0))
        self.rect         = self.sprite.get_rect()
    
    def update(self, dir, s):
        """
        1: left
        2: right
        3: up
        4: down
        """
        if 1:
            self.rect.centerx -= s

        elif 2:
            self.rect.centerx += s

        elif 3:
            self.rect.centery -= s

        elif 4:
            self.rect.centery += s

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > width:
            self.rect.right = width
            bg._STORE.map1=True

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= height:
            self.rect.bottom = height

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


class Enemy_e(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy_e, self).__init__()
        self.sprite_img   = pygame.image.load("imgs/enemy/e.png").convert_alpha()
        self.sprite       = pygame.transform.scale(self.sprite_img, (width/1.5/1.5/1.5, height/1.5/1.5/1.5))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    def update(self, dir, s):
        """
        1: left
        2: right
        3: up
        4: down
        """
        if 1:
            self.rect.centerx -= s

        elif 2:
            self.rect.centerx += s

        elif 3:
            self.rect.centery -= s

        elif 4:
            self.rect.centery += s

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > width:
            self.rect.right = width

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= height:
            self.rect.bottom = height

class Enemy_m(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy_m, self).__init__()
        self.sprite_img   = pygame.image.load("imgs/enemy/m.png").convert_alpha()
        self.sprite       = pygame.transform.scale(self.sprite_img, (width/3/1.5, height/1.5/1.5))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    def update(self, dir, s):
        """
        1: left
        2: right
        3: up
        4: down
        """
        if 1:
            self.rect.centerx -= s

        elif 2:
            self.rect.centerx += s

        elif 3:
            self.rect.centery -= s

        elif 4:
            self.rect.centery += s
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > width:
            self.rect.right = width

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= height:
            self.rect.bottom = height


class Enemy_H(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy_H, self).__init__()
        self.sprite_img   = pygame.image.load("imgs/enemy/boss.png").convert_alpha()
        self.sprite       = pygame.transform.scale(self.sprite_img, (width/3/1.5, height/1.5/1.5))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    def update(self, dir, s):
        """
        1: left
        2: right
        3: up
        4: down
        """
        if dir == 1:
            self.rect.centerx -= s

        elif dir == 2:
            self.rect.centerx += s

        elif dir == 3:
            self.rect.centery -= s

        elif dir == 4:
            self.rect.centery += s

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > width:
            self.rect.right = width

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= height:
            self.rect.bottom = height


def _map1(h, player):
    e=Lazer_e()
    ee=Enemy_e()
    xx=screen.blit(ee.sprite, (142, player.rect.y))

    screen.blit(e.sprite, (bg._STORE.num1, ee.rect.centery-35))
    bg._STORE.num1 += 5

    screen.blit(e.sprite, (bg._STORE.num1, ee.rect.centery-35))
    bg._STORE.num1 += 5

    screen.blit(e.sprite, (bg._STORE.num1, ee.rect.centery-35))
    bg._STORE.num1 += 5


    x=screen.blit(e.sprite, (bg._STORE.num1, ee.rect.centery-35))
    bg._STORE.num1 += 20

    if xx.colliderect(player.rect):
        h.health=0
    
    if x.colliderect(player.rect):
        h.health-=5

    if x.right > width:
        bg._STORE.map1=True


    

def _map2(h):
    screen.blit(Enemy_m().sprite, Enemy_m().rect)


def _Boss(h):
    screen.blit(Enemy_H().sprite, Enemy_H().rect)

def generate_enemies(h, player):
    if   store.trc: return
    if   store.tlc:
        if bg._STORE.map1==False:
            _map1(h, player)
        elif bg._STORE.map1:
            bg.sprite.fill((255,255,255))

    
    elif store.blc:
        _map2(h)

    elif store.brc:
        _Boss(h)