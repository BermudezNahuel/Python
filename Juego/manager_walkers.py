import random
import pygame
from constantes import *
from master_enemigo import Enemigo_master
from auxiliar import *

class Enemigo_walker(Enemigo_master):
    '''
    Esta clase crea al enemigo que camina de derecha a izquierda e izquierda a derecha. Cambia de direccion al chocar con los limites de la pantalla.
    Al colisionar con una proyectil del player mueren
    '''
    def __init__(self,path_stay,col_stay,rows_stay,flip_stay,path_walk,col_walk,rows_walk,flip_walk,x,y,gravity,speed,frame_rate_ms,move_rate_ms,lives,score):
        super().__init__(gravity, frame_rate_ms, move_rate_ms,score)
        
        
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(path_stay,col_stay,rows_stay,flip_stay)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(path_stay,col_stay,rows_stay)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(path_walk,col_walk,rows_walk,flip_walk)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(path_walk,col_walk,rows_walk)
        
        self.contador_colisiones = 0
        self.salir_pantalla = False
        self.speed = speed
        self.vidas = lives
        self.score = score
       
        self.animation = self.stay_l
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #rectangulo colision del personsaje
        self.collition_rect = pygame.Rect(x+(self.rect.width/2)-10,y,self.rect.width/2,30)
        #rectangulo de los pies
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        #rectangulo de la cabeza
        self.head_collition_rect = pygame.Rect(x+(self.rect.width/2)-10,y,self.rect.width/2,GROUND_COLLIDE_H)

        #banderas
        self.eliminado = False
        #self.soltar_vida = False


        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

    def walk(self,borde_r,borde_l):
        if (self.is_fall == False):
            if self.direction == DIRECTION_R:
                self.move_x = +self.speed
                self.animation = self.walk_r
                self.move_x = self.speed
            else:
                self.move_x = -self.speed
                self.animation = self.walk_l
                self.move_x = -self.speed

        if not self.salir_pantalla:
            if(self.is_fall == False):
                if self.collition_rect.colliderect(borde_r):
                    self.direction = DIRECTION_L
                    self.contador_colisiones += 1
                elif self.collition_rect.colliderect(borde_l):
                    self.direction = DIRECTION_R
                    self.contador_colisiones += 1

        if self.contador_colisiones > 6:
            self.salir_pantalla = True
            if self.rect.x > 1200 or self.rect.x < -100:
                self.eliminado = True

    def update(self,delta_ms,plataform_list,bala,player,collition_r,collition_l):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.colision_bala(bala,delta_ms,player)
        self.colision_head(player)
        self.walk(collition_r,collition_l)
        self.herir_player(player,delta_ms)
    
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=BLACK,rect=self.head_collition_rect)
            





#--------------------------------------------------------------------------------------------------------------------------------


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
