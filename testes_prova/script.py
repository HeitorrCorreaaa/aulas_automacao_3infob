import pandas as pd

#1 Leitura de Dados
df_notas = pd.read_excel("notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pd.read_excel("notas_estudantes.xlsx", sheet_name="Atividades")

#2 Inserção de Registro
df_notas.loc[16] = {'Nome': 'Lucas Silva', 'Atividade': 'Prova Final', 'Nota': 8.5}

#3 Atualização de Dados
df_notas.at[1, 'Nota'] = 9.0

#4 Exclusão de Registro
df_notas = df_notas.drop([2])

#5 Filtragem Simples
nota_maior_sete = (df_notas['Nota'] > 7.0)
df_notas_acima_sete = df_notas[nota_maior_sete.values]

#6 Agrupamento e Agregação
df_media_notas = df_notas.groupby('Nome')['Nota'].mean().reset_index()

#7 Projeção de Colunas
df_colunas_projetadas = df_notas[['Nome', 'Nota']]

#8 Filtragem por Texto
prova_final = (df_notas['Atividade'] == 'Prova Final')
df_somente_provas_finais = df_notas[prova_final.values]

#9 Filtragem Composta e Projeção
df_filtrado_e_projetado = df_notas[nota_maior_sete.values][['Nome', 'Atividade']]

#10 Ordenação
df_notas_ordenado = df_notas.sort_values(by='Nome')

#11 Junção de DataFrames
df_mesclado = pd.merge(df_notas, df_atividades, on='Atividade')

#12 Exportação de Dados
df_notas_ordenado.to_excel("notas_estudantes_ordenado.xlsx", index=False)
