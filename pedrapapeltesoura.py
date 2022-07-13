pedra = 1
papel = 2
tesoura = 3

p1 = input('pedra, papel ou tesoura?')

if p1 == 'pedra':
    print('voce escolheu pedra')

if p1 == 'papel':
    print('voce escolheu papel')

if p1 == 'tesoura':
    print('voce escolheu tesoura')

import random
    
escolhapc = random.randrange(1, 3)

if escolhapc == 1:
    print('o computador escolheu pedra')
    
if escolhapc == 2:
    print('o computador escolheu papel')
    
if escolhapc == 3:
    print('o computador escolheu tesoura')


