"""
Seuraan YouTube tutoriaalia, jossa toteutetaan main tiedosto pelille
freeCodeCamp.org "Python Platform Game Tutorial for Beginners"
"""

import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)   #taustaväri valkoinen, kaikki ääriarvossa
WIDTH, HEIGHT = 1000, 800
FPS = 60   #frames per second
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))
