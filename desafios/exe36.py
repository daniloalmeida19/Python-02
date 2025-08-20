#escreva 1 programa que soma 1 emprestimo bancario de financiamento total da casa somando valor da casa o salario e quantos anos vai pagar não pode exceder 30% da salario#

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}.')
print(f'O valor máximo da prestação é de R$ {minimo:.2f}.')

if prestacao > minimo:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
