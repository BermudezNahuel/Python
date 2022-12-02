import pygame
from constantes import *
from auxiliar import Auxiliar

class Cargador_enemy:
    def __init__(self,lista) -> None:
        self.cantidad = 5
        self.lista = lista
        self.lista_draw = [] # En esta lista se almacenan las balas disparas
        print(len(self.lista))
        self.ubicacion_inicial = False
        self.speed = 3
        self.direccion_disparo = DIRECTION_R
        self.tiempo_transcurrido = 0
    
    '''
    def crear_balas(self):
        return [Proyectil() for i in range(self.cantidad)] #Genera una lista en una sola lista usando un for
    '''

    def obtener_bala_disparada(self,enemigos):
        for enemy in enemigos.lista_draw:
            if enemy.disparar and self.lista:
                #Dentro de este condicional se actualizan la ubicacion y la direccion de la bala,hasta que esta se dispara
                bala_disparada = self.lista.pop(0)# Se elimina el objeto que se encuentra en el indice 0, y se lo asigna a la variable bala_disparada
                bala_disparada.direccion = enemy.direction
                bala_disparada.rect.x = int((enemy.rect.w/2) + enemy.rect.x)
                bala_disparada.collition_rect.x = int((enemy.rect.w/2) + enemy.rect.x)
                bala_disparada.rect.y = enemy.rect.y + 15
                bala_disparada.collition_rect.y =  enemy.rect.y + bala_disparada.rect.h + 15
                self.lista_draw.append(bala_disparada)
                enemy.disparar = False
    
    def mover_bala(self):
        for bala in self.lista_draw:
            if bala.direccion == DIRECTION_R:
                bala.rect.x += self.speed
                bala.collition_rect.x += self.speed
            else:
                bala.rect.x -= self.speed
                bala.collition_rect.x -= self.speed

    def update_lista_draw(self):   
        for bala in self.lista_draw:
                if (bala.rect.x > ANCHO_VENTANA or bala.rect.x < 0 or bala.eliminada):
                    self.lista_draw.remove(bala)#se elimina la bala

    '''
    def recargar(self):
        if not self.lista:#pregunto si la lista esta vacia
            self.lista = 
    '''


    def update(self,enemigos,delta_ms):
        #self.recargar(lista_recarga)
        self.obtener_bala_disparada(enemigos)
        self.mover_bala()
        self.update_lista_draw()



    def draw(self,screen):
        for bala in self.lista_draw:
            if DEBUG:
                pygame.draw.rect(screen,color=(BLACK),rect=bala.collition_rect)
            screen.blit(bala.image,bala.rect)