'''
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'stars':4,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }

'''
def calcula_maximo_minimo(lista:list,clave:str,tipo:str="maximo")->dict:
    '''
    Calcula el valor maximo/minimo en funcion a la clave recibida
    de una lista de videos
    
    list: tiene que ser una lista de diccionarios
    clave: tiene que representar una clave del dict que contenga un valor numerico
    tipo: solo puede ser "maximo" o "minimo" 
    
    retorno: el elemento(dict) que contiene el valor maximo 
    '''
    elemento_max_min = {}
    if(type(lista) == type([]) and len(lista)>0 and type(clave) == type("")):
        elemento_max_min = lista[0]
        for elemento in lista:
            if(tipo == "maximo"):
                if(elemento[clave] > elemento_max_min[clave]):
                    elemento_max_min = elemento
            elif(tipo == "minimo"):
                if(elemento[clave] < elemento_max_min[clave]):
                    elemento_max_min = elemento           
    return elemento_max_min


def calcular_tema_mas_visto(lista:list):
    #---------TEMA MAS VISTO----------------
    video = calcula_maximo_minimo(lista,"views","maximo")
    mostrar_video(video)
    #-------------------------------------------

def calcular_tema_menos_visto(lista:list):
    #---------TEMA MENOS VISTO----------------
    video = calcula_maximo_minimo(lista,"views","minimo")
    mostrar_video(video)
    #-------------------------------------------  
def calcular_tema_mas_largo(lista:list):
    #--------- TEMA MAS LARGO ----------------
    video = calcula_maximo_minimo(lista,"length","maximo")
    mostrar_video(video)
    #-------------------------------------------
def calcular_tema_mas_corto(lista:list):
    #--------- TEMA MAS CORTO ----------------
    video = calcula_maximo_minimo(lista,"length","minimo")
    mostrar_video(video)
    #-------------------------------------------

def calcular_promedio_tiempo(lista:list):
    # -------- PROMEDIO TIEMPO ------------
    acumulador_tiempo_videos = 0
    for tema in lista:
        acumulador_tiempo_videos = acumulador_tiempo_videos +  tema["length"]

    print("Promedio: {2} - QTY: {0} - ACUM: {1} ".format(len(lista),acumulador_tiempo_videos, acumulador_tiempo_videos/len(lista)))

def calcular_promedio_vistas(lista:list):
    # -------- PROMEDIO VISTAS ------------
    acumulador_vistas_videos = 0
    for tema in lista:
        acumulador_vistas_videos +=  tema["views"]

    print("Promedio: {0:.2f} millones".format((acumulador_vistas_videos/len(lista))/1000000))

def mostrar_video(video:dict):
    mensaje = "Titulo: {0} \nViews: {1:.2f} M \nDuracion: {2} Seg."
    mensaje += "\nPortada: {3} \nLink: {4} M \nFecha: {5}"
    print(mensaje.format(   video["title"],
                            video["views"]/1000000,
                            video["length"],
                            video["img_url"],
                            video["url"],
                            video["date"]))