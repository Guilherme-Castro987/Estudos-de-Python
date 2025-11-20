# Sets - conjuntos em Python ( tipo set )
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/diagrama-de-venn.html
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutavéis, porpem aceitam apenas 
# tipos imutavéis como valor interno.

# Criando um set 
# set(iteravel) ou {1,2,3}

s1 = set('guilherme') # Usando a função set() os dados ficam fora de ordem
print(s1)

s2 ={'guilherme'} # Usando dessa fomra {} a ordem permanece
print(s2) # isso ocorre porque o set intera o valor dentro dele

s3 = {(1,2)} # Aceita dados imutaveis apenas, se fosse uma lista no lugar dessa tuple, daria erro.
print(s3)

# sets são eficientes para remover valores duplicados de iteráveis.
s4 = {1,1,2,2,3,3,3,4,4}
print(s4) # Ele retorna um de cada valor apenas, remove sozinho os valores duplicados.

# - eles não tem índixes;
# - eles não garantem ordem;
# - eles são interáveis ( for, in , not in)
s5 = {1,2,3,4}
print(3 in s5) # sets são interavéis, nesse exemplo ele retorna True
for numero in s5:
    print(numero)


# métodos úteis:
# add, update, clear, discard

s6 = set()
s6.add('gui') # add adiciona um valor ao conjunto
print(s6)
s6.update('olá mundo') # update também adiciona valores ao conjunto set
print(s6)
s1.clear() # Limpa um set por completo
s6.discard('gui') # elimina diretamente o valor passado como argumento
print(s6)