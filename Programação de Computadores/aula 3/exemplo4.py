import math
import os
os.system('cls')

r=float(input('Digite o raio do circulo em cm: '))

a=(r**2)*math.pi
p=(r*2)*math.pi

print(f'A área do circulo é: {a:.2f}cm²')
print(f'O comprimento do circulo é: {p:.2f}cm')

input('Pressione enter para continuar... ')