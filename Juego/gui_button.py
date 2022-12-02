import pygame
from pygame.locals import *
from gui_widget import Widget


class Button(Widget):
    def __init__(self,master,x,y,w,h,color_background,color_border,on_click,on_click_param,text,font,font_size,font_color):
        super().__init__(master,x,y,w,h,color_background,color_border)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text
        self.font_sys = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        self.render()
        
    def render(self):
        image_text = self.font_sys.render(self._text,True,self.font_color,self.color_background)
        self.slave_surface = pygame.surface.Surface((self.w,self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y
        self.slave_surface.fill(self.color_background)
        self.slave_surface.blit(image_text,(5,5))

    def update(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.render()

    

