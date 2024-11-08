palavra = input('Digite uma palavra: ')
contador = 0

for r in list(palavra):
    if r == 'a':
        contador =+ 1
    elif r == 'e':
        contador =+ 1
    elif r == 'i':
        contador =+ 1
    elif r == 'o':
        contador =+ 1
    elif r == 'u':
        contador =+ 1
print(f'Existem {contador} vogais nessa palavra')

# --------------- Solução CHATGPT ---------------
# palavra = input('Digite uma palavra: ')

# for letra in palavra:
#     if letra.lower() in 'aeiou':
#         contador += 1

# print(f'Existem {contador} vogais nessa palavra')