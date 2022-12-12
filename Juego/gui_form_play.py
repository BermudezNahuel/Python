import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
from constantes import *

from gui_form import Form
from gui_button import *


from plataforma import Lista_plataformas
from manager_walkers import Lista_walkers
from manager_shooters import Lista_shooters
from manager_proyectil import *
from manager_item_bala import Item_bala_list
from manager_item_vida_box import Item_vida_box_list
from manager_trampas import Lista_trampas
from status import *
from status import Score
from json_manager import Json_manager
from highscore import High_score
from manager_voladores import Lista_voladores
from highscore import High_score




class FormPlay(Form):
    '''
    Esta clase crea el formulario donde se carga el juego
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.reinicio = True
        self.music_on_off = True
        self.boton1 = Button(master=self,x=850,y=50,w=50,h=50,color_background=None,color_border=None,on_click=self.on_click_boton1,on_click_param="pantalla_inicio",image_background="images\\botones\\jungle\\btn\\close.png",text=None,font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master=self,x=920,y=50,w=50,h=50,color_background=None,color_border=None,on_click=self.on_click_boton1,on_click_param="menu",text=None,image_background="images\\botones\\jungle\\btn\\settings.png",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton3 = Button_con_atajo(master=self,x=0,y=0,w=0,h=0,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="menu",on_keydown="menu",text="ABRIR B",font="Verdana",font_size=30,font_color=(0,255,0),tecla=0)
        self.highscore = High_score()
        self.highscore.crear()
        self.lista_widget = [self.boton1,self.boton2,self.boton3]
        self.data_nombre = "player"


    def inicializar(self):
        '''
        Este metodo carga todas las propiedades referentes a la plataforma,player,proyectiles, y enemigos. A su vez, recibe estos datos de un archivo json.
        '''
        pygame.mixer.init()
        if self.reinicio:
            self.reinicio = False

            self.administrador_json = Json_manager(path="nuevo_data_nivel.json",nivel_nombre=self.level)

            #setings pantalla
            self.screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
            self.imagen_fondo = pygame.transform.scale(pygame.image.load(self.administrador_json.imagen_fondo).convert(),(ANCHO_VENTANA,ALTO_VENTANA))
            self.surface = self.imagen_fondo
            #-----------------------------------------------------------------------------------------------------------------

            self.sound = pygame.mixer.Sound("PIXEL ADVENTURE\laser5.ogg")
            self.plataformas = Lista_plataformas(lista=self.administrador_json.plataformas)

            self.trampas = Lista_trampas(lista=self.administrador_json.trampas)

            self.collition_r = self.master_surface.get_rect()
            self.collition_r = (0+ANCHO_VENTANA,0,5,1000)
            self.collition_l = self.master_surface.get_rect()
            self.collition_l= (0,0,5,1000)

            self.fuente_score = pygame.font.SysFont("fixedsys",20)

            #PLAYER-----------------------------------------------------------
            self.player = self.administrador_json.player
            self.lista_balas_player = Cargador_player(lista_1=self.administrador_json.proyectil_player,metodo=self.administrador_json.crear_proyectil)
            #ENEMIGOS---------------------------------------------------------
            self.lista_walkers = Lista_walkers(self.administrador_json.walkers, metodo=self.administrador_json.crear_walkers)
            self.lista_shooters = Lista_shooters(self.administrador_json.shooters)
            self.lista_balas_enemy = Cargador_enemy(lista=self.administrador_json.proyectil_enemy,metodo=self.administrador_json.crear_proyectil_enemy)
            self.enemigo_boss = self.administrador_json.boss

            if self.level == "nivel_2":
                self.voladores = Lista_voladores(lista_1=self.administrador_json.voladores,metodo=self.administrador_json.crear_enemigo_volador)
            #ITEMS-------------------------------------------------------------
            self.lista_item_bala = Item_bala_list(self.administrador_json.balas)
            self.lista_item_vida_box = Item_vida_box_list(self.administrador_json.vida_box)
            #BARRAS----VIDA----------SCORE------------TIEMPO-------BALAS------------
            self.barra_vida = Barra_vida()
  
            pygame.mixer.music.load("PIXEL ADVENTURE\Fighting In The Stree.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.1)

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos,delta_ms,keys):
        '''
        Realiza un update de todos los metodos que se encuentra dentro del mismo
        '''
        self.inicializar()
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        self.data_score = str(self.player.score)

        if  self.player.lives == 0 or self.player.cronometro == 0:
            self.data_score = str(self.player.score)
            self.data = (self.data_nombre,self.data_score)
            self.highscore.agregar(self.data)
            self.set_active("you_lose")
            

        if  self.enemigo_boss.fuera_pantalla:
            self.data_score = str(self.player.score)
            self.data = (self.data_nombre,self.data_score)
            self.highscore.agregar(self.data)
            self.set_active("you_win")

        if not self.music_on_off:
            pygame.mixer.music.set_volume(0.0)

        self.trampas.update(player=self.player,delta_ms=delta_ms)

        if self.level == "nivel_2":
            self.voladores.update(bala=self.lista_balas_player,delta_ms=delta_ms,player=self.player,borde_l=self.collition_l,borde_r=self.collition_r)

        #PLAYER-----------------------------------------------------------
        self.player.events(delta_ms,keys)
        self.player.update(delta_ms,self.plataformas,bala_enemigo=self.lista_balas_enemy,fuente_dos=self.fuente_score,boss=self.enemigo_boss)
        self.lista_balas_player.update(self.player,lista_eventos)
        #ENEMIGOS---------------------------------------------------------
        self.lista_walkers.update(bala=self.lista_balas_player,delta_ms=delta_ms,plataform_list=self.plataformas,player=self.player,border_r=self.collition_r,borde_l=self.collition_l,jefe=self.enemigo_boss)
        self.lista_shooters.update(bala=self.lista_balas_player,delta_ms=delta_ms,plataform_list=self.plataformas,player=self.player)
        self.lista_balas_enemy.update(enemigos=self.lista_shooters,delta_ms=delta_ms)
        self.enemigo_boss.update(delta_ms=delta_ms,plataform_list=self.plataformas,bala=self.lista_balas_player,player=self.player)
        #ITEMS-------------------------------------------------------------
        self.lista_item_bala.update(delta_ms=delta_ms,player=self.player,objeto_item=self.lista_balas_player,plataform_list=self.plataformas)
        self.lista_item_vida_box.update(delta_ms=delta_ms,player=self.player,platafor_list=self.plataformas)
        self.barra_vida.update(self.player)

        self.cant_balas = self.lista_balas_player.cantidad_balas
        self.score = self.player.score
        

    def draw(self):
        '''
        Dibuja en la pantalla las superficies que se encuentran dentro de este metodo
        '''
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()


        self.trampas.draw(screen=self.master_surface)

        self.plataformas.draw(self.master_surface)

        self.player.draw(self.master_surface)
        self.lista_balas_player.draw(self.master_surface)

        self.lista_item_vida_box.draw(self.master_surface)
        self.lista_item_bala.draw(self.master_surface)

        self.lista_shooters.draw(self.master_surface)
        self.lista_balas_enemy.draw(self.master_surface)

        self.lista_walkers.draw(self.master_surface)

        self.barra_vida.draw(self.master_surface)

        self.enemigo_boss.draw(self.master_surface)

        if self.level == "nivel_2":
            self.voladores.draw(self.master_surface)
        if DEBUG:
            pygame.draw.rect(self.master_surface,color=GREEN,rect=self.collition_l)
            pygame.draw.rect(self.master_surface,color=GREEN,rect=self.collition_r)