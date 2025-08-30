# To-do List em Python

tarefas = []  
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({"descricao": descricao, "status": "pendente"})
    print("Tarefa adicionada com sucesso!\n")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    print("\n--- LISTA DE TAREFAS ---")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['descricao']} [{tarefa['status']}]")
    print()

def concluir_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        indice = int(input("Digite o número da tarefa para concluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["status"] = "concluída"
            print("Tarefa concluída!\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"Tarefa '{removida['descricao']}' removida.\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def filtrar_tarefas():
    status = input("Filtrar por (pendente/concluída): ").lower()
    filtradas = [t for t in tarefas if t["status"] == status]
    if not filtradas:
        print("Nenhuma tarefa encontrada com esse status.\n")
        return
    print(f"\n--- TAREFAS {status.upper()}S ---")
    for i, tarefa in enumerate(filtradas, start=1):
        print(f"{i}. {tarefa['descricao']} [{tarefa['status']}]")
    print()

def menu():
    while True:
        print("===== TO-DO LIST =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Filtrar tarefas por status")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            filtrar_tarefas()
        elif opcao == "6":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida!\n")
menu()
