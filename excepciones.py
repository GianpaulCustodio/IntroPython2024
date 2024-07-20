try:
    lista = [1,2,3,4]
    print(lista[70])
except IndexError as e:
    print("No compila porque el error es: ",e)