# A função map() no Python é usada para aplicar uma função a cada item de um iterável (lista, tupla, etc.) e retornar um novo iterador com os resultados.

numeros = [1,2,3,4,5]

dobrados = list(map(lambda x: x*2,numeros)) # Aqui o map pegou cada x da lista numeros e aplicou x * 2.
print(dobrados)

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 40},
]

novos_produtos = list(map(lambda p: {'nome': p['nome'],'preco': p['preco'] * 1.1},produtos))
print(novos_produtos)

# map() é basicamente list comprehension com outra sintaxe
# Este map
n2 = list(map(lambda x: x*2,numeros))
print(n2)
# é igual a essa list comprehension
n3 = [x * 2 for x in numeros]
print(n3)

def maiusculo(texto):
    return texto.upper()

nomes = ['guilherme','fabiane']
nomes_m = list(map(maiusculo,nomes)) # map também usa funções já criadas e não apenas a lambda
print(nomes_m)


def duplicar(value):
    return value *2

lista = list(range(10))

lista_duplicada = list(map(duplicar,lista))
print(lista_duplicada)