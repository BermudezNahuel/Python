import pygame
from constantes import *
from auxiliar import*

class Gravedad:
    '''
    Esta clase se encarga de dar gravedad dentro del juego, mofificando la posicion de lso personajes en eje Y 
    '''
    def __init__(self,gravity=10,frame_rate_ms=100,move_rate_ms=50) -> None:
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.gravity = gravity

        self.is_fall = False
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido = 0

    def change_x(self,delta_x):
        '''
        Este metodo modifica aquella propiedades de la clase que estan referencaidas en el eje X
        '''
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        '''
        Este metodo modifica aquella propiedades de la clase que estan referencaidas en el eje Y
        '''
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        '''
        En esta funcion es donde se llevan a cabo finalmente los desplazamientos del personaje
        '''
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False 

    def is_on_plataform(self,plataform_list):
        '''
        Este metodo evalua si el personaje se encuentra sobre una plataforma, para hacerlo caer(aumentar su posicion en el eje Y) en el caso que esto no se cumpla
        '''
        retorno = False
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list.lista_general:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno

    def do_animation(self,delta_ms):
        '''
        Este metodo maneja los sprites de movimiento del personaje, de acuerdo, a los paramtros que se cargan en los atributos self.animation y self.frame
        '''
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0