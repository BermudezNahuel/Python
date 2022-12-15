import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
from constantes import *

from gui_form import Form
from gui_button import *
from gui_textbox import TextBox
from highscore import High_score


class FormScore(Form):
    '''
    Este formulario se encargar de manejar los datos referidos al score realizado por el jugador y los dibuja en pantalla
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.reinicio = True



    def inicializar(self):
        '''
        Este metodo inicializa los atributos que devuelve la base datos
        '''
        if self.reinicio:
            self.reinicio = False
            self.highscore = High_score()
        
            self.score_max =  self.highscore.consultar_scores()

            self.primero = list(self.score_max[0])
            self.segundo = list(self.score_max[1])
            self.tercero = list(self.score_max[2])
            self.cuarto = list(self.score_max[3])
            self.quinto = list(self.score_max[4])
            

            self.tex_1 = ("{0} - {1}").format(self.primero[0],self.primero[1])
            self.tex_2 = ("{0} - {1}").format(self.segundo[0],self.segundo[1])
            self.tex_3 = ("{0} - {1}").format(self.tercero[0],self.tercero[1])
            self.tex_4 = ("{0} - {1}").format(self.cuarto[0],self.cuarto[1])
            self.tex_5 = ("{0} - {1}").format(self.quinto[0],self.quinto[1])
            
            self.boton1 = Button_base(master=self,x=200,y=0,w=600,h=650,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\bg.png",text=None,font="Verdana",font_size=30,font_color=BLACK)
            self.boton2 = Button_con_atajo(master=self,x=1000,y=100,w=400,h=300,color_background=None,color_border=None,text=None,font="Verdana",font_size=30,font_color=BLACK,on_click=self.on_click_boton1,on_click_param="pantalla_inicio",on_keydown="pantalla_inicio",tecla=2)
            
            self.orden1 = Button_base(master=self,x=300,y=100,w=400,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",text=self.tex_1,font="Verdana",font_size=30,font_color=BLACK)
            self.orden2 = Button_base(master=self,x=300,y=200,w=400,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",text=self.tex_2,font="Verdana",font_size=30,font_color=BLACK)
            self.orden3 = Button_base(master=self,x=300,y=300,w=400,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",text=self.tex_3,font="Verdana",font_size=30,font_color=BLACK)
            self.orden4 = Button_base(master=self,x=300,y=400,w=400,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",text=self.tex_4,font="Verdana",font_size=30,font_color=BLACK)
            self.orden5 = Button_base(master=self,x=300,y=500,w=400,h=50,color_background=None,color_border=None,image_background="images\\botones\\jungle\\level_select\\table.png",text=self.tex_5,font="Verdana",font_size=30,font_color=BLACK)
            
            self.lista_widget = [self.boton1,self.boton2,self.orden1,self.orden2,self.orden3,self.orden4,self.orden5]

            self.imagen_fondo = pygame.image.load("images\\images\\locations\\set_bg_03\\02\\game_background_2.png").convert_alpha()
            self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            self.surface = self.imagen_fondo

            self.fuente = pygame.font.Font(None,35)
            self.mensaje = self.fuente.render("Presione ENTER para volver al MENU",True,BLACK)
        

    def on_click_boton1(self, parametro):
        '''
        Este metodo se encarga de ejecutar otros metodos de la clase, y recibe los paramtros dependiendo del boton sobre el que se hizo click
        '''
        self.set_active(parametro)

    
    def update(self, lista_eventos):
        '''
        Actualiza los metodos propios de la clase
        '''
        self.inicializar()
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        

    def draw(self): 
        '''
        Este metodo permite dibujar en la pantalla las superficies de los elementos
        '''
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()
        self.master_surface.blit(self.mensaje,(300,50))