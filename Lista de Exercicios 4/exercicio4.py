fila_cafe = []

while True:
    nome = input("Digite o nome do cliente (ou 'fim' para encerrar): ").strip()
    if nome.lower() == "fim":
        break

    preferencia = input("O cliente prefere esperar 'sentado' (início) ou 'em pé' (final)? ").strip().lower()

    if preferencia == "sentado":
        fila_cafe.insert(0, nome)  
    elif preferencia == "em pé":
        fila_cafe.append(nome)     
    else:
        print("Preferência inválida. Use 'sentado' ou 'em pé'.")


print("\n--- Fila do Café ---")
print("Ordem da fila:", fila_cafe)

if fila_cafe:
    print("Primeiro cliente:", fila_cafe[0])
    print("Último cliente:", fila_cafe[-1])
    print("Total de clientes na fila:", len(fila_cafe))
else:
    print("A fila está vazia.")
