notas = {}

while True:
    entrada = input("Digite o nome do aluno e a nota (ex: 'Maria 8.5') ou 'fim' para encerrar: ")
    if entrada.lower() == "fim":
        break

    if " " in entrada:
        partes = entrada.rsplit(" ", 1)
        nome = partes[0]
        nota_str = partes[1]

        if nota_str.replace(".", "", 1).isdigit():
            nota = float(nota_str)
            notas[nome] = nota
        else:
            print("Nota inválida. Digite um número válido (ex: João 7.5).")
    else:
        print("Formato inválido. Use: Nome Nota (ex: João 7.5)")


if len(notas) > 0:
    media_geral = sum(notas.values()) / len(notas)
    melhor_aluno = max(notas, key=notas.get)
    melhor_nota = notas[melhor_aluno]

    print(f"\nMédia geral das notas: {media_geral:.2f}")
    print(f"Melhor desempenho: {melhor_aluno} com nota {melhor_nota:.2f}")
    print("\nLista completa de alunos e notas:")
    for nome, nota in notas.items():
        print(f"{nome}: {nota:.2f}")
else:
    print("Nenhuma nota foi cadastrada.")
