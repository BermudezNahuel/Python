import pygame
from pygame.locals import *
from constantes import *
from gui.gui_widget import *


class Button_base(Widget_v2):
    '''
    Este boton permite colocarle una imagen como fondo
    '''
    def __init__(self,master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        pygame.font.init()
    
    def render(self):
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        if self.color_background:
            self.slave_surface.fill(self.color_background)
        
        if self.image_background:
            self.slave_surface.blit(self.image_background,(0,0))
        
        if(self._text != None):
            image_text = self._font_sys.render(self._text,True,self._font_color,self.color_background)
            self.slave_surface.blit(image_text,[
                self.slave_rect.width/2 - image_text.get_rect().width/2,
                self.slave_rect.height/2 - image_text.get_rect().height/2
            ])
            
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)

    def update(self,lista_eventos):
        pass

        self.render()


class Button(Widget_v2):
    '''
    Este boton permite colocarle una imagen como fondo
    '''
    def __init__(self,master,x,y,w,h,color_background,color_border,image_background,on_click,on_click_param,text,font,font_size,font_color):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param
    
    def render(self):
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        if self.color_background:
            self.slave_surface.fill(self.color_background)
        
        if self.image_background:
            self.slave_surface.blit(self.image_background,(0,0))
        
        if(self._text != None):
            image_text = self._font_sys.render(self._text,True,self._font_color,self.color_background)
            self.slave_surface.blit(image_text,[
                self.slave_rect.width/2 - image_text.get_rect().width/2,
                self.slave_rect.height/2 - image_text.get_rect().height/2
            ])
            
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)

    def update(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.render()

#-------------------------------------------------------------------------------------------------------------------------------------------

class Button_con_atajo(Widget):
    '''
    Con esta clase de boton se puede usar una tecla determinada para pasar de formularios
    '''
    def __init__(self,master,x,y,w,h,color_background,color_border,on_click,on_click_param,on_keydown,text,font,font_size,font_color,tecla):
        super().__init__(master,x,y,w,h,color_background,color_border)
        self.lista_tecla = [pygame.K_p,pygame.K_m,pygame.K_RETURN]
        self.tecla = self.lista_tecla[tecla]
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.on_keydown = on_keydown
        self._text = text
        self.font_sys = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        self.render()
        
    def render(self):
        '''
        Este metodo
        '''
        self.slave_surface = pygame.surface.Surface((self.w,self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y


    def update(self,lista_eventos):
        '''
        Actualiza los metodos propios de la clase
        '''
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)
            if evento.type == pygame.KEYDOWN:
                if evento.key == self.tecla:
                     self.on_click(self.on_keydown)

        self.render()


class Button_v2(Widget_v2):
    '''
    Este boton es igual al primero, pero cambia de color al posicionarse sobre el y al hacer click 
    '''
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=GREEN,color_border=RED,image_background=None,text="Button",font="Arial",font_size=14,font_color=BLUE,on_click=None,on_click_param=None):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.render()


    def render(self):
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self,lista_eventos):
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER
              
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.render()


class Button_Muerte(Button):
    def __init__(self, master, x, y, w, h, color_background, color_border, image_background, on_click, on_click_param, text, font, font_size, font_color):
        super().__init__(master, x, y, w, h, color_background, color_border, image_background, on_click, on_click_param, text, font, font_size, font_color)

    def update(self):
        self.on_click(self.on_click_param) 
    
