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
pessoa1 = {
    'nome': 'Guilherme',
    'sobrenome': 'Castro',
    'idade': 28,
}
nome = pessoa1.pop('nome') # neste caso, estou apagando a chave 'nome' e adicionando o valor dela a variável nome
print(nome) # mostra o valor de nome 'Guilherme' nesse exemplo.
print(pessoa1) # mostra o dict porém sem a chave nome e seu valor Guilherme
pessoa1.popitem() # remove a última chave do dict
print(pessoa1) # dict sem a chave 'idade'
print(20*'-')
pessoa2 = {
    'nome' : 'Fabiane',
    'sobrenome' : 'Thais',
    'idade' : 34,
}
pessoa2.update({
    'nome': 'Fabi',
    'profissão':'Analista'
}) # Esse metodo atualiza o meu dict, exemplo, eu alterei o nome, e adicionei a profissão
print(pessoa2) # Neste caso, agora o nome é Fabi e temos a chave profissão com o valor analista
pessoa2.update(nome = 'Fabi',sobrenome ='Lopes') # Dessa forma tmabém funciona o update()