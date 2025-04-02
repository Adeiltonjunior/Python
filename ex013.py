s = float(input('Qual o salário do funcionário? R$ '))
aumento = s + (s*10/100)
print('O salário do funcionário que era {:.2f} ficará R${:.2f} após o aumento de 10%!'.format(s, aumento))