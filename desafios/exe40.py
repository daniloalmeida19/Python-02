#Nota de Aluno#

nota = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota + nota2) / 2
print(f'tirando {nota:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media >= 7:
    print('O Aluno está Aprovado')
elif 5 <= media < 7:
    print('O Aluno está de Recuperação')
else:
    print('O Aluno está Reprovado')
    print('Estude mais!')
    print('Você pode melhorar!')
    print('Continue assim!')
    print('Aproveite o tempo livre para estudar!')
    print('Busque ajuda se necessário!')
    

