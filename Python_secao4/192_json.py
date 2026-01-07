import json

pessoa = {
    'nome':'Guilherme',
    'sobrenome':'Castro',
    'enderecos': [
        {'rua':'R1','numero':32},
        {'rua':'R2','numero':55},
    ],
    'altura':1.80,
    'numeros_preferidos':(2,4,6,8,10),
    'dev':True,
    'nada':None
}

with open('192_testando_json.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa,arquivo,indent= 2)