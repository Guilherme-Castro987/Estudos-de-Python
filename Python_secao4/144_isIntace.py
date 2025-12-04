# isInstace para saber se o objeto é de determinado tipo
numero_inteiro = 10
numero_decimal = 1.2
texto = 'Guilherme'
booleano = True

# aqui todos vão retonar como TRUE
print(isinstance(numero_inteiro,int))
print(isinstance(numero_decimal,float))
print(isinstance(texto,str))
print(isinstance(booleano,bool))

# aqui todos vão retornar como FALSE
print(isinstance(numero_inteiro,float))
print(isinstance(numero_decimal,str))
print(isinstance(texto,int))
print(isinstance(booleano,str))


# Também funciona com estruturas de dados, todos aqui vão retonar TRUE
dicionario = {'chave':'valor'}
print(isinstance(dicionario,dict))

lista = [1,2,3,4]
print(isinstance(lista,list))

tuplas = (1,2,3)
print(isinstance(tuplas,tuple))

sets = {1,2,3}
print(isinstance(sets,set))