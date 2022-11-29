import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from lista_proyectiles import Lista_proyectiles
from lista_enemigos import *
from enemigo_walking import Enemigo_walker
from lista_plataformas import Lista_plataformas_nivel_1
from items import *
from lista_items import *
from lista_enemigos_tira_tiros import*
from lista_proyectiles_enemy import*
from status import*
from jefe_uno import Jefe_uno
from item_bala_list import Item_bala_list
from item_vida_box_list import Item_vida_box_list
from crear_json import*
flags = DOUBLEBUF

#llamo a json y almaceno en una variable todos los datos que se encuentran dentro de uno de los dict 
#por ejemplo screen, recorro el dict, y le doy un formato a esa info para pasarla como parametro

info_json = Crear_json_1()
info_json.update()

from archivo_pract_1J import *
screen = pantalla

pygame.init()

clock = pygame.time.Clock()

imagen_fondo

collition_r = imagen_fondo.get_rect()
collition_r = (998,0,1,1000)
collition_l = imagen_fondo.get_rect()
collition_l= (4,0,1,1000)

plataforma_1 = Lista_plataformas_nivel_1()

fuente = pygame.font.Font(None,100)
fuente_score = pygame.font.Font(None,30)
texto = fuente.render("Has Perdido",0,BLACK)

player_1 = Player()


lista_proyectiles_1 = Lista_proyectiles()
lista_balas_enemy = Cargador_enemy()


lista_walkers = Lista_walkers()
lista_enemigos_2 = Lista_shooters()


#boss
lista_jefe = Lista_jefe(cantidad=1,tiempo_spawn=100,enemigo=Jefe_uno)
jefe = Jefe_uno()

#BALAS
lista_item_bala = Item_bala_list()
#VIDA
#lista_items_vida_1 = Lista_spawn_life(cantidad=10,item=Manzana)
lista_item_vida_box = Item_vida_box_list()

#barra estatus
barra_vida = Barra_vida()

#crear plataforma
plataformas = Lista_plataformas_nivel_1()

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
    
    lista_walkers.update(bala=lista_proyectiles_1,delta_ms=delta_ms,plataform_list=plataformas,screen=screen,player=player_1,border_r=collition_r,borde_l=collition_l,jefe=jefe)
    lista_enemigos_2.update(bala=lista_proyectiles_1,delta_ms=delta_ms,plataform_list=plataformas,screen=screen,player=player_1)

    lista_balas_enemy.update(enemigos=lista_enemigos_2,delta_ms=delta_ms)
    lista_balas_enemy.draw(screen)

    lista_item_bala.update(delta_ms=delta_ms,screen=screen,player=player_1,objeto_item=lista_proyectiles_1,plataform_list=plataformas)
    #lista_items_vida_1.update(delta_ms=delta_ms,screen=screen,player=player_1,objeto_item=lista_proyectiles_1,enemigo=lista_enemigo_1,platafor_list=plataformas)
    lista_item_vida_box.update(delta_ms=delta_ms,screen=screen,player=player_1,platafor_list=plataformas)
   
    barra_vida.update(player_1)
    barra_vida.draw(screen)

    jefe.update(delta_ms=delta_ms,plataform_list=plataformas,bala=lista_proyectiles_1,player=player_1)
    jefe.draw(screen)

    pygame.display.flip()
    



    


  



