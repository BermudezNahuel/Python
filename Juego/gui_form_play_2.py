import pygame
from pygame.locals import *
from constantes import *

from gui_form_play_master import FormPlayMaster
from enemigo_volador import Lista_voladores
from json_manager import Json_manager


class FormPlay_2(FormPlayMaster):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active, level):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active, level)

        #self.administrador_json = Json_manager(path="nuevo_data_nivel.json",nivel_nombre=level)
      
        self.voladores = Lista_voladores(lista_1=self.administrador_json.voladores,metodo=self.administrador_json.crear_enemigo_volador)
        
    def update(self, lista_eventos, delta_ms, keys):
        super().update(lista_eventos, delta_ms, keys)
        self.voladores.update(bala=self.lista_proyectiles_1,delta_ms=delta_ms,player=self.player_1,borde_l=self.collition_l,borde_r=self.collition_r)

    def draw(self):
        super().draw()
        self.voladores.draw(self.master_surface)