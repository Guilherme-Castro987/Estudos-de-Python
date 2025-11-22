lista = [1,5,2,9,5,9,3]
lista.sort()
# sorted(lista)    porém essa cria uma nova lista ordenada
print(lista)

lista2 = [
    {'nome':'Guilherme','idade':28},
    {'nome':'daniel','idade':16},
    {'nome':'miguel','idade':9},
    {'nome':'fabiane','idade':34},
    {'nome':'lucas','idade':27},
]

lista2.sort(key=lambda item: item['idade'])

for i in lista2:
    print(i)


print()
print()
print()

n1 = 10
n2 = 10
soma = lambda parametro1,parametro2: parametro1 + parametro2
print(soma(5,5))