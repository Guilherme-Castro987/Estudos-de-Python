'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja 
enviado para o parâmetro, o valor padrão sera usado.
Refatorar: editar o código
'''

def somar(x,y,z = None):
    if z is not None:
        print('foi colocado valor no Z')
    else:
        print('não foi colocado valor no Z')

somar(5,8,5)