# Variáveis livre + nonlocal ( locals , globals)

print(globals())
def fora():
    a =1
    print(locals())
    def dentro():
        print(locals())
        b = 3
        return a,b
    return dentro

funcao = fora()
print(funcao())

