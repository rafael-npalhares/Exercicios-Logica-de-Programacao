# Jogo da Forca:
palavra_secreta = "sarah-linda"

def validar_letra(letra):
    if letra.strip() and not letra.isalpha() and len(letra.split(" ")) == 1:
        return True
    else:
        return False

def oculto():
    global palavra_secreta
    o = []
    for letra in palavra_secreta:
        if letra.isalpha():
            o.append("_")
        else:
            o.append(letra)
    return "".join(o)

def verificar(palavra_secreta, letra):
    verificacao = []
    for i in palavra_secreta:
        verificacao.append(i)
    if letra.lower() in palavra_secreta.lower():
        posicao = 0
        for i in verificacao:
            if i.lower() == letra.lower():
                return posicao
            else:
                posicao += 1
    else:
        return ""
tentativas = 6
letras_usadas = []
palavra_exibida = list(oculto())

while "_" in palavra_exibida and tentativas > 0:
    print("\nPalavra:", " ".join(palavra_exibida))
    print("Tentativas restantes:", tentativas)
    print("Letras usadas:", ", ".join(letras_usadas))

    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_usadas:
        print("Você já usou essa letra.")
        continue

    letras_usadas.append(letra)

    if letra in palavra_secreta.lower():
        for i, l in enumerate(palavra_secreta):
            if l.lower() == letra:
                palavra_exibida[i] = l
        print("Boa! Letra correta.")
    else:
        tentativas -= 1
        print("Letra incorreta.")
if "_" not in palavra_exibida:
    print("\nParabéns! Você descobriu a palavra:", palavra_secreta)
else:
    print("\nVocê perdeu! A palavra era:", palavra_secreta)
