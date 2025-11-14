frase = 'abcdaacbbbbab'
qtd_letras_frase = len(frase)
i = 0
letra_atual = ''
qtd_letra_atual = 0
maior_qtd = 0
maior_letra = ''
while i < qtd_letras_frase:
    letra_atual = frase[i]
    qtd_letra_atual = frase.count(letra_atual)
    i += 1
    if qtd_letra_atual >= maior_qtd:
        maior_qtd = qtd_letra_atual
        maior_letra = letra_atual
print(f'A maior letra é {maior_letra}')
