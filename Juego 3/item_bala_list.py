import pygame
from constantes import *
from auxiliar import Auxiliar
from item_balas import*


class Item_bala_list:
    def __init__(self,cantidad=10,tiempo_spawn=15000) -> None:
        self.cantidad = cantidad
        self.lista_general = self.crear_item()# En esta lista se encuentran los enemigos no spawneados
        self.lista_draw = [] # En esta lista se almacenan los items spawneados
        self.tiempo_spawn = tiempo_spawn
        self.tiempo_transcurrido = 0

    def crear_item(self):
        return [Arma() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for

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

    def update(self,delta_ms,screen,player,objeto_item,plataform_list):
        self.item_spawn(delta_ms)
        self.encontrar_colision(objeto_item)
        for item in self.lista_draw:
            item.update(player,plataform_list,delta_ms)
            item.draw(screen)