import os         # importa a lib os e usa o comando para limpar o terminal
os.system('cls')

'''
pop = remove o último valor da lista criada
del = remove o valor do indice que indicamos para ele
remove = remove o primeiro valor da lista
insert = insere um novo valor na lista no índice que queremos
append = insere um novo valor na lista na última posição
clear = limpa a lista inteira
extend = extender a lista
+= concatenar a lista
'''

# numeros = [2,6,9,1,0,4]
# print(max(numeros))
# print(min(numeros))
# print(sorted(numeros))
# print(len(numeros))

# lista_compras = []
# item = ""
# while True:
#     item = input("Digite o item para adicionar a sua lista de compras: ")
#     lista_compras.append(item)
#     for i in lista_compras:
#         print(i)
#     if item == "":
#         break


# listaA = [1,2,3]
# listaB = [4,5,6]
# lista_master = listaA + listaB # realiza a concatenação das listas
# print(lista_master)
# listaA.extend(listaB) # extende a lista selecionada com outra lista, não precisa atribuir a uma nova váriavel 
# print(listaA)
# listaB += listaA 
# print(listaB)


nomes = ['guilherme','bia']
outros_nomes = nomes.copy()

nomes.append('lucas')
print(outros_nomes)
print(id(outros_nomes,),id(nomes))
