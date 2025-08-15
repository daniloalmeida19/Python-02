#escreva 1 programa que soma 1 emprestimo bancario de financiamento total da casa somando valor da casa o salario e quantos anos vai pagar não pode exceder 30% da salario#

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.'.format(casa, anos, prestacao))
if prestacao > minimo:
    print('Empréstimo negado! A prestação de R$ {:.2f} excede 30% do seu salário.'.format(prestacao))
