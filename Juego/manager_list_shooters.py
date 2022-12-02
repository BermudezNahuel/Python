import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigo_shooter import Enemigo_shooter




class Lista_shooters:
    def __init__(self,lista) -> None:
        self.lista_general = lista
        self.lista_draw = [] # En esta lista se almacenan los enemigos spawneados
        self.tiempo_transcurrido = 0
        #self.crear_enemigos()

    '''
    def crear_enemigos(self):
        for i in range(3):
            self.eje_y += 150
            self.eje_x += 0
            self.lista_general.append(Enemigo_shooter(  x=es_l["x"],
                                                        y=es_l["y"]+self.eje_y,
                                                        direction=es_l["direction"],
                                                        path=es_l["path"],
                                                        columnas=es_l["columnas"],
                                                        filas=es_l["filas"],
                                                        flip=es_l["flip"]))
            self.lista_general.append(Enemigo_shooter(  x=es_r["x"],
                                                        y=es_r["y"]+self.eje_y,
                                                        direction=es_r["direction"],
                                                        path=es_r["path"],
                                                        columnas=es_r["columnas"],
                                                        filas=es_r["filas"],
                                                        flip=es_r["flip"]))
        return self.lista_general
    '''

    def cargar_lista_spawn(self):
        if self.lista_general:
            enemigo_nacido = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(enemigo_nacido)

    def buscar_colision(self):
        '''Comprueba la lista_draw, si encuentra que el atributo booleano "eliminado", de un objeto, se encuentra en True, procede a remover al mismo de la lista'''
        for enemigo in self.lista_draw:
            if enemigo.eliminado:
                self.lista_draw.remove(enemigo)

    def fundir_en_pantalla(self,bala,delta_ms,plataform_list,screen,player):
        for enemigo in self.lista_draw:
            enemigo.update(delta_ms,plataform_list,bala,player)
            enemigo.draw(screen)

    def update(self,bala,delta_ms,plataform_list,screen,player):
        self.cargar_lista_spawn()
        self.buscar_colision()
        self.fundir_en_pantalla(bala,delta_ms,plataform_list,screen,player)