import pygame
from constantes import *
from auxiliar import*
from master_gravedad import*


class Enemigo_master(Gravedad):
    '''
    Esta clase, cumple la funcion de padre cuando se crea un enemigo nuevo. Dentro de la misma se encuentra metodos y atributos que compratiran
    todos los enemigos
    '''
    def __init__(self,gravity,score, frame_rate_ms, move_rate_ms) -> None:
        super().__init__(gravity, frame_rate_ms, move_rate_ms)
        self.score = score

    def change_x(self, delta_x):
        self.head_collition_rect.x += delta_x 
        return super().change_x(delta_x)

    def change_y(self, delta_y):
        self.head_collition_rect.y += delta_y 
        return super().change_y(delta_y)

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def colision_bala(self,bala,delta_ms,player):
        '''Comprueba si existe una colision del enemigo con alguna de las balas. Si existe la colision se modifica la propiedad "eliminada" de bala y "eliminado" del enemigo a True'''
        tamaño_lista = len(bala.lista_draw)
        for i in range(tamaño_lista):
            if self.collition_rect.colliderect(bala.lista_draw[i].collition_rect):
                self.tiempo_transcurrido += delta_ms
                if self.tiempo_transcurrido >50:
                    self.tiempo_transcurrido = 0
                    self.vidas -= 1
                    bala.lista_draw[i].eliminada = True
                    if self.vidas < 1:
                        player.puntos = self.score
                        player.aumentar_puntos = True
                        self.eliminado = True
        
    def colision_head(self,player):
        '''
        Comprueba si existe una colision del rectangulo de la cabeza del enemigo con el rectangulo de los pies del player.Si existe la colision se modifica la propiedad "eliminado" del enemigo a True
        '''
        if self.head_collition_rect.colliderect(player.ground_collition_rect):
            self.eliminado = True
            player.puntos = self.score
            player.aumentar_puntos = True
        
    
    def herir_player(self,player,delta_ms):
        '''
        Compueba si existe una colision del enemigo contra el player, si esto ocurre se mofifica el atributo "injured" del player.
        '''
        if self.collition_rect.colliderect(player.collition_rect):
            self.tiempo_transcurrido += delta_ms
            if self.tiempo_transcurrido >100:
                self.tiempo_transcurrido = 0
                player.injured = True
    