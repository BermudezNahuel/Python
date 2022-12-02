import json
from enemigo_walking import Enemigo_walker
from enemigo_shooter import Enemigo_shooter
from enemigo_boss import Enemigo_boss
from player import Player
from item_balas import Bala
from item_vida_box import Vida_box
from proyectil import Proyectil

class Json_manager:
    def __init__(self,path,nivel_nombre) -> None:
        self.path = path
        self.config_nivel = self.leer_json(self.path)[nivel_nombre]
        #Enemigos
        self.__lista_walkers_dicc = self.config_nivel["enemigos_walkers"]
        self.__lista_walkers = []
        self.crear_walkers()
        self.__lista_shooters_dicc = self.config_nivel["enemigos_shooters"]
        self.__lista_shooters = []
        self.crear_shooters()
        self.__lista_enemigo_boss_dicc = self.config_nivel["enemigo_boss"]
        self.__lista_enemigo_boss = []
        self.crear_enemigo_boss()

        #Player
        self.__player_dicc = self.config_nivel["player"]
        self.__player = []
        self.crear_player()
        #proyectil
        self.__lista_proyectil_dicc = self.config_nivel["proyectil"]
        self.__lista_proyectil = []
        self.crear_proyectil()
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
        self.__lista_walkers_dicc.clear()

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
                            gravity=enemigo["gravity"],
                            frame_rate_ms=enemigo["frame_rate_ms"],
                            move_rate_ms=enemigo["move_rate_ms"])
            )
        self.__lista_shooters_dicc.clear()


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
                )
            )        
        self.__lista_enemigo_boss_dicc.clear() 

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
                Bala(
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
        print("se llamo a crear proyectil")
        for proyectil in self.__lista_proyectil_dicc:
            self.__lista_proyectil.append(
                Proyectil(
                        path=proyectil["path"],
                        w=proyectil["w"],
                        h=proyectil["h"],
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
                )
            )
        #self.__lista_proyectil_dicc.clear()
    

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
