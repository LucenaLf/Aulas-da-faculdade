import os
os.system('cls')
nome = input('Digite seu nome: ')
disciplina = input('Digite sua disciplina: ')
nota1 = float(input('Digite sua 1ª nota: '))
nota2 = float(input('Digite sua 2ª nota: '))
media = (nota1+nota2)/2
print('nome:', nome)
print('disciplina:', disciplina)
print(f'nota1: {nota1:.2f}')
print(f'nota2: {nota2:.2f}')
print(f'media: {media:.2f}')