import time

def cronometrar_funcao(func):
    def interna(*args,**kwargs):
        inicio = time.time()
        resultado = func(*args,**kwargs)
        fim = time.time()
        print(f'O tempo total foi de {fim - inicio} segundos')
        return resultado
    return interna

@cronometrar_funcao
def loop_em_lista(*args,**kwargs):
    for x in args:
        print(x)

loop_em_lista(1,2,3,4,5,6)