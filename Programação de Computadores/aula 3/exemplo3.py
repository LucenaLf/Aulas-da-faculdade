import math
import os
os.system('cls')

num=float(input('Digite um número real: '))
absoluto=math.fabs(num)
inteiro=math.floor(absoluto)
raiz=math.sqrt(absoluto)
fatorial=math.factorial(inteiro)

print(f'O valor absoluto de {num} é: {absoluto}')
print(f'O valor da parte inteira de {num} é: {inteiro}')
print(f'O valor da raiz de {num} é: {raiz:.2f}')
print(f'O valor da fatorial de {num} é: {fatorial}')

input('Pressione enter para continuar...')