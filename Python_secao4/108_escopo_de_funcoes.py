# Exitem vários escopos, escoopo do módulo ( arquivo), escopo das funções

x = 1 # essa variavel é do escopo do módulo
y = 7
# podemos acessar valores de fora, mas não conseguimos acessar valores internos
def primeira_funcao(): # aqui é o escopo da função
    print(x)
    def segunda_funcao():
        print(x)
        y = 2
        print(y)
    segunda_funcao()

primeira_funcao()
print(y)