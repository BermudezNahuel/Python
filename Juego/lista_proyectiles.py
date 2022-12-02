import pygame
from constantes import *

class Lista_proyectiles:
    def __init__(self,metodo,lista_1) -> None:
        self.metodo = metodo
        self.lista_general = lista_1
        print(len(self.lista_general))

        self.lista_draw = [] # En esta lista se almacenan las balas disparas
        self.ubicacion_inicial = False
        self.speed = 5
        self.direccion_disparo = DIRECTION_R
        self.tiempo_transcurrido = 0

    
    def cargar_lista_general(self):
        self.lista_general = self.metodo()
        print("se ejecuta cargar_lista general")
        #self.crear_lista
        #print(len(self.crear_lista))
    
        

    def obtener_bala_disparada(self,player):
        if self.ubicacion_inicial and self.lista_general:
            #Dentro de este condicional se actualizan la ubicacion y la direccion de la bala,hasta que esta se dispara
            bala_disparada = self.lista_general.pop(0)# Se elimina el objeto que se encuentra en el indice 0, y se lo asigna a la variable bala_disparada
            bala_disparada.direccion = player.direction
            bala_disparada.rect.x = int((player.rect.w/2) + player.rect.x)
            bala_disparada.collition_rect.x = int((player.rect.w/2) + player.rect.x)
            bala_disparada.rect.y = player.rect.y + 15
            bala_disparada.collition_rect.y =  player.rect.y + bala_disparada.rect.h + 15
            self.lista_draw.append(bala_disparada)
            self.ubicacion_inicial = False
    

    
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
                    
    
    def recargar(self):
        self.cargar_lista_general()
    
    


    def event(self,lista_eventos,delta_ms):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s and self.lista_general:
                    self.tiempo_transcurrido += delta_ms
                    if self.tiempo_transcurrido > 100:
                        self.tiempo_transcurrido = 0
                    self.ubicacion_inicial = True
                if evento.key == pygame.K_w:
                    self.recargar()
                    

    def update(self,player):
        self.obtener_bala_disparada(player)
        self.mover_bala()
        self.update_lista_draw()


    def draw(self,screen):
        for bala in self.lista_draw:
            if DEBUG:
                pygame.draw.rect(screen,color=(BLACK),rect=bala.collition_rect)
            screen.blit(bala.image,bala.rect)
