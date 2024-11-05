# Exercício 6: Peça ao usuário uma lista de números e ordene a lista em ordem crescente. (Não use funções prontas de ordenação.)

numeros_ini = []
numeros = []
cont = 0
troca_posicao = 0

while True: 
    entrada = input("Digite um número: \n")

    if entrada.strip() == "":
        break

    if not entrada.isdigit():
        print("Por favor digite um número válido: ")
        continue

    numeros.append(int(entrada))
    numeros_ini.append(int(entrada))
    
    for i in range(len(numeros)):
        for j in range(0, len(numeros) - i - 1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print(f"A lista informada foi: {numeros_ini} \nA lista ordenada é: {numeros}")





