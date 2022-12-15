import warnings
warnings.filterwarnings("ignore") 
import pygame
from pygame.locals import *
import sys
from constantes import *
from gui.gui_form import Form
from constantes import *
from gui.gui_form_selector_nivel import FormSelectorNivel
from gui.gui_form_play import FormPlay
from gui.gui_menu import *
from gui.gui_form_play import *
from gui.gui_form_inicio import FormInicio
from gui.gui_form_lose import FormLose
from gui.gui_form_win import FormWin
from gui.gui_form_ingreso import FormIngreso
from gui.gui_form_score import FormScore



class FormManager:
    def __init__(self,screen) -> None:
        self.pantalla_ingreso = FormIngreso(name="pantalla_ingreso",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA//1.5,h=ALTO_VENTANA//1.3,color_background=(255,255,255),color_border=(255,0,255),active=True)
        self.pantalla_inicio = FormInicio(name="pantalla_inicio",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA//1.5,h=ALTO_VENTANA//1.3,color_background=(255,255,255),color_border=(255,0,255),active=False)
        self.pantalla_scores = FormScore(name="pantalla_scores",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA//1.5,h=ALTO_VENTANA//1.3,color_background=(255,255,255),color_border=(255,0,255),active=False)
        self.seleccionar_nivel = FormSelectorNivel(name="seleccionar_nivel",master_surface = screen,x=250,y=100,w=500,h=500,color_background=(255,255,255),color_border=(255,0,255),active=False)
        self.play = FormPlay(name="master",master_surface = screen,x=0,y=0,w=ALTO_VENTANA,h=ANCHO_VENTANA,color_background=(255,255,255),color_border=(255,0,255),active=False)
        self.menu = FormMenu(name="menu",master_surface = screen,x=ANCHO_VENTANA//3,y=ALTO_VENTANA//3,w=ANCHO_VENTANA//2,h=ANCHO_VENTANA//1.5,color_background=WHITE,color_border=WHITE,active=False)
        self.menu_inicio = FormMenuInicio(name="menu_inicio",master_surface = screen,x=ANCHO_VENTANA//3,y=ALTO_VENTANA//3,w=ANCHO_VENTANA//2,h=ANCHO_VENTANA//2,color_background=WHITE,color_border=WHITE,active=False)
        self.you_lose = FormLose(name="you_lose",master_surface = screen,x=300,y=200,w=ANCHO_VENTANA//1.2,h=ALTO_VENTANA//1.5,color_background=WHITE,color_border=WHITE,active=False)
        self.you_win = FormWin(name="you_win",master_surface = screen,x=ANCHO_VENTANA//3,y=ALTO_VENTANA//3,w=ANCHO_VENTANA//2,h=ANCHO_VENTANA//1.5,color_background=WHITE,color_border=WHITE,active=False)


    def Gestionar_formularios(self,lista_eventos,delta_ms,keys):

        if(self.pantalla_ingreso.active):
            self.pantalla_ingreso.update(lista_eventos)
            self.pantalla_ingreso.draw()

        elif(self.pantalla_inicio.active):
            self.pantalla_inicio.update(lista_eventos)
            self.pantalla_inicio.draw()
            self.pantalla_scores.reinicio = True

        elif(self.pantalla_scores.active):
            self.pantalla_scores.update(lista_eventos)
            self.pantalla_scores.draw()
  
        elif(self.seleccionar_nivel.active):
            self.seleccionar_nivel.update(lista_eventos)
            self.seleccionar_nivel.draw()
            self.play.reinicio = True
                   
        elif(self.play.active):
            self.play.update(lista_eventos,delta_ms,keys)
            self.play.draw()

        elif(self.menu.active):
            self.menu.update(lista_eventos)
            self.menu.draw()

        elif(self.menu_inicio.active):
            self.menu_inicio.update(lista_eventos)
            self.menu_inicio.draw()
                
        elif(self.you_lose.active):
            self.you_lose.update(lista_eventos)
            self.you_lose.draw()
            self.play.reinicio = True

        elif(self.you_win.active):
            self.you_win.update(lista_eventos)
            self.you_win.draw()
            self.play.reinicio = True
