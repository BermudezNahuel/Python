import pygame
from constantes import *
from auxiliar import Auxiliar
from items import *



class Lista_items:
    def __init__(self,cantidad,tiempo_spawn,item) -> None:
        self.cantidad = cantidad
        self.item = item
        self.lista_general = self.crear_item()# En esta lista se encuentran los enemigos no spawneados
        self.lista_draw = [] # En esta lista se almacenan los items spawneados
        self.tiempo_spawn = tiempo_spawn
        self.tiempo_transcurrido = 0

    def crear_item(self):
        return [self.item() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for

    def item_spawn(self,delta_ms):
        '''Saca enemigos de la lista_general y los agrega a la lista_draw, para esto tiene en cuenta un parametro de tiempo.'''
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido >= self.tiempo_spawn and self.lista_general:
            enemigo_nacido = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(enemigo_nacido)
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


####################################################################################


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
                vida_aparecida = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
                vida_aparecida.rect.x = enemy.head_collition_rect.x
                vida_aparecida.rect.y = enemy.head_collition_rect.y
                vida_aparecida.collition_rect.x = enemy.head_collition_rect.x + 10
                vida_aparecida.collition_rect.y = enemy.head_collition_rect.y
                #if enemy.direction == DIRECTION_L:
                vida_aparecida.rect.x += 15
                vida_aparecida.collition_rect.x += 15
                #else:
                #    vida_aparecida.rect.x += 50
                #    vida_aparecida.collition_rect.x -= 50
                self.lista_draw.append(vida_aparecida)


    def encontrar_colision(self,objeto_item):
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

###################################################################################

class Lista_drop_banana:
    def __init__(self,cantidad,item) -> None:
        self.cantidad = cantidad
        self.item = item
        self.lista_general = self.crear_item()# En esta lista se encuentran los enemigos no spawneados
        self.lista_draw = [] # En esta lista se almacenan los items spawneados
        self.tiempo_transcurrido = 0

    def crear_item(self):
        return [self.item() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for

    def item_spawn(self,delta_ms):
        '''Saca objetos de la lista_general y los agrega a la lista_draw, para esto tiene en cuenta un parametro de tiempo.'''
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido > 5000 and self.lista_general:
            self.tiempo_transcurrido = 0
            vida_aparecida = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(vida_aparecida)


    def encontrar_colision(self,objeto_item):
        '''Comprueba la lista_draw, si encuentra que el atributo booleano "eliminado", de un objeto, se encuentra en True, procede a remover al mismo de la lista'''
        for item in self.lista_draw:
            if item.eliminado:
                self.lista_draw.remove(item)
                #self.crear_item()


    def update(self,delta_ms,screen,player,objeto_item,platafor_list):
        self.item_spawn(delta_ms)
        self.encontrar_colision(objeto_item)
        for item in self.lista_draw:
            item.update(player,platafor_list,delta_ms)
            item.draw(screen)