# Exercício 7: Receba uma lista de nomes e um nome para pesquisar. Informe se o nome está na lista e sua posição.

nomes = []
cont = 0

while True: 
    entrada = input("Digite um nome: ")

    if entrada.strip() == "":
        break

    if entrada.isalpha():
        nomes.append(entrada)

nome_procurado = input("Digite o nome que deseja pesquisar: ")
encontrado = False

for i in range(len(nomes)):
    if nome_procurado == nomes[i]:
        print(f"O nome informado: {nome_procurado} está na lista!")
        print(f"Posição: {i}")
        print(f"A sequencia de nomes digitada foi: {nomes}")
        encontrado = True
        break
    
if encontrado == False:
    print(f"O nome informado: {nome_procurado} não está na lista.")

