'''
Argumentos nomeados e não nomeados no Python
Argumentos nomeados tem nome com sinal de igual =
Argumentos não nomeados recebe apenas o argumento (valor)
'''
# Definição da função
def soma(x,y):
    print(x+y)
    # nesse caso a minha função esta retornando none

print(soma) # nesse caso eu estou me referindo ao nome da função, e não ao valor dela. É necessário colocar os ()
# 1 e 2 aqui são argumentos posicionais, que dependem da posição dos parâmetros da função.
soma(3,2) # nesse caso eu estou pedindo a ação da função
soma(y=3,x=3) # nesse caso, eu estou definindo a ordem que eu quero dos argumentos.( não posicionais)
