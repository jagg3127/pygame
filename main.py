import pygame 
from   pygame.locals  import *
from   initial_screen import x, screen, deminsions
from   entities.players        import player, health, _STORE, direct
from   entities.background     import bg
from   entities.enemy          import generate_enemies, Lazer
ALL=[player]
lazer  = Lazer()
width  = deminsions[0]
height = deminsions[1]
white  = (255, 255, 255)

for item in ALL:
    screen.blit(item.sprite, item.rect)

pygame.display.flip()

while _STORE.run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();break

    screen.blit(bg.sprite, bg.rect)
    keyinput = pygame.key.get_pressed()
    
    health.check_health()
    player.update(keyinput)


    for item in ALL:
        screen.blit(item.sprite, item.rect)
    pygame.draw.rect(screen, (255, 0, 0), screen.get_rect(), 3)
    player.draw_health(screen)
    

        
    # update display
    pygame.display.flip()








while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();break
    
    sprite_img   = pygame.image.load("imgs/dead.png").convert_alpha()
    sprite       = pygame.transform.scale(sprite_img, screen.get_size())
    rect         = sprite.get_rect()
    rect.centerx = (width//2)
    rect.centery = (height//2)
    screen.blit(sprite, rect)
    pygame.display.flip()
