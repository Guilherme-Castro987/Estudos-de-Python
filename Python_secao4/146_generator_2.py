
def generator(n=0): # toda função que tem o yield é uma genertor function
    yield 1  # yield tem a funsão de pausar
    print('continuando...') # essa parte é executada após a chamada do next da segunda vez, pois esta no meio entre a primeira e a segunda.
    yield 2 # para pular para o próximo yield é necessário o next
    return 'acabou' # essa parte do código só vai aparecer quando estourar uma excessão.

gen = generator(n=0)
print(next(gen)) # usando o yield podemos usar o next, igual fazemos com o iterator 
print(next(gen)) # como temos 2 yield dentro da generator function podemos usar mais um next
# print(next(gen)) # Se esse print estiver ativo, vai dar um erro de Stopinterator: 'acabou' pois vai retornar no erro, o meu 'return' da minha função.
# no caso acima como estamos chamando mais uma vez o print('continuando..') vai ser executado.


def generator2(inicio = 0 , fim = 10):
    while True: # aqui foi criado um loop infinito dentro da generator function para percorrer toda a função e pausar de acordo com os yield.
        yield inicio 
        inicio += 1
        if inicio > fim:
            return 'acabou..'

gen2 = generator2(10,30) # aqui criamos uma 'cópia' do range(10,30)
for i in gen2: # aqui usamos um for para percorrer dentro da função respeitando as pausas do yield.
    print(i)