import json
import pygame
from constantes import*
from pygame.locals import *

def leer_json(path:str):
    with open(path,"r") as archivo:
        lista = json.load(archivo)
        lista = lista["nivel"]
        return (lista)

lista_nivel = leer_json("practicaLaboProg1\Juego 3\data.json")
dicc_screen = lista_nivel[0]["screen"]
dicc_imagen_fondo = lista_nivel[1]["imagen_fondo"]
dicc_enemigo_1 = lista_nivel[2]["enemigo_1"]
dicc_enemigo_2 = lista_nivel[3]["enemigo_2"]
dicc_vida_box = lista_nivel[4]["banana"]
dicc_item_bala = lista_nivel[5]["arma"]
dicc_player = lista_nivel[6]["player"]
dicc_lista_walkers= lista_nivel[7]["lista_walkers"]
dicc_plataformas= lista_nivel[8]



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
plat = dicc_plataformas
print(lista_nivel)
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