import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
from constantes import *

from gui_form import Form
from gui_button import *


class FormSelectorNivel(Form):
    '''
    Este formulario se encarga de permitir al jugador elegir un nivel determinado al hacer click sobre uno de los botones que representa a cada nivel
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.lista_1 =["master","nivel_1"]
        self.lista_2 =["master","nivel_2"]
        self.lista_3 =["master","nivel_3"]
        
        self.boton1 = Button_v2(master=self,x=300,y=250,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param=self.lista_1,text="1",font="Verdana",font_size=30,font_color=BLACK)
        self.boton2 = Button_v2(master=self,x=500,y=250,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param=self.lista_2,text="2",font="Verdana",font_size=30,font_color=BLACK)
        self.boton3 = Button_v2(master=self,x=700,y=250,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param=self.lista_3,text="3",font="Verdana",font_size=30,font_color=BLACK)
        self.boton4 = Button_v2(master=self,x=500,y=400,w=250,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton2,on_click_param="pantalla_inicio",text="Volver Inicio",font="Verdana",font_size=30,font_color=BLACK)
        self.boton5 = Button_base(master=self,x=10+ANCHO_VENTANA//10,y=10,w=ANCHO_VENTANA//4,h=ALTO_VENTANA//8,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\header.png",text=None,font="Verdana",font_size=30,font_color=WHITE)
        

        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5]
        
        self.imagen_tabla = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\level_select\\bg.png").convert_alpha(),(500,400))
        self.surface = self.imagen_tabla



    def on_click_boton1(self, parametro):
        '''
        Este metodo se encarga de ejecutar otros metodos de la clase, y recibe los paramtros dependiendo del boton sobre el que se hizo click
        '''
        self.set_active(parametro[0])
        self.forms_dict[parametro[0]].level = parametro[1]

    def on_click_boton2(self, parametro):
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