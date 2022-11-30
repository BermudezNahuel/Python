import pygame
import random
from constantes import *
from auxiliar import Auxiliar
from master_gravedad import Gravedad
from manager_json import *

class Banana(Gravedad):
    def __init__(self,path=vb["path"],col=vb["col"],rows=vb["rows"],y=vb["y"],x=vb["x"],gravity=vb["gravity"],frame_rate_ms=vb["frame_rate_ms"],move_rate_ms=vb["move_rate_ms"]) -> None:
        super().__init__(gravity, frame_rate_ms, move_rate_ms)
        self.objeto = Auxiliar.getSurfaceFromSpriteSheet(path,col,rows)
        self.frame = 0
        self.animation = self.objeto
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(x)
        self.rect.y = y
        self.rect.w = 15
        self.rect.h = 15
        self.rect.h = int(self.rect.h/3)
        self.collition_rect = pygame.Rect(self.rect.x+10,self.rect.y+5+self.rect.h,15,15)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.y += 10
        self.ground_collition_rect.height = GROUND_COLLIDE_H

        self.eliminado = False
        self.gravity = gravity
        self.move_y = 0


    def colision(self,player):
        if self.collition_rect.colliderect(player.ground_collition_rect):
            self.eliminado = True
            player.aumentar_vida = True
            player.carga_de_vida = 1
            

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,color=WHITE,rect=self.collition_rect)
        screen.blit(self.image,self.rect)
    
    def update(self,player,plataform_list,delta_ms):
        self.colision(player)
        self.do_animation(delta_ms)
        self.is_on_plataform(plataform_list)
        self.do_movement(delta_ms,plataform_list)