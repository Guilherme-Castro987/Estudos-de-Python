# reduce - faz a redução de um iterável em um valor

from functools import reduce


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


total = 0
for x in produtos:
    total += x['preco']
print(total)

print(sum([p['preco'] for p in produtos]))

def funcao_do_reduce(total, produto): # nesta funcão estamos pegando o total 
    return total + produto['preco']


total_reduce = reduce( # aqui estamos colocando o reduce direto em uma variavel contadora
    funcao_do_reduce, # aqui passamos uma função para ele
    produtos, # aqui passamos o iterador
    0 # aqui passamos o valor incial, igual fizemos acima com total = 0
)
print(total_reduce)
