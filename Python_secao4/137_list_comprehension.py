# List comprenhension no Python 
# List comprehension é uma forma rápida de criar listas a partir de iteravéis.
#como criar essa lista abaixo

print(list(range(10)))

# 1° forma

lista1 = []
for x in range(10): # assim usamos o clássico for para iterar pela nossa lista e cria-la
    lista1.append(x)
    print(lista1)

print(50*'-')
lista2 = [valor_que_sera_adicionado for valor_que_sera_adicionado in range(10)] # A esquerda sempre fica o valor que você quer adicionar na lista, logo após vem a função que você quer realizar com esse valor.
# Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista2)
print(50*'-')
lista3 = [n1 * 2 for n1 in range(10)] # Neste caso estou fazendo uma função, antes da função do for, para cada n1 no meu for, eu faço o n1 que será adiconado multiplicar por 2
print(lista3) # Saída: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


lista4 = []
for y in range(10): # Neste caso, estou fazendo a mesma coisa que fiz acima na list comprehension, porém com mais linhas.
    numero_para_adicionar = y * 2
    lista4.append(numero_para_adicionar)

print(lista4) # Saída: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]