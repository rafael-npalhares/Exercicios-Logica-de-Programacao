funcionarios = []

def cadastrar_funcionario():
    nome = input("Digite o nome do novo funcionário: ")
    funcionarios.append(nome)
    print(f"Funcionário {nome} cadastrado com sucesso!")

def listar_funcionarios():
    if funcionarios:
        print("\nLista de Funcionários:")
        for funcionario in funcionarios:
            print(funcionario)
    else:
        print("Nenhum funcionário cadastrado.")

def buscar_funcionario():
    nome = input("Digite o nome do funcionário que deseja buscar: ")
    if nome in funcionarios:
        print(f"Funcionário {nome} encontrado.")
    else:
        print(f"Funcionário {nome} não encontrado.")

def excluir_funcionario():
    nome = input("Digite o nome do funcionário que deseja excluir: ")
    if nome in funcionarios:
        funcionarios.remove(nome)
        print(f"Funcionário {nome} excluído com sucesso.")
    else:
        print(f"Funcionário {nome} não encontrado.")

def exibir_menu():
    opcao = ''
    
    while opcao != '5': 
        print("\nMenu:")
        print("1. Cadastrar novo funcionário")
        print("2. Listar todos os funcionários")
        print("3. Buscar um funcionário pelo nome")
        print("4. Excluir um funcionário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            buscar_funcionario()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            print("Saindo do programa...")
        else:
            print("Opção inválida. Tente novamente.")

exibir_menu()
