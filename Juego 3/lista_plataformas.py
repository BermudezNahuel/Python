import json
from constantes import *
from plataforma import Plataform


class Lista_plataformas_nivel_1:
    def __init__(self) -> None:
        self.lista_general = []
 
        self.lista_general.append(Plataform(x=0,y=560,width=150,height=25,type=13))
        self.lista_general.append(Plataform(x=190,y=500,width=810-190,height=25,type=13))
        self.lista_general.append(Plataform(x=850,y=560,width=150,height=25,type=13))

        self.lista_general.append(Plataform(x=0,y=460,width=150,height=25,type=13))
        self.lista_general.append(Plataform(x=190,y=400,width=810-190,height=25,type=13))
        self.lista_general.append(Plataform(x=850,y=460,width=150,height=25,type=13))

        self.lista_general.append(Plataform(x=0,y=360,width=150,height=25,type=13))
        self.lista_general.append(Plataform(x=190,y=300,width=810-190,height=25,type=13))
        self.lista_general.append(Plataform(x=850,y=360,width=150,height=25,type=13))

        self.lista_general.append(Plataform(x=0,y=630,width=1000,height=25,type=13))

    def draw(self,screen):
        for plataforma in self.lista_general:
            plataforma.draw(screen)



