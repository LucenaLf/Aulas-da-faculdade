import math
import os
os.system('cls')

sombra=float(input('Digite o comprimento da sombra em m: '))
ang=float(input('Digite o ângulo em graus: '))
ang=math.radians(ang)
alt=math.tan(ang)*sombra

print(f'A altura do prédio é: {alt:.2f}')

input('Precione enter para continuar: ')