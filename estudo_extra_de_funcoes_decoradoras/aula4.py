def pai():
    print('Oi eu sou a função pai')
    def filho():
        print('Oi eu sou a função filho')
        # A função pai, decide devolver a função filho 
    return filho

# vamos 'capturar' o filho

minha_funcao_filho = pai()
minha_funcao_filho()