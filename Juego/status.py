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
    def __init__(self) -> None:
        self.puntaje_total = 0
        self.datos = ()
        self.fuente = pygame.font.SysFont("fixedsys",30)
    
    def manejar_score(self,player):
        '''
        Al eliminar un enemigo este metodo se encargar de sumar una determinada cantidad de puntos al score del player
        '''
        if player.aumentar_puntos:
            player.score += player.puntos
            player.aumentar_puntos = False

    def render_score(self):
        self.texto_score = self.fuente.render("Score: {0}".format(self.score),0,BLACK)

    def update(self,lista_enemigos,player,delta_ms,boss):
        self.render_score
        self.manejar_score(lista_enemigos,player)
        self.actualizar_cronometro(self,delta_ms,boss)

    def draw(self,screen):
        screen.blit(self.texto_score,(0,100))

class Tiempo:
    def __init__(self) -> None:
        self.tiempo_cronometro = 0
        self.fuente = pygame.font.SysFont("fixedsys",30)
        self.cronometro = 100
        self.texto_cronometro = ""

    def disminuir_tiempo(self,delta_ms,boss):
        if not boss.eliminado:
            self.tiempo_cronometro += delta_ms
            if self.tiempo_cronometro >= 1000:
                self.cronometro -= 1
                self.tiempo_cronometro = 0
            self.texto_cronometro = self.fuente.render("Tiempo: {0}".format(self.cronometro),0,BLACK)

    def update(self,delta_ms,boss):
        self.disminuir_tiempo(delta_ms,boss)

    
