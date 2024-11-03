# Exercício 3: Recebe um número e retorna a tabuada

numero = int(input("Digite um número: "))
print("A tabuada do número ", numero, " é: \n")

for num in range(1,11):
    print(numero, " x ", num, " = ", (numero * num), "\n")