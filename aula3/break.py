# Comando Break: Interrompe o laço de repetição.

nomes = ['Lucas', 'Jesuely', 'Caua', 'Filipe']
nome_iniciado_com_c = ''

for nome in nomes:
  if nome.startswith('C'):
    nome_iniciado_com_c = nome
    break
  print(nome)

print('O primeiro nome iniciado com C é', nome_iniciado_com_c)