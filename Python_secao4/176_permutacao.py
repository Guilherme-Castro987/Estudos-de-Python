'''
Combinations , Permutations e Product - Itertools
Combinação - ordem não importa  - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - ordem importa e repete valores únicos
'''
from itertools import combinations , permutations , product

pessoas = ['joão','joana','luiz','leticía',]

camisetas = [
    ['preta','branca'],
    ['p','m','g'],
    ['masculino','feminino']
]

print(*list(combinations(pessoas,2)),sep='\n') # aqui estamos criando grupos de 2, mas poderia ser mais 
# com isso, conseguimos formar combinações possiveis 
print(20*'-')
print(*list(permutations(pessoas,2)),sep='\n') # O permutations permite que criemos todos os tipos de grupos possíveis 
print(20*'-')
print(*list(product(*camisetas)),sep='\n')
# Já no  caso do product, ele cria grupos de possiveis junções de cada lista dentro do iteravél