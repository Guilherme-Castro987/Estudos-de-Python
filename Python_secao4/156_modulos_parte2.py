# Entendendo seus primeiros módulos Python
# O primeiro módulo executado chama-se : __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ esta em baixo dele 
# Ele não reconhece pastas e módulos acima do __main__ padrão
#O Python conhce todos os módulos e pacotes presentes no caminhos de sys.path

import teste_de_modulo
import sys


print('Nome do módulo: ', __name__)
print(teste_de_modulo.pessoa)
print(teste_de_modulo.soma(10,10))