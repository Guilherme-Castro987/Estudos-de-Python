def meu_decorador(funcao_original):
    def embrulho():
        print('----inicio da execução-----')
        funcao_original() # Aqui executamos a função que recebemos
        print('----fim da execução-----')
    return embrulho

def dizer_oi():
    print('oi')

nova_funcao = meu_decorador(dizer_oi)
nova_funcao()