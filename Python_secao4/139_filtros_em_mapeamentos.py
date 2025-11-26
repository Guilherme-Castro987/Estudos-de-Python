# Podemos realizar todos os tipo de filtros nas listas e em dicionários também.
# Temos 2 tipos de filtros 

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_filtrados = list(filter(lambda x: x>5,numeros)) # nesse caso usando a função filter, onde usamos a função lambda e a condição
print(numeros_filtrados) # Saída: [6, 7, 8, 9, 10]

pessoas = [
    {"nome": "Ana", "idade": 15},
    {"nome": "Guilherme", "idade": 28},
    {"nome": "Fabiane", "idade": 34},
]

adultos = list(filter(lambda i: i['idade'] >= 18,pessoas)) # também podemos usar a mesma função em dicionários usando o filter
print(adultos) # Saída: [{'nome': 'Guilherme', 'idade': 28}, {'nome': 'Fabiane', 'idade': 34}]

# oque vem a esquerda do 'for' é mapeamento, a direita é filtro.
lista = [n for n in range(10) if n < 5]  # neste caso estamos usando o um 'filtro' usando o if dentro da nossa list comprehension
print(lista) # saída: [0, 1, 2, 3, 4]

print(50*"-")

produtos = [
    {'p1': 'produto 1','preco': 10},
    {'p2': 'produto 2','preco': 20},
    {'p3': 'produto 3','preco': 30},
    {'p4': 'produto 4','preco': 40},
]

produtos_filtrados = list(filter(lambda p: p['preco'] >= 20,produtos)) # aqui estamos novamente filtrando um dict que esta dentro de uma list, usando a função filter com a lambda.
print(produtos_filtrados) # Saída: [{'p2': 'produto 2', 'preco': 20}, {'p3': 'produto 3', 'preco': 30}, {'p4': 'produto 4', 'preco': 40}]

# No caso abaixo, estou realizando o mesmo filtro que a função filter acima, porém usando apenas list comprehension.
produtos_filtrados2 = [item for item in produtos if item['preco']>=20]
print(produtos_filtrados2) # Saída: [{'p2': 'produto 2', 'preco': 20}, {'p3': 'produto 3', 'preco': 30}, {'p4': 'produto 4', 'preco': 40}]



