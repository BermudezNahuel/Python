import pygame
from constantes import *
from auxiliar import Auxiliar
from master_gravedad import*

class Player(Gravedad):
    def __init__(self, 
                    path_walk,col_walk,rows_walk,flip_r_walk,flip_l_walk,
                    path_stay,col_stay,rows_stay,flip_r_stay,flip_l_stay,
                    path_jump,col_jump,rows_jump,flip_r_jump,flip_l_jump,
                    path_hit,col_hit,rows_hit,flip_r_hit,flip_l_hit,
                    path_fall,col_fall,rows_fall,flip_r_fall,flip_l_fall,
                    x,y,lives,speed_walk,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,interval_time_jump) -> None:
        
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(path_walk,col_walk,rows_walk,flip_r_walk)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(path_walk,col_walk,rows_walk,flip_l_walk)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(path_stay,col_stay,rows_stay,flip_r_stay)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(path_stay,col_stay,rows_stay,flip_l_stay)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(path_jump,col_jump,rows_jump,flip_r_jump)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(path_jump,col_jump,rows_jump,flip_l_jump)
        self.fall_r = Auxiliar.getSurfaceFromSpriteSheet(path_fall,col_fall,rows_fall,flip_r_fall)
        self.fall_l = Auxiliar.getSurfaceFromSpriteSheet(path_fall,col_fall,rows_fall,flip_l_fall)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet(path_hit,col_hit,rows_hit,flip_r_hit)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet(path_hit,col_hit,rows_hit,flip_l_hit)
    

        self.frame = 0
        self.lives = lives
        self.score = 0
        self.texto_perdio = ""
        self.texto_cronometro= ""
        self.cronometro = 100
        self.tiempo_cronometro = 0
        self.texto_score = ""
        self.move_x = 0
        self.move_y = 0
        self.carga_de_vida = 0
        self.speed_walk =  speed_walk
        self.jump_power = jump_power
        self.gravity = gravity
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height-5)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.bala_collition_rect = pygame.Rect(self.collition_rect)
        self.bala_collition_rect.h = 25

        self.is_fall = False
        self.is_jump = False
        self.injured = False
        self.aumentar_vida = False
        self.invencibilidad= False
        self.aumentar_puntos = False

        self.tiempo_transcurrido = 0

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        self.tiempo_hit_animation = 0

        self.sonido_salto = pygame.mixer.Sound("PIXEL ADVENTURE\sonido_salto.mp3")
        self.sonido_salto.set_volume(0.3)


    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 1)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
                #self.sonido_salto.play()
            else:
                self.move_x = int(self.move_x / 1)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
                #self.sonido_salto.play()
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        #if(self.animation != self.stay_r and self.animation != self.stay_l and self.invencibilidad == False):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self, delta_x):
        super().change_x(delta_x)
        self.bala_collition_rect.x += delta_x

    def change_y(self, delta_y):
        super().change_y(delta_y)
        self.bala_collition_rect.y += delta_y
   
    def do_movement(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
                    if self.direction == DIRECTION_R:
                        self.animation = self.fall_r
                    else:
                        self.animation = self.fall_l
                    self.frame = 0   
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False
        
    def colision_bala(self,bala_enemigo):#Comprueba si existe una colision del enemigo con alguna de las balas. Si existe la colision se modifica la propiedad "eliminada" de bala y "eliminado" del enemigo a True
        tamaño_lista = len(bala_enemigo.lista_draw)
        for i in range(tamaño_lista):
                if self.bala_collition_rect.colliderect(bala_enemigo.lista_draw[i].collition_rect):
                    self.injured =True
                    bala_enemigo.lista_draw[i].eliminada = True
    

    def modo_invencible(self,delta_ms):
        if self.injured:
            self.invencibilidad = True
            self.tiempo_transcurrido += delta_ms
            if self.tiempo_transcurrido > 2000:
                self.tiempo_transcurrido = 0
                self.invencibilidad = False

    def damage(self):
        if self.injured and not self.invencibilidad:
            if self.lives > 0:
                self.lives -= 1
            self.injured = False
            if(self.direction == DIRECTION_R):
                self.change_x(-70)
            else:
                self.change_x(+70)

    def recargar_vida(self):
        if self.aumentar_vida:
            self.lives += self.carga_de_vida
            if self.lives > 5:
                self.lives = 5
            self.aumentar_vida = False
    
    def manejar_score(self,lista_enemigos):
        for enemy in lista_enemigos.lista_draw:
            if self.aumentar_puntos:
                self.score += enemy.score
                self.aumentar_puntos = False


    def mostrar_score(self,fuente_dos):
        self.texto_score = fuente_dos.render("Score: {0}".format(self.score),0,BLACK)

    def mostrar_cronometro(self,fuente_dos,delta_ms,boss):
        if not boss.eliminado:
            self.tiempo_cronometro += delta_ms
            if self.tiempo_cronometro >= 1000:
                self.cronometro -= 1
                self.tiempo_cronometro = 0
            self.texto_cronometro = fuente_dos.render("Tiempo: {0}".format(self.cronometro),0,BLACK)

    def update(self,delta_ms,plataform_list,bala_enemigo,lista_enemigos,fuente_dos,boss):
        self.damage()
        self.modo_invencible(delta_ms)
        self.recargar_vida()
        self.colision_bala(bala_enemigo)
        self.manejar_score(lista_enemigos)
        self.mostrar_score(fuente_dos)
        self.mostrar_cronometro(fuente_dos,delta_ms,boss)
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        #self.game_over(fuente_dos)
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,255),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=GREEN,rect=self.bala_collition_rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        screen.blit(self.texto_score,(850,50))
        screen.blit(self.texto_cronometro,(700,50))


    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()

        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido
