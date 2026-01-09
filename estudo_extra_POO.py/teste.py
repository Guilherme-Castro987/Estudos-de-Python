class personagem:
    def __init__(self,nome,hp,atk,level):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.level = level

class npc(personagem):
    pass

class inimigo(personagem):
    pass

def atacar(atacante,alvo):
    alvo.hp -= atacante.atk

meu_personagem = npc('Guilherme',10,3,1)
meu_inimigo = inimigo('Inimigo 1',7,2,1)

print(meu_personagem.hp)
print(meu_inimigo.hp)
atacar(meu_personagem,meu_inimigo)
print(meu_personagem.hp)
print(meu_inimigo.hp)
