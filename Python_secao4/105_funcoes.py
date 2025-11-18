'''
Introdução a Funções (def) em Python
Funcões são trechos de códigos  usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros ( argumentos )
e retornar um valor especifico.
Por padrão, funções Python retornam None (nada).
'''
# Usamos o sinal de = caso queremos que se não for digitado nada nos parâmetros seja auto completado com o valor que escolhemos.
def somar(a=0,b=0): # Parâmetros são as 'variavéis' que criamos dentro da função.
    print(f'A soma entre {a} e {b} é {a+b}')
somar(5,5) # Argumentos são os valores que colocamos nos parenteses quando chamamos a função.