biblioteca = []

def cadastrar_livro():
    print("\n--- Cadastro de livro ---")
    
    titulo = input("Informe o título do livro: ")
    autor = input("Informe o autor do livro: ")
    
    livro = {
        "titulo": titulo,
        "autor": autor,
        "disponivel": 1
    }
    biblioteca.append(livro)
    print("Livro cadastrado com sucesso!\n")

def listar_livros():
    print("\n--- Listagem de livros ---")
    
    if not biblioteca:
        print("Nenhum livro cadastrado ainda.")

    for i, livro in enumerate(biblioteca):
        if livro['disponivel'] == 1:
            status = 'disponível'
        else:
            status = 'emprestado'

        print(f"{i} - {livro['titulo']} - {livro['autor']} - {status}")
    
    print()
    
def emprestar_livro():
    titulo = input("Digite o nome do livro que será emprestado: ")
    
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            if livro['disponivel'] == 1:
                livro['disponivel'] = 0
            else:
                print("Livro não disponível.")
    
    print()
    
def devolver_livro():
    titulo = input("Digite o nome do livro que será devolvido: ")
    
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            if livro['disponivel'] == 0:
                livro['disponivel'] = 1
            else:
                print("Livro já devolvido.")
    
    print()

def deletar_livro():
    listar_livros()

    if len(biblioteca) > 0:
        indice = int(input("Escolha o número do livro que quer remover: "))
        biblioteca.pop(indice)
        print("Livro removido com sucesso.")

def mostrar_menu():
    print("Biblioteca do Lukinhas: ")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Deletar livro")
    print("6 - Sair")

escolha = 0
while escolha != 6:
    mostrar_menu()
    escolha = int(input("Escolha uma das opções: "))

    if escolha == 1:
        cadastrar_livro()
    elif escolha == 2:
        listar_livros()
    elif escolha == 3:
        emprestar_livro()
    elif escolha == 4:
        devolver_livro()
    elif escolha == 5:
        deletar_livro()
    elif escolha == 6:
        print("Volte sempre!")
    else:
        print("Escolha inválida!")
