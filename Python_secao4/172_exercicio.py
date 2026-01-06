# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA','SP','MG','RJ']
# resultado
# [('Salvador', 'BA'),('Ubatuba','SP'),('Belo Horizonte','MG')]

# A função abaixo cumpre o papel de unir as listas
def zipper(lista1,lista2):
    intervalo_maximo = min(len(lista1),len(lista2))
    return [
        (lista1[i],lista2[i]) for i in range(intervalo_maximo)
    ]
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA','SP','MG','RJ']
print(zipper(l1,l2))


# agora outra forma de fazer isso, usando a própria ferrameta do python 'zip'

print(zip(l1,l2)) # aqui ele retorna o local onde esse objeto esta
print(list(zip(l1,l2))) # aqui essa função faz a mesma coisa que a nossa funcao zipper

# em todos esses exemplos estamos usando a lista menor como base

# porém também podemos usar a lista maior como base

from itertools import zip_longest
print(list(zip_longest(l1,l2,fillvalue= "Sem valor"))) # aqui essa função faz a mesma coisa que a nossa funcao porém pegando a lista maior como base
# usamos o método fillvalue para preecher valores 'none'
