import pygame
from   pygame.locals  import *
from   initial_screen import deminsions
#from   background     import bg 
width = deminsions[0]
height = deminsions[1]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sprite_img   = pygame.image.load("imgs/up1.png").convert_alpha()
        self.sprite       = pygame.transform.scale(self.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    # Move the sprite based on user keypresses
    def update(self, keyinput):
        if keyinput[K_LEFT]:
            self.rect.centerx -= 2
            pd=Player_direction(4)

        elif keyinput[K_RIGHT]:
            self.rect.centerx += 2
            pd=Player_direction(3)

        elif keyinput[K_UP]:
            self.rect.centery -= 2
            pd=Player_direction(1)

        elif keyinput[K_DOWN]:
            self.rect.centery += 2
            pd=Player_direction(2)
        elif keyinput[K_SPACE]:
            pd=1
        else:
            pd=Player_direction(0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height
        
        if pd!=1:
            pd.update()
        else:
            self.fire() 
    
    def fire(self):
        pass

player=Player()
class Player_direction():
    """
    dir 1: up
    dir 2: down
    dir 3: right
    dir 4: left
    """
    def __init__(self, dir: int):
        super(Player_direction, self).__init__()
        if dir==1:
            self.up=True;self.down=False;self.right=False;self.left=False

        elif dir==2:
            self.up=False;self.down=True;self.right=False;self.left=False

        elif dir==3:
            self.up=False;self.down=False;self.right=True;self.left=False

        elif dir==4:
            self.up=False;self.down=False;self.right=False;self.left=True

        else:
            self.up=False;self.down=False;self.right=False;self.left=False

    def update(self):
        p=player
        if _STORE.up2==False and self.up:
            _STORE.x=0
            p.sprite_img   = pygame.image.load("imgs/up1.png").convert_alpha()
            p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            _STORE.up2=True; _STORE.down2=False; _STORE.right2=False; _STORE.left2=False

        elif _STORE.up2 and self.up:
            _STORE.x=_STORE.x+1
            if _STORE.x>10 and _STORE.x <20:
                p.sprite_img   = pygame.image.load("imgs/up1.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x<=5:
                p.sprite_img   = pygame.image.load("imgs/up2.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x > 25:
                _STORE.up2=False; _STORE.down2=False; _STORE.right2=False; _STORE.left2=False


        elif _STORE.down2==False and self.down:
            _STORE.x=0
            p.sprite_img   = pygame.image.load("imgs/down1.png").convert_alpha()
            p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            _STORE.up2=False; _STORE.down2=True; _STORE.right2=False; _STORE.left2=False

        elif _STORE.down2 and self.down:
            _STORE.x=_STORE.x+1
            if _STORE.x>10 and _STORE.x <20:
                p.sprite_img   = pygame.image.load("imgs/down1.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x<=5:
                p.sprite_img   = pygame.image.load("imgs/down2.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x > 25:
                _STORE.up2=False; _STORE.down2=False; _STORE.right2=False; _STORE.left2=False

        elif _STORE.right2==False and self.right:
            _STORE.x=0
            p.sprite_img   = pygame.image.load("imgs/right1.png").convert_alpha()
            p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            _STORE.up2=False; _STORE.down2=False; _STORE.right2=True; _STORE.left2=False


        elif _STORE.right2 and self.right:
            _STORE.x=_STORE.x+1
            if _STORE.x>10 and _STORE.x <20:
                p.sprite_img   = pygame.image.load("imgs/right1.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x<=5:
                p.sprite_img   = pygame.image.load("imgs/right2.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x > 25:
                _STORE.up2=False; _STORE.down2=False; _STORE.right2=False; _STORE.left2=False

        elif _STORE.left2==False and self.left:
            _STORE.x=0
            p.sprite_img   = pygame.image.load("imgs/left1.png").convert_alpha()
            p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            _STORE.up2=False; _STORE.down2=False; _STORE.right2=False; _STORE.left2=True


        elif _STORE.left2 and self.left:
            _STORE.x=_STORE.x+1
            if _STORE.x>10 and _STORE.x <20:
                p.sprite_img   = pygame.image.load("imgs/left1.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x<=5:
                p.sprite_img   = pygame.image.load("imgs/left2.png").convert_alpha()
                p.sprite       = pygame.transform.scale(p.sprite_img, (width/3/1.5/1.5, height/1.5/1.5/1.5))
            elif _STORE.x > 25:
                _STORE.up2=False; _STORE.down2=False; _STORE.right2=False; _STORE.left2=False



class _STORE:
    x=0
    up2=False
    down2=False
    right2=False
    left2=False
