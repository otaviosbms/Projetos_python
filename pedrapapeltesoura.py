import random
pedra = range(1, 3)
papel = range(4, 6)
tesoura = range(7, 9)

p1 = input('pedra, papel ou tesoura?')

if p1 == 'pedra':
    print('voce escolheu pedra')


escolhapc = random.randrange(1, 9)
print(escolhapc)
if escolhapc == 1 and escolhapc == 2 and escolhapc = 3:
    print('o computador escolheu pedra')
    
if escolhapc == 4 and escolhapc == 5 and escolhapc = 6:
    print('o computador escolheu papel')
    
if escolhapc == 7 and escolhapc == 8 and escolhapc = 9:
    print('o computador escolheu tesoura')

