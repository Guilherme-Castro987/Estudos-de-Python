from time import sleep

def atrasar(segundos):
    def principal(func):
        def interna(*args,**kwargs):
            sleep(segundos)
            result = func(*args,**kwargs)
            print(f'Sua função foi atrasada {segundos} segundos')
            return result
        return interna
    return principal

@atrasar(2)
def dizer_oi():
    print('Oi')

dizer_oi()
print(dizer_oi.__name__)