import pygame
import sys

pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Game window")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.flip()
            
pygame.exit()