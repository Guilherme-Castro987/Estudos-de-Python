# count é um iterator infinito ( itertools)
from itertools import count

c1 = count()
c2 = range(10)

print(next(c1))
print(next(c1))
print(next(c1))

print('c1', hasattr(c1,'__iter__')) # Aqui eu consigo ver se o c1 é um interavel, para que o count funcione
print('c1', hasattr(c1,'__next__')) # Aqui eu vejo que alem de um iteravél ele também tem um iterator dentro dele, pois ele possuí o método __next__

# Aqui vamos ver que o range é um iteravel porém não possui um iterator nele
print('c2', hasattr(c2,'__iter__'))
print('c2', hasattr(c2,'__next__'))