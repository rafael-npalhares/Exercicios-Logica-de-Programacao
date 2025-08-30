inventario = []

while True:
    nome_item = input("Nome do item (ou 'fim' para encerrar): ").strip().lower()
    if nome_item == "fim":
        break

    regiao = input("Região onde foi encontrado: ").strip().lower()

    try:
        quantidade = int(input("Quantidade coletada: ").strip())
    except ValueError:
        print("Quantidade inválida. Use um número inteiro.")
        continue

    inventario.append({
        "item": nome_item,
        "regiao": regiao,
        "quantidade": quantidade
    })
if inventario:
    print("\n--- Inventário de Itens Coletados ---")
    for i, entrada in enumerate(inventario, start=1):
        print(f"{i}. {entrada['quantidade']}x {entrada['item'].capitalize()} (Região: {entrada['regiao'].capitalize()})")
else:
    print("\nNenhum item foi registrado.")
