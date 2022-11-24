import pygame 
from   pygame.locals  import *
from   players        import player
from   initial_screen import x, screen, deminsions
from   imports.ss     import spritesheet

import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
from imports.mainanim import SpriteStripAnim

surface = pygame.display.set_mode((100,100))
FPS = 120
frames = FPS / 12
strips = []
for x in range(0, 18):
    print(x)
"""
black = Color('black')
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = strips[n].next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()
            elif e.key == K_RETURN:
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter()
    surface.fill(black)
    surface.blit(image, (0,0))
    pygame.display.flip()
    image = strips[n].next()
    clock.tick(FPS)
"""