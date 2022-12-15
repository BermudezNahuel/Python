import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_manager import FormManager



flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

running = True
manager = FormManager(screen=screen)


while running:        
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    
    manager.Gestionar_formularios(lista_eventos,delta_ms,keys)
    
        
    pygame.display.flip()




    


  



