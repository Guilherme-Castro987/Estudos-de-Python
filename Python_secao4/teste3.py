def verificar_turno(funcao_original):
    # O que colocar nos parênteses aqui para aceitar um nome?
    def wrapper(nome_do_associado):
        turno_atual = "dia"
        if turno_atual == 'dia':
            # E como passar esse nome para a função original aqui?
            funcao_original(nome_do_associado)
        else:
            print("Bloqueado.")
    return wrapper

def gerar_relatorio_aura(nome):
    print(f"Gerando relatório para: {nome}")

funcao_com_nome = verificar_turno(gerar_relatorio_aura)
funcao_com_nome("Carlos Silva")