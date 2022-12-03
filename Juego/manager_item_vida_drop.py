import pygame
import random
from constantes import *
from auxiliar import Auxiliar
from master_gravedad import Gravedad


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

#----------------------------------------------------------------------------------------------------------

class Lista_spawn_life:
    def __init__(self,cantidad,item) -> None:
        self.cantidad = cantidad
        self.item = item
        self.lista_general = self.crear_item()# En esta lista se encuentran los enemigos no spawneados
        self.lista_draw = [] # En esta lista se almacenan los items spawneados
        self.tiempo_transcurrido = 0

    def crear_item(self):
        return [self.item() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for

    def item_spawn(self,enemigo):
        '''Saca enemigos de la lista_general y los agrega a la lista_draw, para esto tiene en cuenta un parametro de tiempo.'''
        for enemy in enemigo.lista_draw:
            if enemy.eliminado and self.lista_general:
                item = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
                item.rect.x = enemy.head_collition_rect.x
                item.rect.y = enemy.head_collition_rect.y
                item.collition_rect.x = enemy.head_collition_rect.x + 10
                item.collition_rect.y = enemy.head_collition_rect.y
                item.rect.x += 15
                item.collition_rect.x += 15

                self.lista_draw.append(item)


    def encontrar_colision(self):
        '''Comprueba la lista_draw, si encuentra que el atributo "eliminado", de un objeto se encuentra en True, removu al objeto de la lista_draw'''
        for item in self.lista_draw:
            if item.eliminado:
                self.crear_item()
                self.lista_draw.remove(item)
                

    def update(self,delta_ms,screen,player,objeto_item,enemigo,platafor_list):
        self.item_spawn(enemigo)
        self.encontrar_colision(objeto_item)
        for item in self.lista_draw:
            item.update(player,platafor_list,delta_ms)
            item.draw(screen)
