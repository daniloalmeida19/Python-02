print ('{:=^40}'.format(' LOJAS DANILO '))
preco = float(input('Preço das compras: R$ '))
print(f'Formas de pagamento')
print(f'[ 1 ] à vista dinheiro/cheque')
print(f'[ 2 ] à vista cartão')
print(f'[ 3 ] 2x no cartão')
print(f'[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? ')) # Solicita a opção de pagamento

total = preco # Inicializa o total com o preço original. Será modificado conforme a opção.

if opcao == 1:
    # À vista dinheiro/cheque: 10% de desconto
    total = preco * 0.90
elif opcao == 2:
    # À vista cartão: 5% de desconto
    total = preco - (preco * 0.05)
elif opcao == 3:
    # 2x no cartão: preço normal (total já é 'preco' devido à inicialização)
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS')
elif opcao == 4:
    # 3x ou mais no cartão: 20% de juros
    totparc = int(input('Quantas parcelas? '))
    total = preco * 1.20 # Aplica juros de 20%
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R$ {parcela:.2f} COM JUROS')
else:
    # Opção inválida
    print(' OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    # total permanece 'preco' (valor original) neste caso.
print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.')
#Desafio 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista cartão: 5% de desconto
#- 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros
#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
