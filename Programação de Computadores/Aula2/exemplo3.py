import os
os.system("cls")
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1+num2
sub =  num1-num2
mult = num1*num2
div = num1/num2
resto = num1%num2
media = (num1+num2)/2

print('O resultado da soma é: ', soma )
print('O resultado da subtração é: ', sub)
print('O resultado da multiplicação é: ', mult)
print('O resultado da divisão é: ', div)
print('O resto da divisão é: ', resto)
print('A media dos valores é: ', media)