# ICS3U
# Assignment 2: Action
# Jacky Liang

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
pygame.init()

speed = random.randint (5, 10)

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Space ship sprite
class SpaceShip (pygame.sprite.Sprite):

    def __init__ (self, c, w, h, v) :
        super ().__init__()

        self.image = pygame.Surface ([w+100, h+100])
        self.image.fill (WHITE)
        self.image.set_colorkey (WHITE)

        self.width = w
        self.height = h
        self.color = c
        self.speed = v

        # Draw Space ship (cockpit with 2 thrusters)
        pygame.draw.rect (self.image, c, [25, 50, w, h])
        pygame.draw.rect (self.image, RED, [15, 25, w, h//2])
        pygame.draw.rect (self.image, BLUE, [15, 75, w, h//2])

        self.rect = self.image.get_rect ()

    def moveRight (self, speed) :
        self.rect.x += self.speed * speed/20

    def changeSpeed (self, speed) :
        self.speed = speed

    def repaint (self, color) :
        self.color = color
        pygame.draw.rect (self.image, self.color, [0, 0, self.width, self.height])
        pygame.draw.rect (self.image, self.color, [-25, 25, self.width, self.height])
        pygame.draw.rect (self.image, self.color, [-25, -25, self.width, self.height])
            
# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

spriteList = pygame.sprite.Group ()

ship1 = SpaceShip (GREEN, 55, 25, 20)
ship1.rect.x = 200
ship1.rect.y = SCREENHEIGHT // 2

spriteList.add (ship1)

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

        
    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill (WHITE)

    # Queue different shapes and lines to be drawn
    spriteList.draw (screen)

    # Update the screen with queued shapes
    pygame.display.flip ()

    # --- Limit to 60 frames per second
    clock.tick (60)

# Once the main program loop is exited, stop the game engine
pygame.quit ()
