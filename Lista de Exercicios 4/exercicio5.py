itens_vendidos = []

while True:
    entrada = input("Digite o item e o preço (ex: 'elmo 150'), ou 'fechar' para encerrar: ").strip()
    
    if entrada.lower() == "fechar":
        break

    partes = entrada.split()
    if len(partes) != 2:
        print("Formato inválido. Use: nome_do_item preço (ex: 'elmo 150')")
        continue

    nome_item, preco_str = partes
    try:
        preco = float(preco_str)
        itens_vendidos.append((nome_item, preco))
    except ValueError:
        print("Preço inválido. Digite um número (ex: 150).")

if itens_vendidos:
    item_mais_caro = max(itens_vendidos, key=lambda x: x[1])

    total = sum(preco for _, preco in itens_vendidos)

    itens_ordenados = sorted(itens_vendidos, key=lambda x: x[1])

    print("\n--- Relatório de Vendas ---")
    print(f"Item mais caro: {item_mais_caro[0]} (R$ {item_mais_caro[1]:.2f})")
    print(f"Total arrecadado: R$ {total:.2f}")
    print("Itens do mais barato ao mais caro:")
    for item, preco in itens_ordenados:
        print(f"- {item}: R$ {preco:.2f}")
else:
    print("\nNenhum item foi registrado.")
