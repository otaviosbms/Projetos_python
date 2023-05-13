print('calculadora Python:\n')

teste = "mateus"

a = float(input("Primeiro Numero:\n"))
b = input("operador(+,-,*,/,**):\n")

while b != '+' and b != '-' and b != '*' and b!= '/' and b != '**':
    b = input("o seu operador é inválido\nescolha outro:\n")
 
c = float(input("Segundo Numero:\n"))


if b == '+':
    print('resultado:',a + c)


if b == '-':
    print('resultado:',a - c)


if b == '*':
    print('resultado:',a * c)


if b == '/':
    print('resultado:',a / c)


if b == '**':
    print('resultado:',a ** c)
