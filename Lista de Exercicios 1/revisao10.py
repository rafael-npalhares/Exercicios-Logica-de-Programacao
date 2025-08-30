palavra_secreta = "banana"

letras_reveladas = ["_"] * len(palavra_secreta)
letras_reveladas[0] = palavra_secreta[0]  

tentativas = 0
indice_revelar = 1  

print("Bem-vindo ao Mini Termo!")
print("Adivinhe a palavra. Dica:")
print("".join(letras_reveladas))

while True:
    tentativa = input("Digite sua tentativa: ").strip().lower()
    tentativas += 1

    if tentativa == palavra_secreta:
        print(f"Parabéns! Você acertou a palavra '{palavra_secreta}' em {tentativas} tentativas.")
        break
    else:
        if indice_revelar < len(palavra_secreta):
            letras_reveladas[indice_revelar] = palavra_secreta[indice_revelar]
            indice_revelar += 1
        print("Tente novamente. Dica:")
        print("".join(letras_reveladas))
