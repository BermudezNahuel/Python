import pygame
from pygame.locals import *
from constantes import *
from json_manager import Json_manager

from gui_form_play_1 import FormPlay_1

class FormNivel_3(FormPlay_1):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active,level):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active,level)

        #self.administrador_json = Json_manager(path="nuevo_data_nivel.json",nivel_nombre=level)
        