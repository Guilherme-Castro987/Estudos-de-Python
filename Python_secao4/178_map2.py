notas = [10,20,30,40]

notas_mais_5 = list(map(lambda x: x + 5,notas))
# o map usa uma determinada função que você escolhe e distribui ela para todos os valores da lista
print(notas_mais_5)

# aqui estou fazendo a mesma coisa, porém usando uma list comprehension
notas2 = [x + 5 for x in notas]
print(notas2)