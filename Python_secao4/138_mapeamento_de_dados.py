produtos = [
    {'nome': 'p1', 'preco':20},
    {'nome': 'p2', 'preco':30},
    {'nome': 'p3', 'preco':40},
]
# mapeamento é quando pegamos cada item de uma lista e transforma em outro valor 
novos_produtos = [produto['nome'] for produto in produtos]
print(*novos_produtos, sep='\n')
print()
nomes = [p['nome'] for p in produtos] # aqui estou criando uma nova lista, porém apenas com os nomes
print(nomes)
print()
precos = [p['preco'] for p in produtos] # aqui estou criando uma nova lista, porém apenas com os preços
print(precos)
print()
preco_ajustado = [
    {'nome': p['nome'],'preco':p['preco'] * 1.10} # aqui estou criando a mesma lista, porém com os preços 10% maiores.
    for p in produtos
]
print(preco_ajustado)

# Ou seja, sempre que você cria uma nova lista, usando dados de outra lista, ou percorre uma lista para alterar dados.
# isso é o mapeamento de dados.