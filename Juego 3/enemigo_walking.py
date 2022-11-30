import pygame
from constantes import *
from master_enemigo import Enemigo_master
from auxiliar import *
from manager_json import *

class Enemigo_walker(Enemigo_master):
    def __init__(self,  path_stay=ew_2["stay"]["path"], col_stay=ew_2["stay"]["col"],rows_stay=ew_2["stay"]["rows"],flip_stay=ew_2["stay"]["flip"], 
                        path_walk=ew_2["walk"]["path"], col_walk=ew_2["walk"]["col"],rows_walk=ew_2["walk"]["rows"],flip_walk=ew_2["walk"]["flip"], 
                        x=ew_2["char"]["x"],y=ew_2["char"]["y"],gravity=ew_2["char"]["gravity"],speed=ew_2["char"]["speed"],
                        frame_rate_ms=ew_2["char"]["frame_rate_ms"],move_rate_ms=ew_2["char"]["move_rate_ms"],lives=ew_2["char"]["lives"],score=ew_2["char"]["score"]):
        super().__init__(gravity, frame_rate_ms, move_rate_ms)
        
        
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
        self.band_movimiento = False
        self.mov_on_off = True
        self.eliminado = False
        self.soltar_vida = False
        self.eliminado = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

    def walk(self,borde_r,borde_l):
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

        if self.contador_colisiones > 5:
            self.salir_pantalla = True
            if self.rect.x > 1200 or self.rect.x < -100:
                self.eliminado = True

    def update(self,delta_ms,plataform_list,bala,player,collition_r,collition_l):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.colision_bala(bala,delta_ms,player)
        #self.colision_head(player)
        self.walk(collition_r,collition_l)
        self.herir_player(player,delta_ms)
    
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=BLACK,rect=self.head_collition_rect)
            
