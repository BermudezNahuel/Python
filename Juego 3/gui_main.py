import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_select_level import FormSelectLevel
from gui_form_nivel_1 import FormNivel_1
from gui_form_nivel_2 import FormNivel_2
from comenzar import FormStartGame


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()


form_select_nivel = FormSelectLevel(name="form_menu_A",master_surface = screen,x=0,y=100,w=700,h=400,color_background=(255,255,0),color_border=(255,0,255),active=True)
nivel_1 = FormNivel_1(name="nivel_1",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)
nivel_2 = FormNivel_2(name="nivel_2",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)
comenzar_juego = FormStartGame(name="comenzar",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)

while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    if(form_select_nivel.active):
        form_select_nivel.update(lista_eventos)
        form_select_nivel.draw()

    elif(comenzar_juego.active):
        comenzar_juego.update(lista_eventos)
        comenzar_juego.draw()

    elif(nivel_1.active):
        nivel_1.update(lista_eventos)
        nivel_1.draw()

    elif(nivel_2.active):
        nivel_2.update(lista_eventos)
        nivel_2.draw()

        
    pygame.display.flip()




    


  



