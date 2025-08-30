agenda = {}

while True:
    entrada = input("Digite o dia da semana e o compromisso (ex: 'terça reunião') ou 'fim' para encerrar: ").strip()
    if entrada.lower() == "fim":
        break

    if " " in entrada:
        dia, compromisso = entrada.split(" ", 1)
    else:
        print("Entrada inválida. Digite no formato: 'dia compromisso'.")
        continue

    dia = dia.lower()

    if dia not in agenda:
        agenda[dia] = []

    agenda[dia].append(compromisso)

print("\nCompromissos cadastrados:")
for dia, compromissos in agenda.items():
    print(f"{dia.capitalize()}:")
    for c in compromissos:
        print(f"  - {c}")

total_compromissos = sum(len(c) for c in agenda.values())
print(f"\nTotal de compromissos cadastrados: {total_compromissos}")

if agenda:
    dia_mais_compromissos = max(agenda, key=lambda d: len(agenda[d]))
    quantidade = len(agenda[dia_mais_compromissos])
    print(f"\nDia com mais compromissos: {dia_mais_compromissos.capitalize()} ({quantidade} compromisso(s))")
else:
    print("\nNenhum compromisso cadastrado.")



