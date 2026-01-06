'''
Imagine que você queira criar uma função para calcular o preço final de um produto após um desconto. 🛒

Se a função precisar do preço original e da porcentagem de desconto, como você escreveria a linha do def (o cabeçalho) para essa função?

'''

def calcular_desconto(preco,desconto):
    return f'O preço do produto com o desconto de {desconto} fica de {preco} para {preco - desconto}'


desconto = calcular_desconto(5,2)
print(desconto)