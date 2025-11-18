pessoa = {
    'Nome':'Guilherme',
    'Sobrenome':'Castro',
    'Idade': 28,
    'Altura': 1.8,
    'Endereços': [
        {'Rua': 'tal tal','numero': 123},
        {'Rua': 'outra rua','numero': 321},
    ],
}

pessoa_2 = {}
chave = 'nome'
pessoa_2[chave] = 'Guilherme Castro'
print(pessoa_2[chave])
pessoa_2['Sobrenome'] = 'Castro'
print(pessoa_2)
del pessoa_2['Sobrenome'] # Apaga a chave
print(pessoa_2)


print(pessoa_2.get('idade','Essa chave não existe')) # Get (pegar) tenta pegar o valor de uma chave, pprém se não encontrar
                                                     # ele retorna none ou o valor que eu escolher.

