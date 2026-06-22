import pandas as pd

# 1. Leitura e Inspeção
# Leia as abas "Vendas" e "Metas" em df_vendas e df_metas.
# Em seguida, exiba os tipos de dados (dtypes) de df_vendas e verifique se
# existem valores nulos em cada coluna (use isnull().sum()).
df_vendas = pd.read_excel("vendas.xlsx", sheet_name="Vendas")
df_metas = pd.read_excel("vendas.xlsx", sheet_name="Metas")
df_vendas.dtypes
df_vendas.isnull().sum()


# 2. Criação de Coluna Calculada
# Crie uma nova coluna 'ValorTotal' em df_vendas, igual a
# Quantidade * ValorUnitario.
df_vendas['ValorTotal'] = df_vendas['Quantidade'] * df_vendas['ValorUnitario']


# 3. Conversão e Extração de Datas
# Garanta que a coluna 'DataVenda' esteja no formato datetime
# (pd.to_datetime). Depois, crie uma coluna 'MesVenda' contendo apenas o
# mês (número) de cada venda.
df_vendas['DataVenda'] = pd.to_datetime(df_vendas['DataVenda'])
df_vendas['MesVenda'] = df_vendas['DataVenda'].dt.month


# 4. Classificação Condicional
# Crie uma coluna 'Porte' que receba:
#   'Grande' se ValorTotal > 1000
#   'Médio'  se ValorTotal estiver entre 300 e 1000 (inclusive)
#   'Pequeno' caso contrário
def classificar_porte(valor):
    if valor > 1000:
        return 'Grande'
    elif valor >= 300:
        return 'Médio'
    else:
        return 'Pequeno'

df_vendas['Porte'] = df_vendas['ValorTotal'].apply(classificar_porte)


# 5. Remoção de Duplicados
# Suponha que o mesmo Pedido possa aparecer duplicado por erro de
# importação. Remova linhas duplicadas considerando a coluna 'Pedido'
# (mantenha a primeira ocorrência).
df_vendas = df_vendas.drop_duplicates(subset='Pedido', keep='first')


# 6. Agrupamento Multi-nível
# Agrupe df_vendas por 'Vendedor' e 'MesVenda', somando o 'ValorTotal'.
# O resultado deve ter colunas Vendedor, MesVenda e ValorTotal (use
# reset_index() para "desempilhar" o índice duplo).
df_vendas_mes = df_vendas.groupby(['Vendedor', 'MesVenda'])['ValorTotal'].sum().reset_index()


# 7. Tabela Dinâmica (Pivot Table)
# Construa uma tabela dinâmica (pivot_table) com Vendedor nas linhas,
# MesVenda nas colunas, e a soma de ValorTotal como valores.
# Preencha eventuais células vazias com 0 (fill_value=0).
df_pivot = pd.pivot_table(df_vendas, index='Vendedor', columns='MesVenda', values='ValorTotal', aggfunc='sum', fill_value=0)


# 8. Top-N por Grupo
# Para cada Categoria de produto, encontre o Produto com maior
# ValorTotal somado (ou seja: agrupe por Categoria e Produto, some
# ValorTotal, e depois pegue a linha de maior valor em cada Categoria).
# Dica: groupby + idxmax(), ou sort_values() + groupby().head(1).
df_categoria_produto = df_vendas.groupby(['Categoria', 'Produto'])['ValorTotal'].sum().reset_index()
df_top_produto = df_categoria_produto.sort_values('ValorTotal', ascending=False).groupby('Categoria').head(1)


# 9. Junção com Validação de Meta
# Combine df_vendas (já agregado por Vendedor, com soma de ValorTotal) com
# df_metas usando 'Vendedor' como chave. Crie uma coluna 'BateuMeta'
# (True/False) indicando se o total vendido por cada vendedor foi maior
# ou igual à MetaMensal.
df_total_vendedor = df_vendas.groupby('Vendedor')['ValorTotal'].sum().reset_index()
df_metas_check = pd.merge(df_total_vendedor, df_metas, on='Vendedor')
df_metas_check['BateuMeta'] = df_metas_check['ValorTotal'] >= df_metas_check['MetaMensal']


# 10. Contagem de Frequência
# Use value_counts() para descobrir qual Categoria de produto teve mais
# pedidos registrados (contagem de linhas, não soma de valores).
contagem_categorias = df_vendas['Categoria'].value_counts()


# 11. Filtragem com Múltiplas Condições (E / OU)
# Selecione os pedidos em que a Categoria seja 'Eletrônicos' E o
# ValorTotal seja maior que 500, OU a Categoria seja 'Móveis' E a
# Quantidade seja maior que 3.
mascara_complexa = ((df_vendas['Categoria'] == 'Eletrônicos') & (df_vendas['ValorTotal'] > 500)) | \
                    ((df_vendas['Categoria'] == 'Móveis') & (df_vendas['Quantidade'] > 3))
df_vendas_filtrado = df_vendas[mascara_complexa]


# 12. Renomeando e Reorganizando Colunas
# Renomeie a coluna 'ValorTotal' para 'Total (R$)' e reordene as colunas
# do DataFrame de modo que 'Pedido' e 'Cliente' apareçam primeiro.
df_vendas = df_vendas.rename(columns={'ValorTotal': 'Total (R$)'})
colunas_ordenadas = ['Pedido', 'Cliente'] + [c for c in df_vendas.columns if c not in ('Pedido', 'Cliente')]
df_vendas = df_vendas[colunas_ordenadas]


# 13. Exportação em Múltiplas Abas com Formatação (openpyxl)
# Exporte para um arquivo "relatorio_vendas.xlsx" com DUAS abas:
#   - "Vendas Detalhadas": df_vendas completo
#   - "Resumo por Vendedor": o resultado agrupado da Questão 6
# Na aba "Resumo por Vendedor", deixe o cabeçalho (linha 1) em negrito.
from openpyxl.styles import Font

with pd.ExcelWriter("relatorio_vendas.xlsx", engine='openpyxl') as writer:
    df_vendas.to_excel(writer, sheet_name='Vendas Detalhadas', index=False)
    df_vendas_mes.to_excel(writer, sheet_name='Resumo por Vendedor', index=False)
    planilha_resumo = writer.sheets['Resumo por Vendedor']
    for celula in planilha_resumo[1]:
        celula.font = Font(bold=True)


# 14. Função Reutilizável
# Escreva uma função classificar_desempenho(vendedor, df_vendas, df_metas)
# que recebe o nome de um vendedor e retorna uma string:
#   "Meta batida" ou "Meta não batida", comparando o total vendido por
# ele com sua meta mensal. Teste a função com pelo menos um vendedor.
def classificar_desempenho(vendedor, df_vendas, df_metas):
    total_vendido = df_vendas.loc[df_vendas['Vendedor'] == vendedor, 'Total (R$)'].sum()
    meta = df_metas.loc[df_metas['Vendedor'] == vendedor, 'MetaMensal'].values[0]
    return "Meta batida" if total_vendido >= meta else "Meta não batida"

classificar_desempenho('Vendedor Exemplo', df_vendas, df_metas)