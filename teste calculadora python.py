print('_calculadora Python:_\n')

a= float(input('primeiro numero:\n'))
c= input('operador(+,-,*,/,**):\n')
b= float(input('segundo numero:\n'))


if c == '+':
    print('resultado:',a+b)
      
if c == '-':
    print('resultado:',a-b)
    
if c == '/':
    print('resultado:',a/b)
    
if c == '*':
    print('resutado:',a*b)
    
if c == '**':
    print('resultado:',a**b)

elif c != '+' and c != '-' and c != '*' and c != '/' and c != '**':
    print('operador invalido.')

