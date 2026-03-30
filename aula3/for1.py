# Estrutura de Repetição For
# Utilizado para repetir um conjunto de instruções, quando sabemos quantas vezes a instrução deve ser repetida.

# Exemplo
# Laço For: (Valor inicial, Valor final, Passo)
# Range -> Intervalo de valores

# Intervalo Gerado -> 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1, 10, 1):
  print(i, end=' ')
print('\n')

# Intervalo Gerado -> 1, 3, 5
for i in range(1, 7, 2):
  print(i, end=' ')
print('\n')

# Intervalo Gerado -> 0, -1, -2, -3
for i in range(0, -4, -1):
  print(i, end=' ')
print('\n')

# Range(10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
  print(i, end=' ')