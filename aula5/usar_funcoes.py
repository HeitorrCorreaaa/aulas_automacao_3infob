import aula4.funcao as funcao

#usando as funções

funcao.imprimir('digite o primeiro numero: ')
n1 = funcao.ler()

funcao.imprimir('digite o segundo numero: ')
n2 = funcao.ler()

resposta = funcao.somar (n1, n2)
funcao.imprimir(f"o resultado é: {resposta}")
