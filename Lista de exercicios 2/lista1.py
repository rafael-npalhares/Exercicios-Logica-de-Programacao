#CRUD de contatos
contatos = []

def adicionar_contato():
    nome = input("digite o nome do contato: ")
    telefone = input("digite o número do contato: ")
    email = input("digite o email: ")
    if telefone.isnumeric() and nome.isalpha():
        contato = {
            "nome" : nome, 
            "telefone" : telefone,
            "email" : email
        }
        contatos.append(contato)
def listar_contatos():
    if contatos:
        for i, contato in enumerate(contatos):
            print(f"contato {i+1}: \nnome: {contato["nome"]} \ntelefone: {contato["telefone"]} \nemail: {contato["email"]}")
            print()

def buscar(contatoX):
    if contatos: 
        for i in contatos:
            if i["nome"].lower() == contatoX.lower():
                print(f"nome: {i["nome"]} \ntelefone: {i["telefone"]} \nemail: {i["email"]}")
    else:
        print("Esse contato não foi encontrado ou você não possui contatos.")

def editar(contatoX):
    global contatos
    if contatos:
        for i, contato in enumerate(contatos):
            if contato["nome"].lower() == contatoX.lower():
                nome = input("digite o novo nome do contato: ")
                telefone = input("digite o novo número do contato: ")
                email = input("digite o novo email: ")
                contatos[i] = {
                                "nome" : nome, 
                                "telefone" : telefone,
                                "email" : email
                            }
    else:
        print("Esse contato não foi encontrado ou você não possui contatos.")

def remover(contatoX):
    if contatos:
        for i, contato in enumerate(contatos):
            if contato["nome"].lower() == contatoX.lower():
                contatos.remove(contatos[i])
    else:
        print("Esse contato não foi encontrado ou você não possui contatos.") 

def menu():
    while True:
        print("SELECIONE UMA OPÇÃO\n===================================================\n1- Adicionar Contato\n2- Listar Contato\n3- Buscar contato\n4- Editar contato \n5- Remover contato\n6- Sair")
        entrada = int(input())
        if entrada == 1:
            adicionar_contato()
        if entrada == 2:
            listar_contatos()
        if entrada == 3:
            contatoX = input("digite o contato que deseja buscar: ")
            buscar(contatoX)
        if entrada == 4:
            listar_contatos()
            print()
            contatoY = input("digite o NOME do contato que deseja editar: ")
            editar(contatoY)
        if entrada == 5:
            listar_contatos()
            print()
            contatoZ = input("digite o nome do contato que deseja eliminar: ")
            remover(contatoZ)
        if entrada == 6: 
            break


menu()
    
