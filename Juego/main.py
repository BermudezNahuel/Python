import pygame
from pygame.locals import *
import sys
from constantes import *
from lista_plataformas import Lista_plataformas_nivel_1
from manager_list_walkers import Lista_walkers
from manager_list_shooters import Lista_shooters
from lista_proyectiles_enemy import Cargador_enemy
from lista_proyectiles import Lista_proyectiles
from manager_list_item_bala import Item_bala_list
from manager_list_vida_box import Item_vida_box_list
from status import*
from json_manager import Json_manager

'''
import warnings
warnings.filterwarnings('ignore')
'''


screen = pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()

clock = pygame.time.Clock()

administrador_json = Json_manager(path="nuevo_data_nivel.json",nivel_nombre="nivel_1")

fuente = pygame.font.Font(None,100)
fuente_score = pygame.font.Font(None,30)
texto = fuente.render("Has Perdido",0,BLACK)


#ESCENARIO-------------------------------------------------------
imagen_fondo = pygame.image.load("C:\\Users\\Nahuel\\Documents\\TUP\\P y L 1\\programacion-y-laboratorio-1\\Juego\\images\\images\\locations\\set_bg_01\\mountain\\all.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
plataformas = Lista_plataformas_nivel_1()
collition_r = imagen_fondo.get_rect()
collition_r = (998,0,1,1000)
collition_l = imagen_fondo.get_rect()
collition_l= (4,0,1,1000)


#PLAYER-----------------------------------------------------------
player_1 = administrador_json.player
lista_proyectiles_1 = Lista_proyectiles(lista_1=administrador_json.proyectil_player,metodo=administrador_json.crear_proyectil)
#lista_proyectiles_1 = Lista_proyectiles(administrador_json.proyectil)


#ENEMIGOS---------------------------------------------------------
lista_walkers = Lista_walkers(administrador_json.walkers)
lista_shooters = Lista_shooters(administrador_json.shooters)
lista_balas_enemy = Cargador_enemy(lista=administrador_json.proyectil_enemy)
enemigo_boss = administrador_json.boss


#ITEMS-------------------------------------------------------------
lista_item_bala = Item_bala_list(administrador_json.balas)
lista_item_vida_box = Item_vida_box_list(administrador_json.vida_box)

#barra estatus
barra_vida = Barra_vida()



while True:     

    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
  
    plataformas.draw(screen=screen)


    player_1.events(delta_ms,keys)
    player_1.update(delta_ms,plataformas,bala_enemigo=lista_balas_enemy,lista_enemigos=lista_walkers,fuente_dos=fuente_score)
    player_1.draw(screen)
   
    lista_proyectiles_1.event(lista_eventos=lista_eventos,delta_ms=delta_ms)
    lista_proyectiles_1.update(player_1)
    lista_proyectiles_1.draw(screen)
    
    lista_walkers.update(bala=lista_proyectiles_1,delta_ms=delta_ms,plataform_list=plataformas,screen=screen,player=player_1,border_r=collition_r,borde_l=collition_l,jefe=enemigo_boss)
    lista_shooters.update(bala=lista_proyectiles_1,delta_ms=delta_ms,plataform_list=plataformas,screen=screen,player=player_1)

    lista_balas_enemy.update(enemigos=lista_shooters,delta_ms=delta_ms)
    lista_balas_enemy.draw(screen)

    lista_item_bala.update(delta_ms=delta_ms,screen=screen,player=player_1,objeto_item=lista_proyectiles_1,plataform_list=plataformas)
    #lista_items_vida_1.update(delta_ms=delta_ms,screen=screen,player=player_1,objeto_item=lista_proyectiles_1,enemigo=lista_enemigo_1,platafor_list=plataformas)
    lista_item_vida_box.update(delta_ms=delta_ms,screen=screen,player=player_1,platafor_list=plataformas)
   
    barra_vida.update(player_1)
    barra_vida.draw(screen)

    enemigo_boss.update(delta_ms=delta_ms,plataform_list=plataformas,bala=lista_proyectiles_1,player=player_1)
    enemigo_boss.draw(screen)

    pygame.display.flip()
    



    


  



