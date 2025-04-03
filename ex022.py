nome = str(input('Qual o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


