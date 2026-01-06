def duplicar(funcao_original):
    def embrulho():
        funcao_original()
        funcao_original()
    return embrulho


@duplicar
def bom_dia():
    print('Bom dia')

bom_dia()