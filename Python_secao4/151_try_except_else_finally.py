# Try , Except , Else , Finally


# try não pode ficar sozinho no código, porém ele nõo pode ficar com o Else sozinho.

try:
    ...
except: ...  # nesse exemplo pode

try:
    ...
finally:
    ... # nesse exemplo também pode

# menos com o else

try:
    a = 5
    b = 0
    c = a / b
except ZeroDivisionError as erro: # ZeroDivisionError é uma classe que esta herdando a classe principal Exception.
    # esse ' as ' é usado para criar uma variavel, que vai armazenar a mensagem de erro que ocorreu
    print('tentou dividir por zero!')
    print(erro) # neste caso estou pedindo para printar, lembrando que ela não mostra o tipo de erro, mas sim a mensagem que vem após o tipo.
    print(erro.__class__.__name__) # desse formato, eu consigo pegar o nome do erro especifico.
except NameError:
    print('nome não esta definido!')
except (TypeError,IndexError): # se quiser passar mais de uma excessão, pod usar uma tupla.
    print('teste')

except Exception: # essa clase é a maior de todas as classes de erros, ela não permite que nenhum erro passe.
    print('ERRO DESCONHECIDO!') # Essa é a classe superior, ela trata qualquer erro.


print('continuar')
