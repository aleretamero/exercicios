# Faça um programa em python que abra e reproduza um audio de um arquivo mp3.

from playsound import playsound
import pygame

# playsound("pok1.mp3")

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
