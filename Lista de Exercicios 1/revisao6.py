#Agenda de contatos (simples):
agenda = dict()
def verificar_pessoa(pessoa):
    if pessoa.lower() == "finalizar":
        return False 
    if " " in pessoa:
        if pessoa.split(" ") and not pessoa.isnumeric():
            return True
    elif not pessoa.isnumeric():
        return True
    else: return False

def verificar_numero(numero):
    if numero.lower() == "finalizar":
        return False
    if numero.isnumeric():
            return True
    else: return False

def adicionar(pessoa, numero):
    agenda[f"{pessoa}"] = f"{numero}"

def procurar(nome):
    for chave, valor in agenda.items():
        if not chave.isnumeric() and chave.lower() == nome.lower():
            print(f"{chave} : {valor}")
            return
    else:
        print(f"{nome} não encontrado na agenda!")
def listar():
    if agenda:
        for chave, valor in agenda.items():
            print(f"{chave} : {valor}")
        return
    else: print("A agenda está vazia!")

while True:
    entrada = input("ESCOLHA A OPÇÃO DESEJADA: \n1- Adicionar pessoa na agenda. \n2- encontrar pessoa na agenda.\n3- listar pessoas na agenda. \n4- sair do sistema.\n")
    if entrada == "1":
        valido = False 
        while not valido:
            pessoa = input("digite o nome da pessoa: ")
            valido = verificar_pessoa(pessoa)
        valido2 = False
        while not valido2:
            numero = input("digite seu numero: ")
            valido2 = verificar_numero(numero)
        adicionar(pessoa, numero)
    if entrada == "2":
        valido = False 
        while not valido:
            nome = input("digite o nome da pessoa que deseja achar na agenda: ")
            valido = verificar_pessoa(nome)
        procurar(nome)
    if entrada == "3":
        listar()
    if entrada == "4":
        break