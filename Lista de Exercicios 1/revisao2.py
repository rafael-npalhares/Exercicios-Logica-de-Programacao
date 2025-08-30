qnt = 0 
nome = input("digite seu nome: ")
print(nome.upper())
nomes = nome.split(" ")
print(f"O primeiro nome é: {nomes[0]}")
for i in nome:
    if i == " ":
        qnt += 0
    else:
        qnt += 1

print(f"a quantidade de letras é: {qnt}")