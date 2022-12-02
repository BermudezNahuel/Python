import pygame
from constantes import *
from auxiliar import Auxiliar
from items import *


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
