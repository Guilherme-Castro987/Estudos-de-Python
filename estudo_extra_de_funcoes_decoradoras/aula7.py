def meu_decorador(funcao_original):
    def embrulho():
        print('----inicio da execução-----')
        funcao_original() # Aqui executamos a função que recebemos
        print('----fim da execução-----')
    return embrulho

@meu_decorador
def dizer_oi():
    print('oi')

dizer_oi()