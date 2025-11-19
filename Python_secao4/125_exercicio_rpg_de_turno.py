import random
import sys

def criar_npc(nome):
    npc = {
        'Personagem': nome,
        'lv' : 1,
        'exp': 0,
        'atk': 5,
        'hp': 50,
    }
    return npc

def criar_inimigo():
    inimigo = {
        'Inimigo': 'Inimigo teste',
        'lv': random.randint(personagem['lv'],personagem['lv'] + 3),
        'atk': random.randint(1,8),
        'hp': 30,
    }
    return inimigo

# def atacar(alvo,atacante):
#         alvo.update({
#              'hp':alvo['hp'] - atacante['atk']
#         })
#         return alvo,atacante

personagem = criar_npc(input("Escolha o nome do seu personagem: "))


while True:
    print(69*'-')
    novo_inimigo = criar_inimigo()
    while novo_inimigo['hp'] != 0:
        print(25*'-','Sua vez de atacar',25*'-')
        for x,y in personagem.items():
            print(f'{x}: {y}')
        print(30*'-')
        for x,y in novo_inimigo.items():
            print(f'{x}: {y}')
        input('Digite algo para atacar: ')
        novo_inimigo.update({
            'hp': novo_inimigo['hp'] - personagem['atk']
        })
        if novo_inimigo['hp'] == 0:
            print('VOCÊ GANHOU!!!!')
            sys.exit()
        print(25*'-','Vez do inimigo atacar',20*'-')
        personagem.update({
            'hp': personagem['hp'] - novo_inimigo['atk']
        })
        if personagem['hp'] == 0:
            print('VOCÊ PERDEU :(')
            sys.exit()
        for x,y in personagem.items():
            print(f'{x}: {y}')
        print(30*'-')
        for x,y in novo_inimigo.items():
            print(f'{x}: {y}')
        input('Inimigo te atacou, digite algo para continuar: ')
    



