aventuras_por_dia = {
    'segunda': [],
    'terça': [],
    'quarta': [],
    'quinta': [],
    'sexta': [],
    'sábado': [],
    'domingo': []
}


total_aventuras = 0


while True:
    entrada = input("Digite o dia e a aventura (ex: 'quarta caça ao tesouro') ou 'fim' para encerrar: ").strip().lower()
    
    if entrada == "fim":
        break

    partes = entrada.split(maxsplit=1)
    if len(partes) < 2:
        print("Entrada inválida. Use o formato: 'dia aventura'")
        continue

    dia, aventura = partes
    if dia not in aventuras_por_dia:
        print("Dia inválido. Use um dia da semana válido.")
        continue

    aventuras_por_dia[dia].append(aventura)
    total_aventuras += 1


dia_mais_aventuras = max(aventuras_por_dia, key=lambda d: len(aventuras_por_dia[d]))


print(f"\n Total de aventuras registradas: {total_aventuras}")
print(f" Dia com mais aventuras: {dia_mais_aventuras.capitalize()}\n")

print(" Aventuras por dia:")
for dia, aventuras in aventuras_por_dia.items():
    print(f"{dia.capitalize()}:")
    for aventura in aventuras:
        print(f"  - {aventura}")
    if not aventuras:
        print("  (nenhuma aventura registrada)")
