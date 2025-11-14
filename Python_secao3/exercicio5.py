nome = "Guilherme"
qnt_letras = len(nome)
contador = 0
novo_nome = ''
while contador <= qnt_letras -1:
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador +=1
print(novo_nome)