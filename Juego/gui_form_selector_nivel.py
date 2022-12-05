import pygame
from pygame.locals import *
from constantes import *

from gui_form import Form
from gui_button import Button


class FormSelectorNivel(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=int((ANCHO_VENTANA-450)/4),y=50,w=150,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="play_1",text="nivel 1",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master=self,x=int((ANCHO_VENTANA-450)/4)*2+150,y=50,w=150,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="play_2",text="nivel 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton3 = Button(master=self,x=int((ANCHO_VENTANA-450)/4)*3+350,y=50,w=150,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="play_3",text="nivel 3",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

        #self.imagen_fondo = pygame.image.load("images\\images\\locations\\set_bg_03\\02\\game_background_2.png").convert()
        #self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        #self.surface = self.imagen_fondo


    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()