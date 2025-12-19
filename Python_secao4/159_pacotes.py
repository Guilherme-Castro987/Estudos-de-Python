from sys import path

import aula_159_package.modulo_teste3 # Aqui estou importando o package inteiro
soma = aula_159_package.modulo_teste3.soma_do_modulo(10,10) # importanto ele inteiro, eu preciso passar o 'caminho' correto até ele


from aula_159_package.modulo_teste3 import soma_do_modulo # aqui estou importanto paenas o modulo que eu quero
soma2 = soma_do_modulo(10,10) # podendo usar apenas o que esta dentro do módulo.


from aula_159_package import modulo_teste3 # podemos também importar dessa forma
soma3 = modulo_teste3.soma_do_modulo(10,10) # eu achamo apenas o módulo dentro do package

from aula_159_package.modulo_teste3 import * # Fazendo isso, eu chamo tudo que esta dentro do __All__ no meu módulo
print(variavel1) # consigo chamar as variaveis dentro do módulo
print(variavel2)


print(soma)
print(soma2)
print(soma3)


# print(__name__)
# print(*path , sep='\n')

