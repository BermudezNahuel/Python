import warnings
warnings.filterwarnings("ignore")
import pygame
from pygame.locals import *
from constantes import *

from gui.gui_form import *
from gui.gui_button import *


class FormMenu(FormularioMenu):
    '''
    Esta clase crea el formulario menu que se activa cuando ya se esta dentro del nivel, para poder modificar algunas configuraciones
    '''
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active)

        self.boton2 = Button_v2(master=self,x=100,y=350,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\play.png",on_click=self.on_click_boton1,on_click_param="master",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton_off = Button_v2(master=self,x=250,y=350,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\sound_off.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton_on = Button_v2(master=self,x=450,y=350,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\misic.png",on_click=self.on_click_boton7,on_click_param=True,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton4 = Button_con_atajo(master=self,x=0,y=0,w=0,h=0,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="master",on_keydown="master",text="ABRIR B",font="Verdana",font_size=30,font_color=(0,255,0),tecla=0)
        self.boton5 = Button(master=self,x=ANCHO_VENTANA//10,y=10,w=ANCHO_VENTANA//5,h=ALTO_VENTANA//10,color_background=None,color_border=None,image_background="images\\botones\\jungle\pause\\header.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.boton2,self.boton_off,self.boton_on,self.boton4,self.boton5]

        self.cuadro_madera = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\pause\\bg.png").convert_alpha(),(400,300))
        self.surface = self.cuadro_madera
       
    
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
      
    

class FormMenuInicio(FormularioMenu):
    '''
    Esta clase crea el primer menu de opciones en la pantalla de inicio, en la cual se puede acceder a la opcion de sacar la musica
    '''
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, color_border, active)

        #self.boton1 = Button_v2(master=self,x=100,y=150,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\play.png",on_click=self.on_click_boton1,on_click_param="pantalla_inicio",text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton2 = Button_v2(master=self,x=250,y=150,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\music_off.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton3 = Button_v2(master=self,x=400,y=150,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\misic.png",on_click=self.on_click_boton7,on_click_param=True,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton4 = Button_v2(master=self,x=400,y=350,w=200,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param="pantalla_inicio",text="Volver",font="Verdana",font_size=30,font_color=BLACK)
        '''
        Reservado para los efectos de sonido
        self.boton2 = Button_v2(master=self,x=250,y=150,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\sound_off.png",on_click=self.on_click_boton7,on_click_param=False,text=None,font="Verdana",font_size=30,font_color=WHITE)
        self.boton3 = Button_v2(master=self,x=400,y=150,w=50,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\btn\\sound.png",on_click=self.on_click_boton7,on_click_param=True,text=None,font="Verdana",font_size=30,font_color=WHITE)
        '''
        
        self.lista_widget = [self.boton2,self.boton3,self.boton4]

        self.cuadro_madera = pygame.transform.scale(pygame.image.load("images\\botones\\jungle\\pause\\bg.png").convert_alpha(),(400,300))

        self.surface = self.cuadro_madera
    
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton7(self, parametro):
        '''
        Este metodo se encarga de cambiar el valor de un atributo de la clase pantalla_inicio. Toma como parametro un valor booleano que recibe del boton2 del boton3
        '''
        self.forms_dict["pantalla_inicio"].on_off = parametro
        self.forms_dict["pantalla_inicio"].on_off = parametro


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
    
    