import json
import pygame
from pygame.locals import *
from constantes import*

class Crear_json_1:
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
                                                "path": "images\images\locations\set_bg_01\mountain/all.png"
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
                                                "speed":13, 
                                                "frame_rate_ms":100, 
                                                "move_rate_ms":50,
                                                "lives":4,
                                                "score":100}, 
                                             "stay":{ 
                                                "path":"PIXEL ADVENTURE\Recursos\Enemies/AngryPig/Idle (36x30).png", 
                                                "col":9, 
                                                "rows":1, 
                                                "flip":1}, 
                                             "walk":{
                                                "path":"PIXEL ADVENTURE\Recursos\Enemies/AngryPig/Run (36x30).png", 
                                                "col":12, 
                                                "rows":1, 
                                                "flip":1
                                             }}})

         self.data["nivel"].append({"banana":{"path":"PIXEL ADVENTURE\Recursos\Items\Fruits\Bananas.png","col":17,"rows":1,"x":[150,350,550,750],"y":590,"gravity":10, "frame_rate_ms":100, "move_rate_ms":50}})
         self.data["nivel"].append({"arma":{"path":"PIXEL ADVENTURE\Recursos/estrella.png","col":1,"rows":1,"x":[100,200,300,400,500,600,700,800,900],"y":575,"scale":0.1,"gravity":10, "frame_rate_ms":100, "move_rate_ms":50}})

         self.data["nivel"].append({"player":{"stay":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/programacion-y-laboratorio-1\/PIXEL ADVENTURE/Recursos/Main Characters/Ninja Frog/Idle (32x32).png",
                                                   "col": 11,
                                                   "rows": 1,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "walk":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/programacion-y-laboratorio-1\/PIXEL ADVENTURE/Recursos/Main Characters/Ninja Frog/Run (32x32).png",
                                                   "col": 12,
                                                   "rows": 1,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "jump":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/programacion-y-laboratorio-1\/PIXEL ADVENTURE/Recursos/Main Characters/Ninja Frog/Jump (32x32).png",
                                                   "col": 1,
                                                   "rows":1 ,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "hit":{
                                                   "path": "C:/Users/Nahuel/Documents/TUP/programacion-y-laboratorio-1\/PIXEL ADVENTURE/Recursos/Main Characters/Ninja Frog/Hit (32x32).png",
                                                   "col": 7,
                                                   "rows": 7,
                                                   "flip_r":0, 
                                                   "flip_l":1 
                                                   },
                                          "char":{
                                                   "x":400,
                                                   "y":600,
                                                   "lives":5,
                                                   "speed_walk":6 ,
                                                   "gravity":12 ,
                                                   "jump_power":15 ,
                                                   "frame_rate_ms":100 ,
                                                   "move_rate_ms":50 ,
                                                   "jump_height": 60,
                                                   "interval_time_jump" :300}
                                          }})
         self.data["nivel"].append({"lista_walkers":{"cantidad": 20,
                                                   "tiempo_spawn": 8000,
                                                   }})

         self.data["nivel"].append({"plataformas":{
                                                   "p_1":{"x":0,"y":560,"w":150,"h":25,"type": 13},
                                                   "p_6":{"x":0,"y":460,"w":150,"h":25,"type":13},
                                                   "p_2":{"x":0,"y":360,"w":150,"h":25,"type":13},
                                                   "p_3":{"x":850,"y":560,"w":150,"h":25,"type":13},
                                                   "p_4":{"x":850,"y":460,"w":150,"h":25,"type":13},
                                                   "p_5":{"x":850,"y":360,"w":150,"h":25,"type":13},
                                                   "p_7":{"x":190,"y":400,"w":620,"h":25,"type":13},
                                                   "p_8":{"x":190,"y":460,"w":150,"h":25,"type":13},
                                                   "p_9":{"x":0,"y":190,"w":150,"h":25,"type":13},
                                                   "p_10":{"x":0,"y":630,"w":1000,"h":25,"type":13}
                                                   }})


         with open('C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/Juego 3/data.json','w') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False )

'''
usar_json = Crear_json_1()
usar_json.update()
'''
