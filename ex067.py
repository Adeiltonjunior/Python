while True:
    n = int(input('Você quer saber a tabuada de qual número? '))
    print('-'*30)
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA ENCERRADO. Volte quando quiser e puder.')
