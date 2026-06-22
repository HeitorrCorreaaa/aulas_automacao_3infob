import pandas as pd

# 1. Leitura de Dados
# Carregue o arquivo "funcionarios.xlsx", armazenando a aba "Funcionarios"
# em um DataFrame chamado df_funcionarios e a aba "Departamentos" em um
# DataFrame chamado df_departamentos.
df_funcionarios = pd.read_excel("funcionarios.xlsx", sheet_name="Funcionarios")
df_departamentos = pd.read_excel("funcionarios.xlsx", sheet_name="Departamentos")
 
 
# 2. Inserção de Registro
# Adicione um novo registro a df_funcionarios com:
#   Nome: 'Camila Rocha' | Cargo: 'Analista de Dados' | Salario: 4500.00
df_funcionarios.loc[17] = {'Nome': 'Camila Rocha', 'Cargo': 'Analista de Dados', 'Salario': 4500.00}
 
 
# 3. Atualização de Dados
# Atualize o salário do funcionário 'Camila Rocha' para 4800.00.
df_funcionarios.at[17, 'Salario'] = 4800.00
 
 
# 4. Exclusão de Registro
# Exclua de df_funcionarios o registro de índice 3.
df_funcionarios = df_funcionarios.drop([3])
 
 
# 5. Filtragem Simples
# Selecione os registros de df_funcionarios com Salario maior que 3000.00.
salario_maior_3000 = (df_funcionarios['Salario'] > 3000.00)
df_funcionarios_acima_3000 = df_funcionarios[salario_maior_3000.values]
 
 
# 6. Agrupamento e Agregação
# Agrupe df_funcionarios por Cargo e calcule a média salarial de cada cargo.
df_media_salario = df_funcionarios.groupby('Cargo')['Salario'].mean().reset_index()
 
 
# 7. Projeção de Colunas
# Selecione apenas as colunas 'Nome' e 'Salario'.
df_colunas_projetadas = df_funcionarios[['Nome', 'Salario']]
 
 
# 8. Filtragem por Texto
# Selecione os registros em que o Cargo seja exatamente 'Analista de Dados'.
analista_dados = (df_funcionarios['Cargo'] == 'Analista de Dados')
df_somente_analistas = df_funcionarios[analista_dados.values]
 
 
# 9. Filtragem Composta e Projeção
# Selecione apenas 'Nome' e 'Cargo' dos funcionários com Salario > 3000.00.
df_filtrado_e_projetado = df_funcionarios[salario_maior_3000.values][['Nome', 'Cargo']]
 
 
# 10. Ordenação
# Ordene df_funcionarios pelo Salario, do maior para o menor.
df_funcionarios_ordenado = df_funcionarios.sort_values(by='Salario', ascending=False)
 
 
# 11. Junção de DataFrames (Merge)
# Combine df_funcionarios e df_departamentos usando 'Cargo' como chave.
df_mesclado = pd.merge(df_funcionarios, df_departamentos, on='Cargo')
 
 
# 12. Exportação de Dados
# Salve o DataFrame ordenado da Questão 10 em "funcionarios_ordenado.xlsx",
# sem incluir o índice.
df_funcionarios_ordenado.to_excel("funcionarios_ordenado.xlsx", index=False)