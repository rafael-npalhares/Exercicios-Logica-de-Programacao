nomes = []
notas = []
while True:
    print("digite 'sair' para finalizar o programa.")
    entrada = input("diga o nome do aluno: ")
    if entrada == "sair":
        break
    nomes.append(entrada)
    entrada2 = float(input(f"digite a nota do aluno {entrada}:"))
    notas.append(entrada2)
for i, nota in enumerate(notas):
    if nota >= 7:
        print(nomes[i])