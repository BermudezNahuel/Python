import pygame
from constantes import *
import random




class Lista_walkers:
    def __init__(self,lista,metodo) -> None:
        self.metodo = metodo
        self.lista_general = lista
        self.lista_draw = [] # En esta lista se almacenan los enemigos spawneados
        self.tiempo_spawn = 5000
        self.tiempo_transcurrido = 0
        self.primera = True
        self.bandera_primero = True

    '''
    def crear_enemigos(self):
        return [() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for
    
    
    def recargar_enemigos(self,jefe):
        #if jefe.lista_draw:
            if len(self.lista_draw) < self.cantidad:
                self.crear_enemigos()
    '''
    
    def enemigo_spawn(self,delta_ms):
        '''Saca enemigos de la lista_general y los agrega a la lista_draw, para esto tiene en cuenta un parametro de tiempo.'''
        if self.primera:
            enemigo_nacido = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(enemigo_nacido)
            self.primera = False
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido >= self.tiempo_spawn and self.lista_general:
            enemigo_nacido = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            enemigo_nacido.direction = random.choice([DIRECTION_L,DIRECTION_R])
            self.lista_draw.append(enemigo_nacido)
            self.tiempo_transcurrido = 0

    def encontrar_colision(self):
        '''Comprueba la lista_draw, si encuentra que el atributo booleano "eliminado", de un objeto, se encuentra en True, procede a remover al mismo de la lista'''
        for enemigo in self.lista_draw:
            if enemigo.eliminado:
                self.lista_draw.remove(enemigo)

    def recargar(self):
        if not self.lista_general:#pregunto si la lista esta vacia
            self.lista_general = self.metodo()

    def update(self,bala,delta_ms,plataform_list,player,border_r,borde_l,jefe):
        '''
        if self.bandera_primero:
            self.crear_enemigo_dos()
            self.bandera_primero = False
        '''
        self.enemigo_spawn(delta_ms)
        self.encontrar_colision()
        self.recargar()
        for enemigo in self.lista_draw:
            enemigo.update(delta_ms,plataform_list,bala,player,border_r,borde_l)
            
    def draw(self,screen):
        for enemigo in self.lista_draw:
            enemigo.draw(screen)


class Lista_jefe:
    def __init__(self,cantidad,tiempo_spawn,enemigo) -> None:
        self.cantidad = cantidad
        self.lista_general = self.crear_enemigos(enemigo)# En esta lista se encuentran los enemigos no nacidos
        self.lista_draw = [] # En esta lista se almacenan los enemigos spawneados
        self.tiempo_spawn = tiempo_spawn
        self.tiempo_transcurrido = 0
        self.primera = True
        self.bandera_primero = True

    
    def crear_enemigos(self,enemigo):
        return [enemigo() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for

    def enemigo_spawn(self,delta_ms):
        '''Saca enemigos de la lista_general y los agrega a la lista_draw, para esto tiene en cuenta un parametro de tiempo.'''
        
        if self.primera:
            enemigo_nacido = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(enemigo_nacido)
            self.primera = False
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido >= self.tiempo_spawn and self.lista_general:
            enemigo_nacido = self.lista_general.pop(0)# elimino el primer elemento de la lista, y los almaceno en enemigo nacido
            self.lista_draw.append(enemigo_nacido)
            self.tiempo_transcurrido = 0

    def encontrar_colision(self):
        '''Comprueba la lista_draw, si encuentra que el atributo booleano "eliminado", de un objeto, se encuentra en True, procede a remover al mismo de la lista'''
        for enemigo in self.lista_draw:
            if enemigo.eliminado:
                self.lista_draw.remove(enemigo)

    def update(self,bala,delta_ms,plataform_list,screen,player):
        self.enemigo_spawn(delta_ms)
        self.encontrar_colision()
        for enemigo in self.lista_draw:
            enemigo.update(delta_ms,plataform_list,bala,player)
            enemigo.draw(screen)
