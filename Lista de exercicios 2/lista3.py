pokemons = []

def cadastrar_pokemon():
    nome = input("Nome do Pokémon: ")
    tipo = input("Tipo do Pokémon: ")
    ataque = int(input("Ataque do Pokémon: "))
    vida = int(input("Pontos de vida do Pokémon: "))
    pokemons.append({"nome": nome, "tipo": tipo, "ataque": ataque, "vida": vida})
    print(f"{nome} cadastrado com sucesso.\n")

def listar_pokemons():
    if not pokemons:
        print("Nenhum Pokémon cadastrado.\n")
        return
    print("\n--- POKÉDEX ---")
    for i, p in enumerate(pokemons, start=1):
        print(f"{i}. {p['nome']} | Tipo: {p['tipo']} | Ataque: {p['ataque']} | Vida: {p['vida']}")
    print()

def batalhar():
    if len(pokemons) < 2:
        print("Cadastre pelo menos 2 Pokémons para batalhar.\n")
        return
    
    listar_pokemons()
    try:
        i1 = int(input("Número do primeiro Pokémon: ")) - 1
        i2 = int(input("Número do segundo Pokémon: ")) - 1

        if i1 == i2 or i1 not in range(len(pokemons)) or i2 not in range(len(pokemons)):
            print("Escolha inválida.\n")
            return

        p1 = pokemons[i1].copy()
        p2 = pokemons[i2].copy()

        print(f"\nBATALHA: {p1['nome']} VS {p2['nome']}\n")

        while p1["vida"] > 0 and p2["vida"] > 0:
            p2["vida"] -= p1["ataque"]
            print(f"{p1['nome']} atacou {p2['nome']} (Vida restante: {max(p2['vida'],0)})")
            if p2["vida"] <= 0:
                print(f"{p1['nome']} venceu a batalha.\n")
                break

            p1["vida"] -= p2["ataque"]
            print(f"{p2['nome']} atacou {p1['nome']} (Vida restante: {max(p1['vida'],0)})")
            if p1["vida"] <= 0:
                print(f"{p2['nome']} venceu a batalha.\n")
                break

    except ValueError:
        print("Entrada inválida.\n")

def menu():
    while True:
        print("===== POKÉDEX =====")
        print("1. Cadastrar Pokémon")
        print("2. Listar Pokémons")
        print("3. Batalhar")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pokemon()
        elif opcao == "2":
            listar_pokemons()
        elif opcao == "3":
            batalhar()
        elif opcao == "4":
            print("Saindo da Pokédex.")
            break
        else:
            print("Opção inválida.\n")

menu()

