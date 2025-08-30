produtos = {}

while True:
    entrada = input("Digite o nome do produto e o preço (ex: 'Arroz 5.50') ou 'fim' para encerrar: ").strip()
    if entrada.lower() == "fim":
        break

    if " " in entrada:
        nome, preco_str = entrada.rsplit(" ", 1)
        try:
            preco = float(preco_str.replace(",", "."))
        except ValueError:
            print("Preço inválido. Tente novamente.")
            continue
    else:
        print("Formato inválido. Use: Nome Preço (ex: Arroz 5.50)")
        continue

    produtos[nome] = preco

if produtos:
    mais_caro = max(produtos, key=produtos.get)
    preco_mais_caro = produtos[mais_caro]

    total = sum(produtos.values())

    ordenados = sorted(produtos.items(), key=lambda item: item[1])

    print(f"\nProduto mais caro: {mais_caro} - R$ {preco_mais_caro:.2f}")
    print(f"Total gasto: R$ {total:.2f}")
    print("\nLista de produtos e preços (em ordem de valor):")
    for nome, preco in ordenados:
        print(f"{nome}: R$ {preco:.2f}")
else:
    print("Nenhum produto foi cadastrado.")
