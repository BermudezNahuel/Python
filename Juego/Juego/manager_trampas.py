import pygame
from auxiliar import Auxiliar
from constantes import *



class Trampa_estatica:
    '''
    Esta clase crea las trampas
    '''
    def __init__(self,x,y,path,col,rows,frame_rate_ms=150,move_rate_ms=50) -> None:

        self.stay = Auxiliar.getSurfaceFromSpriteSheet(path,col,rows)
        self.frame = 0
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido = 0
       
        self.collition_rect = pygame.Rect(x+3,y-5,self.rect.width-5,self.rect.height)


    def do_animation(self,delta_ms):
        '''
        Este metodo maneja los sprites de movimiento del personaje, de acuerdo, a los paramtros que se cargan en los metodos
        '''
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def herir_player(self,player,delta_ms):
        if self.collition_rect.colliderect(player.collition_rect):
            self.tiempo_transcurrido += delta_ms
            if self.tiempo_transcurrido >100:
                self.tiempo_transcurrido = 0
                player.injured = True
    
    def update(self,delta_ms,player):
        self.do_animation(delta_ms)
        self.herir_player(player,delta_ms)
    
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)

#-------------------------------------------------------------------------------------

class Lista_trampas:
    def __init__(self,lista) -> None:
        self.lista = lista
    
    def update(self,delta_ms,player):
        for tramp in self.lista:
            tramp.update(delta_ms,player)
    
    def draw(self,screen):
        for tramp in self.lista:
            tramp.draw(screen)
