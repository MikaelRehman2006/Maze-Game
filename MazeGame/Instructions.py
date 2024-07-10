# Pygame base template for opening a window - MVC version
#
# @author Koushik Jayakumar & Mikael Rehman
# @course ICS3UC
# @date 2021/11/09 Last modified
# Simpson College Computer Science
# http://programarcadegames.com/
#
## Pygame setup

import pygame

pygame.init()

WHITE = (255, 255, 255)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

instructions = pygame.image.load("Instructions.png").convert()
instructions_pos = [0,0]

done = False
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(instructions,instructions_pos)
    pygame.display.flip()
    screen.fill(WHITE)
