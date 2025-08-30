senha_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha do cofre: ")
    
    if senha == senha_correta:
        print("Cofre aberto")
        break
    else:
        tentativas += 1
        print("Senha incorreta!")

if tentativas == max_tentativas:
    print("Limite de tentativas atingido!")
