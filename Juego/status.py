import pygame
from constantes import *
from auxiliar import Auxiliar

class Barra_vida:
    def __init__(self) -> None:
        self.corazones = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Nahuel\\Documents\TUP\P y L 1\programacion-y-laboratorio-1\\Juego\\PIXEL ADVENTURE\\barra_vida.png",2,3,scale=0.6)
        self.frame = 0
        self.animation = self.corazones
        self.image = self.animation[self.frame]

    def modificar_vida(self,player):
        if player.lives == 5:
            self.frame = 0
        elif player.lives == 4:
            self.frame = 2
        elif player.lives == 3:
            self.frame = 4
        elif player.lives == 2:
            self.frame = 1
        elif player.lives == 1:
            self.frame = 3
        elif player.lives == 0:
            self.frame = 5
       
    '''
    def do_animation(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0
    '''
    
    def update(self,player):
        self.modificar_vida(player)
        #self.do_animation()


    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,(50,0))

class Score:
    def __init__(self) -> None:
        self.fuente = pygame.font.Font(None,100)
        self.fuente_score = pygame.font.Font(None,30)
    
    def mostrar_score(self,fuente_dos):
        self.texto_score = fuente_dos.render("Score: {0}".format(self.score),0,BLACK)

    def game_over(self,player_list):
        pass
        if player_list.lista_draw.eliminado:
            self.texto = self.fuente.render("GAME OVER",0,BLACK)
            
    

