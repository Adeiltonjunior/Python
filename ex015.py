km = float(input('Qual a quantidade de km rodados? '))
d = int(input('Quantos dias o carro ficou alugado? '))
custo = (60 * d) +  (0.15 * km)
print('Se o seu carro foi alugado por {} dia(s), e rodou {}km(s), o custo a ser pago é de R${:.2f}.'.format(d,km,custo))
