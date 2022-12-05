import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigo_shooter import Enemigo_shooter




class Lista_shooters:
    def __init__(self,lista) -> None:
        self.lista_general = lista
        self.lista_draw = [] # En esta lista se almacenan los enemigos spawneados
        self.tiempo_transcurrido = 0


    def cargar_lista_spawn(self):
        if self.lista_general:
            enemigo_nacido = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(enemigo_nacido)

    def buscar_colision(self):
        '''Comprueba la lista_draw, si encuentra que el atributo booleano "eliminado", de un objeto, se encuentra en True, procede a remover al mismo de la lista'''
        for enemigo in self.lista_draw:
            if enemigo.eliminado:
                self.lista_draw.remove(enemigo)

    def update(self,bala,delta_ms,plataform_list,player):
        self.cargar_lista_spawn()
        self.buscar_colision()
        for enemigo in self.lista_draw:
            enemigo.update(delta_ms,plataform_list,bala,player)
                 
    def draw(self,screen):
        for enemigo in self.lista_draw:
            enemigo.draw(screen)