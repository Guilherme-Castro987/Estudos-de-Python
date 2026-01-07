import json

with open('192_testando_json.json','r',encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)
print(pessoa['nome'])