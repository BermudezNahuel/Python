import pygame
from pygame.locals import *

from gui_form import Form
from gui_button import Button
import pygame
from pygame.locals import *
import sys
from constantes import *

from plataforma import Lista_plataformas
from manager_list_walkers import Lista_walkers
from manager_list_shooters import Lista_shooters
from lista_proyectiles_enemy import Cargador_enemy
from lista_proyectiles import Cargador_player
from manager_item_bala import Item_bala_list
from manager_list_vida_box import Item_vida_box_list
from status import*
from json_manager import Json_manager

class FormComenzar(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        #self.nivel_nombre = nivel
        self.boton1 = Button(master=self,x=50,y=150,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="form_menu_A",text="ABRIR A",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master=self,x=200,y=150,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="form_menu_A",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
        self.lista_widget = [self.boton1,self.boton2]
        
        #-----------------------------------------------------------------------------------------------------------------
        self.administrador_json = Json_manager(path="nuevo_data_nivel.json",nivel_nombre="nivel_1")
        self.imagen_fondo = pygame.transform.scale(pygame.image.load(self.administrador_json.imagen_fondo).convert(),(ANCHO_VENTANA,ALTO_VENTANA))


        self.plataformas = Lista_plataformas(lista=self.administrador_json.plataformas)

        self.collition_r = self.imagen_fondo.get_rect()
        self.collition_r = (998,0,1,1000)
        self.collition_l = self.imagen_fondo.get_rect()
        self.collition_l= (4,0,1,1000)

        self.fuente_score = pygame.font.Font(None,30)

        #PLAYER-----------------------------------------------------------
        self.player_1 = self.administrador_json.player
        self.lista_proyectiles_1 = Cargador_player(lista_1=self.administrador_json.proyectil_player,metodo=self.administrador_json.crear_proyectil)


        #ENEMIGOS---------------------------------------------------------
        self.lista_walkers = Lista_walkers(self.administrador_json.walkers)
        self.lista_shooters = Lista_shooters(self.administrador_json.shooters)
        self.lista_balas_enemy = Cargador_enemy(lista=self.administrador_json.proyectil_enemy,metodo=self.administrador_json.crear_proyectil_enemy)
        self.enemigo_boss = self.administrador_json.boss


        #ITEMS-------------------------------------------------------------
        self.lista_item_bala = Item_bala_list(self.administrador_json.balas)
        self.lista_item_vida_box = Item_vida_box_list(self.administrador_json.vida_box)

        #barra estatus
        self.barra_vida = Barra_vida()
        

    #def juego(self,lista_eventos,delta_ms,keys,screen):
        


    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos,delta_ms,keys,screen):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataformas,bala_enemigo=self.lista_balas_enemy,lista_enemigos=self.lista_walkers,fuente_dos=self.fuente_score)
        self.lista_proyectiles_1.event(lista_eventos=lista_eventos,delta_ms=delta_ms)
        self.lista_proyectiles_1.update(self.player_1)
        self.lista_walkers.update(bala=self.lista_proyectiles_1,delta_ms=delta_ms,plataform_list=self.plataformas,screen=screen,player=self.player_1,border_r=self.collition_r,borde_l=self.collition_l,jefe=self.enemigo_boss)
        self.lista_shooters.update(bala=self.lista_proyectiles_1,delta_ms=delta_ms,plataform_list=self.plataformas,screen=screen,player=self.player_1)
        self.lista_balas_enemy.update(enemigos=self.lista_shooters,delta_ms=delta_ms)
        self.lista_item_bala.update(delta_ms=delta_ms,screen=screen,player=self.player_1,objeto_item=self.lista_proyectiles_1,plataform_list=self.plataformas)
        #lista_items_vida_1.update(delta_ms=delta_ms,screen=screen,player=self.player_1,objeto_item=self.lista_proyectiles_1,enemigo=lista_enemigo_1,platafor_list=self.plataformas)
        self.lista_item_vida_box.update(delta_ms=delta_ms,screen=screen,player=self.player_1,platafor_list=self.plataformas)
        self.barra_vida.update(self.player_1)
        self.enemigo_boss.update(delta_ms=delta_ms,plataform_list=self.plataformas,bala=self.lista_proyectiles_1,player=self.player_1)
  

    def draw(self,screen): 
        super().draw()
        screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())
        self.plataformas.draw(screen)

        self.player_1.draw(screen)
    
        self.lista_proyectiles_1.draw(screen)
        

        self.lista_balas_enemy.draw(screen)

        self.barra_vida.draw(screen)

        self.enemigo_boss.draw(screen)
        #self.plataformas.draw(screen)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()