#pandas: biblioteca em python que permite a manipulação de arquivos
#em formato tabular, ex: planilhas e tabelas. 

#edição de dados(inserir, Atualizar e excluir)


#instalação
#pip install pandas

#importar biblioteca (as renomeira o pacote "abreviação")
import pandas as pd

#ler uma planilha do excel
#cria a variavel planilha que vai guardar a planilha do excel
#em pandas chamamos a planilha de Dataframe

planilha = pd.read_excel('aula9\\Dados 3INFOB.xlsx')

#mostra os dados da planos
#print (planilha)

#imprime a cabeça da planilha: Quantas linhas da parte de cima eu quero imprimir
#print(planilha.head(3))

#imprimir as últimas 3 linhas 
#print(planilha.tail(5))

nova = planilha.head(4)
nova = nova.tail(2)
print(nova)

planilha.loc[len(planilha)] = ['pablo', 52, 1.8, 'M']
print(planilha)

planilha.loc[16] = ['pablo', 52, 1.8, 'masculino']
print(planilha)

planilha.loc[16] = ['pablo', 52, 1.8, 'masculino']
print(planilha)
