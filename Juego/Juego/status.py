import pygame
from constantes import *
from auxiliar import Auxiliar

class Barra_vida:
    '''
    Esta clase se encarga de dibujar la imagen de la barra de vida y modificarla tanto cuando el player sufre algun daño o cuando consigue un item de vida
    '''
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
    
    def update(self,player):
        self.modificar_vida(player)
        #self.do_animation()


    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,(-5,-20))

class Score:
    def __init__(self,player) -> None:
        self.fuente = pygame.font.Font(None,100)
        self.fuente_score = pygame.font.Font(None,25)
        self.puntaje_total = 0
        self.score = player.score
        self.datos = ()
    
    def manejar_score(self,lista_enemigos):
        for enemy in lista_enemigos.lista_draw:
            if self.aumentar_puntos:
                self.score += enemy.score
                self.aumentar_puntos = False


    def mostrar_score(self,fuente_dos):
        self.texto_score = fuente_dos.render("Score: {0}".format(self.score),0,BLACK)

    def mostrar_cronometro(self,fuente_dos,delta_ms,boss):
        if not boss.eliminado:
            self.tiempo_cronometro += delta_ms
            if self.tiempo_cronometro >= 1000:
                self.cronometro -= 1
                self.tiempo_cronometro = 0
            self.texto_cronometro = fuente_dos.render("Tiempo: {0}".format(self.cronometro),0,BLACK)

    def update(self):
        pass
    
