import sqlite3

class High_score:
    '''
    Esta clase permite modificar la base de datos del jugador para almacenar su puntaje
    '''
    def __init__(self) -> None:
        self.datos = ()
        self.score_max = []

    def crear(self):
        '''
        Este metodo crea la base de datos
        '''
        with sqlite3.connect("bd_highscore.db") as conexion:
            try:
                sentencia = ''' create  table if not exists personajes
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
        '''
        Este metodo permite agregar informacion a la base de datos
        '''
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
        '''
        Este metodo se encarga de eliminar de la base de datos, utilizando como parametro el valor del ID
        '''
        id = id
        with sqlite3.connect("bd_highscore.db") as conexion:
            sentencia = "DELETE FROM personajes WHERE id=?"
            conexion.execute(sentencia,(id,))

    
    '''
    def update(self):
        Actualiza la clase, ejecutando los metodos
        self.consultar_scores()

    '''
'''

data = High_score()

id = "20"

data.eliminar(id)
'''




