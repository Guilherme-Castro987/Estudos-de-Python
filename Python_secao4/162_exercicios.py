import copy
# Exercícios 
produtos = [
    {'nome':'Produto 5','preco': 10.00},
    {'nome':'Produto 1','preco': 22.32},
    {'nome':'Produto 3','preco': 10.11},
    {'nome':'Produto 2','preco': 105.87},
    {'nome':'Produto 4','preco': 69.90},

]
# Aumente o preço dos produtos em 10%
# Gere novos produtos por deep copy ( cópia profunda )

copia_profunda = copy.deepcopy(produtos)
for produto in copia_profunda:
    produto['preco'] = round(produto['preco'] * 1.1 , 2)
    print(produto,sep="\n")

# Ordene os produtos por nome decrescente 
# Gere produtos ordenados por nome por deep copy

produtos_ordenados_por_nome= sorted(
    copy.deepcopy(produtos),key= lambda p: p['nome'],
    reverse= True
)

print(*produtos_ordenados_por_nome,sep='\n')

# Ordene os produtos por preco crescente 
# Gere produtos ordenados por preco por deep copy

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), key= lambda i: i['preco'],
)
print(*produtos_ordenados_por_preco,sep='\n')