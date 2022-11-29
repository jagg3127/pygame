import pygame
from   pygame.locals  import *
from   initial_screen import screen, deminsions
width = deminsions[0]
height = deminsions[1]

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        """self.sprite_img   = pygame.image.load("imgs/up1.png").convert_alpha()
        self.sprite       = pygame.transform.scale(self.sprite_img, screen.get_size())"""
        self.sprite = pygame.Surface(screen.get_size())
        self.sprite.fill((255, 255, 255))
        self.rect         = self.sprite.get_rect()
        self.rect.centerx = (width//2)
        self.rect.centery = (height//2)
    
    # Move the sprite based on user keypresses
    def update(self):
        pass

    class _STORE:
        trc=True
        tlc=False
        brc=False
        blc=False
        main=0
        num1=426
        map1=False
        map2=False

    class move:
        def left(player):
            store= bg._STORE; trc=store.trc;tlc=store.tlc;brc=store.brc;blc=store.blc
            player.rect.centerx = (width-mv)
            if trc:
                store.tlc=True
                store.trc=False
                if store.map1==False:
                    bg.sprite.fill(TLC)
                else:
                    bg.sprite.fill(TRC)


            elif brc:
                store.blc=True
                store.brc=False
                bg.sprite.fill(BLC)
        
        def right(player):
            store= bg._STORE; trc=store.trc;tlc=store.tlc;brc=store.brc;blc=store.blc
            player.rect.centerx = mv
            if tlc:
                store.trc=True
                store.tlc=False
                bg.sprite.fill(TRC)
            
            elif blc:
                store.brc=True
                store.blc=False
                bg.sprite.fill(BRC)

        def up(player):
            store= bg._STORE;brc=store.brc;blc=store.blc
            player.rect.centery = (height-mvu)
            if brc:
                store.trc=True
                store.blc=False
                bg.sprite.fill(TRC)

            elif blc:
                store.tlc=True
                store.blc=False
                bg.sprite.fill(TLC)

        def down(player):
            store= bg._STORE; trc=store.trc;tlc=store.tlc
            player.rect.centery = mvu
            if tlc:
                store.blc=True
                store.tlc=False
                bg.sprite.fill(BLC)

            elif trc:
                store.brc=True
                store.trc=False
                bg.sprite.fill(BRC)

TRC=(255, 255, 255)
TLC=(0, 0, 0)
BRC=(0, 255, 255)
BLC=(255, 0, 255)

mv=142
mvu=161
bg=Background()