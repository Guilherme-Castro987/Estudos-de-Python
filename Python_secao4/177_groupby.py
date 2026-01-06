# groupby - agrupando valores ( itertools)
from itertools import groupby

alunos = [
    {'nome':'Guilherme','nota':'A'},
    {'nome':'Faiane','nota':'B'},
    {'nome':'Amanda','nota':'C'},
    {'nome':'Lucas','nota':'A'},
    {'nome':'Felipe','nota':'D'},
    {'nome':'Luiz','nota':'C'},
    {'nome':'Ricardo','nota':'D'},
    {'nome':'Miguel','nota':'A'},
]

# Aqui foi criado uma função para que possamos usar as notas como parâmetro para o Key=, assim conseguimos ordenar o dict dentro da lista pelas notas.
def ordena(aluno):
    return aluno['nota']


# Aqui abaixo temos a maneira de usar a Lambda com a Key, porém temos repetição de código
# alunos_agrupadps = sorted(alunos,key= lambda x: x['nota'])
# grupos = groupby(alunos_agrupadps, key= lambda y: y['nota'])


# Aqui estamos criando uma lista de alunos agrupados ordenados pela nota
alunos_agrupadps = sorted(alunos,key=ordena)
grupos = groupby(alunos_agrupadps, key=ordena) # Aqui criamos grupos usando o groupby

# Aqui vamos percorrer chave e 'valor' de cada grupo
for chave , grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)