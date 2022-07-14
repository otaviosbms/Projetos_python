user = input('coloque um usuario')
pasw = input('escolha uma senha')

while pasw == user:
    pasw = input('escolha uma senha diferente do seu usuario')
    break
if user != pasw:
    print('concluido')

