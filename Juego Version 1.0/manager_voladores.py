import pygame
from constantes import *
from auxiliar import *
import random

class Enemy_volador:
    def __init__(self,path_fly,col_fly,rows_fly,flip_fly,speed,lives,score,x,y,direction,move_rate_ms,frame_rate_ms) -> None:
        self.fly_r = Auxiliar.getSurfaceFromSpriteSheet(path_fly,col_fly,rows_fly,flip_fly)
        self.fly_l = Auxiliar.getSurfaceFromSpriteSheet(path_fly,col_fly,rows_fly)

        self.frame = 0
        self.contador_colisiones = 0
        self.salir_pantalla = False
        self.speed = speed
        self.vidas = lives
        self.score = score
        self.eliminado = False
       
        self.animation = self.fly_l
        self.direction = direction
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_y = 0
        self.move_x = 0

        #rectangulo colision del personsaje
        self.collition_rect = pygame.Rect(x+(self.rect.width/2)-10,y,self.rect.width/2,30)

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido = 0

    def fly(self,borde_r,borde_l):
 
        if self.direction == DIRECTION_R:
            self.move_x = +self.speed
            self.animation = self.fly_r
            self.move_x = self.speed
        else:
            self.move_x = -self.speed
            self.animation = self.fly_l
            self.move_x = -self.speed

        if not self.salir_pantalla:
                if self.collition_rect.colliderect(borde_r):
                    self.direction = DIRECTION_L
                    self.contador_colisiones += 1
                    self.move_y = 50
                    self.change_y(self.move_y)
                elif self.collition_rect.colliderect(borde_l):
                    self.direction = DIRECTION_R
                    self.contador_colisiones += 1
                    self.move_y = 50
                    self.change_y(self.move_y)


        if self.contador_colisiones > 8:
            self.salir_pantalla = True
            if self.rect.x > 1200 or self.rect.x < -100:
                self.eliminado = True


    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y

    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            #self.change_y(self.move_y)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def colision_bala(self,bala,delta_ms,player):
        '''Comprueba si existe una colision del enemigo con alguna de las balas. Si existe la colision se modifica la propiedad "eliminada" de bala y "eliminado" del enemigo a True'''
        tamaño_lista = len(bala.lista_draw)
        for i in range(tamaño_lista):
            if pygame.Rect.colliderect(bala.lista_draw[i].collition_rect,self.collition_rect):
                self.tiempo_transcurrido += delta_ms
                if self.tiempo_transcurrido >50:
                    self.tiempo_transcurrido = 0
                    self.vidas -= 1
                    bala.lista_draw[i].eliminada = True
                    if self.vidas < 1:
                        self.eliminado = True
                        player.aumentar_puntos = True


    def herir_player(self,player,delta_ms):
        if self.collition_rect.colliderect(player.collition_rect):
            self.tiempo_transcurrido += delta_ms
            if self.tiempo_transcurrido >75:
                self.tiempo_transcurrido = 0
                player.injured = True

    def update(self,borde_r,borde_l,delta_ms,bala,player):
        self.fly(borde_r,borde_l)
        self.do_animation(delta_ms)
        self.do_movement(delta_ms)
        self.colision_bala(bala,delta_ms,player)
        self.herir_player(player,delta_ms)

    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)


#--------------------------------------------------------------------------------------------------------------

class Lista_voladores:
    def __init__(self,metodo,lista_1) -> None:
        self.metodo = metodo
        self.lista_general = lista_1
        self.lista_draw = [] # En esta lista se almacenan los enemigos spawneados
        self.tiempo_spawn = 8000
        self.tiempo_transcurrido = 0
        self.primera = True
        self.bandera_primero = True

    def cargar_lista_general(self):
        self.lista_general = self.metodo()
    
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

    def update(self,bala,delta_ms,player,borde_r,borde_l):
        self.enemigo_spawn(delta_ms)
        self.encontrar_colision()
        #self.recargar_enemigos(jefe)
        for enemigo in self.lista_draw:
            enemigo.update(borde_r,borde_l,delta_ms,bala,player)
            
    def draw(self,screen):
        for enemigo in self.lista_draw:
            enemigo.draw(screen)