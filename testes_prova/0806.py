import pandas as pd

df_notas = pd.read_excel('./notas_estudantes.xlsx', sheet_name='Notas')
df_atividades = pd.read_excel('./notas_estudantes.xlsx', sheet_name='Atividades')
df_notas.loc[len(df_notas)] = {
    'Nome': 'Lucas Silva',
    'Atividade': 'Prova Final',
    'Nota': 8.5
}
df_notas.loc[df_notas.loc[(df_notas["Nome"] == "Ana Souza") & (df_notas["Atividade"] == "Trabalho 1")].index, ["Nota"]] = 9

df_notas.drop(df_notas.loc[(df_notas["Nome"] == "Pedro Santos") & (df_notas["Atividade"] == "Prova 1")].index, inplace=True)

df_notas[df_notas["Nota"] > 7]

media = df_notas.groupby("Nome")["Nota"].mean()
print(f"\nMédia das notas:\n{media}")

notas = df_notas[['Nome', 'Nota']]
print(f"\nNotas:\n{notas}")

provaFinal = df_notas[df_notas['Atividade'] == 'Prova Final']
print(f"\nProva Final:\n{provaFinal}")

filtrado = df_notas[df_notas['Nota'] > 7][['Nome', 'Atividade']]
print(f"\nAcima de 7:\n{filtrado}")

ordenado = df_notas.sort_values(by='Nome')
print(f"\nNotas por nome:\n{ordenado}")

merge = pd.merge(df_notas, df_atividades, on='Atividade', how='left')
print(f"\nNotas juntado com atividades:\n{merge}")

merge.to_excel('notas_estudantes_ordenado.xlsx', index=False)

print(f"\nNotas dos estudantes:\n{df_notas}")