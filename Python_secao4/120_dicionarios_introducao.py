'''
Dicionárois em Python ( tipo Dict)
Dicionários são estruturas de dados do tipo chave e valor
Chaves podem ser consideradas como o índice que vimos na lista
e podem ser de tipos imutáveis.
como: str,int,float,bool,tuple,etc.
Valor pode ser qualquer outro tipo de dados incluindo outro dict
Usamos as chaves{} ou a class dict para criar um dicionário.
'''
# Diconários normalmente são usados para 'coisas' que normalmente podem conter atributos (produtos,pessoas, etc..)


pessoa = ['Guilherme','Castro',28,"Mansuor"]
pessoa_2 = {
    'Nome':'Guilherme',
    'Sobrenome':'Castro',
    'Idade': 28,
    'Altura': 1.8,
    'Endereços': [
        {'Rua': 'tal tal','numero': 123},
        {'Rua': 'outra rua','numero': 321},
    ],
}

print(pessoa_2)
print()
for chave in pessoa_2:
    print(chave,": ",pessoa_2[chave],sep="")