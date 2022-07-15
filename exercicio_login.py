while true:
user = input('coloque um usuario\n')
pasw = input('escolha uma senha\n')

if pasw == user:
    print('concluido')
    break
else:
    print('sua senha não pode ser igual o usuario')

