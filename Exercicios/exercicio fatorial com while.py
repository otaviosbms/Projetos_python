def fatorial(numero):
  contador = 1
  resultado = 1
  while contador <= numero:
    resultado = resultado * contador
    contador = contador + 1
    print(resultado)

fatorial(5)
