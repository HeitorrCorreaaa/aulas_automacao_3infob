import pandas as pd

planilha =("exercicios//notas_estudantes.xlsx")

#sheet_name, seleciona a coluna pelo nome dela
df_notas = pd.read_excel(planilha, sheet_name='Notas')
df_atividades = pd.read_excel(planilha, sheet_name='Atividades')

#está adicionando dados a planilha através do [len(df_notas)], o len joga para a ultima linha se usarmos {}, é necessário escrever o nome da linha que deseja adicionar novos dados ex: {'Nome': 'lucas silva'}
df_notas.loc [len(df_notas)]={'Nome': 'lucas silva','Nota': 8.5, 'Atividade': 'prova final'}
print (df_notas)

#altera determinado dado pela linha selecionada com [], no () deve ser digitado em ordem oque se deseja alterar
df_notas.loc[1] = ('Ana souza', 'Trabalho 1', 9)
print(df_notas)

#inplace exclui na planilha atual, se nao colocar o inplace ele cria uma nova planilha com o dado excluido, o .drop exclui o dado
df_notas.drop(df_notas.loc[(df_notas['Nome'] == "Pedro Santos") & (df_notas['Atividade'] == "Prova 1"), "Nota"].index, inplace=True)
print(df_notas)


#df_notas é o nosso dado,  [df_notas['Nota'] > 7.0], esse trecho está pegando os dados da linha que digitarmos no segundo [], nesse caso o "Nota"
notas_7 = df_notas [df_notas['Nota'] > 7.0] 
print(notas_7)

resposta = df_notas.groupby('nome')



