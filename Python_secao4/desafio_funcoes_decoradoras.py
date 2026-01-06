def verificar_turno(funcao_original):
    def wrapper():
        turno_atual = "dia"
        if turno_atual == 'dia':
            funcao_original()
        else:
            raise TypeError('o relatório é apenas para o turno da manhã')
    return wrapper

def gerar_relatorio_aura():
    print("Gerando relatório de desempenho do associado...")

funcao_para_executar = verificar_turno(gerar_relatorio_aura)
funcao_para_executar()