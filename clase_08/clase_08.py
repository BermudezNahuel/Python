import json

'''
with open("data.jason") as file:
    data

De esta manera se arma la lista

def parse_csv("nombre_archivo":str) ->list: 
    lista_rta = []
    archivo = open(nombre_archivo,"r")
    for linea in archivo:
        linea.split(",")
        video = {}
        video["title"] = lista[0]
        video["views"] = lista[1]
        video["length"] = lista[2]
        video["img_url"] = lista[3]
        video["url"] = lista[4]
        video["date"] = lista[5]
        lista_rta.append(video)
    archivo.close
    return lista_rta

lista_bzrp = parse_csv("ruta del archivo")
print(lista_bzrp)

______________________________________________________________________________________

def generar_csv(lista):
    with open(nombre_archivo,"w") as archivo
        for video in lista:

            mensaje = "{0},{1},{2},{4},{5}"
            mensaje = mensaje. format ( video["title"],
                                        video["views"],
                                        video["length"],
                                        video["img_url"],
                                        video["url"],
                                        video["date"]
                                        )
            archivo.write(mensaje)

lista_bzrp = parse_csv("ruta del archivo")
print(lista_bzrp)


____________________________________________________________________________________

def parse_json(n_archivo:str) ->list:
    with open(n_archivo,"r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["bzrp]

lista_bzrp = parse_json("ubicacion del archivo")
#print(lista)

bzrp_app(lista_bzrp)















'''