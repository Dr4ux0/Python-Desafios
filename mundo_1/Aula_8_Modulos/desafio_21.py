# Faça um programa em Python que abra e reproduza um arquivo mp3
from time import sleep

import pygame
import time

pygame.init()
pygame.mixer.music.load('23.mp3')
pygame.mixer.music.play()
pygame.event.wait()
sleep(10000)