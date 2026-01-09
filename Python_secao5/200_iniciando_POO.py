class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def dizer_oi():
        print('oi')


p1 = Pessoa('Guilherme',28,1.80)

print(p1.nome)
print(p1.idade)
print(p1.altura)
Pessoa.dizer_oi()