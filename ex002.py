# Exercício 2: Solicite ao usuário uma palavra e conte quantas vogais existem na palavra.

cont = 0
lista = list(input("Digite uma palavra: "))
for letra in lista:
    match letra:
        case 'a':
            cont += 1
        case 'e':
            cont += 1
        case 'i':
            cont += 1
        case 'o':
            cont += 1
        case 'u':
            cont += 1

print("A palavra digitada contém ", cont, " vogais.")    
