import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
from constantes import *

from gui_form import Form
from gui_button import *
from gui_textbox import TextBox


class FormInicio(Form):
    '''
    Este es el segundo formulario al que se accede y muestra btones para comenzar a jugar, para entrar a las configuraciones del juego y para poder visualizar los puntajes maximos
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        pygame.mixer.init()
        pygame.mixer.music.load("PIXEL ADVENTURE\Fighting In The Stree.mp3")
        pygame.mixer.music.play(10)
        pygame.mixer.music.set_volume(0.1)
        
        self.boton1 = Button_base(master=self,x=300,y=150,w=400,h=300,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\bg.png",text=None,font="Verdana",font_size=30,font_color=BLACK)
        self.boton2 = Button_v2(master=self,x=1000,y=450,w=300,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param="seleccionar_nivel",text="Jugar",font="Verdana",font_size=30,font_color=BLACK)
        self.boton3 = Button_v2(master=self,x=1000,y=600,w=300,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param="menu_inicio",text="Configuracion",font="Verdana",font_size=30,font_color=BLACK)
        self.boton4 = Button_v2(master=self,x=1000,y=750,w=300,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",on_click=self.on_click_boton1,on_click_param="pantalla_scores",text="Scores",font="Verdana",font_size=30,font_color=BLACK)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]

        self.imagen_fondo = pygame.image.load("images\\images\\locations\\set_bg_03\\02\\game_background_2.png").convert_alpha()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.surface = self.imagen_fondo
        self.on_off = True

    def on_click_boton1(self, parametro):
        '''
        Este metodo se encarga de ejecutar otros metodos de la clase, y recibe los paramtros dependiendo del boton sobre el que se hizo click
        '''
        self.set_active(parametro)

    def music_on_off(self):
        if not self.on_off:
            pygame.mixer.music.set_volume(0.0)
        else:
            pygame.mixer.music.set_volume(0.1)
    
    def update(self, lista_eventos):
        '''
        Actualiza los metodos propios de la clase
        '''
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        self.music_on_off()

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()


