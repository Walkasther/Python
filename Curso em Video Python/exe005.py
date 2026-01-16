import math
import random
import pygame





a = float(input("digite um numero "))
print(math.floor(a))

co = float(input('Qual o tamanho do cateto oposto? '))
ca = float(input('Qual o tamanho do cateto adjacente? '))

print('O tamanho da Hipotenusa é: {}'.format(int(math.sqrt(pow(co,2) + pow(ca,2)))))
print('O tamanho da Hipotenuza é: {}'.format(math.hypot(co,ca)))

angulo = int(input('Qual o angulo em graus?'))
#converter o angulo em radiano:
angulo_radiano = math.radians(angulo)

#calcula o seno, cosseno e tangente
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

print('seno: {:.3f}, cosseno: {:.3f}, tangente: {:.3f},'.format(seno, cosseno, tangente))

a1 = 'mateus'
a2 = 'pedro'
a3 = 'sergio'
a4 = 'ricardo'

print(random.choice([a1,a2,a3,a4]))
print(random.sample([a1,a2,a3,a4],4))

pygame.mixer.init()
pygame.mixer.music.load('C:/Users/SONY VAIO/Music/até que enfim estamos juntos.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
