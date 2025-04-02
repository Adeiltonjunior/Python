p = float(input('Qual é o preço do produto? R$ '))
desc = p - (p*5/100)
print('O produto que custava {}, ficará por {} após o desconto!'.format(p, desc))
