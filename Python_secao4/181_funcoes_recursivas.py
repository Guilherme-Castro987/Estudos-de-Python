# Funções recursivas e recursividade
# - funções que podem se chamar de volta
'''
úteis para dividir problemas grandes em partes menores
toda função recursiva deve ter 
- um problema que possa ser dividido em partes menores
- um caso recursivo que resolve o problema pequeno
- um caso base para a recursão
- fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
'''

# aqui eu usei o loop para descobrir o fatorial de n
# n = 5
# total = 1

# for x in range(n,0,-1):
#     total *= x
# print(total)


# aqui eu usei uma função recursiva para descobrir o fatorial de n
def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n -1)

print(factorial(5))