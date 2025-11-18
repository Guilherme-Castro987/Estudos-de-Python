'''
Higher Order Functions
Funções de primeira classe
'''

def saudacao(msg):
    return msg

def executa(funcao,msg):
    return funcao(msg)


v = executa(saudacao,'Olá Mundo!')
print(v)
'''
neste caso foi definido a função saudacao recebendo o parâmetro msg e retornando ele
logo em seguida foi definido a função executa recebendo 2 parâmetros, sendo um deles o parâmetro da primeira função
e retornando uma função com o argumento já definido no parâmetro
quando a variável v recebe a função executa, eu preciso colocar 2 argumentos, um é qual função eu quero executar e o outro a mensagem.
'''