# Operadores úteis:
# União | união (union) - une
# intersecção & (intersection) - itens presente em ambos 
# diferença - itens presentes apenas no set da esquerda
# diferença simétrica ^ - itens que não estão em ambos os sets


s1 = {1,2,3} # 1 esta presente apenas no s1, 2 e 3 em ambos os sets
s2 = {2,3,4} # 4 apenas no s2

# Todos os operadores abaixo funcionam igualmente as funções que cada um representa.

s3 = s1.union(s2) # Faz a união e retira os duplicados
s4 = s1.intersection(s2) # Mosta os itens em ambos
s5 = s1.symmetric_difference(s2) # Mostra os itens diferentes em cada
s6 = s1 | s2
s7 = s1 & s2
s8 = s1 - s2
s9 = s1 ^ s2

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)

