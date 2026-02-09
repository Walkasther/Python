# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

import pygame

print('\033[4;1mReproduzindo...')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('audio/ate_que_enfim_estamos_juntos.mp3')
pygame.mixer.music.play()
pygame.event.wait()

