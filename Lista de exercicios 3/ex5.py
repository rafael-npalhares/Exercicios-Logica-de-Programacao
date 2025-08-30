itens = []

while True:
    item = input("Digite o nome do item (ou 'fim' para encerrar): ").strip()
    if item.lower() == "fim":
        break

    posicao = input("Colocar no início ou final? (digite 'inicio' ou 'final'): ").strip().lower()

    if posicao == "inicio":
        itens.insert(0, item)
    elif posicao == "final":
        itens.append(item)
    else:
        print("Posição inválida. O item será adicionado ao final por padrão.")
        itens.append(item)

print("\nEstrutura completa:")
print(itens)

if itens:
    print(f"Primeiro item: {itens[0]}")
    print(f"Último item: {itens[-1]}")
else:
    print("Nenhum item foi adicionado.")

print(f"Total de itens adicionados: {len(itens)}")
