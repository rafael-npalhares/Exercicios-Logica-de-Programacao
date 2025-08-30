from collections import defaultdict

biblioteca = defaultdict(list) 

while True:
    nome = input("Nome do livro (ou 'fim' para encerrar): ").strip()
    if nome.lower() == "fim":
        break

    genero = input("Gênero do livro: ").strip().lower()

    try:
        quantidade = int(input("Quantidade disponível: ").strip())
    except ValueError:
        print("Quantidade inválida. Por favor, digite um número inteiro.")
        continue

  
    biblioteca[genero].append({"nome": nome, "quantidade": quantidade})


print("\n--- Livros agrupados por gênero ---")
for genero, livros in biblioteca.items():
    print(f"\nGênero: {genero.capitalize()}")
    for livro in livros:
        print(f" - {livro['nome']} (Quantidade: {livro['quantidade']})")

print("\n--- Total de livros por gênero ---")
for genero, livros in biblioteca.items():
    total_quantidade = sum(l["quantidade"] for l in livros)
    print(f"{genero.capitalize()}: {total_quantidade} livro(s)")


livro_mais_estoque = None
for livros in biblioteca.values():
    for livro in livros:
        if livro_mais_estoque is None or livro["quantidade"] > livro_mais_estoque["quantidade"]:
            livro_mais_estoque = livro

print("\n--- Livro com maior quantidade disponível ---")
if livro_mais_estoque:
    print(f"{livro_mais_estoque['nome']} com {livro_mais_estoque['quantidade']} unidade(s)")
else:
    print("Nenhum livro cadastrado.")


print(f"\nQuantidade de gêneros diferentes cadastrados: {len(biblioteca)}")
