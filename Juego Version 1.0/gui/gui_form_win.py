import warnings
warnings.filterwarnings("ignore")
import pygame
from pygame.locals import *
from constantes import *

from gui.gui_form import *
from gui.gui_button import *


class FormWin(FormularioMenu):
    '''
    Este es un formulario, el cual se activa cuando el player derrota al enemigo_boss. El mismo cuenta con 2 botones, uno que vuelve a la pantalla de inicio y otro
    permite jugar el nivel 
    '''
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active)

        self.boton1 = Button(master=self,x=ANCHO_VENTANA//10,y=10,w=ANCHO_VENTANA//5,h=ALTO_VENTANA//10,color_background=None,color_border=None,image_background="images\\botones\\jungle\\you_win\\header.png",on_click=None,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton2 = Button_v2(master=self,x=400,y=250,w=250,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param="pantalla_inicio",text="Volver Inicio",font="Fixedsys",font_size=30,font_color=BLACK)
        self.boton3 = Button_v2(master=self,x=400,y=450,w=250,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param="master",text="Volver a Jugar",font="Fixedsys",font_size=30,font_color=BLACK)
       
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

        self.cuadro_madera = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\pause\\bg.png").convert_alpha(),(400,300))
        self.surface = self.cuadro_madera

    
    def on_click_boton1(self, parametro):
        '''
        Este metodo se encarga de ejecutar otros metodos de la clase, y recibe los paramtros dependiendo del boton sobre el que se hizo click
        '''
        self.set_active(parametro)


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
