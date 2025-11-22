def executa(funcao,*args):
    return funcao(*args)


def soma(x,y):
    return x + y # aqui é uma função que soma dois números usando def normalmente

soma2 = lambda x,y: x + y # neste caso eu criei e mesma função porém em lambda
print(soma2(5,5)) # necessário passar os argumentos, saída 10


def cria_multiplicador(multiplicador): # aqui é uma fução que chama outra função e realizar a multiplicação
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


multiplicar = lambda m: lambda n: n * m # aqui é a mesma função, uma lambda chamando outra e realiza a multiplicação
print(multiplicar(5)(5)) # por ter uma função dentro da outra, é necessário passar os argumentos separados


multiplicar2 = cria_multiplicador(5) # chamando a função convencional 
print(multiplicar2(5)) # como o primeiro argumento já foi passado direto na função, aqui passamos apenas o segundo argumento.