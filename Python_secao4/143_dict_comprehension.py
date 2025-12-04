produto = {
    'nome':'Caneta Azul',
    'preco': 2.5,
    'categoria': 'escritorio',
}

dc = {chave : valor for chave,valor in produto.items()}
print(dc)

set1 = {x for x in range(10)}
print(set1)