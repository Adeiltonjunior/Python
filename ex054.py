from datetime import date
atual = date.today().year
for pessoa in range(1, 8):
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        print('essa pessoa é maior de idade')
    else:
        print('Essa pessoa é menor de idade')
