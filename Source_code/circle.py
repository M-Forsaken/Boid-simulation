import random
import pygame
from Helper import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

WINDOW_SIZE = (1200, 700)
root = (0,0)
root2 = (500,400)
root3 = (500,200)
radius = 100
radius2 = 100
radius3 = 100
heading = -180
left_heading = 0
right_heading = 0
points = []

pygame.init()
running = True

if __name__ == "__main__":
    screen = pygame.display.set_mode(WINDOW_SIZE)
    while running:
        screen.fill((0,0,0))
        root = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        points +=(get_Acollision_heading(
            root, heading, radius, root2, radius2))
        pygame.draw.circle(screen,(0,40,70),root2,radius2,0)
        for point in points:
            pygame.draw.line(screen,(255,255,255),root,point,1)
        points = []
        pygame.display.update()



