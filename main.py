import pygame 
from   pygame.locals  import *
from   initial_screen import x, screen, deminsions
from   players        import player

width = deminsions[0]
height = deminsions[1]

white = (255, 255, 255)
background = pygame.Surface(screen.get_size())
background.fill(white)

screen.blit(background, (0, 0))
screen.blit(player.sprite, player.rect)

pygame.display.flip()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();break

    keyinput = pygame.key.get_pressed()
    
    player.update(keyinput)

    screen.blit(background, (0,0))
    screen.blit(player.sprite, player.rect)
    # update display
    pygame.display.flip()