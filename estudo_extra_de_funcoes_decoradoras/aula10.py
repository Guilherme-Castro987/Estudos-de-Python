def meu_decorador(funct):
    def embrulho(*args,**kwargs): # pode vir oque for como argumento que dá para guardar
        print('Inicio')
        resultado = funct(*args,**kwargs) # passamos todos argumentos para dentro dda função original
        print('fim')
        return resultado
    return embrulho

