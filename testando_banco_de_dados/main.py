# Importa a Lib do SQlite para usarmos
import sqlite3
# Cria uma conexão com o banco de dados ( cria um arquivo .bd)
conexao = sqlite3.connect('meuBanco.db')
# Cria um tipo de cursor que permite navegar pelo nosso banco de dados
ponteiro = conexao.cursor()
# Cria uma tabela no nosso banco de dados
ponteiro.execute(
    '''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )
'''
)
nome_usuario = 'Catarina'
idade = 3

ponteiro.execute(
    '''
    INSERT INTO pessoas (nome,idade)
    VALUES (?,?)
''',(nome_usuario,idade)
)

conexao.commit() # Salva as alterações que realizou no seu banco de dados.
print('Banco de dados acessado com sucesso!!')
print('Tabela pessoas criada.')
print(f'Úsuario {nome_usuario} foi inserido no banco de dados que você criou!')


# Executa um comando de consulta
ponteiro.execute('SELECT * FROM pessoas')
# Busca todos os resultados da sua consulta 
resultados = ponteiro.fetchall()
print('\n---Pessoas no banco de dados---')
for linha in resultados:
    print(linha)
conexao.close()