from datetime import date
ano = int(input('Qua ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é BISSEXTO'.formart(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
