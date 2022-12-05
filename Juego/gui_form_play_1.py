import pygame
from pygame.locals import *
from constantes import *
from gui_form_play_master import FormPlayMaster


class FormPlay_1(FormPlayMaster):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active, level):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active, level)