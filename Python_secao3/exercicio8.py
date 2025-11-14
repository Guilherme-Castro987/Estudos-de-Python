'''
Faça uma lista de compras com listas
O úsuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista 
Não permita que o programa quebre com erros de indices inexistentes na lista.
'''

lista_compras = []
while True:
    print("Selecione uma opção:")
    escolha = input("[i]Inserir [a]Apagar [l]Listar: ").upper()
    if escolha == 'L':
        for i,y in enumerate(lista_compras):
            print(i,y)
    elif escolha == "I":
        item = input("Digite o item que deseja inserir na lista: ").upper()
        lista_compras.append(item)
    elif escolha == "A":
        excluir = input('Digite o item que deseja excluir: ').upper()
        if excluir not in lista_compras:
            print('Não foi possível excluir esse item pois ele não existe na lista!')
        else:
            lista_compras.remove(excluir)
            print('Iem removido da lista com sucesso!')
    else:
        print('Digite um valor válido!')