def validar_largo(objeto):
    '''
    Valida que el largo del elemento sea mayor a 0
    Si se cumple retorna un True, sino un False
    Objeto: elemento a medir
    '''
    if len(objeto) > 0:
        retorno = True
    else:
        retorno = False
    return retorno

def validar_entero(objeto:int):
    '''
    Valida si el elemento es un entero, si esto es verdad
    devuelve un True, sino un false

    objeto: ingresar un elemento
    '''
    if type(objeto) == int:
        retorno = True
    else:
        retorno = False
    return retorno

def validar_str(objeto:str):
    '''
    Valida si el elemento es un string, si esto es verdad
    devuelve un True, sino un false

    objeto: ingresar un elemento
    '''
    if type(objeto) == str:
        retorno = True
    else:
        retorno = False
    return retorno

def validar_float(objeto:float):
    '''
    Valida si el elemento es un flotante, si esto es verdad
    devuelve un True, sino un false

    objeto: ingresar un elemento
    '''
    if type(objeto) == float:
        retorno = True
    else:
        retorno = False
    return retorno

def validar_dicc_no_vacio(objeto:dict):
    '''
    Validad que el objeto sea una diccionario y este no este vacio
    si cumple los requisitos retorna un True, sino un False
    objeto: ingresar una diccionario
    '''
    if type(objeto) == dict and validar_largo(objeto):
        retorno = True
    else:
        retorno = False
    return retorno

def validar_lista_no_vacia(objeto:list):
    '''
    Validad que el objeto sea una lista y esta no este vacia
    si cumple los requisitos retorna un True, sino un False
    objeto: ingresar una lista
    '''
    if type(objeto) == list and validar_largo(objeto):
        retorno = True
    else:
        retorno = False
    return retorno
        