'''
Métodos útis dos dicionários em Python
Len - conta a quantidade de CHAVES ( não é um método pois não é algo  que esta dentro do dicionário)
Keys - iterável com as chaves
Values - iterável com os valores
setdefault - adiciona valor se achave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave 
pop - Apaga um item com a chave especificada(del)
popitem - apaga o último item adicionado
update - Atualiza um dicionário com outro
'''

pessoa = {
    'nome': 'Guilherme',
    'sobrenome': "Castro",
    #'idade': 28,
}

pessoa.setdefault('idade',0) # adicionando um valor a chave idade se ela não existir

usando_len_de_outra_forma = pessoa.__len__()
qnt_chaves = len(pessoa)
print(usando_len_de_outra_forma)
print(qnt_chaves)
print(list(pessoa.keys()))
print(list(pessoa.values())) # apenas alterando o valor para uma lista.
print(50*'-')
for valor in pessoa.values(): # fazendo um loop para ver os valores dentro das chaves do nosso dict
    print(valor)
print(50*'-')
for valor in pessoa: # fazendo um loop para ver as chaves
    print(valor)
print(50*'-')
for chave,valor in pessoa.items(): # fazendo um loop para ver as chaves e os valores juntos.
    print(chave , valor)