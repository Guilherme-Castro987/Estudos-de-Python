def fabrica_de_saudacoes(nome_do_pai):
    def saudar():
        # A função interna usa uma variável de função externa
        print(f'Olá, eu sou o filho do {nome_do_pai}')
    return saudar

meu_filho = fabrica_de_saudacoes('Carlos')
meu_filho()