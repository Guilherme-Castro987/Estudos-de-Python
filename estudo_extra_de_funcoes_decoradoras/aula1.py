# funções Lambda

def saudacao2(nome):
    print(f'Olá {nome}')


saudacao = lambda nome: print(f'Olá {nome}')

saudacao('Guilherme')
saudacao2('Guilherme')