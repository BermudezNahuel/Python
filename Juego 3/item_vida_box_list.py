import pygame
from constantes import *
from auxiliar import Auxiliar
from items import *
from item_vida_box import*

class Item_vida_box_list:
    def __init__(self,cantidad = 20) -> None:
        self.cantidad = cantidad
        self.lista_general = self.crear_item()
        self.lista_draw = []
        self.tiempo_transcurrido = 0

    def crear_item(self):
        return [Banana() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for

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