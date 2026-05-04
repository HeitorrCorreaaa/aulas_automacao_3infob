from aula4.funcao import imprimir, ler, somar

#usando as funções

imprimir('digite o primeiro numero: ')
n1 = ler()

imprimir('digite o segundo numero: ')
n2 = ler()

resposta = somar (n1, n2)
imprimir(f"o resultado é: {resposta}")
