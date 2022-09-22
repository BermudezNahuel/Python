def calcula_maximo_minimo(lista:list,clave:str,tipo:str) -> dict:
    '''
    Calcula el maximo/minimo en base a la clave recibida
    
    Recive una lista de diccionarios, la clave que se utilizara para calcular
    y el tipo de calculo a realizar ("maximo" o "minimo")
    
    Retorna el diccionario que contienen el maximo/minimo o -1 en caso de error
    '''
    retorno = -1
    if(type(lista) == type(list()) and type(clave) == type(str()) and len(lista) > 0):
        max_min = lista[0]
        for video in lista:
            if(tipo == "maximo" and (video[clave] > max_min[clave])):
                max_min = video
            if(tipo == "minimo" and (video[clave] < max_min[clave])):
                max_min = video
        retorno = max_min
    
    return retorno

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

def transformar_fecha_carga(date:str)->dict:
    '''
    Transforma un str con el formato     
        2022-07-06 00:00:00
    en un diccionario
    {   
        "fecha" : "6/7/2022"
        "hora" : "00:00:00"
    } 
    '''
    fecha,hora=date.split(" ")
    anio,mes,dia=fecha.split("-")
    dict_date = {}
    dict_date["fecha"] = "{0}/{1}/{2}".format(dia,mes,anio)
    dict_date["hora"] =  hora
    return dict_date
                
    
def transformar_titulo(titulo:str) -> dict:
    '''
    Si es una session tiene la siguiente forma
        ['QUEVEDO', '||', 'BZRP', 'Music', 'Sessions', '#52']
    => puedo armar el diccionario
            {   
                "tipo" : "BZRP MUSIC SESSIONS"
                "artista" : "Quevedo"
                "numero" :  52
            }
    Sino es un session
    => retornara el diccionario 
            {   
                "tipo" : "NO SESSIONS"
            }
    '''
    retorno={}
    lista_titulo = titulo.split('BZRP Music Sessions')
    if(len(lista_titulo)==2):
        #Si entro es un titulo de session
        retorno["tipo"] = "BZRP Music Sessions".upper()
        retorno["artista"] = lista_titulo[0].capitalize().replace("||","").strip()
        retorno["numero"] = lista_titulo[1].replace("#","").strip()
    else:
        retorno["tipo"] = "NO SESSIONS"
    
    return retorno

def test(lista:list):
    for tema in lista:
        nuevo_titulo =  transformar_titulo(tema["title"])
        nueva_fecha = transformar_fecha_carga(tema["date"])
        if(nuevo_titulo["tipo"] != "NO SESSIONS"):
            texto = '''
            Tipo : {0}
            Artista: {1}
            Número:  {2}
            Fecha: {3}
            Hora: {4}'''
            print(texto.format(nuevo_titulo["tipo"],
                               nuevo_titulo["artista"],
                               nuevo_titulo["numero"],
                               nueva_fecha["fecha"],
                               nueva_fecha["hora"]))
            
            
