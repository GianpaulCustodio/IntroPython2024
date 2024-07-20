edad = int(input("Ingrese la edad: "))

mi_diccionario = {
    'nombre' : 'Gianpaul',
    'apellido' : 'Custodio',
    'edad' : 25
}

#Imprimir edad
#print(mi_diccionario['apellido'])

#actualizar diccionario
mi_diccionario['edad'] = edad

#print(mi_diccionario['edad'])
print(f"En Octubre recién cumpliré {mi_diccionario['edad']}")