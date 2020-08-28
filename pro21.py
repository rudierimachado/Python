#coding: utf-8
#----------------------------------------------------------------
#  Um programa que abre e reproduz o áudio de um arquivo MP3.
#----------------------------------------------------------------
#  Tocando um MP3 - Exercício #021
#----------------------------------------------------------------

import pygame,mutagen.mp3


opc = str(input('\n Digite bora, para curtir uma  musica:')).lower()

if opc == 'bora':


	mp3file = 'mu.mp3'
	pygame.mixer.init(frequency=mutagen.mp3.MP3(mp3file).info.sample_rate)
	pygame.mixer.music.load(mp3file)
	pygame.mixer.music.play()
	pygame.init()
	pygame.event.wait()

print('obrigado')	

