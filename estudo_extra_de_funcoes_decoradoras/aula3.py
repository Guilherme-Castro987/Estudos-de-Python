def saudar():
    return "Olá"


def executar_funcao(funcao_alvo):
    print(funcao_alvo())

executar_funcao(saudar)
print(type(saudar))
print(type(saudar()))