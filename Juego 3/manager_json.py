import json
import pygame
from constantes import*
from pygame.locals import *

def leer_json(path:str):
    with open(path,"r") as archivo:
        lista = json.load(archivo)
        lista = lista["nivel"]
        return (lista)

nivel_1 = leer_json("C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/Juego 3/data.json")
dicc_screen = nivel_1[0]["screen"]
dicc_imagen_fondo = nivel_1[1]["imagen_fondo"]
dicc_enemigo_1 = nivel_1[2]["enemigo_1"]
dicc_enemigo_2 = nivel_1[3]["enemigo_2"]
dicc_vida_box = nivel_1[4]["banana"]
dicc_item_bala = nivel_1[5]["arma"]
dicc_player = nivel_1[6]["player"]
dicc_lista_walkers= nivel_1[7]["lista_walkers"]




pantalla = pygame.display.set_mode((dicc_screen["x"],dicc_screen["y"]),
                                    dicc_screen["flag"],
                                    dicc_screen["16"]
                                    )

imagen_fondo = pygame.transform.scale(pygame.image.load(dicc_imagen_fondo["path"]).convert(),
                                                       (dicc_imagen_fondo["x"],dicc_imagen_fondo["y"])
                                     )

es_l = dicc_enemigo_1["enemy_L"]
es_r = dicc_enemigo_1["enemy_R"]

ew_2 = dicc_enemigo_2
vb = dicc_vida_box
ib= dicc_item_bala
player = dicc_player
lew = dicc_lista_walkers

'''

def screen():
    lista_screen = []
    lista_coordenadas = []
    for key,valor in dicc_screen.items():
        if key == "x" or key == "y":
            lista_coordenadas.append(valor)
        else:
            lista_screen.append(valor)
        coordenadas = tuple(lista_coordenadas)
        #screen = pygame.display.set_mode(info)


    lista_screen.insert(0,coordenadas)
    tupla_screen = tuple(lista_screen)
    
    print(tupla_screen)
    print(coordenadas)
    return tupla_screen

print(screen)
info = screen()
print(info)

'''