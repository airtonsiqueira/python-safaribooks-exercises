def listPalindromos(palavras):
    palindromos = []
    for index, palavra in enumerate(palavras):
        if(str(palavra) == str(palavra)[::-1]):
            palindromos.append(palavra)
    return palindromos


def ehPalindromo(palavra):
    if len(palavra) < 2:
        return True
    for x in range(0, round(len(palavra) / 2)):
        y = x - 1
        if(palavra[x] == palavra[y]):
            return True
        y = y - 1


palavras = []

with open("./resources/palavras.txt", "r", encoding="utf-8") as f:
    for line in f:
        palavras.append(line.replace('\n', ''))

    palin = listPalindromos(palavras)
    print(palin)
