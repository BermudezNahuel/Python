import pygame
from gui_button import Button






class Reloj(Button):
    def __init__(self, master, x, y, w, h, color_background, color_border, on_click, on_click_param, text, font, font_size, font_color):
        super().__init__(master, x, y, w, h, color_background, color_border, on_click, on_click_param, text, font, font_size, font_color)