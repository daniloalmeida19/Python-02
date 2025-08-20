# Conversão de bases numéricas

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Coverter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} em BINÁRIO é {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} em OCTAL é {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} em HEXADECIMAL é {hex(num)[2:]}')     
else:
    print('Opção inválida. Tente novamente.')
