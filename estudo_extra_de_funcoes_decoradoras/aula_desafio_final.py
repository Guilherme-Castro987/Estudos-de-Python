from functools import wraps
nivel_necessario = 10

def validar_nivel(nivel_usuario):
    def decorador(func):
        @wraps(func)
        def interna(*args,**kwargs):
            if nivel_usuario >= nivel_necessario:
                result = func(*args,**kwargs)
                return result
            else:
                print('Acesso negado')
        return interna
    return decorador

@validar_nivel(11)
def abrir_sistema():
    print('Sistema foi liberado')


abrir_sistema()
print(abrir_sistema.__name__)