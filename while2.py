#while

continuar = True

while continuar:
    print("digite o nome do aluno: ")
    aluno = input()

    resp = int(input("deseja continuar: \n0 para não\n1 para sim:"))
    if resp == 0:
        continuar = False
