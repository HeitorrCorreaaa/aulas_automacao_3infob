# Comando Continue
# Ignora o resto dos comandos dentro do loop e continua do início na próxima intereção

# Dicionários de estudantes
aluno1 = {
  'nome': 'Pablo',
  'idade': 17,
  'sexo': 'M'
}

aluno2 = {
  'nome': 'Carlos',
  'idade': 18,
  'sexo': 'M'
}

aluno3 = {
  'nome': 'Samara',
  'idade': 17,
  'sexo': 'F'
}

# Lista com dicionários
alunos = [aluno1, aluno2, aluno3]

for aluno in alunos:
  if aluno['idade'] >= 18:
    continue
  print(f'Olá {aluno['nome']}, qual é o seu passatempo')
  aluno['hobbie'] = input('')

print(alunos)