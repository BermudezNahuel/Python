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

