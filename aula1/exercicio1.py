#entrada salario do rapaizinho
salario = float(input('informe seu salário: '))

#calculos salario menos descontos
calculoSalarioInss = 11/100 * salario
calculoSalarioFgts =  7.5/100 * salario
salarioliquido =  salario - (calculoSalarioFgts  + calculoSalarioInss)

#saida do salario e descontos
print('seu salario é: ', salarioliquido)
print('desconto inss:', calculoSalarioInss)
print('desconto fgts:', calculoSalarioFgts)