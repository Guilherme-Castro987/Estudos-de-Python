produtos = [
    {'nome': 'p1', 'preco':20},
    {'nome': 'p2', 'preco':30},
    {'nome': 'p3', 'preco':40},
]

novos_produtos = [produto['nome'] for produto in produtos]
print(*novos_produtos, sep='\n')