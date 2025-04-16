from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('YOU WIN')
            v += 1
        else:
            print('YOU LOSE')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('YOU WIN')
            v += 1
        else:
            print('YOU LOSE')
            break
    print('PLAY AGAIN')
print(f'GAME OVER LOSER! YOU WIN {v} TIMES.')