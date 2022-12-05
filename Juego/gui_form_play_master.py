import pygame
from pygame.locals import *
from constantes import *

from gui_form import Form
from gui_button import Button


from plataforma import Lista_plataformas
from manager_list_walkers import Lista_walkers
from manager_list_shooters import Lista_shooters
from manager_proyectil import *
from manager_item_bala import Item_bala_list
from manager_item_vida_box import Item_vida_box_list
from manager_trampas import Lista_trampas
from status import *
from json_manager import Json_manager



class FormPlayMaster(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,level):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.level = level
        self.bandera= True

        self.administrador_json = Json_manager(path="nuevo_data_nivel.json",nivel_nombre=level)

        self.screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

        self.boton1 = Button(master=self,x=400,y=0,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="seleccionar_nivel",text="Menu Inicio",font="Verdana",font_size=30,font_color=(0,255,0))
        #self.boton2 = Button(master=self,x=250,y=0,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="play_1",text="Reiniciar",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.boton1]
        
        self.imagen_fondo = pygame.transform.scale(pygame.image.load(self.administrador_json.imagen_fondo).convert(),(ANCHO_VENTANA,ALTO_VENTANA))
        self.surface = self.imagen_fondo
        #-----------------------------------------------------------------------------------------------------------------

        self.sound = pygame.mixer.Sound("PIXEL ADVENTURE\laser5.ogg")
        self.plataformas = Lista_plataformas(lista=self.administrador_json.plataformas)

        self.trampas = Lista_trampas(lista=self.administrador_json.trampas)


        self.collition_r = self.master_surface.get_rect()
        self.collition_r = (1000,0,5,1000)
        self.collition_l = self.master_surface.get_rect()
        self.collition_l= (0,0,5,1000)

        self.fuente_score = pygame.font.Font(None,30)

        #PLAYER-----------------------------------------------------------
        self.player_1 = self.administrador_json.player
        self.lista_proyectiles_1 = Cargador_player(lista_1=self.administrador_json.proyectil_player,metodo=self.administrador_json.crear_proyectil)


        #ENEMIGOS---------------------------------------------------------
        self.lista_walkers = Lista_walkers(self.administrador_json.walkers, metodo=self.administrador_json.crear_walkers)
        self.lista_shooters = Lista_shooters(self.administrador_json.shooters)
        self.lista_balas_enemy = Cargador_enemy(lista=self.administrador_json.proyectil_enemy,metodo=self.administrador_json.crear_proyectil_enemy)
        self.enemigo_boss = self.administrador_json.boss


        #ITEMS-------------------------------------------------------------
        self.lista_item_bala = Item_bala_list(self.administrador_json.balas)
        self.lista_item_vida_box = Item_vida_box_list(self.administrador_json.vida_box)

        #barra estatus
        self.barra_vida = Barra_vida()
    

    def musica_juego(self):
        pygame.mixer.music.load("PIXEL ADVENTURE\Fighting In The Stree.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
     
    def valores_reset(self):
        self.administrador_json = Json_manager(path="nuevo_data_nivel.json",nivel_nombre=self.level)
        self.player_1 = self.administrador_json.player
        self.lista_proyectiles_1 = Cargador_player(lista_1=self.administrador_json.proyectil_player,metodo=self.administrador_json.crear_proyectil)
        self.lista_walkers = Lista_walkers(self.administrador_json.walkers)
        self.lista_shooters = Lista_shooters(self.administrador_json.shooters)
        self.lista_balas_enemy = Cargador_enemy(lista=self.administrador_json.proyectil_enemy,metodo=self.administrador_json.crear_proyectil_enemy)
        self.enemigo_boss = self.administrador_json.boss
        self.lista_item_bala = Item_bala_list(self.administrador_json.balas)
        self.lista_item_vida_box = Item_vida_box_list(self.administrador_json.vida_box)
    
    
    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos,delta_ms,keys):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

        if self.bandera:
            self.musica_juego()
            self.bandera = False

        self.trampas.update(player=self.player_1,delta_ms=delta_ms)

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataformas,bala_enemigo=self.lista_balas_enemy,lista_enemigos=self.lista_walkers,fuente_dos=self.fuente_score,boss=self.enemigo_boss)
        self.lista_proyectiles_1.event(lista_eventos=lista_eventos,delta_ms=delta_ms)
        self.lista_proyectiles_1.update(self.player_1)

        self.lista_walkers.update(bala=self.lista_proyectiles_1,delta_ms=delta_ms,plataform_list=self.plataformas,player=self.player_1,border_r=self.collition_r,borde_l=self.collition_l,jefe=self.enemigo_boss)
        
        self.lista_shooters.update(bala=self.lista_proyectiles_1,delta_ms=delta_ms,plataform_list=self.plataformas,player=self.player_1)
        self.lista_balas_enemy.update(enemigos=self.lista_shooters,delta_ms=delta_ms)
        self.lista_item_bala.update(delta_ms=delta_ms,player=self.player_1,objeto_item=self.lista_proyectiles_1,plataform_list=self.plataformas)
        self.lista_item_vida_box.update(delta_ms=delta_ms,player=self.player_1,platafor_list=self.plataformas)
        self.barra_vida.update(self.player_1)
        self.enemigo_boss.update(delta_ms=delta_ms,plataform_list=self.plataformas,bala=self.lista_proyectiles_1,player=self.player_1)
        #self.plataformas.update(bala=self.lista_proyectiles_1)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()


        self.trampas.draw(screen=self.master_surface)

        self.plataformas.draw(self.master_surface)

        self.player_1.draw(self.master_surface)
        self.lista_proyectiles_1.draw(self.master_surface)

        self.lista_item_vida_box.draw(self.master_surface)
        self.lista_item_bala.draw(self.master_surface)

        self.lista_shooters.draw(self.master_surface)
        self.lista_balas_enemy.draw(self.master_surface)

        self.lista_walkers.draw(self.master_surface)

        self.barra_vida.draw(self.master_surface)

        self.enemigo_boss.draw(self.master_surface)
        
        pygame.draw.rect(self.master_surface,color=GREEN,rect=self.collition_l)
        pygame.draw.rect(self.master_surface,color=GREEN,rect=self.collition_r)