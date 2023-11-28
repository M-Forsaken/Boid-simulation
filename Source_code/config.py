import random
import pygame
import math
import numpy as np
import os

CWD = os.getcwd()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(64)

# screen size
# 1920 1080
# 1366 768
# parameters
clock = pygame.time.Clock()
Width = 1366
Height = 768
TimeStep = 0
last_time = pygame.time.get_ticks()
alignmentF = 0.1
cohesionF = 0.1
separationF = 1
avoidF = 10
screenF = 30
separation_toggle = False
cohesion_toggle = False
alignment_toggle = False
avoid_toggle = False
completed = True
running = True
obs_radius = 50
screenMargin = 50
Flock = []
Obstacle = []
Heading_Points = []
Show_UI = True


# message variable
font = pygame.font.Font(CWD + '/assets/retro_font.ttf', 14)
menufont = pygame.font.Font(CWD + '/assets/retro_font.ttf', 11)
text = font.render('default', True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.topleft = (70, Height - 100)
text_alpha = 0
fade = True
start = pygame.time.get_ticks()
mess_queue = []

# FPS_text variable
FPS = 60
FPS_text = font.render('default', True, (255, 255, 255), (0, 0, 0))
FPS_textRect = FPS_text.get_rect()
FPS_textRect.topleft = (50, 40)

# Music and sound
pygame.mixer.music.load(CWD + '/assets/sound/BackGround_Music.mp3')
pygame.mixer.music.play(-1, 0, 500)
click_sound = pygame.mixer.Sound(CWD +'/assets/sound/click_sound.wav')
click_sound.set_volume(0.4)




