from collections import defaultdict


filmes_por_pessoa = defaultdict(list)
notas_por_genero = defaultdict(list)

filme_mais_bem_avaliado = None
pessoa_mais_filmes = None
contador_filmes_por_pessoa = defaultdict(int)

generos_registrados = set()

while True:
    pessoa = input("Nome da pessoa (ou 'fim' para encerrar): ").strip()
    if pessoa.lower() == "fim":
        break

    filme = input("Nome do filme: ").strip()
    genero = input("Gênero do filme: ").strip().lower()
    try:
        nota = float(input("Nota para o filme (0 a 10): ").strip())
        if nota < 0 or nota > 10:
            print("A nota deve estar entre 0 e 10.")
            continue
    except ValueError:
        print("Nota inválida. Use um número entre 0 e 10.")
        continue


    filmes_por_pessoa[pessoa].append({"filme": filme, "genero": genero, "nota": nota})
    notas_por_genero[genero].append(nota)
    contador_filmes_por_pessoa[pessoa] += 1
    generos_registrados.add(genero)

    if (filme_mais_bem_avaliado is None) or (nota > filme_mais_bem_avaliado["nota"]):
        filme_mais_bem_avaliado = {"filme": filme, "pessoa": pessoa, "nota": nota}

print("\n---  Filmes assistidos por pessoa ---")
for pessoa, filmes in filmes_por_pessoa.items():
    print(f"\n {pessoa}:")
    for info in filmes:
        print(f" - {info['filme']} ({info['genero'].capitalize()}) - Nota: {info['nota']}")


print("\n---  Média de notas por gênero ---")
for genero, notas in notas_por_genero.items():
    media = sum(notas) / len(notas)
    print(f"{genero.capitalize()}: {media:.2f}")


print("\n---  Filme mais bem avaliado ---")
if filme_mais_bem_avaliado:
    print(f"{filme_mais_bem_avaliado['filme']} (Nota: {filme_mais_bem_avaliado['nota']}) - assistido por {filme_mais_bem_avaliado['pessoa']}")
else:
    print("Nenhum filme avaliado.")


print("\n---  Pessoa que assistiu mais filmes ---")
if contador_filmes_por_pessoa:
    pessoa_top = max(contador_filmes_por_pessoa, key=contador_filmes_por_pessoa.get)
    print(f"{pessoa_top} assistiu {contador_filmes_por_pessoa[pessoa_top]} filme(s)")
else:
    print("Nenhuma pessoa registrada.")


print(f"\n---  Gêneros registrados: {len(generos_registrados)} ---")
