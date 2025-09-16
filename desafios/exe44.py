print ('{:=^40}'.format(' LOJAS DANILO '))
preco = float(input('Preço das compras: R$ '))
print(f'Formas de pagamento')
print(f'[ 1 ] à vista dinheiro/cheque')
print(f'[ 2 ] à vista cartão')
print(f'[ 3 ] 2x no cartão')
print(f'[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 0.2)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R$ {parcela:.2f} COM JUROS')
else:
    total = preco
    print(' OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.')
#Desafio 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista cartão: 5% de desconto
#- 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros
#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
