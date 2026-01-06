def repetir(vezes):
    # Esta camada recebe o argumento 'vezes'
    def decorador_real(func):
        # Esta camada recebe a função
        def embrulho(*args, **kwargs):
            # Esta camada executa a lógica
            for _ in range(vezes):
                resultado = func(*args, **kwargs)
            return resultado
        return embrulho
    return decorador_real

@repetir(vezes=3)
def saudar():
    print("Olá!")

saudar()