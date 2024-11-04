# Exercício 5: Verifica se uma palavra recebida é um palíndromo (é lida da mesma forma de trás para frente, ignorando espaços e pontuação)

palavra = input("Digite uma palavra: \n").lower()
palavra = ''.join(char for char in palavra if char.isalnum())

if palavra == palavra[::-1]:
    print(f"A palavra inserida {palavra} é um palíndromo.")
else :
    print(f"A palavra inserida {palavra} não é um palíndromo.")