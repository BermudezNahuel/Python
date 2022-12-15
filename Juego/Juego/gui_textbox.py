import pygame
from pygame.locals import *
from gui_widget import *
from constantes import *


class TextBox(Widget_v2):
    '''
    Esta clase crea un boton que sirve como un input para tomar los datos del player
    '''
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=GREEN,color_border=RED,image_background=None,text="Button",font="Arial",font_size=14,font_color=BLUE,on_click=None,on_click_param=None):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.writing_flag = False
        self.nombre = ""
        self.render()
        
    def render(self):
        '''
        Modica el color del boton al pasar el o hacer click con el mouse sobre el boton
        '''
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def actualizar_nombre(self):
        '''
        Actualiza el nombre se cargo en la caja de texto
        '''
        self.nombre = self._text

    def update(self,lista_eventos):
        '''
        Actualiza todoas metodos de la clase
        '''
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(self.writing_flag):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN :
                self.writing_flag = self.slave_rect_collide.collidepoint(evento.pos)
                self._text = ""
            if evento.type == pygame.KEYDOWN and self.writing_flag:
                if evento.key == pygame.K_RETURN:
                    self.writing_flag = False
                    self.actualizar_nombre()
                elif evento.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += evento.unicode

        self.render()

    

