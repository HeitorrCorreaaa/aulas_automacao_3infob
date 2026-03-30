def somar(n1,n2):
    return n1+n2

def imprimir(texto):
    print(texto)


def ler():
    return int((input()))

def pulaLinha():
    print('\n')

imprimir('digite o primeiro numero: ')
n1 = ler()

imprimir('digite o segundo numero: ')
n2 = ler()

resposta = somar (n1, n2)
imprimir(f"o resultado é: {resposta}")



