x = float(input('nota 1'))
y = float(input('nota2'))


def media():
   conta = (x + y) / 2
   print(conta)
   if conta >= 5:
        print('aprovado')
   else:
       print('reprovado')

media()
