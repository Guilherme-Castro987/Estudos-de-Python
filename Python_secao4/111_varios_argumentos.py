x ,y,*resto = 1,2,3,4,5 # Neste caso estou definindo que x esta recebendo 1 , y 2 , e todos os outros recebem resto
print(x)
print(y)
print(resto) # resto se torna uma variavel com tipo list

def maior(*args): # ele transforma esses parâmetros em uma tupla
    print(args)
    args = list(args) # aqui estou transformando o parâmetro em uma lista, caso eu precise mudar a estrutura dela.
    return max(args)

print(maior(9,8,7,6,10))