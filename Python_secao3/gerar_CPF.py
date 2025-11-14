'''
CPF: 470.038.888-90
Colete a soma  dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex: 470.038.888-90 (470038888)
    10  9  8  7  6  5  4  3  2
*   4   7  0  0  3  8  8  8  8
    40 63  0  0  18 40 32 24 16

Somar todos os resultados:
40+63+8+7+18+40+32+24+16 = 233
Multipicar o resultado por 10
233 * 10 = 2330
Obter o resto da divisão da conta anterior por 11
2480 % 11 = 5
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:


'''
import sys
import random

cpf_gerado = ''
for numero in range(0,9):
    cpf_gerado += str(random.randint(0,9))
cpf_fatiado = []
contador = 10
soma = 0
for i in cpf_gerado:
    cpf_fatiado.append(int(i))

for y in range(0,9):
    soma += (contador*cpf_fatiado[y])
    contador -= 1

soma *= 10
if soma % 11 > 9:
    digito1 = 0
else:
    digito1 = soma % 11

'''
Calculo do segundo digito do CPF
CPF: 470.038.888.90
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma 
contagem regressiva começando de 11
'''
contador2 = 11
soma2 = 0
cpf_fatiado.append(digito1)
for x in range(0,10):
    soma2 +=(contador2*cpf_fatiado[x])
    contador2 -= 1
soma2 *= 10
if soma2 % 11 > 9:
    digito2 = 0
else:
    digito2 = soma2 % 11

cpf_fatiado.append(digito2)
print(*cpf_fatiado,sep='')
