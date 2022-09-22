'''
caracteres especiales
\n --> permite ingresar un salto de linea

variable.format(variable1, variable2, variable3...)

Metodos de STR: procesan datos string

STRIP
variable.strip() : elimina caracteres en blanco

LOWER
variable.lower(): convierte a las letras a minuscula

UPPER
variable.upper(): convierte la primer letra en mayuscula

REPLACE
variable = "gato"
variable.replace("Parametro1", "Parametro2") 
-Parametro1: ingreso el valor que quiero reemplazar
-Parametro2: ingreso el valor que reemplazara al "Paramentro1"
variable.replace("gato", "perro")
Se reemplaza el valor "gato" por "perro" dentro de la variable

SPLIT
variable.split("parametro")
Este metodo se encarga de separa la cadena utilzando como separador
el parametro ingresado. Este metodo NO DEVUELVE un STRING, sino que devuelve
una LISTA.
varible = "P, C, J".split(",") #['P','c','j']

JOIN
variable = +
variable.join(['A','B','C']) --> devuelve "A+B+C"

ZFILL
variable.zfill(parametro)--> agrega y rellena con 0 hasta completar
el numero de caracteres ingresado en el parametro(se debe ingresar un entero)
variable = "06"
variable.zfill(5) # "00006"

ISALPHA
variable.isalpha() --> devuelve un booleano, evalua si todos los caracteres son alfabeticos

ISALNUM
variable.isalnum() --> devuelve un booleano, evalua si todos los caracteres son alfanumericos

COUNT
variable.count("lo_que_quiero_buscar") --> devuelve la cantidad de ocurrencias que aparecen !!!Devuelve un INT¡¡¡¡

LEN
len(variable) --> devuelve un entero que indica cuantos caracteres componen la cadena

SLICE --> devuelve una cadena nueva
cadena = "Hola mundo"
cadena[parametro1:parametro2]
-parametro1: se debe ingresar un numero que indica donde comenzara el corte
-parametro2: se debe ingresar un numero que indica donde finaliza el corte
print(cadena[5:10]) --> " Mundo"
En el caso que se omita el parametro1, por defecto corta desde el primer caracter 
print(cadena[:5]) --> "Hola"--> devuelve una cadena nueva
En el caso el parametro2, por defecto se toma como fin de corte el ultimo caracter
print(cadena[6:]) --> "Mundo" 

variable = f"Nombre: {nombre_variable}


'''