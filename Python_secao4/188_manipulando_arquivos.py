# r (leitura) , w (escrita) , x (para criação), a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)

# Context manager - with ( abre e fecha ) 

# Importante: para colocar o caminho, se não quiser colocar as \\ para separar os locais, pode colocr o 'r' antes de inciar o caminho
# ficaria assim: caminho_arquivo = r'C:\1 - Programação\Documentos\Udemy\'

caminho_arquivo = 'C:\\1 - Programação\\Documentos\\Udemy\\' # Aqui estamos passando o caminho para o arquivo
caminho_arquivo += 'aula188.txt' # aqui estamos concatenando o nome do arquivo com o caminho

# arquivo = open(caminho_arquivo,'w') # aqui abrimos o arquivo e usando o 'w' que já cria o arquivo se ele não existir e se existir apenas abre ou escreve algo
# arquivo.close() # Aqui estamos fechando o arquivo, sempre precisamos fazer isso

with open(caminho_arquivo,'w') as arquivo: # Aqui usando o with ele já abre e fecha o arquivo sozinho.
    # print('Olá mundo')            # Lembrando que 'arquivo' é uma variável que foi criada para armazenar o arquivo criado, poderia ser qualquer nome.
    # print('Seu arquivo vai ser fechado')
    arquivo.write('Linha 1\n') # Aqui estamos usando o método 'write' do objeto 'arquivo' que criamos, para escrever algo no arquivo.
    arquivo.write('Linha 2\n') # Precisamos usar a \n para quebrar as linhas igual usamos dentro do print por exemplo.

with open(caminho_arquivo,'r') as arquivo: # aqui usamos o 'r' que é para leitura
    print(arquivo.read()) # estamos lendo o arquivo.

with open(caminho_arquivo,'w+') as arquivo: # aqui estamos usando o 'w+' para que o arquivo possa ser leitura e escrita
    arquivo.write('Consegui escrever')
    arquivo.seek(0,0) # usamos o método seek para colocar o cursor novamente no top do arquivo, para que possa ler oque esta abaixo
    print(arquivo.read()) # assim podemos ler a primeira linha do nosso arquivo, sem o seek ele traria uma linha em branco

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# Vamos fazer muito uso desses métodos 
with open(caminho_arquivo,'w+',encoding='utf-8') as arquivo: # aqui estou usando o encoding como utf-8 para que aceite caracteres especiais
    arquivo.write('Linha 1\n') # aqui estamos apenas criando várias linhas para demontração
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Linha 4\n')
    arquivo.write('atenção\n')
    arquivo.seek(0,0) # aqui estou colocando novamente o ponteiro do arquivo para o inicio
    print(arquivo.read()) # para que possamos vizualizar do inicio

    arquivo.seek(0,0) # aqui eu coloco novamente o ponteiro no começo para que possa ler tudo do inicio
    for linha in arquivo.readlines(): # aqui eu crio um loop paraque eu possa ler todas as linhas usando o ' readlines '
        print(linha,end="") # o 'readlines' cria uma lista de str para mim, então basta apenas percorrer essa lista normalmente