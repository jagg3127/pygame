import pygame
from   initial_screen          import screen, deminsions
from   entities.background     import bg
store=bg._STORE
width = deminsions[0]
height = deminsions[1]


class Lazer_e(pygame.sprite.Sprite):
    def __init__(self):
        super(Lazer_e, self).__init__()
        self.sprite = pygame.Surface((45,10))
        self.sprite.fill((0,205,0))
        self.rect         = self.sprite.get_rect()

class Lazer_m(pygame.sprite.Sprite):
    def __init__(self):
        super(Lazer_m, self).__init__()
        self.sprite = pygame.Surface((60,9))
        self.sprite.fill((255,255,0))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    def update(self, dir, s, tp, m):
        """
        1: left
        2: up
        3: right
        4: down
        """

        if not map22.one:
            self.sprite = pygame.Surface((55,10))
            self.sprite.fill((255,255,0))  
            self.rect         = self.sprite.get_rect()
            if m.u:
                tp.rot_center(90)
                m.u=False
    
            while not self.rect.left < 0:
                self.rect.centerx -= s
            else:
                self.rect.left = 0
                self.sprite = None
                self.rect   = None
                map22.m=Lazer_m()
                map22.mm=Enemy_m()
            
            map22.one=True
        
        elif not map22.two:
                
        
            self.sprite = pygame.Surface((55,10))
            self.sprite.fill((255,255,0))
            self.rect         = self.sprite.get_rect()
            while not self.rect.right > width:
                self.rect.centerx += s
            else:    
                self.rect.right = width
                self.sprite = None
                self.rect   = None
                map22.m=Lazer_m()
                map22.mm=Enemy_m()

            map22.two=True

        self.sprite = pygame.Surface((10,55))
        self.sprite.fill((255,255,0))
        self.rect         = self.sprite.get_rect()
        self.rect.centery -= s

        self.sprite = pygame.Surface((10,55))
        self.sprite.fill((255,255,0))
        self.rect.centery += s

        if self.rect.right > width:
            self.rect.right = width
            self.sprite = None
            self.rect   = None
            return True

        if self.rect.top <= 0:
            self.rect.top = 0
            self.sprite = None
            self.rect   = None
            return True

        if self.rect.bottom >= height:
            self.rect.bottom = height
            self.sprite = None
            self.rect   = None
            return True
        
        return False

    

        return rotated_image, new_rect
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
        
    def rot_center(self, angle):
        rotated_image = pygame.transform.rotate(self.sprite_img, angle)
        new_rect = rotated_image.get_rect(center = self.rect.center)
        self.sprite_img=rotated_image; self.sprite=pygame.transform.scale(self.sprite_img, (width/3/1.5, height/1.5/1.5)); self.rect= new_rect


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

    screen.blit(e.sprite, (bg._STORE.num1, ee.rect.centery-40))
    bg._STORE.num1 += 5

    screen.blit(e.sprite, (bg._STORE.num1, ee.rect.centery-35))
    bg._STORE.num1 += 5

    screen.blit(e.sprite, (bg._STORE.num1, ee.rect.centery-30))
    bg._STORE.num1 += 5


    x=screen.blit(e.sprite, (bg._STORE.num1, player.rect.centery))
    bg._STORE.num1 += 25

    if xx.colliderect(player.rect):
        h.health=0
    
    if x.colliderect(player.rect):
        h.health-=5

    if x.right > width-330:
        bg._STORE.map1=True


class map22:
    m=Lazer_m()
    mm=Enemy_m()
    r=1
    u=True
    one=False
    two=False
    three=False
    four=False

def _map2(h):
    mm=map22.mm
    m=map22.m
    screen.blit(mm.sprite, mm.rect)
    screen.blit(m.sprite, m.rect)
    x=m.update(map22.r, 6, mm, map22)
    if x:
        map22.m=Lazer_m()
        map22.mm=Enemy_m()
        if map22.r >= 4: map22.r=1
        else:            map22.r+=1

        

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