# 1. Função original ( o presente )
def imprimir_nome():
    print('Guilherme')

# 2. A Função decoradora ( a embalagem )
def embalar_mensagem(funcao_original):
    def wrapper():
        print("Olá, tudo bem?") # coisa nova
        funcao_original() # executa a original
    return wrapper

# 3. Criando a função nova
funcao_com_saudacao = embalar_mensagem(imprimir_nome)

# 4. Executando
funcao_com_saudacao()

'''
neste exemplo quando criei a função 'funcao_com_saudacao' eu dei a ela a função de 'wrapper', ou seja
ela primeiro vai executar oque esta lá dentro primeiro 'print("Olá, tudo bem?")'e logo em seguida
vai executar o 'funcao_original()' que recebeu 'funcao_com_saudacao = embalar_mensagem(imprimir_nome)' aqui o imprimir_nome
então ela sobe para a funcao imprimir_nome e executa oque esta lá dentro 'print('Guilherme')'
'''