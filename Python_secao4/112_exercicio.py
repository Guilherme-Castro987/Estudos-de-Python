# Exercícios com Funções

# Crie uma função que multiplique todos os argumentos
# não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor da variável

# crie uma função que fala se o número é par ou impar.
# retorne o resultado.

def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado
print(multiplicar(3,3,3))


def par_ou_impar(value = 0):
    if value & 1 == 0:
        return "Par"
    return "Impar"      # neste caso eu não preciso do 'else' devido ao return
print(par_ou_impar(3))