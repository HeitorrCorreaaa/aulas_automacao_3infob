while True:

    try:
        n1 = float(input("digite o primeiro numero:"))
        n2 = float(input("digite o segundo numero:"))
        c = n1/n2
        print("resultado", c)
    except ZeroDivisionError:
        print("voce não pode dividir por 0")
    except ValueError:
        print('o valor digitado é invalido')
    except Exception as e:
        print("ocorreu um erro", e)