dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O preço da sua passagem será de R${:.2f}.'.format(preco))

