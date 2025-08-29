r1 = float(input(' primeiro segmento: '))
r2 = float(input(' segundo segmento: '))
r3 = float(input(' terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é ESCALENO!')
    else:
        print('O triângulo é ISÓSCELES!')
        