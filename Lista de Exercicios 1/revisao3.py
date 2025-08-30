lista = []
for i in range(5):
    numero = int(input("digite um numero para adicionar a lista: "))
    lista.append(numero)
print(f"O maior é: {max(lista)}")
print(f"O menor é: {min(lista)}")
print(f"A média é dos valores é: {sum(lista)/len(lista)}")