'''
O que é Polimorfismo?
A palavra significa "muitas formas". Na POO, isso permite que classes diferentes tenham métodos com o mesmo nome, mas que se comportam de maneiras diferentes.
Pense assim: tanto o cachorro quanto o gato "emitem um som", certo? Em vez de termos métodos com nomes diferentes (latir e miar), poderíamos ter um único método chamado emitir_som que funciona para qualquer animal.
'''

class animal: # Classe Pai (Superclasse)
    def __init__(self,nome,):
        self.nome = nome

    def emitir_som(self):
        return f'O {self.nome} emitiu um som: '

class cachorro(animal):
    
    def emitir_som(self):
        print('Au au')
        return super().emitir_som()


class gato(animal):
    def emitir_som(self):
        print('Miau Miau')
        return super().emitir_som()


dog = cachorro('Bob')
dog.emitir_som()

cat = gato('Marley')
cat.emitir_som()