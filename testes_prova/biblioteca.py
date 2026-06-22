import pandas as pd

# 1. Leitura de Dados
# Leia "biblioteca.xlsx" para um DataFrame chamado tabela.
tabela = pd.read_excel("biblioteca.xlsx")


# 2. Visualização
# Exiba os 3 últimos registros do DataFrame.
tabela.tail(3)


# 3. Inserção de Registro
# Insira um novo livro:
#   Codigo: 4 | Titulo: 'A Revolução dos Bichos' | Autor: 'George Orwell'
#   Disponivel: 'Sim'
tabela.loc[4] = {'Codigo': 4, 'Titulo': 'A Revolução dos Bichos', 'Autor': 'George Orwell', 'Disponivel': 'Sim'}


# 4. Atualização de Dados
# Atualize o livro "1984" para Disponivel = 'Sim'.
tabela.loc[tabela['Titulo'] == '1984', 'Disponivel'] = 'Sim'


# 5. Exclusão de Registro
# Exclua o livro que está na linha de índice 0.
tabela = tabela.drop([0])


# 6. Exportação de Dados
# Exporte o DataFrame atualizado para "biblioteca_atualizada.xlsx".
tabela.to_excel("biblioteca_atualizada.xlsx", index=False)


# 7. Desafio
# Exiba apenas os livros do autor "George Orwell".
mascara_orwell = tabela['Autor'] == 'George Orwell'
livros_orwell = tabela[mascara_orwell]
livros_orwell