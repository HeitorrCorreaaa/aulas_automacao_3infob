senha = True

while senha: 
    usuario = input("digite o usuario de login: ")
    senha = input("digite a senha do login: ")

    if senha == "admin123" and usuario == "admin":
        print ('bem vindo')
        senha = False