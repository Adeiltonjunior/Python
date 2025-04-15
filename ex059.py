from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior número é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Finalizando o programa...')
        sleep(1)
        print('Quase lá...')
        sleep(1)
        print('Agora foi. ')
    else:
        print('Opção inválida! Tente novamente.')
    print('-=-' * 10)
print('Fim do programa! Volte sempre!')
