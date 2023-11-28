#classes

import pygame as pg 

class Rocket: #Its a rectangle
    def __init__(self,screen,width,height):
        self.screen = screen
        self.image = pg.image.load("rocket.png")
        self.image = pg.transform.scale(self.image, (200,85))

        self.rect = self.image.get_rect()
        self.s_width = width
        self.s_heigth = height
        self.rect.center = (self.s_width//2,self.s_heigth//2)
        self.color = (255,255,255)

        self.velocity = 6
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def check_for_edge(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.s_width:
            self.rect.right = self.s_width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.s_heigth:
            self.rect.bottom = self.s_heigth

    def update_position(self):
        if self.move_left == True:
            self.rect.x -= self.velocity
        if self.move_right == True:
            self.rect.right += self.velocity
        if self.move_up == True:
            self.rect.top -= self.velocity
        if self.move_down == True:
            self.rect.bottom += self.velocity

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
        self.update_position()
        self.check_for_edge()

        
