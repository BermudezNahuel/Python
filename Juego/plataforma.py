import pygame
from constantes import *
from auxiliar import Auxiliar



class Plataform:
    def __init__(self,x,y,width,height,type=1):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/images/tileset/forest/Tiles/{0}.png",18,flip=False,w=width,h=height)
        self.tipo = type
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H-3

    def escalar_imagen(self):
        for cubo in self.image_list:
            cubo = pygame.transform.scale(cubo,(100,100))

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        

class Lista_plataformas:
    def __init__(self,lista) -> None:
        self.lista_general = lista

    def draw(self,screen):
        for plataforma in self.lista_general:
            plataforma.draw(screen)