#  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame # PROGRAMA NÃO FUNCIONOU - NÃO TOCA O ARQUIVO - ERRO DIZENDO QUE O ARQUIVO NÃO FOI LOCALIZADO NO DIRETÓRIO, MAS O ARQUIVO ESTÁ NO LOCAL.
pygame.init()
pygame.mixer.init()
pygame.mixer_music.load('alice_chains.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


