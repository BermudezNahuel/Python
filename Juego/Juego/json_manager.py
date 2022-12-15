import warnings
warnings.filterwarnings("ignore") 
import json
from manager_walkers import Enemigo_walker
from manager_shooters import Enemigo_shooter
from manager_boss import Enemigo_boss
from player import Player
from manager_item_bala import Item_bala
from manager_item_vida_box import Vida_box
from manager_proyectil import Proyectil
from plataforma import Plataform
from manager_trampas import Trampa_estatica
from manager_voladores import Enemy_volador

class Json_manager:
    '''
    Esta clase se encarga de manejar el json, tiene como parametro principal, ladireccion de json y el nivel con el que se va a trabajar
    '''
    def __init__(self,path,nivel_nombre) -> None:
        self.path = path
        self.nivel = nivel_nombre
        self.config_nivel = self.leer_json(self.path)[self.nivel]
        
        #Escenario
        self.__imagen_fondo = self.config_nivel["imagen_fondo"]["path"]
        
        #Plataformas
        self.__lista_plataformas_dicc = self.config_nivel["plataformas"]
        self.__lista_plataformas = []
        self.crear_plataformas()

        #Trampas
        self.__lista_trampas_dicc = self.config_nivel["trampas"]
        self.__lista_trampas = []
        self.crear_trampas()

        #Enemigos:
        self.__lista_walkers_dicc = self.config_nivel["enemigos_walkers"]
        self.__lista_walkers = []
        self.crear_walkers()

        self.__lista_shooters_dicc = self.config_nivel["enemigos_shooters"]
        self.__lista_shooters = []
        self.crear_shooters()

        self.__lista_enemigo_boss_dicc = self.config_nivel["enemigo_boss"]
        self.__lista_enemigo_boss = []
        self.crear_enemigo_boss()

        if nivel_nombre == "nivel_2":
            self.__lista_enemigo_volador_dicc = self.config_nivel["enemigos_voladores"]
            self.__lista_enemigo_volador = []
            self.crear_enemigo_volador()

        

        #Player
        self.__player_dicc = self.config_nivel["player"]
        self.__player = []
        self.crear_player()
        #proyectil del player
        self.__lista_proyectil_dicc = self.config_nivel["proyectil"]
        self.__lista_proyectil = []
        self.crear_proyectil()
        #proyectil del enemigo
        self.__lista_proyectil_enemy_dicc = self.config_nivel["proyectil"]
        self.__lista_proyectil_enemy = []
        self.crear_proyectil_enemy()
        #Items_balas
        self.__lista_balas_dicc = self.config_nivel["balas"]
        self.__lista_balas = []
        self.crear_balas()
        #item_vida
        self.__lista_vida_box_dicc = self.config_nivel["vida_item"]
        self.__lista_vida_box = []
        self.crear_vida_box()




    def leer_json(self,path:str):
        with open(path,"r") as archivo:
            return json.load(archivo)

    def crear_plataformas(self):
        for plataforma in self.__lista_plataformas_dicc:
            self.__lista_plataformas.append(
                Plataform(
                    x=plataforma["x"],
                    y=plataforma["y"],
                    width=plataforma["width"],
                    height=plataforma["height"],
                    type=plataforma["type"],
                )
            )
        self.__lista_plataformas_dicc.clear()

    def crear_trampas(self):
        for trampa in self.__lista_trampas_dicc:
            self.__lista_trampas.append(
                Trampa_estatica(
                    x=trampa["x"],
                    y=trampa["y"],
                    path=trampa["path"],
                    col=trampa["col"],
                    rows=trampa["rows"],
                    frame_rate_ms=trampa["frame_rate_ms"],
                    move_rate_ms=trampa["move_rate_ms"]
                )
            )
        self.__lista_trampas_dicc.clear()

    def crear_walkers(self):
        for enemigo in self.__lista_walkers_dicc:
            self.__lista_walkers.append(
                Enemigo_walker(
                            path_stay=enemigo["stay"]["path"],
                            col_stay=enemigo["stay"]["col"],
                            rows_stay=enemigo["stay"]["rows"],
                            flip_stay=enemigo["stay"]["flip"],
                            path_walk=enemigo["walk"]["path"],
                            col_walk=enemigo["walk"]["col"],
                            rows_walk=enemigo["walk"]["rows"],
                            flip_walk=enemigo["walk"]["flip"], 
                            x=enemigo["char"]["x"],y=enemigo["char"]["y"],
                            gravity=enemigo["char"]["gravity"],
                            speed=enemigo["char"]["speed"],
                            frame_rate_ms=enemigo["char"]["frame_rate_ms"],
                            move_rate_ms=enemigo["char"]["move_rate_ms"],
                            lives=enemigo["char"]["lives"],
                            score=enemigo["char"]["score"]
                            )
            )
        return self.__lista_walkers

    def crear_shooters(self):
        for enemigo in self.__lista_shooters_dicc:
            self.__lista_shooters.append(
                Enemigo_shooter(
                            x=enemigo["x"],
                            y=enemigo["y"],
                            direction=enemigo["direction"],
                            path=enemigo["path"],
                            columnas=enemigo["columnas"],
                            filas=enemigo["filas"],
                            flip=enemigo["flip"],
                            vidas=enemigo["vidas"],
                            gravity=enemigo["gravity"],
                            frame_rate_ms=enemigo["frame_rate_ms"],
                            move_rate_ms=enemigo["move_rate_ms"],
                            score=enemigo["score"])
            )
        return self.__lista_shooters


    def crear_enemigo_boss(self):
        for boss in self.__lista_enemigo_boss_dicc:
            self.__lista_enemigo_boss.append(
                Enemigo_boss(
                    path_stay=boss["path_stay"],
                    col_stay=boss["col_stay"],
                    rows_stay=boss["rows_stay"],
                    flip_stay_r=boss["flip_stay_r"],
                    flip_stay_l=boss["flip_stay_l"],
                    scale_stay=boss["scale_stay"],
                    path_hit=boss["path_hit"],
                    col_hit=boss["col_hit"],
                    rows_hit=boss["rows_hit"],
                    flip_hit_r=boss["flip_hit_r"],
                    flip_hit_l=boss["flip_hit_l"],
                    scale_hit=boss["scale_hit"],
                    x=boss["x"],
                    y=boss["y"],
                    direction=boss["direction"],
                    gravity=boss["gravity"],
                    frame_rate_ms=boss["frame_rate_ms"],
                    move_rate_ms=boss["move_rate_ms"],
                    score = boss["score"],
                    lives=boss["lives"]
                )
            )        
        self.__lista_enemigo_boss_dicc.clear()

    def crear_enemigo_volador(self):
        for enemy in self.__lista_enemigo_volador_dicc:
            self.__lista_enemigo_volador.append(
                Enemy_volador(
                    path_fly=enemy["path_fly"],
                    col_fly=enemy["col_fly"],
                    rows_fly=enemy["rows_fly"],
                    flip_fly=enemy["flip_fly"],
                    speed=enemy["speed"],
                    lives=enemy["lives"],
                    score=enemy["score"],
                    x=enemy["x"],
                    y=enemy["y"],
                    direction=enemy["direction"],
                    frame_rate_ms=enemy["frame_rate_ms"],
                    move_rate_ms=enemy["move_rate_ms"]
                )
            )        
        return self.__lista_enemigo_volador


    def crear_player(self):
        for player in self.__player_dicc:
            self.__player.append(
                Player(
                    path_walk=player["walk"]["path"],
                    col_walk=player["walk"]["col"], 
                    rows_walk=player["walk"]["rows"], 
                    flip_r_walk=player["walk"]["flip_r"], 
                    flip_l_walk=player["walk"]["flip_l"],
                    path_stay=player["stay"]["path"], 
                    col_stay=player["stay"]["col"], 
                    rows_stay=player["stay"]["rows"], 
                    flip_r_stay=player["stay"]["flip_r"], 
                    flip_l_stay=player["stay"]["flip_l"],
                    path_jump=player["jump"]["path"], 
                    col_jump=player["jump"]["col"], 
                    rows_jump=player["jump"]["rows"], 
                    flip_r_jump=player["jump"]["flip_r"], 
                    flip_l_jump=player["jump"]["flip_l"],
                    path_fall=player["fall"]["path"], 
                    col_fall=player["fall"]["col"], 
                    rows_fall=player["fall"]["rows"], 
                    flip_r_fall=player["fall"]["flip_r"], 
                    flip_l_fall=player["fall"]["flip_l"],
                    path_hit=player["hit"]["path"], 
                    col_hit=player["hit"]["col"], 
                    rows_hit=player["hit"]["rows"], 
                    flip_r_hit=player["hit"]["flip_r"], 
                    flip_l_hit=player["hit"]["flip_l"],
                    x=player["char"]["x"], y=player["char"]["y"], 
                    lives=player["char"]["lives"], 
                    speed_walk=player["char"]["speed_walk"], 
                    gravity=player["char"]["gravity"], 
                    jump_power=player["char"]["jump_power"],
                    frame_rate_ms=player["char"]["frame_rate_ms"], 
                    move_rate_ms=player["char"]["move_rate_ms"], 
                    jump_height=player["char"]["jump_height"], 
                    interval_time_jump=player["char"]["interval_time_jump"]
                        )
                    )
        self.__player_dicc.clear()    

    def crear_balas(self):
        for bala in self.__lista_balas_dicc:
            self.__lista_balas.append(
                Item_bala(
                    path = bala["path"], 
                    col = bala["col"],
                    rows = bala["rows"],
                    x = bala["x"],
                    y = bala["y"],
                    scale = bala["scale"],
                    gravity = bala["gravity"],
                    frame_rate_ms = bala["frame_rate_ms"],
                    move_rate_ms = bala["move_rate_ms"] 
                )
            )        
        self.__lista_balas_dicc.clear() 

    def crear_vida_box(self):
        for vida in self.__lista_vida_box_dicc:
            self.__lista_vida_box.append(
                Vida_box(
                    path=vida["path"],
                    col=vida["col"],
                    rows=vida["rows"],
                    y=vida["y"],
                    x=vida["x"],
                    gravity=vida["gravity"],
                    frame_rate_ms=vida["frame_rate_ms"],
                    move_rate_ms=vida["move_rate_ms"]
                )
            )        
        self.__lista_vida_box_dicc.clear() 



    def crear_proyectil(self):
        for proyectil in self.__lista_proyectil_dicc:
            self.__lista_proyectil.append(
                Proyectil(
                        path=proyectil["path"],
                        w=proyectil["w"],
                        h=proyectil["h"],
                        speed=proyectil["speed"]
                )
            )
        return self.__lista_proyectil
    
    
    def crear_proyectil_enemy(self):
        for proyectil in self.__lista_proyectil_enemy_dicc:
            self.__lista_proyectil_enemy.append(
                Proyectil(
                        path=proyectil["path"],
                        w=proyectil["w"],
                        h=proyectil["h"],
                        speed=proyectil["speed"]
                )
            )
        return self.__lista_proyectil_enemy
    

    '''
    def recargar_proyectil(self):
        self.crear_proyectil()
        return self.proyectil
    '''    

    @property
    def walkers(self):
        return self.__lista_walkers

    @property
    def shooters(self):
        return self.__lista_shooters

    @property
    def boss(self):
        return self.__lista_enemigo_boss[0]

    @property
    def player(self):
        return self.__player[0]

    @property
    def balas(self):
        return self.__lista_balas
    
    @property
    def vida_box(self):
        return self.__lista_vida_box
    
    @property
    def proyectil_player(self):
        return self.__lista_proyectil

    @property
    def proyectil_enemy(self):
        return self.__lista_proyectil_enemy
    
    @property
    def imagen_fondo(self):
        return self.__imagen_fondo

    @property
    def plataformas(self):
        return self.__lista_plataformas

    @property
    def trampas(self):
        return self.__lista_trampas

    @property
    def voladores(self):
        return self.__lista_enemigo_volador
