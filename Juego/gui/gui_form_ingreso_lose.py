import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
from constantes import *

from gui.gui_form import Form
from gui.gui_button import *
from gui.gui_textbox import TextBox
from manager_bd import High_score


class FormIngresoLose(Form):
    '''
    Crea el formulario de ingreso donde el jugador ingresa su nombre, que sera utiliazdo para registrar el puntaje realizado al jugar
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button_base(master=self,x=300,y=150,w=550,h=300,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\bg.png",text=None,font="Verdana",font_size=30,font_color=BLACK)
        self.boton2 = TextBox(master=self,x=1150,y=600,w=300,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",text="Ingrese su Nombre",font="Verdana",font_size=30,font_color=BLACK,on_click=self.on_click_botonNombre)
        self.boton4 = Button_con_atajo(master=self,x=1000,y=150,w=400,h=300,color_background=None,color_border=None,text=None,font="Verdana",font_size=30,font_color=BLACK,on_click=self.on_click_boton1,on_click_param="you_lose",on_keydown="you_lose",tecla=2)
        self.lista_widget = [self.boton1,self.boton2,self.boton4]

        self.imagen_fondo = pygame.image.load("images\\images\\locations\\set_bg_03\\02\\game_background_2.png").convert_alpha()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        self.surface = self.imagen_fondo

        self.fuente = pygame.font.Font(None,35)
        self.mensaje = self.fuente.render("Ingrese su nombre y presione ENTER",True,BLACK)
        
        

    def on_click_boton1(self, parametro):
        '''
        Este metodo se encarga de ejecutar otros dos metodos, de la clase, y recibe los paramtros dependiendo del boton sobre el que se hizo click
        '''
        self.on_click_botonNombre()
        self.set_active(parametro)

    def on_click_botonNombre(self):
        self.forms_dict["master"].data_nombre = self.boton2.nombre
        self.score = self.forms_dict["master"].data_score
        self.info_player = (self.boton2.nombre,self.score)
        self.base = High_score()
        self.base.agregar(self.info_player)
        print(self.info_player)


    
    
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
        self.master_surface.blit(self.mensaje,(340,200))