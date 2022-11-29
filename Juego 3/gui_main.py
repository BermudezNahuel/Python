import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_nivel_1 import FormMenuNivel_1
from gui_form_nivel_2 import FormMenuNivel_2
#from crear_json_copy import*
#from crear_json import*
from comenzar import FormComenzar


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()


form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=0,y=100,w=700,h=400,color_background=(255,255,0),color_border=(255,0,255),active=True)
nivel_1 = FormMenuNivel_1(name="nivel_1",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)
nivel_2 = FormMenuNivel_2(name="nivel_2",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=0,y=100,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)
comenzar = FormComenzar(name="comenzar",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False)

while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    if(form_menu_A.active):
        form_menu_A.update(lista_eventos)
        form_menu_A.draw()

    elif(form_menu_B.active):
        form_menu_B.update(lista_eventos)
        form_menu_B.draw()

    elif(comenzar.active):
        #info_json = Crear_json_1()
        #info_json.update()
        print("comenzar")
        comenzar.update(lista_eventos)
        comenzar.draw()

    elif(nivel_1.active):
        #info_json = Crear_json_1()
        #info_json.update()
        print("nivel 1")
        nivel_1.update(lista_eventos)
        nivel_1.draw()

    elif(nivel_2.active):
        #info_json = Crear_json_2()
        #info_json.update()
        print("nivel 2")
        nivel_2.update(lista_eventos)
        nivel_2.draw()

        
    pygame.display.flip()




    


  



