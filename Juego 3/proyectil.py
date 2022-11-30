import pygame
from constantes import *
from auxiliar import Auxiliar


class Proyectil:
    def __init__(self) -> None:
        self.image = pygame.image.load("PIXEL ADVENTURE/estrella.png")
        self.image = pygame.transform.scale(self.image,(15,15))
        self.rect = self.image.get_rect()
        #self.mostrar_bala = True
        self.rect.h = int(self.rect.h/3)
        self.collition_rect = pygame.Rect(self.rect.x,self.rect.y+self.rect.h,15,15)
        self.eliminada = False
        self.direccion = DIRECTION_R

