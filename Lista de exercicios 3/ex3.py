#🧩 3. Coleta de Palavras Únicas
palavras = []
encontrado = 0
resposta = ""
while resposta.lower() != "sair":
    resposta = input("\ndiga uma palavra para adicionar a lista ou 'sair' para finalizar o programa:\n")
    if resposta.isdecimal() or resposta.lower() == "sair":
     break
    else: 
       palavras.append(resposta)

unicas = set(palavras)
print(unicas)

print(f"\nQuantidade de palavras diferentes: {len(unicas)}")

print("\nLista em ordem alfabética:")
for palavra in sorted(unicas, key=str.lower):
    print(palavra)
    if palavra == "python":
       encontrado = 1
if encontrado == 1:
   print("\nA palavra 'Python' foi digitada.") 
else:
   print("\nA palavra 'Python' não foi digitada.")

