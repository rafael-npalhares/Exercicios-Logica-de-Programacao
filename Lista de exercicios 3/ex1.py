numeros = []
while True:
    resposta = input("diga o numero que quer adicionar na lista ou um NAO numero para finalizar: ")
    if not resposta.isdecimal():
        break
    numeros.append(int(resposta))
if numeros:
  print("qtd:", len(numeros))
  print("Média:", sum(numeros)/len(numeros))
  print("maior:", max(numeros))    
  print("menor:", min(numeros))