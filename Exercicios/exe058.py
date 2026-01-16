#Melhore o jogo do desafio 028, onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar
#adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('{:-^50}'.format('JOGO DA ADIVINHAÇÃO'))

n = randint(0,10)
n1 = int(input('\033[30;107mVamos ver se você adivinha o número que eu pensei!!\033[m\nDigite um número entre 0 e 10: '))
c = 1
while n1 != n:
    c += 1
    s = 'Mais' if n1 < n else 'Menos'
    n1 = int(input('\033[31mNúmero errado! tente de novo haha(dica: %s): ' % s))
print('\033[32m')
if c == 1:
    print('Parabéns! Você acertou de primeira!!')
else:
    print('Aeee! Finalmente você acertou. Você precisou de %i tentativas para acertar!' % c)
