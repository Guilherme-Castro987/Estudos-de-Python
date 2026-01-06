from time import sleep
from functools import wraps # 1. Importamos a ferramenta

def atrasar(segundos):
    def principal(func):
        @wraps(func) # 2. Usamos o wraps antes da função interna
        def interna(*args, **kwargs):
            sleep(segundos)
            result = func(*args, **kwargs)
            return result
        return interna
    return principal

@atrasar(2)
def dizer_oi():
    """Esta função diz oi."""
    print('Oi')

dizer_oi()
print(dizer_oi.__name__) # Agora imprimirá 'dizer_oi'!