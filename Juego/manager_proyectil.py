import pygame
from constantes import *
from auxiliar import Auxiliar


class Proyectil:
    def __init__(self,path,h,w,speed) -> None:
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        #self.mostrar_bala = True
        self.rect.h = int(self.rect.h/3)
        self.speed = speed
        self.collition_rect = pygame.Rect(self.rect.x,self.rect.y+self.rect.h-3,8,8)
        self.eliminada = False
        self.direccion = DIRECTION_R


#--------------------------------------------------------------------------------------------------------------

class Cargador_player:
    def __init__(self,metodo,lista_1) -> None:
        self.metodo = metodo
        self.lista_general = lista_1

        self.lista_draw = [] # En esta lista se almacenan las balas disparas
        self.disparo_on_off = False
        self.tiempo_transcurrido = 0

        self.sonido_disparo = pygame.mixer.Sound("PIXEL ADVENTURE\laser5.ogg")
    
    def cargar_lista_general(self):
        self.lista_general = self.metodo()
 
    def disparar(self,player):
        if self.disparo_on_off and self.lista_general:
            #Dentro de este condicional se actualizan la ubicacion y la direccion de la bala,hasta que esta se dispara
            bala_disparada = self.lista_general.pop(0)# Se elimina el objeto que se encuentra en el indice 0, y se lo asigna a la variable bala_disparada
            bala_disparada.direccion = player.direction
            bala_disparada.rect.x = int((player.rect.w/2) + player.rect.x)
            bala_disparada.collition_rect.x = int((player.rect.w/2) + player.rect.x)
            bala_disparada.rect.y = player.rect.y + 15
            bala_disparada.collition_rect.y =  player.rect.y + bala_disparada.rect.h + 15
            self.lista_draw.append(bala_disparada)
            self.disparo_on_off = False

    def mover_bala(self):
        for bala in self.lista_draw:
            if bala.direccion == DIRECTION_R:
                bala.rect.x += bala.speed
                bala.collition_rect.x += bala.speed
            else:
                bala.rect.x -= bala.speed
                bala.collition_rect.x -= bala.speed

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
                    self.disparo_on_off = True
                    self.sonido_disparo.play()
                if evento.key == pygame.K_w:
                    self.recargar()
                    

    def update(self,player):
        self.disparar(player)
        self.mover_bala()
        self.update_lista_draw()


    def draw(self,screen):
        for bala in self.lista_draw:
            if DEBUG:
                pygame.draw.rect(screen,color=(BLACK),rect=bala.collition_rect)
            screen.blit(bala.image,bala.rect)

#-------------------------------------------------------------------------------------------------------------------------------------------



class Cargador_enemy:
    def __init__(self,lista,metodo) -> None:
        self.metodo = metodo
        self.lista = lista
        self.lista_draw = [] # En esta lista se almacenan las balas disparas
        self.ubicacion_inicial = False
        self.tiempo_transcurrido = 0
    
    def crear_balas(self):
        self.lista = self.metodo()
    
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
                bala.rect.x += bala.speed
                bala.collition_rect.x += bala.speed
            else:
                bala.rect.x -= bala.speed
                bala.collition_rect.x -= bala.speed

    def update_lista_draw(self):   
        for bala in self.lista_draw:
                if (bala.rect.x > ANCHO_VENTANA or bala.rect.x < 0 or bala.eliminada):
                    self.lista_draw.remove(bala)#se elimina la bala

    
    def recargar(self):
        if not self.lista:#pregunto si la lista esta vacia
            self.lista = self.metodo()
    


    def update(self,enemigos,delta_ms):
        self.recargar()
        self.obtener_bala_disparada(enemigos)
        self.mover_bala()
        self.update_lista_draw()



    def draw(self,screen):
        for bala in self.lista_draw:
            if DEBUG:
                pygame.draw.rect(screen,color=(BLACK),rect=bala.collition_rect)
            screen.blit(bala.image,bala.rect)