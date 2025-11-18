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

d1 ={
    'chave1': 1,
    'chave2': 2,
    'lista':[0,1,2],
}

d2 = d1 # nesse caso o d2 não esta recebendo o valor de d1, mas sim apontando para d1

d2['chave1'] = 1000
print(d1) # nesse caso, mesmo alterando o d2, oque esta sendo alterado é o valor de d1 no qual ele esta se referindo
# então nesses casos, se quiser copiar os dados não é dessa forma que se faz, dessa forma é apenas para se referir ao valores.

#---------------------------------------------------------------------------------------------------------------------
print(50*'-')
# exemplo de copia rasa
d2 = d1.copy() # isso é uma cópia rasa, porém ela não copia dados mutaveis, exemplo de uma lista
d2['chave1'] = 50
print(d2)
d2['lista'][0] = 15 # neste caso estou tentando alterar o valor da lista dentro do dict, porém os dois estão apontando para o mesmo lugar
print(d2)

# impartar o deppcopy que é a cópia profunda
print(50*'-')
import copy

d3 = copy.deepcopy(d1) # Neste caso estamos fazendo uma cópia profunda
print(d3) # Esse tipo de cópia copia profundamente oque você quer.