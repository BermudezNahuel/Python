import pygame
import random
from constantes import *
from auxiliar import Auxiliar
from master_gravedad import Gravedad

class Item_bala(Gravedad):
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
        '''
        Actualiza los metodos propios de la clase
        '''
        self.colision(player)
        self.do_animation(delta_ms)
        self.is_on_plataform(plataform_list)
        self.do_movement(delta_ms,plataform_list)

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,color=WHITE,rect=self.collition_rect)
            pygame.draw.rect(screen,color=RED,rect=self.ground_collition_rect)
        screen.blit(self.image,self.rect)

#-------------------------------------------------------------------------------------------


class Item_bala_list:
    def __init__(self,lista) -> None:
        self.lista_general = lista# En esta lista se encuentran los enemigos no spawneados
        self.lista_draw = [] # En esta lista se almacenan los items spawneados
        self.tiempo_spawn = 15000
        self.tiempo_transcurrido = 0


    def item_spawn(self,delta_ms):
        '''Saca enemigos de la lista_general y los agrega a la lista_draw, para esto tiene en cuenta un parametro de tiempo.'''
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido >= self.tiempo_spawn and self.lista_general:
            item = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(item)
            self.tiempo_transcurrido = 0

    def encontrar_colision(self,objeto_item):
        '''Comprueba la lista_draw, si encuentra que el atributo booleano "eliminado", de un objeto, se encuentra en True, procede a remover al mismo de la lista'''
        for item in self.lista_draw:
            if item.eliminado:
                self.lista_draw.remove(item)
                objeto_item.recargar()

    def update(self,delta_ms,player,objeto_item,plataform_list):
        self.item_spawn(delta_ms)
        self.encontrar_colision(objeto_item)
        for item in self.lista_draw:
            item.update(player,plataform_list,delta_ms)

    
    def draw(self,screen):
        for item in self.lista_draw:
            item.draw(screen)