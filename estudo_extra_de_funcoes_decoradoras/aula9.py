def meu_decorador(funcao_original):
    def embrulho(*args,**kwargs): # A mochila aceita tudo
        print('------inicio-------')
        funcao_original(*args,**kwargs) # Passa tudo para a original
        print('------fim-------')
    return embrulho
@meu_decorador
def exibe_nome(nome):
    print(nome)

exibe_nome('Guilherme')