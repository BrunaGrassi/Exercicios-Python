# Exercício 4: Peça ao usuário uma quantidade N de números e retorne a soma deles

soma = 0

while True:
    entrada = input("Digite um número para somar ou pressione 'enter' para sair: \n")
    if entrada == "" or entrada == " ":
        break

    if not entrada.isdigit():
        print("Digite um número válido: \n")
        continue

    else: 
        num = int(entrada)
        soma += num

print("A soma dos números é: ", soma)

