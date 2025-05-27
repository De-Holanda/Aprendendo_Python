
palavra = "abacate"

contador_vogais = 0

for letra in palavra:
    letra = letra.upper()
    if letra in "aeiou":
        contador_vogais += 1

print("a palavra", palavra, "tem", contador_vogais, "vogais")