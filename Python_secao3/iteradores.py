'''
Iteravél : str, range(), etc  (__iter__)
Iterador : é quem sabe passar um valor por vez
next : me entrega o próximo valor
iter : me entrega seu iterador
'''
# for letra in texto
texto = 'Gui' # Iteravél
iterador = iter(texto) # Iterador

while True:
    try:
        letra = next(iterador)
        print(letra)                # É assim que o FOR funciona pr baixo dos panos
    except StopIteration:
        break


# nome = iter('Guilherme')
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())

# numeros = str(12345)
# print(type(numeros))
# for numero in numeros:
#     print(numero)