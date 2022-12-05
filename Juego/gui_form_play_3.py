import pygame
from pygame.locals import *
from constantes import *

from gui_form import Form
from gui_button import Button


from plataforma import Lista_plataformas
from manager_list_walkers import Lista_walkers
from manager_list_shooters import Lista_shooters
from lista_proyectiles_enemy import Cargador_enemy
from lista_proyectiles import Cargador_player
from manager_item_bala import Item_bala_list
from manager_list_vida_box import Item_vida_box_list
from manager_trampas import Lista_trampas
from status import*
from json_manager import Json_manager
from gui_form_play_master import FormPlayMaster


class FormPlay_3(FormPlayMaster):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active, level):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active, level)