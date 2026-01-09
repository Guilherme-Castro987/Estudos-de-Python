'''
A Herança 🧬 funciona como uma árvore genealógica no código. Ela permite que criemos uma classe "Pai" (ou Superclasse) com características gerais e classes "Filhas" (ou Subclasses) que herdam tudo o que o pai tem, mas podem adicionar suas próprias especialidades.
O principal objetivo é o reuso de código. Se vários objetos compartilham as mesmas características, não precisamos escrever o mesmo código várias vezes.
'''

class animal: # Classe Pai (Superclasse)
    def __init__(self,nome,sexo,cor):
        self.nome = nome
        self.sexo = sexo
        self.cor = cor

    def comer(self):
        print(f'{self.nome} está comendo...')

    def andar(self):
        print(f'{self.nome} está andando...')

class cachorro(animal): # Classe Filha ( Subclasse) herda de animal
    def __init__(self, nome, sexo, cor,raca): # aqui acrescentamos a 'raca' dentro do construtor
        super().__init__(nome, sexo, cor) # o super() chama o __init__ da classe pai nesse caso 'animal' que esta dentro do parênteses
        self.raca = raca


    def latir(self):
        print(f'{self.nome}, um {self.raca} esta latindo: Au au!!')

class gato(animal):
    def __init__(self, nome, sexo, cor,vidas):
        super().__init__(nome, sexo, cor)
        self.vidas = vidas

    def miar(self):
        print('Miauu!')

    def contar_vidas(self):
        print(f'O {self.nome} tem {self.vidas} vidas.')