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
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
## MODEL - Data use in system
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Loop until the user clicks the close button.

x_1 = 150
x_2 = 250
background_music = pygame.mixer.Sound("A-HA - Take On Me.mp3")
death_sound = pygame.mixer.Sound("Shotgun - QuickSounds.com.mp3")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Set up timer
pygame.time.set_timer(pygame.USEREVENT, 1000, True)
countdown = 45

all_sprites_list_1 = pygame.sprite.Group()

# Create player attributes
class Player(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
    def __init__(self, x, y):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("character_1.jpg").convert()

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def changespeed_1(self, x, y):
        """ Change the speed of the player"""
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

#Create attributes to create borders
class Block(pygame.sprite.Sprite):

    def __init__(self,width, height,pos_x,pos_y,color):

        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()


#Create black coloured blocks
class Block_1(pygame.sprite.Sprite):

    def __init__(self,width, height,pos_x,pos_y,color):

        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        
# Create red coloured blocks
class Block_2(pygame.sprite.Sprite):

    def __init__(self,width, height,pos_x,pos_y,color):

        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]


# set player position and attributes
player_1 = Player(10, 15)
all_sprites_list_1.add(player_1)

player_1.rect.x = 100
player_1.rect.y = 500

# Create Sprite lists
bad_block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()
finish_block_list = pygame.sprite.Group()

# Create Maze blocks
block = Block(10,600,100,100,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block(800,10,100,100,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)


block = Block_1(10,600,795,300,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(800,10,400,600,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_2(140,50,720,100,RED)
all_sprites_list_1.add(block)
finish_block_list.add(block)

for i in range(3):
    block = Block_1(10,600,x_1,400,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    x_1 += 200

for i in range(3):
    block = Block_1(10,600,x_2,200,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    x_2 += 200

## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player_1.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player_1.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, 3)
        elif event.type == pygame.USEREVENT:
                # Decrease the countdown
                if countdown > 0:
                    countdown = countdown - 1
                    # Reset the timer
                    pygame.time.set_timer(pygame.USEREVENT, 1000, True)
                else:
                    all_sprites_list_1.remove(player_1)
 
    
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_1.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player_1.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player_1.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, -3)

    # Game logic
    # update 
    all_sprites_list_1.update()
    # play background music
    background_music.play()

    # Collision with the finish line
    blocks_hit_list_1 = pygame.sprite.spritecollide(player_1, finish_block_list, False)

    # Collision with the maze 
    blocks_hit_list_2 = pygame.sprite.spritecollide(player_1, bad_block_list, False)

    for block in blocks_hit_list_2:
        death_sound.play()
        all_sprites_list_1.remove(player_1)
        font = pygame.font.SysFont('Rock wall',50,True,False)
        text = font.render("You Lose!",True,BLACK)
        screen.blit(text,[20,40])
        countdown = 0
    #If player finishes the game
    for block in blocks_hit_list_1:
        all_sprites_list_1.remove(player_1)
        good_block_list.add(player_1)
        font = pygame.font.SysFont('Rock wall',25,True,False)
        text = font.render("You Win!",True,BLACK)
        screen.blit(text,[20,40])
        countdown = 0
        #done = False -- Reid

    if player_1 not in all_sprites_list_1:
        if player_1 in good_block_list:
            all_sprites_list_1.remove(player_1)
            countdown = 0
            #done = False -- Reid
        else:
            all_sprites_list_1.remove(player_1)
            font = pygame.font.SysFont('Rock wall',50,True,False)
            text = font.render("You Lose!",True,BLACK)
            screen.blit(text,[20,40])
            countdown = 0
           
    ## VIEW     
    # Draw
    # Update Screen
    pygame.display.flip()
    screen.fill(WHITE)
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render("Start",True,BLACK)
    screen.blit(text,[20,540])
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render("End",True,BLACK)
    screen.blit(text,[675,40])
    all_sprites_list_1.draw(screen) 
    pygame.draw.rect(screen, GREEN, [0, 0, 70, 50], 0)
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render(str(countdown), True, BLACK)
    screen.blit(text, [10, 10])
    clock.tick(60)
# Close the window and quit
pygame.quit()
