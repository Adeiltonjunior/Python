print('Gerador de PA')
print('-=-' * 5)
primeiro = int(input('Primeiro termo = '))
razao = int(input('Razão da PA= '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 10:
    total = mais + total
    while cont <= total:
        print('{} ¬ '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
