import pygame
import random
from constantes import *
from auxiliar import Auxiliar
from master_gravedad import Gravedad

class Bala(Gravedad):
    def __init__(self,path,col,rows,scale,x,y,gravity,frame_rate_ms,move_rate_ms) -> None:
        super().__init__(gravity, frame_rate_ms, move_rate_ms)
        self.scale=scale
        self.objeto = Auxiliar.getSurfaceFromSpriteSheet(path,col,rows,scale=self.scale)
        self.animation = self.objeto
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(x)
        self.rect.y = y
        self.mostrar_item = True
        self.rect.h = int(self.rect.h/3)
        self.collition_rect = pygame.Rect(self.rect.x+5,self.rect.y + self.rect.h,15,15)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.y += 10
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        #self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        
        self.eliminado = False
        self.gravity = 14
        self.move_y = 0
    
    def colision(self,player):
        if self.collition_rect.colliderect(player.collition_rect):
            self.eliminado = True
    


    def update(self,player,plataform_list,delta_ms):
        self.colision(player)
        self.do_animation(delta_ms)
        self.is_on_plataform(plataform_list)
        self.do_movement(delta_ms,plataform_list)

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,color=WHITE,rect=self.collition_rect)
            pygame.draw.rect(screen,color=RED,rect=self.ground_collition_rect)
        screen.blit(self.image,self.rect)