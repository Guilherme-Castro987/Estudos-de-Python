'''
Crie funções que duplicam, triplicam, quadruplicam o número recebido como parâmetros
'''
def criar_multiplicador(multiplicador): # Cria uma função que vai criar outra função para realizar a multiplicação
    def multiplicar(numero): # Função que solicita o multiplicador que desejamos
        return numero * multiplicador # aqui ela esta usando o parâmetro da fução externa com a interna dela mesma 
    return multiplicar # ao final ela retorna a própria função interna

duplicar = criar_multiplicador(2) # aqui criamos outra função, dentro de uma variavel

print(duplicar(2)) # aqui usamos a função e adicionamos o valor de argumento da função interna para o parâmetro.


