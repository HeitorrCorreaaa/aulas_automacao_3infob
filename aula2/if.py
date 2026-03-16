#condição if

#entrada
nome = input("digite seu nome: ")
idade = int(float(input("digite sua idade: ")))

#processamento
if (idade < 18):
    autorizacao = input ('os pais autorizaram a viagem?[sim/não]: ')

print(f'realizando o embarque {nome}')