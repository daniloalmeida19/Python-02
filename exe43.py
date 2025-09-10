peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura? (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.1f}")
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal.")
elif 18.5 <= imc < 25:
    print("PARABÉNS! Você está na faixa de PESO NORMAL.")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO.")
elif 30 <= imc < 40:
    print("CUIDADO! Você está com OBESIDADE, Cuidado!")
else:
    print("Risco de VIDA! Você está com OBESIDADE MÓRBIDA.")
    
    




