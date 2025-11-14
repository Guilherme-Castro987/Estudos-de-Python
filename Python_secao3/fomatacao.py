'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal de - ou +
ex:.:0>-100,.1f
conversion flags - !r !s !a __repr__  __str__
'''
salario = 4.625
print(f'{salario:.2f}')


variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >2}")
'''
n1 = 5
for x in range(11):
    print(f"{n1}x{x}={n1*x}")
'''

print(f'{1530.223626:,.3f}')
print(f'O Hexadecimal de 1500 é {1500:x}')
print(f'{1500!r}')
