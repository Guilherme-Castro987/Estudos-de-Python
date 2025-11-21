lista_de_lista_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,2,4,5,6,6,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,4,3,2,1],
    [1,2,3,6,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,2,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
]

def encontra_primeiro_duplicado(lista_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

for lista in lista_de_lista_de_inteiros:
    print(encontra_primeiro_duplicado(lista))