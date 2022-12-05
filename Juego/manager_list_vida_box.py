import pygame

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

    def update(self,delta_ms,player,platafor_list):
        self.item_spawn(delta_ms)
        self.encontrar_colision()
        for item in self.lista_draw:
            item.update(player,platafor_list,delta_ms)

    def draw(self,screen):
        for item in self.lista_draw:
            item.draw(screen)