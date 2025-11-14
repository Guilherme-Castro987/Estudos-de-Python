'''
Interpolação básica de strings
s - string
d / i  - int
f - float
x / X - Hexadecimal 
'''

n2 = 300
nome = "Guilherme"
preco = 1000.958976
n1 = 200.954382
variavel = '%s, o preço total foi R$%.1f' %(nome,preco)
print(variavel)
print("%f"%n1)
print('O Hexadecimal de %i é %x'%(n2,n2))