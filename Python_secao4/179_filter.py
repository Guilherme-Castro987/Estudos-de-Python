# filter é um filtro funcional

def print_iter(iterador):
    print(*list(iterador),sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# podemos usar um filtro dentro da list comprehesion ( programação estruturada)
novos_produtos = [p for p in produtos if p['preco'] > 10]

# podemos usar um filtro usando a função filtro ( programação funcional)
novos_produtos_com_filter = filter(lambda p: p['preco'] > 100 , produtos)
# para o filter usamos primeiro a função que queremos, para definir o filtro e em seguida a lista (iterador) que queremos fazer isso


print_iter(produtos)
print_iter(novos_produtos)
print_iter(novos_produtos_com_filter)