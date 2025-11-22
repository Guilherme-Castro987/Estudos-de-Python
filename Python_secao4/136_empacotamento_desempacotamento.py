# Empacotamento e desempacotamento de dicionários
a,b = 1,2
a,b = a,b
print(a,b)


pessoa = {
    'nome':'guilherme',
    'sobrenome': 'castro'
}

x,y = pessoa.values() # por padrão quando desempacotamos um dict pegamos apenas o valor das chaves, mas colocando um método após o dict podemos mudar isso.
print(x,y) # saída: guilherme castro


dados_da_pessoa = {
    'idade': 28,
    'altura': 1.80,
}


pessoa_completa = {**pessoa,**dados_da_pessoa} # dessa forma conseguimos realizar a extração dos 2 dicts que unilos a uma única variavél.
print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments ( argumentos nomeados)

def mostro_argumentos_nomeados(*args,**kwargs):
    for chave , valor in kwargs.items():
        print(f'{chave}: {valor}')

mostro_argumentos_nomeados(nome = 'guilherme',sobrenome = 'castro')

# **kwargs te permite passar um dicionário como argumento de uma função.

 