#escreva 1 programa que soma 1 emprestimo bancario de financiamento total da casa somando valor da casa o salario e quantos anos vai pagar não pode exceder 30% da salario#

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f} por mês.')
print(f'30% do salário é R$ {salario * 0.3:.2f}.')
