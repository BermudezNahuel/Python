import pygame
from constantes import *
from auxiliar import Auxiliar
from master_enemigo import*

class Enemigo_shooter(Enemigo_master):
    

    def __init__(self,x,y,direction,path,columnas,filas,flip,gravity=10,frame_rate_ms=150,move_rate_ms=50) -> None:

        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(path=path,columnas=columnas,filas=filas,flip=flip)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(path=path,columnas=columnas,filas=filas,flip=flip)

        self.vidas = 1
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.gravity = gravity
        self.animation = self.stay_r
        self.direction = direction
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #rectangulo del personsaje
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y-5,self.rect.width/3,self.rect.height)
        #rectangulo de los pies
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        #rectangulo de la cabeza
        self.head_collition_rect = pygame.Rect(self.collition_rect)
        self.head_collition_rect.height = GROUND_COLLIDE_H
        self.head_collition_rect.y = y
        #collision para que comience a disparar
        self.disparo_collition_rect = pygame.Rect(x,y,300,GROUND_COLLIDE_H)
        self.disparo_collition_rect_l = pygame.Rect(x-300,y,300,GROUND_COLLIDE_H)
        self.disparo_collition_rect_r = pygame.Rect(x,y,300,GROUND_COLLIDE_H)



        self.is_fall = False
        self.eliminado = False
        self.soltar_vida = False
        self.disparar = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms


        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general

    def definir_rect(self):
        if self.direction == DIRECTION_R:    
            self.disparo_collition_rect = self.disparo_collition_rect_r
        else:
            self.disparo_collition_rect = self.disparo_collition_rect_l

    def stay(self):
        if(self.direction == DIRECTION_R):
            self.animation = self.stay_r
        else:
            self.animation = self.stay_l
        self.move_x = 0
        self.move_y = 0
        self.frame = 0

    def change_y(self, delta_y):
        super().change_y(delta_y)
        self.disparo_collition_rect.y += delta_y

    def comenzar_disparos(self,player,delta_ms):
        if self.disparo_collition_rect.colliderect(player.collition_rect):
            self.tiempo_transcurrido += delta_ms
            if self.tiempo_transcurrido > 500:
                self.tiempo_transcurrido = 0
                self.disparar = True

    def update(self,delta_ms,plataform_list,bala,player):
        self.stay()
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.colision_bala(bala,delta_ms,player)
        #self.colision_head(player)
        self.comenzar_disparos(player,delta_ms)
        self.definir_rect()
    
    
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if(DEBUG):
            #pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=BLACK,rect=self.head_collition_rect)
            pygame.draw.rect(screen,color=GREEN,rect=self.disparo_collition_rect)
        



