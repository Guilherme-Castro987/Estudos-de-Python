from random import randint

numero_sorteado = randint(0,10)
numero_escolhido = set()
tentativas = 1

while True:
    numero_escolhido = input("Escolha um número: ")
    if numero_sorteado in numero_escolhido:
        print(f'Parabéns, você acertou, o número sorteado era {numero_sorteado} !')
        print(f'Tentativas: {tentativas}')
        break

    print('Você errou!')
    print(f'Tentativas: {tentativas}')
    tentativas += 1    
