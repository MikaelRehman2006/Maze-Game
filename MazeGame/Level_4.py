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
BLUE = (0, 0, 255)

x_1 = 150
x_2 = 250
background_music = pygame.mixer.Sound("Van-Halen-Jump.mp3")
death_sound = pygame.mixer.Sound("Shotgun - QuickSounds.com.mp3")

score = 1
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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

        self.image = pygame.image.load("character_4.png").convert()

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
# Create teleport block
class Block_7(pygame.sprite.Sprite):

    def __init__(self,width, height,pos_x,pos_y,color):

        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
# Create lazerbeam
class Block_8(pygame.sprite.Sprite):

    def __init__(self,width, height,pos_x,pos_y,color):

        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
# Create heart
class Heart(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("heart.jpg").convert()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
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

def credits():
    if player_1 in good_block_list:
        credits = pygame.image.load("credits.png")
        credits_pos = [0,0]
        screen.blit(credits,credits_pos)
    else:
        font = pygame.font.SysFont('Rock wall',50,True,False)
        text = font.render("Try Again!",True,BLACK)
        screen.blit(text,[400,300])

# set player position and attributes
player_1 = Player(10, 15)
all_sprites_list_1.add(player_1)

# Player positions
player_1.rect.x = 30
player_1.rect.y = 50

# Create Sprite lists
bad_block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()
finish_block_list = pygame.sprite.Group()
teleport_block_list = pygame.sprite.Group()
life_list = pygame.sprite.Group()
life_list_2 = pygame.sprite.Group()

# Create heart
heart = Heart(GREEN, 20, 15)
heart.rect.x = 40
heart.rect.y = 240
all_sprites_list_1.add(heart)
life_list_2.add(heart)

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
    
block = Block_2(125,90,400,55,RED)
all_sprites_list_1.add(block)
finish_block_list.add(block)

offset_x = 200
for i in range(3):
    block = Block_1(10,200,offset_x,200,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200 
    
offset_x = 200
for i in range(3):
    block = Block_1(10,200,offset_x,450,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200 

offset_x = 200
for i in range(3):
    block = Block_1(125,10,offset_x,350,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200 

offset_x = 200
for i in range(3):
    block = Block_1(125,10,offset_x,300,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200 

offset_x = 200
for i in range(3):
    block = Block_1(125,10,offset_x,550,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200

offset_x = 200
for i in range(3):
    block = Block_1(125,10,offset_x,100,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200

offset_x = 300
for i in range(2):
    block = Block_1(100,10,offset_x,200,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200

offset_x = 300
for i in range(2):
    block = Block_1(100,10,offset_x,450,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200

offset_y = 450
for i in range(2):
    block = Block_1(10,200,658,offset_y,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x -= 250

offset_y = 450
for i in range(2):
    block = Block_1(10,200,143,offset_y,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x -= 250

offset_y = 450
for i in range(2):
    block = Block_1(80,10,50,offset_y,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 250

offset_y = 200
for i in range(2):
    block = Block_1(80,10,750,offset_y,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_y += 250

offset_y = 210
for i in range(2):
    block = Block_1(10,50,715,offset_y,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_y -= 20


offset_y = 440
for i in range(2):
    block = Block_1(10,50,85,offset_y,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_y += 20

block = Block_1(10,60,710,450,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(10,70,85,200,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

offset_x = 143
for i in range(2):
    block = Block_1(10,150,offset_x,20,BLACK)
    all_sprites_list_1.add(block)
    bad_block_list.add(block)
    offset_x += 200

block = Block_1(170,10,115,200,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(139,10,10,200,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(20,20,25,570,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

block = Block_1(20,20,700,570,BLACK)
all_sprites_list_1.add(block)
bad_block_list.add(block)

# Create spikes
x = 5
for i in range(4):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 170
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 720
for i in range(4):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 170
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20


x = 5
for i in range(4):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 205
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 720
for i in range(4):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 205
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20


x = 5
for i in range(4):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 420
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 720
for i in range(4):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 420
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 5
for i in range(4):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 455
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 720
for i in range(4):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 455
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20


x = 250
for i in range(5):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 420
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 250
for i in range(5):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 455
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 450
for i in range(5):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 420
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 450
for i in range(5):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 455
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 250
for i in range(5):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 170
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 250
for i in range(5):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 205
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 450
for i in range(5):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 170
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 450
for i in range(5):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 205
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 140
for i in range(6):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 70
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20


x = 540
for i in range(6):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 70
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 140
for i in range(6):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 70
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 540
for i in range(6):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 320
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 140
for i in range(6):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 300
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20


x = 340
for i in range(2):
    block = Block_3(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 320
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

x = 400
for i in range(3):
    block = Block_4(GREEN, 20, 15)
        # Set a random location for the block
    block.rect.x = x
    block.rect.y = 300
    bad_block_list.add(block)
    all_sprites_list_1.add(block)
    x += 20

# Create teleport block
block = Block_7(20,20,115,55,BLUE)
all_sprites_list_1.add(block)
teleport_block_list.add(block)

# Create lazerbeam
block = Block_8(670,20,365,570,RED)
all_sprites_list_1.add(block)
life_list.add(block)
 
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

        # Catch a user event - change colour
    # Decrease the countdown
    # Update
    all_sprites_list_1.update()
    background_music.play()
    # Collision with the finish line
    blocks_hit_list_1 = pygame.sprite.spritecollide(player_1, finish_block_list, False)
    # Collision with the maze
    blocks_hit_list_2 = pygame.sprite.spritecollide(player_1, bad_block_list, False)
    # Collision with the teleport block
    blocks_hit_list_3 = pygame.sprite.spritecollide(player_1, teleport_block_list, True)
    # Collision with the lazerbeam
    blocks_hit_list_4 = pygame.sprite.spritecollide(player_1, life_list, True)
    # Collision with the heart
    blocks_hit_list_5 = pygame.sprite.spritecollide(player_1, life_list_2, True)

    #If player finishes the game
    for block in blocks_hit_list_2:
        death_sound.play()
        all_sprites_list_1.remove(player_1)
        font = pygame.font.SysFont('Rock wall',40,True,False)
        text = font.render("You Lose!",True,BLACK)
        screen.blit(text,[150,40])
        countdown = 0
        credits()
        done = False

    for block in blocks_hit_list_1:
        countdown = 0
        all_sprites_list_1.remove(player_1)
        good_block_list.add(player_1)
        font = pygame.font.SysFont('Rock wall',50,True,False)
        text = font.render("You Win!",True,BLACK)
        screen.blit(text,[160,40])
        font = pygame.font.SysFont('Rock wall',50,True,False)
        text = font.render("Champion!",True,BLACK)
        screen.blit(text,[500,40])
        credits()
        done = False

    for block in blocks_hit_list_3: 
        player_1.rect.x += 55
        all_sprites_list_1.add(player_1)

    for block in blocks_hit_list_4:
        score -= 1
        if score == 0:
            all_sprites_list_1.remove(player_1)

    for block in blocks_hit_list_5:
        score += 1

    if score == 0:
        font = pygame.font.SysFont('Rock wall',40,True,False)
        text = font.render("You Lose!",True,BLACK)
        screen.blit(text,[150,40])
        countdown = 0
        death_sound.play()
        credits()
        done = False

    if player_1 not in all_sprites_list_1:
        if player_1 in good_block_list:
            all_sprites_list_1.remove(player_1)
            countdown = 0
            done = False
        else:
            all_sprites_list_1.remove(player_1)
            font = pygame.font.SysFont('Rock wall',40,True,False)
            text = font.render("You Lose!",True,BLACK)
            screen.blit(text,[150,40])
            credits()
            done = False

    ## VIEW     
    # Draw
    
    # Update Screen
    pygame.display.flip()
    screen.fill(WHITE)
    all_sprites_list_1.draw(screen) 
    pygame.draw.rect(screen, GREEN, [0, 0, 70, 50], 0)
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render(str(countdown), True, BLACK)
    screen.blit(text, [10, 10])
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render("Start",True,BLACK)
    screen.blit(text,[20,80])
    font = pygame.font.SysFont('Rock wall',50,True,False)
    text = font.render("End",True,BLACK)
    screen.blit(text,[375,30])
    clock.tick(60)
# Close the window and quit
pygame.quit()
