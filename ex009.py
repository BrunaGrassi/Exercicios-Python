# Exercício 9: Crie um programa que gere uma senha aleatória com uma quantidade definida de caracteres. A senha deve incluir letras maiúsculas, minúsculas, números e símbolos especiais.

import string
import random

seq = string.ascii_letters + string.digits + string.punctuation

senha = ''.join(random.choices(seq, k=15))

print("A nova senha é: " + senha)


