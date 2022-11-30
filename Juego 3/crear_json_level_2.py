import json
import pygame
from pygame.locals import *
from constantes import*



class Crear_json_2:
   def __init__(self) -> None:
   
         self.data = {}
         self.data['nivel'] = []
   def update(self):
         self.data["nivel"].append({"screen":{"x":ANCHO_VENTANA,
                                          "y":ALTO_VENTANA,
                                          "flag": DOUBLEBUF,
                                          "16": 16
                                          }
                                 }
         )
         self.data["nivel"].append({"imagen_fondo":{"x":ANCHO_VENTANA,
                                                "y":ALTO_VENTANA,
                                                "path": "images\images\locations\set_bg_01\city/all.png"
                                                }
                                 }
         )

         self.data["nivel"].append({"enemigo_1":{
                                       "enemy_L":{
                                          "x":20,
                                          "y":25,
                                          "direction":DIRECTION_R,
                                          "path":"PIXEL ADVENTURE\Recursos\Enemies\AngryPig\Idle (36x30).png",
                                          "columnas":9,
                                          "filas":1,
                                          "flip":1},      
                                       "enemy_R":{
                                          "x":950,
                                          "y":25,
                                          "direction":DIRECTION_L,
                                          "path":"PIXEL ADVENTURE\Recursos\Enemies\AngryPig\Idle (36x30).png",
                                          "columnas":9,
                                          "filas":1,
                                          "flip":0
                                       },      
                                             }
                              })
         self.data["nivel"].append({"enemigo_2":{  
                                             "char":{
                                                "x":500, 
                                                "y":170, 
                                                "gravity":10, 
                                                "speed":10, 
                                                "frame_rate_ms":75, 
                                                "move_rate_ms":50,
                                                "lives":2,
                                                "score":100}, 
                                             "stay":{ 
                                                "path":"PIXEL ADVENTURE/Recursos/Enemies/Chicken/Idle (32x34).png", 
                                                "col":13, 
                                                "rows":1, 
                                                "flip":1}, 
                                             "walk":{
                                                "path":"PIXEL ADVENTURE/Recursos/Enemies/Chicken/Run (32x34).png", 
                                                "col":14, 
                                                "rows":1, 
                                                "flip":1
                                             }}})

         self.data["nivel"].append({"banana":{"path":"PIXEL ADVENTURE/Recursos/Items/Fruits/Bananas.png","col":17,"rows":1,"x":[150,350,550,750],"y":590,"gravity":10, "frame_rate_ms":100, "move_rate_ms":50}})
         self.data["nivel"].append({"arma":{"path":"PIXEL ADVENTURE/Recursos/estrella.png","col":1,"rows":1,"x":[100,200,300,400,500,600,700,800,900],"y":575,"scale":0.1,"gravity":10, "frame_rate_ms":100, "move_rate_ms":50}})

         self.data["nivel"].append({"player":{"stay":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/P y L 1/PIXEL ADVENTURE/Recursos/Main Characters/Mask Dude/Idle (32x32).png",
                                                   "col": 11,
                                                   "rows": 1,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "walk":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/P y L 1/PIXEL ADVENTURE/Recursos/Main Characters/Mask Dude/Run (32x32).png",
                                                   "col": 12,
                                                   "rows": 1,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "jump":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/P y L 1/PIXEL ADVENTURE/Recursos/Main Characters/Mask Dude/Jump (32x32).png",
                                                   "col": 1,
                                                   "rows":1 ,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "hit":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/P y L 1/PIXEL ADVENTURE/Recursos/Main Characters/Mask Dude/Hit (32x32).png",
                                                   "col": 7,
                                                   "rows": 7,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "char":{
                                                   "x":400,
                                                   "y":600,
                                                   "lives":5,
                                                   "speed_walk":8 ,
                                                   "gravity":10 ,
                                                   "jump_power":15 ,
                                                   "frame_rate_ms":100 ,
                                                   "move_rate_ms":50 ,
                                                   "jump_height": 60,
                                                   "interval_time_jump" :300}
                                          }})
         self.data["nivel"].append({"lista_walkers":{"cantidad": 20,
                                                   "tiempo_spawn": 8000,
                                                   }})

         with open('C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/Juego 3/data.json', 'w') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False )


'''

usar_json = Crear_json_2()
usar_json.update()
{"dic_pig": {
            "path_stay":"Enemies/AngryPig/Idle (36x30).png",
            "columnas_stay":9,
            "filas_stay":1,
            "flip_stay":1,
            "path_walk":"Enemies/AngryPig/Walk(36x30).png",
            "columnas_walk":9,
            "filas_walk":1,
            "flip_walk":0,
            }
}
path_stay =dic_pig["path_stay"]
columnas_stay =dic_pig["columnas_stay"]
filas_stay =dic_pig["filas_stay"]
flip_stay =dic_pig["flip_stay"]
path_walk =dic_pig["path_walk"]
columnas_walk =dic_pig["columnas_walk"]
filas_walk =dic_pig["filas_walk"]
flip_walk =dic_pig["flip_walk"]                       
'''
