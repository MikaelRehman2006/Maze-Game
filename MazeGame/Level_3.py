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

#Positions for the fire images
fire_image = pygame.image.load("fire.jpg").convert()
fire_position = [360,425]

fire_image_1 = pygame.image.load("fire.jpg").convert()
fire_position_1 = [555,326]

fire_image_2 = pygame.image.load("fire.jpg").convert()
fire_position_2 = [634,326]

fire_image_3 = pygame.image.load("fire.jpg").convert()
fire_position_3 = [700,326]

fire_image_4 = pygame.image.load("fire.jpg").convert()
fire_position_4 = [155,326]

# Loop until the user clicks the close button.
# Background Music 
background_music = pygame.mixer.Sound("Never Gonna Give You Up Original.mp3")

death_sound = pygame.mixer.Sound("Shotgun - QuickSounds.com.mp3")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Timer 
pygame.time.set_timer(pygame.USEREVENT, 1000, True)
countdown = 60

all_sprites_list_1 = pygame.sprite.Group()
#Player class
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

        self.image = pygame.image.load("character_3.jpg").convert()

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
# Create borders
class Block(pygame.sprite.Sprite):

    def __init__(self,width, height,pos_x,pos_y,color):

        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
# Create black coloured blocks
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
# Create spikes at 0 degrees
class Block_3(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Spike.png").convert()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
# Create spikes at 180 degrees
class Block_4(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Spike.png").convert()
        self.image = pygame.transform.rotate(self.image,180)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
# Create spikes at 90 degrees clockwise
class Block_5(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Spike.png").convert()
        self.image = pygame.transform.rotate(self.image,-90)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
# Create spikes at 90 degrees counter-clockwise
class Block_6(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("Spike.png").convert()
        self.image = pygame.transform.rotate(self.image,90)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

# set player position and attributes
player_1 = Player(15, 10)
all_sprites_list_1.add(player_1)

# Player positions
player_1.rect.x = 600
player_1.rect.y = 550

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

block = Block_2(140,90,720,50,RED)
all_sprites_list_1.add(block)
finish_block_list.add(block)

block = Block_1(300,10,700,500,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(10,350,550,330,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(10,350,450,450,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(100,10,405,270,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(300,10,405,150,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(10,350,350,440,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(10,350,250,320,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(120,10,195,500,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(10,400,140,300,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(660,10,465,100,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

# This represents the spikes
x = 460
for i in range(7):
    block = Block_3(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = x
    block.rect.y = 568
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x +=20

x = 530
for i in range(15):
    block = Block_4(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = x
    block.rect.y = 155
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x -= 20

y = 175
for i in range(16):
    block = Block_5(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = 255
    block.rect.y = y
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    y += 20

y = 175
for i in range(16):
    block = Block_6(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = 520
    block.rect.y = y
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    y += 20

x = 350
for i in range(5):
    block = Block_3(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = x
    block.rect.y = 240
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x +=20

y = 263
for i in range(16):
    block = Block_5(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = 450
    block.rect.y = y
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    y += 20

y = 264
for i in range(16):
    block = Block_6(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = 318
    block.rect.y = y
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    y += 20

x = 235
for i in range(6):
    block = Block_4(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = x
    block.rect.y = 503
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x -= 20

y = 95
for i in range(20):
    block = Block_6(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = 110
    block.rect.y = y
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    y += 20

x = 135
for i in range(25):
    block = Block_3(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = x
    block.rect.y = 68
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

y = 50
for i in range(27):
    block = Block_5(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = 10
    block.rect.y = y
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    y += 20

x = 33
for i in range(14):
    block = Block_3(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = x
    block.rect.y = 568
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x +=20

x = 30
for i in range(31):
    block = Block_4(GREEN, 20, 15)
    # Set a random location for the block
    block.rect.x = x
    block.rect.y = 10
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20


## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    #Moving player code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.changespeed(-5, 0)
            elif event.key == pygame.K_RIGHT:
                player_1.changespeed(5, 0)
            elif event.key == pygame.K_UP:
                player_1.changespeed(0, -5)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, 5)

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
                player_1.changespeed(5, 0)
            elif event.key == pygame.K_RIGHT:
                player_1.changespeed(-5, 0)
            elif event.key == pygame.K_UP:
                player_1.changespeed(0, 5)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, -5)
    
    # Game logic
    # Update
    all_sprites_list_1.update()
    background_music.play()
    # Collision with the finish line
    blocks_hit_list_1 = pygame.sprite.spritecollide(player_1, finish_block_list, False)
    # Collision with maze
    blocks_hit_list_2 = pygame.sprite.spritecollide(player_1, bad_block_list, False)
    
    #If player finishes the game
    for block in blocks_hit_list_2:
        death_sound.play()
        all_sprites_list_1.remove(player_1)
        font = pygame.font.SysFont('Rock wall',50,True,False)
        text = font.render("You Lose!",True,BLACK)
        screen.blit(text,[20,40])
        countdown = 0

    for block in blocks_hit_list_1:
        all_sprites_list_1.remove(player_1)
        good_block_list.add(player_1)
        font = pygame.font.SysFont('Rock wall',50,True,False)
        text = font.render("You Win!",True,BLACK)
        screen.blit(text,[20,40])
        
        
    if player_1 not in all_sprites_list_1:
        if player_1 in good_block_list:
            all_sprites_list_1.remove(player_1)
            font = pygame.font.SysFont('Rock wall',50,True,False)
            text = font.render("Winner",True,BLACK)
            screen.blit(text,[400,30])
            countdown = 0
        else:
            all_sprites_list_1.remove(player_1)
            font = pygame.font.SysFont('Rock wall',50,True,False)
            text = font.render("You Lose!",True,BLACK)
            screen.blit(text,[20,40])
    ## VIEW     
    # Draw
    # Update Screen
    #Blit fire images
    pygame.display.flip()
    screen.fill(WHITE)
    all_sprites_list_1.draw(screen) 
    screen.blit(fire_image,fire_position)
    screen.blit(fire_image_1,fire_position_1)
    screen.blit(fire_image_2,fire_position_2)
    screen.blit(fire_image_3,fire_position_3)
    screen.blit(fire_image_4,fire_position_4)
    pygame.draw.rect(screen, GREEN, [17, 10, 50, 30], 0)
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render(str(countdown), True, BLACK)
    screen.blit(text, [20, 10])
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render("Start",True,BLACK)
    screen.blit(text,[680,520])
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render("End",True,BLACK)
    screen.blit(text,[675,30])
    clock.tick(60)
# Close the window and quit
pygame.quit()
