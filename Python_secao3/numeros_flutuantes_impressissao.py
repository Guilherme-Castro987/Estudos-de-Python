'''
Imprecisão de pontos flutuantes no Python
Double-precision floating-point format IEEE 754

'''
import decimal
n1 = 0.7
n2 = 0.1
n3 = decimal.Decimal(n1 + n2)

print(f'{n3:.1f}')
print(f'{0.1+0.2}')