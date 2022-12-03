import pygame
import random
from constantes import *
from auxiliar import Auxiliar
from master_gravedad import Gravedad

class Vida_box(Gravedad):
    def __init__(self,path,col,rows,y,x,gravity,frame_rate_ms,move_rate_ms) -> None:
        super().__init__(gravity, frame_rate_ms, move_rate_ms)
        self.objeto = Auxiliar.getSurfaceFromSpriteSheet(path,col,rows)
        self.frame = 0
        self.animation = self.objeto
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(x)
        self.rect.y = y
        self.rect.w = 15
        self.rect.h = 15
        self.rect.h = int(self.rect.h/3)
        self.collition_rect = pygame.Rect(self.rect.x+10,self.rect.y+5+self.rect.h,15,15)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.y += 10
        self.ground_collition_rect.height = GROUND_COLLIDE_H

        self.eliminado = False
        self.gravity = gravity
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

#-------------------------------------------------------------------------------------------

class Item_vida_box_list:
    def __init__(self,lista) -> None:
        self.lista_general = lista
        self.lista_draw = []
        self.tiempo_transcurrido = 0


    def item_spawn(self,delta_ms):
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido > 15000 and self.lista_general:
            self.tiempo_transcurrido = 0
            item = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(item)

    def encontrar_colision(self):
        for item in self.lista_draw:
            if item.eliminado:
                self.lista_draw.remove(item)

    def update(self,delta_ms,screen,player,platafor_list):
        self.item_spawn(delta_ms)
        self.encontrar_colision()
        for item in self.lista_draw:
            item.update(player,platafor_list,delta_ms)
            item.draw(screen)