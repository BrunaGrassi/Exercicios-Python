# # Exercício 10.2: Implemente uma função que calcule o fatorial de um número usando recursão.

print("Calcular o fatorial de um número. ")
num = int(input("Insira um número: "))

def fat(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fat(num - 1)
    
resultado = fat(num)
print("O resultado é: " , resultado)