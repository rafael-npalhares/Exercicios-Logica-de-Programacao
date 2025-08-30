palavras_magicas = set()

while True:
    palavra = input("Digite uma palavra mágica (ou 'acabar' para encerrar): ").strip().lower()
    
    if palavra == "acabar":
        break
    palavras_magicas.add(palavra)


lista_palavras = list(palavras_magicas)

quantidade = len(lista_palavras)


if lista_palavras:
    mais_longa = max(lista_palavras, key=len)
else:
    mais_longa = None

tem_abracadabra = "abracadabra" in palavras_magicas


print(f"\nVocê coletou {quantidade} palavra(s) mágica(s) única(s).")

if mais_longa:
    print(f"A palavra mágica mais longa é: '{mais_longa}'")
else:
    print("Nenhuma palavra mágica foi coletada.")

print("A palavra 'abracadabra' está na lista?" , "Sim" if tem_abracadabra else "Não")
