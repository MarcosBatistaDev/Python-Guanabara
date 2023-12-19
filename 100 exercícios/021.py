#  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import os
pygame.init()
if os.path.exists('Astra.mp3'):
  pygame.mixer.music.load('Astra.mp3')
  pygame.mixer.music.play()
  pygame.mixer.music.set_volume(1)

  clock = pygame.time.Clock()
  clock.tick(10)

  while pygame.mixer.music.get_busy():
     pygame.event.poll()
     clock.tick(10)
else:
  print('O arquivo musica.mp3 não está no diretório do script Python')