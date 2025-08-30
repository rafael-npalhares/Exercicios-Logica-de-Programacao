#🧩 1. Exploradores do Espaço]
planetas = []
visitados = 0 
while True:
    entrada = input("digite o nome do planeta que você visitou(digite um numero ou escreva 'parar' para finalizar):\n")
    if entrada.lower() == "parar" or entrada.isdecimal():
      break
    else:
       planetas.append(entrada)
       visitados = visitados + 1

print("\n--- Relatório da Missão Espacial ---")

if planetas:
    planeta_mais_longo = ""
    print("\nPlanetas visitados em ordem alfabética:")
    for planeta in sorted(planetas):
        print(f"- {planeta}")

        if len(planeta) > len(planeta_mais_longo):
            planeta_mais_longo = planeta
    print(f"Total de planetas visitados: {visitados}")
    print(f"o planeta com o nome mais longo é {planeta_mais_longo} ")
else:
    print("Nenhum planeta foi visitado nesta missão.")