def recebe_nome(function_origin):
    def interna(nome):
        function_origin()
        print(nome)
    return interna


@recebe_nome
def saudacao():
    print('Seja bem vindo')

exibir = saudacao('Guilherme')
