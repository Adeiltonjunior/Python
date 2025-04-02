medida = float(input('Digite aqui uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m equivale a {:.0f}cm e a {:.0f}mm.'.format(medida, cm, mm))