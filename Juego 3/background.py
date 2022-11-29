import pygame
from constantes import *
from auxiliar import Auxiliar




class Backgroung:
    def __init__(self) -> None:
        self.image = Auxiliar.getSurfaceFromSpriteSheet("PIXEL ADVENTURE\Recursos\Background\Yellow.png",1,1)
        self.frame = 0
        self.rect = self.image[self.frame].get_rect()
        self.ancho = self.rect.w
        self.alto = self.rect.h


    def construir_fondo(self):
        self.ancho_fondo = int(ANCHO_VENTANA/self.ancho)
        self.alto_fondo = int(ANCHO_VENTANA/self.alto)
        





image = Auxiliar.getSurfaceFromSpriteSheet("PIXEL ADVENTURE\Recursos\Background\Yellow.png",1,1)
rect = image[0].get_rect()
alto = rect.h
print(alto)