import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_selector_nivel import FormSelectorNivel
from gui_form_nivel_1 import FormMenuNivel_1
from gui_form_nivel_2 import FormMenuNivel_2
from comenzar import FormComenzar


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()


seleccionar_nivel = FormSelectorNivel(name="nivel_1",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=True)
nivel_1 = FormMenuNivel_1(name="nivel_1",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)
nivel_2 = FormMenuNivel_2(name="nivel_2",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)
comenzar = FormComenzar(name="comenzar",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)

while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    if(seleccionar_nivel.active):
        seleccionar_nivel.update(lista_eventos)
        seleccionar_nivel.draw()

    
    elif(comenzar.active):
        comenzar.update(lista_eventos)
        comenzar.draw()

    elif(nivel_1.active):
        nivel_1.update(lista_eventos)
        nivel_1.draw()

    elif(nivel_2.active):
        nivel_2.update(lista_eventos)
        nivel_2.draw()

        
    pygame.display.flip()




    


  



