import os
os.system('cls')

#1- Vamos criar um programa que solicite ao usuário um número inteiro com três dígitos e exiba esse número com os dígitos invertidos.

num=int(input('Digite um número inteiro com três digitos: '))

d1= num//100
d2= num%100//10
d3= num%100%10

print(f'{d3} {d2} {d1}')

input('Pressione enter para continuar... ')