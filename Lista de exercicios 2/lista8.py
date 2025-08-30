nomes = ["Lucas", "João", "Pedro", "Letícia"]

nome_usuario = input("Digite um nome: ")

if nome_usuario in nomes:
    print(f'O nome {nome_usuario} está na lista!')
else:
    print(f'O nome {nome_usuario} não está na lista.')
