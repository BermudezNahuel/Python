from data_stark import lista_personajes
'''
{
'nombre': 'Howard the Duck', 
'identidad': 'Howard (Last name unrevealed)', 
'empresa': 'Marvel Comics', 
'altura': '79.349999999999994', 
'peso': '18.449999999999999', 
'genero': 'M', 'color_ojos': 
'Brown', 'color_pelo': 'Yellow', 
'fuerza': '2', 'inteligencia': ''
}
'''
altura_max = float(lista_personajes[0]['altura'])

for heroes in lista_personajes:
    altura = float(heroes['altura'])
    if altura > altura_max:
        altura_max = altura
        altura_max_nombre = heroes['nombre']
print(altura_max_nombre, altura_max)
    

