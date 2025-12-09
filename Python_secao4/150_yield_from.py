# yield from
# essa função permite chamar outras generator function...


def gen1 (): # aqui eu criei uma generator function
    print('começou gen1') # após chamar o yield from, ele entra aqui.
    yield 1
    yield 2 
    yield 3
    print('terminou gen1') # e finaliza aqui, voltando para o gen2


def gen2(): # aqui criei outra
    print('começou gen2') # como eu chamei o gen2, ele vai começar por aqui, até chegar no yield from e chamar o gen1
    yield from gen1() # porém usado o yield from, me permite continuar de onde a função antiga termina
    yield 4
    yield 5
    yield 6
    print('terminou gen2') # aqui finalizado tudo.

generator = gen2() # aqui chamamos a segunda função que vai chamar a primeira 

for numero in generator:
    print(numero)