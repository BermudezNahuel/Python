import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_selector_nivel import FormSelectorNivel
from gui_form_play_1 import FormPlay_1
from gui_form_play_2 import FormPlay_2
from gui_form_play_3 import FormPlay_3


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)


seleccionar_nivel = FormSelectorNivel(name="seleccionar_nivel",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=True)
play_1 = FormPlay_1(name="play_1",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False,level="nivel_1")
play_2 = FormPlay_2(name="play_2",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False,level="nivel_2")
play_3 = FormPlay_3(name="play_3",master_surface = screen,x=0,y=0,w=1000,h=700,color_background=(255,255,255),color_border=(255,0,255),active=False,level="nivel_3")

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

    if(seleccionar_nivel.active):
        seleccionar_nivel.update(lista_eventos)
        seleccionar_nivel.draw()
        
    elif(play_1.active):
        play_1.update(lista_eventos,delta_ms,keys)
        play_1.draw()
        
    elif(play_2.active):
        play_2.update(lista_eventos,delta_ms,keys)
        play_2.draw()
        
    elif(play_3.active):
        play_3.update(lista_eventos,delta_ms,keys)
        play_3.draw()
        
        
    pygame.display.flip()




    


  



