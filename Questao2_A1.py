def VogalporX(texto):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    textomod = ""
    for letra in texto:
        if letra in vogais:
            textomod += 'x'
        else:
            textomod += letra
    return textomod

TextoDoUso= input("Digite o texto: ")
textomod = VogalporX(TextoDoUso)
print("Seu Texto com as letras X é: ", textomod)