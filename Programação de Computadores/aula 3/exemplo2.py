import math
import os
os.system ("cls")

num=float(input('Digite um número para saber a raiz: '))

r= math.sqrt(math.fabs(num))

print(f'A raiz de {num:.0f} é: {r:.2f}')

input('Pressione enter para continuar...')