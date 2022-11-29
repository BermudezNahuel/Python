import pygame
import random
from constantes import *
from auxiliar import Auxiliar
from master_gravedad import Gravedad

class Arma(Gravedad):
    def __init__(self,x=300,y=575, gravity=10, frame_rate_ms=100, move_rate_ms=50) -> None:
        super().__init__(gravity, frame_rate_ms, move_rate_ms)
        self.objeto = Auxiliar.getSurfaceFromSpriteSheet("PIXEL ADVENTURE\Recursos/estrella.png",columnas=1,filas=1,scale=0.1)
        self.animation = self.objeto
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([100,200,300,400,500,600,700,800,900])
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
    
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,color=WHITE,rect=self.collition_rect)
            pygame.draw.rect(screen,color=RED,rect=self.ground_collition_rect)
        screen.blit(self.image,self.rect)


    def update(self,player,plataform_list,delta_ms):
        self.colision(player)
        self.do_animation(delta_ms)
        self.is_on_plataform(plataform_list)
        self.do_movement(delta_ms,plataform_list)



class Manzana(Gravedad):
    def __init__(self,x=100,y=300, gravity=5, frame_rate_ms=100, move_rate_ms=50) -> None:
        super().__init__(gravity, frame_rate_ms, move_rate_ms)

        self.objeto = Auxiliar.getSurfaceFromSpriteSheet("PIXEL ADVENTURE\Recursos\Items\Fruits\Apple.png",columnas=17,filas=1)
        self.frame = 0
        self.animation = self.objeto
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.h = int(self.rect.h/3)
        self.collition_rect = pygame.Rect(x,y-self.rect.h,15,15)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.y -= 10
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        
        
        
        self.gravity = 14
        self.move_y = 0
    
        self.eliminado = False
        self.mostrar_item = True


    def colision(self,player):
        if self.collition_rect.colliderect(player.collition_rect):
            self.eliminado = True
            player.aumentar_vida = True
            player.carga_de_vida = 1

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,color=WHITE,rect=self.collition_rect)
            pygame.draw.rect(screen,color=RED,rect=self.ground_collition_rect)
        screen.blit(self.image,self.rect)
    
    def update(self,player,plataform_list,delta_ms):
        self.colision(player)
        self.do_animation(delta_ms)
        self.is_on_plataform(plataform_list)
        self.do_movement(delta_ms,plataform_list)


class Banana(Gravedad):
    def __init__(self,x=200,y=0,gravity=10, frame_rate_ms=100, move_rate_ms=50) -> None:
        super().__init__(gravity, frame_rate_ms, move_rate_ms)
        self.objeto = Auxiliar.getSurfaceFromSpriteSheet("PIXEL ADVENTURE\Recursos\Items\Fruits\Bananas.png",columnas=17,filas=1)
        self.frame = 0
        self.animation = self.objeto
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = 15
        self.rect.h = 15
        self.mostrar_item = True
        self.rect.h = int(self.rect.h/3)
        self.collition_rect = pygame.Rect(x+10,y+5+self.rect.h,15,15)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.y += 10
        self.ground_collition_rect.height = GROUND_COLLIDE_H

        self.eliminado = False
        self.gravity = 5
        self.move_y = 0


    def colision(self,player):
        if self.collition_rect.colliderect(player.ground_collition_rect):
            self.eliminado = True
            player.aumentar_vida = True
            player.carga_de_vida = 1
            

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,color=WHITE,rect=self.collition_rect)
        screen.blit(self.image,self.rect)
    
    def update(self,player,plataform_list,delta_ms):
        self.colision(player)
        self.do_animation(delta_ms)
        self.is_on_plataform(plataform_list)
        self.do_movement(delta_ms,plataform_list)

