import pandas as pd

#ler a planilha do excel utilizando pandas
planilha = pd.read_excel('aula8\\alunos.xlsx')

#imprime a variavel planilha
print(planilha)

#imprime os dados do aluno gael / imprime a linha 2

print(planilha.loc[2])
print(planilha.loc[2, ['nome', 'idade',]])

#atualizar os dados
planilha.loc[2, 'nome'] = 'Heitor Castilho'
planilha.loc[2,['nome', 'idade']] = ['Heitor Castilho', 20]

#imprime novamente os dados da planilha
print(planilha)


