#fAÇA 1 PROGRAMA DE ALISTAMENTO MILITAR POR IDADE#

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade < 18:
    print(f'Você ainda não tem idade para se alistar falta(m) {18 - idade} ano(s).')

elif idade == 18:
    print(f'Você deve se alistar IMEDIATAMENTE!')

elif idade < 18:
    print(f' Ainda faltam {idade, ano} anos para o alistamento.')  
   
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {nasc + 18}.')
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')



