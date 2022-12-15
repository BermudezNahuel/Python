import pygame
from constantes import *
from auxiliar import Auxiliar
import sys

class Barra_vida:
    '''
    Esta clase se encarga de dibujar la imagen de la barra de vida y modificarla tanto cuando el player sufre algun daño o cuando consigue un item de vida
    '''
    def __init__(self) -> None:
        self.corazones = Auxiliar.getSurfaceFromSpriteSheet("C:PIXEL ADVENTURE\\salud-8bits.png",1,5,scale=0.1)
        self.frame = 0
        self.animation = self.corazones
        self.image = self.animation[self.frame]

    def modificar_vida(self,player):
        if player.lives == 5:
            self.frame = 0
        elif player.lives == 4:
            self.frame = 1
        elif player.lives == 3:
            self.frame = 2
        elif player.lives == 2:
            self.frame = 3
        elif player.lives == 1:
            self.frame = 4
        elif player.lives == 0:
            self.frame = 4
    
    def update(self,player):
        self.modificar_vida(player)
        


    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,(0,0))



#--------------------------------------------------------------------------------------------------------------------------------

class Barra_score:
    def __init__(self) -> None:
        self.datos = ()
        self.fuente = pygame.font.SysFont('Verdana', 30, True, False)
    
    def manejar_score(self,player):
        '''
        Al eliminar un enemigo este metodo se encargar de sumar una determinada cantidad de puntos al score del player
        '''
        if player.aumentar_puntos:
            player.score += player.puntos
            player.aumentar_puntos = False

    def render_score(self,player):
        self.texto_score = self.fuente.render("Score: {0}".format(player.score),0,BLACK)

    def update(self,player):
        self.manejar_score(player)
        self.render_score(player)

    def draw(self,screen):
        screen.blit(self.texto_score,(790,650))




class Barra_tiempo:
    def __init__(self) -> None:
        self.tiempo_cronometro = 0
        self.fuente = pygame.font.SysFont('Verdana', 30, True, False)
        self.cronometro = 100
        self.texto_cronometro = ""

    def disminuir_tiempo(self,delta_ms,boss):
        if not boss.eliminado:
            self.tiempo_cronometro += delta_ms
            if self.tiempo_cronometro >= 1000:
                self.cronometro -= 1
                self.tiempo_cronometro = 0
            self.texto_cronometro = self.fuente.render("Time: {0}".format(self.cronometro),0,BLACK)

    def update(self,delta_ms,boss):
        self.disminuir_tiempo(delta_ms,boss)
    
    def draw(self,screen):
        screen.blit(self.texto_cronometro,(450,0))


class Barra_proyectiles:
    def __init__(self) -> None:
        self.cant_balas = 0
        self.fuente = pygame.font.SysFont("Verdana",25)
        self.texto_proyectiles = ""

    def actualizar_cantidad(self,lista_proyectiles):
        self.cant_balas = len(lista_proyectiles.lista_general)

    def render(self):
        self.texto_proyectiles = self.fuente.render("Estrellas: {0}".format(self.cant_balas),0,BLACK)

    def update(self,lista_proyectiles):
        self.actualizar_cantidad(lista_proyectiles)
        self.render()
    
    def draw(self,screen):
        screen.blit(self.texto_proyectiles,(20,50))