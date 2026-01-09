class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade # Atributo privado

    @property
    def idade(self):
        """Este é o Getter: permite ler a idade como se fosse um atributo comum."""
        return self.__idade

    @idade.setter
    def idade(self, valor):
        """Este é o Setter: permite alterar a idade com validação."""
        if valor > 0:
            self.__idade = valor
        else:   
            print("Erro: A idade deve ser positiva!")

class cachorro(Animal):
 ...

dog = cachorro('Marley',0)
print(dog.idade)