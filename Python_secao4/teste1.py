def mensagem5():
    print('Essa é a mensagem de numero 5')

def mensagem4():
    print('Essa é a mensagem de numero 4')

def mensagem3():
    print('Essa é a mensagem de numero 3')

def mensagem2():
    print('Essa é a mensagem de numero 2')

def mensagem1():
    print('Essa é a mensagem de numero 1')

def decoradora(*args):
    def interna():
        print('Essa é a mensagem da funcao interna, que deve acontecer primeiro.')
        for x in args:
            x()
    return interna

exibir_mensagens = decoradora(mensagem1,mensagem2,mensagem3,mensagem4,mensagem5)
exibir_mensagens()
    