import sqlite3

class High_score:
    def __init__(self) -> None:
        self.datos = ()
        self.score_max = []

    def crear(self):
        with sqlite3.connect("bd_highscore.db") as conexion:
            try:
                sentencia = ''' create  table personajes
                                (
                                        id integer primary key autoincrement,
                                        nombre text,
                                        puntaje real
                                )
                            '''
                conexion.execute(sentencia)
                print("tabla highscore")                       
            except sqlite3.OperationalError:
                print("La tabla highscore ya existe")    


    def agregar(self,datos):
        with sqlite3.connect("bd_highscore.db") as conexion:
            try:
                conexion.execute("insert into personajes(nombre,puntaje) values (?,?)", datos) 
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")


    def consultar_scores(self):
        with sqlite3.connect("bd_highscore.db") as conexion:
            cursor=conexion.execute('''
                                        SELECT nombre, puntaje
                                        FROM personajes 
                                        ORDER BY puntaje DESC
                                        LIMIT 5;
                                    '''
                                    )
            for fila in cursor:
                self.score_max.append(fila)
        return self.score_max

    def eliminar(self,id):
        id = id
        with sqlite3.connect("bd_highscore.db") as conexion:
            sentencia = "DELETE FROM personajes WHERE id=?"
            conexion.execute(sentencia,(id,))

    def update(self):
        '''
        Actualiza los metodos propios de la clase
        '''
        self.consultar_scores()
        
data = High_score()

id = "4"

data.eliminar(id)


