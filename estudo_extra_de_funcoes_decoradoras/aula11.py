def duplicar(func):
    def embrulho(*args,**kwargs):
        print('Duplicando a função original')
        func(*args,**kwargs)
        resultado = func(*args,**kwargs)
        print('Função original duplicada')
        return resultado
    return embrulho
@duplicar
def exibe_qualquer_coisa(*args,**kwargs):
    print(args,kwargs)

exibe_qualquer_coisa('Guilherme',idade = 28)