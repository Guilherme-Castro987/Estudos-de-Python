# Classes possuem atributos ( caracteristicas como cor e modelo )
# E também possuem métodos ( ação, como acelerar )

class cachorro():
    # agora vamos chamar o 'contrutor' que cria o nosso molde 
    def __init__(self,raça,cor,idade):
        self.raça = raça # Atributo
        self.cor = cor # Atributo
        self.idade = idade

    # agora vamos criar os métodos desse objeto 'cachorro'
    def latir(self):
        print('au au') # método

    def brincar(self):
        print('O cachorro esta brincando')   # método


    def fazer_aniversário(self):
        self.idade += 1

meu_pet = cachorro('Labrador','Amarelo',9) # Aqui estou criando uma instância da minha classe 'cachorro'
print(meu_pet.raça) # aqui estou chamando o atributo raça
print(meu_pet.cor) # aqui estou chamando o atributo cor
meu_pet.latir() # aqui estou chamando o método latir
meu_pet.brincar() # aqui estou chamando o método brincar
print(meu_pet.idade) # aqui meu cachorro tem 9 anos 
meu_pet.fazer_aniversário() # aqui eu aumento a idade do meu cachoro para +1 a cada vez que esse método é chamado
print(meu_pet.idade) # agora meu cachorro tem 10 anos

# Aqui eu estou criando outra instância da classe cachorro, e uma nõ afeta a outra, são 2 objetos diferentes.
pet2 = cachorro('Pastor Alemão','Preto',5)
print(pet2.idade)
pet2.fazer_aniversário()
print(pet2.idade)

