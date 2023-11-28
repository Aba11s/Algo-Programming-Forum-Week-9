# Try it urself chapter 12-14


import pygame as pg
from sys import exit

from sprites import Rocket

# Fund the mentals
pg.init()
screen = pg.display.set_mode((1200,600))
pg.display.set_caption("Nuke simulator")
clock = pg.time.Clock()
running = True

# Settings

background = pg.Surface((1200,600))
background.fill((0,0,255))


rocket = Rocket(screen,1200,600)
# Main loop

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                rocket.velocity = 12
            
            if event.key == pg.K_a:
                rocket.move_left = True
            if event.key == pg.K_d:
                rocket.move_right = True
            if event.key == pg.K_w:
                rocket.move_up = True
            if event.key == pg.K_s:
                rocket.move_down = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                rocket.velocity = 6

            if event.key == pg.K_a:
                rocket.move_left = False
            if event.key == pg.K_d:
                rocket.move_right = False
            if event.key == pg.K_w:
                rocket.move_up = False
            if event.key == pg.K_s:
                rocket.move_down = False


    # blit
    screen.blit(background,(0,0))

    rocket.blitme()

    clock.tick(60)
    pg.display.flip()

    

