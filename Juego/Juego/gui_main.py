import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_selector_nivel import FormSelectorNivel
from gui_form_play import FormPlay
from gui_menu import *
from gui_form_play import *
from gui_form_inicio import FormInicio
from gui_form_lose import FormLose
from gui_form_win import FormWin
from gui_form_ingreso import FormIngreso
from gui_form_score import FormScore


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()







pantalla_ingreso = FormIngreso(name="pantalla_ingreso",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA//1.5,h=ALTO_VENTANA//1.3,color_background=(255,255,255),color_border=(255,0,255),active=True)
pantalla_inicio = FormInicio(name="pantalla_inicio",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA//1.5,h=ALTO_VENTANA//1.3,color_background=(255,255,255),color_border=(255,0,255),active=False)
pantalla_scores = FormScore(name="pantalla_scores",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA//1.5,h=ALTO_VENTANA//1.3,color_background=(255,255,255),color_border=(255,0,255),active=False)
seleccionar_nivel = FormSelectorNivel(name="seleccionar_nivel",master_surface = screen,x=250,y=100,w=500,h=500,color_background=(255,255,255),color_border=(255,0,255),active=False)
master = FormPlay(name="master",master_surface = screen,x=0,y=0,w=ALTO_VENTANA,h=ANCHO_VENTANA,color_background=(255,255,255),color_border=(255,0,255),active=False)
menu = FormMenu(name="menu",master_surface = screen,x=ANCHO_VENTANA//3,y=ALTO_VENTANA//3,w=ANCHO_VENTANA//2,h=ANCHO_VENTANA//1.5,color_background=WHITE,color_border=WHITE,active=False)
menu_inicio = FormMenuInicio(name="menu_inicio",master_surface = screen,x=ANCHO_VENTANA//3,y=ALTO_VENTANA//3,w=ANCHO_VENTANA//2,h=ANCHO_VENTANA//2,color_background=WHITE,color_border=WHITE,active=False)
you_lose = FormLose(name="you_lose",master_surface = screen,x=ANCHO_VENTANA//3,y=ALTO_VENTANA//3,w=ANCHO_VENTANA//2,h=ANCHO_VENTANA//1.5,color_background=WHITE,color_border=WHITE,active=False)
you_win = FormWin(name="you_win",master_surface = screen,x=ANCHO_VENTANA//3,y=ALTO_VENTANA//3,w=ANCHO_VENTANA//2,h=ANCHO_VENTANA//1.5,color_background=WHITE,color_border=WHITE,active=False)



running = True


while running:        
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    if(pantalla_ingreso.active):
        pantalla_ingreso.update(lista_eventos)
        pantalla_ingreso.draw()

    elif(pantalla_inicio.active):
        pantalla_inicio.update(lista_eventos)
        pantalla_inicio.draw()
        pantalla_scores.reinicio = True

    elif(pantalla_scores.active):
        pantalla_scores.update(lista_eventos)
        pantalla_scores.draw()

    
    elif(seleccionar_nivel.active):
        seleccionar_nivel.update(lista_eventos)
        seleccionar_nivel.draw()
        master.reinicio = True
        
        
    elif(master.active):
        master.update(lista_eventos,delta_ms,keys)
        master.draw()


    elif(menu.active):
        menu.update(lista_eventos)
        menu.draw()

    elif(menu_inicio.active):
        menu_inicio.update(lista_eventos)
        menu_inicio.draw()
    
    
    elif(you_lose.active):
        you_lose.update(lista_eventos)
        you_lose.draw()
        master.reinicio = True

    elif(you_win.active):
        you_win.update(lista_eventos)
        you_win.draw()
        master.reinicio = True
    
        
    pygame.display.flip()




    


  



