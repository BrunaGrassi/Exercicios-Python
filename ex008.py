# Exercício 8: Solicite ao usuário uma frase e conte quantas vezes cada caractere aparece. Dica: você pode usar um dicionário para armazenar as contagens.

contagem = {}

frase = input("Digite uma frase: ")

for char in frase:
    if char in contagem:
        contagem[char] += 1
    else:
        contagem[char] = 1

print("A quantidade de vezes que cada letra aparece na frase é: ")
for letra, cont in contagem.items():
    print(f"{letra}: {cont}")

