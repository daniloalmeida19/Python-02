# Programa para aprovar um empréstimo bancário para a compra de uma casa.
# O valor da prestação mensal não pode exceder 30% do salário do comprador.

valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao_mensal = valor_casa / (anos * 12)
limite_prestacao = salario * 0.30

print(f'\nPara pagar uma casa de R$ {valor_casa:.2f} em {anos} anos, a prestação será de R$ {prestacao_mensal:.2f}.')
print(f'O valor máximo da prestação, correspondente a 30% do seu salário, é de R$ {limite_prestacao:.2f}.')

if prestacao_mensal > limite_prestacao:
    print('\nEmpréstimo NEGADO! O valor da prestação excede o seu limite permitido.')
else:
    print('\nEmpréstimo APROVADO! Parabéns!')
