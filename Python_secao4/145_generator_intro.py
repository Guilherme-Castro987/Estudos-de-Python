import sys

# Generator são funções que sabem 'pausar' elas não ocorrem de uma única vez

lista = [ n for n in range(10000)] # igual uma lista que é crida toda ao mesmo tempo, ela salva de uma única vez  todos os valores na memória.
generator = (x for x in range(10000))

print(sys.getsizeof(lista)) # a lista tem 85.176 bytes, e vai aumentando de acordo com o tamanho dela.
print(sys.getsizeof(generator)) # esse generator tem 192 bytes, e sempre vai ter esse valor

# A função 'getsizeof' mostra o tamanho do objeto em bytes


print(next(generator))
print(next(generator)) # assim conseguimos usar o next também nele, porém sem precisar criar a lista inteira de uma única vez.
print(next(generator))
print(next(generator))

# vantagens da lista é que como ela é criada de uma vez eu posso acessar qualquer valor dela, cosigo usar o len para contar etc...