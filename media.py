nome = input('Digite seu nome: ')
media = 0
for contador in range (1,5,1):
    nota = float(input(f'Insira a {contador}ª notado do aluno: '))
    media = media + nota 
    resultado = media/4
faltas = int(input('Digite o numero de faltas: '))
if resultado>=7 and faltas<=5:
    print('Aprovado')
elif resultado>=7 and faltas>5:
    print('Reprovado por falta')
elif resultado<7 and faltas<=5:
    print('Reprovado por media')        
else:
    print('Reprovado')
print('Nome do Aluno:', nome)
print('Sua media de notas é:{}'.format (resultado))