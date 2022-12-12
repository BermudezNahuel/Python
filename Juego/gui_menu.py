import warnings
warnings.filterwarnings("ignore")
import pygame
from pygame.locals import *
from constantes import *

from gui_form import *
from gui_button import *


class FormMenu(FormularioMenu):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active)

        self.boton2 = Button_v2(master=self,x=ANCHO_VENTANA//10,y=ALTO_VENTANA//2,w=ANCHO_VENTANA//20,h=ANCHO_VENTANA//20,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\play.png",on_click=self.on_click_boton1,on_click_param="master",text=None,font="Verdana",font_size=30,font_color=WHITE)
        #self.boton2.slave_rect.center = (200//2,150//2)
        self.boton3 = Button_v2(master=self,x=ANCHO_VENTANA//4,y=ALTO_VENTANA//2,w=ANCHO_VENTANA//20,h=ANCHO_VENTANA//20,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\sound_off.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton4 = Button_con_atajo(master=self,x=0,y=0,w=0,h=0,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="master",on_keydown="master",text="ABRIR B",font="Verdana",font_size=30,font_color=(0,255,0),tecla=0)
        self.boton5 = Button(master=self,x=ANCHO_VENTANA//10,y=10,w=ANCHO_VENTANA//5,h=ALTO_VENTANA//10,color_background=None,color_border=None,image_background="images\\botones\\jungle\pause\\header.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.boton2,self.boton3,self.boton4,self.boton5]

        self.cuadro_madera = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\pause\\bg.png").convert_alpha(),(400,300))
        self.surface = self.cuadro_madera
        #self.imagen_pausa = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\pause\\header.png").convert_alpha(),(100,50))
        #self.slave_rect.center = (200,150)
        #self.surface = self.cuadro_madera
    
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton7(self, parametro):
        self.forms_dict["master"].music_on_off = parametro


    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        #self.master_surface.blit(self.imagen_pausa,(100,0))
    

class FormMenuInicio(FormularioMenu):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active)

        self.boton2 = Button_v2(master=self,x=100,y=150,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\play.png",on_click=self.on_click_boton1,on_click_param="pantalla_inicio",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton3 = Button_v2(master=self,x=250,y=150,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\sound_off.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        #self.boton4 = Button_con_atajo(master=self,x=0,y=0,w=0,h=0,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="master",on_keydown="master",text="ABRIR B",font="Verdana",font_size=30,font_color=(0,255,0),tecla=0)
        #self.boton5 = Button_v2(master=self,x=100,y=20,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\pause\\header.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        #self.boton5 = Button(master=self,x=200,y=50,w=300,h=50,color_background=None,color_border=None,on_click=self.on_click_boton1,on_click_param="pantalla_inicio",image_background="images\\botones\\jungle\pause\\header.png",text=None,font="Verdana",font_size=30,font_color=(0,255,0))
        
        self.lista_widget = [self.boton2,self.boton3]

        self.cuadro_madera = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\pause\\bg.png").convert_alpha(),(400,300))
        self.surface = self.cuadro_madera
        #self.imagen_pausa = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\pause\\header.png").convert_alpha(),(100,50))
        #self.slave_rect.center = (200,150)
        #self.surface = self.cuadro_madera
    
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton7(self, parametro):
        self.forms_dict["master"].music_on_off = parametro


    def update(self, lista_eventos):
        '''
        Actualiza los metodos propios de la clase
        '''
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        #self.master_surface.blit(self.imagen_pausa,(100,0))
    
    