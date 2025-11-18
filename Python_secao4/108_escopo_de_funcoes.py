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

global a # se quiser definir uma variavel como global
def primeira():
    a = 1
    print(id(a))
    def segunda():
        a = 2
        print(id(a))
        def terceira():
            a = 3
            print(id(a))
        terceira()
    segunda()

primeira() # aqui podemos ver 3 variaveis (a) porém cada uma em um local diferente da memória.