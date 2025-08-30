estoque = {}

while True:
    nome = input("Nome do alimento (ou 'fim' para encerrar): ").strip()
    if nome.lower() == "fim":
        break

    categoria = input("Categoria (ex: 'legume', 'fruta', 'grão'): ").strip().lower()
    
    quantidade_str = input("Quantidade em unidades: ").strip()
    if not quantidade_str.isdigit():
        print("Quantidade inválida. Digite um número inteiro.")
        continue
    
    quantidade = int(quantidade_str)

    if categoria not in estoque:
        estoque[categoria] = []
    
    estoque[categoria].append((nome, quantidade))


print("\nAlimentos agrupados por categoria:")
for categoria, alimentos in estoque.items():
    print(f"\nCategoria: {categoria.capitalize()}")
    for nome, quantidade in alimentos:
        print(f" - {nome}: {quantidade} unidades")


print("\nTotal de unidades por categoria:")
for categoria, alimentos in estoque.items():
    total_unidades = sum(qtd for _, qtd in alimentos)
    print(f"{categoria.capitalize()}: {total_unidades} unidades")


maior_alimento = None
maior_quantidade = -1
for alimentos in estoque.values():
    for nome, quantidade in alimentos:
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            maior_alimento = nome

if maior_alimento:
    print(f"\nAlimento com maior quantidade cadastrada: {maior_alimento} ({maior_quantidade} unidades)")


num_categorias = len(estoque)
print(f"\nNúmero de categorias diferentes utilizadas: {num_categorias}")
