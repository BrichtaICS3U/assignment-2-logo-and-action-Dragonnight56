# ICS3U
# Assignment 2: Action
# Jacky Liang

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
pygame.init()

# Set and play background music 
pygame.mixer.pre_init (frequency = 44100, size=-16, channels=2, buffer=4096 )
# Official source (I converted their youtube video of it): https://ocremix.org/remix/OCR03452
pygame.mixer.music.load ("Kirby 64 ReMix by glitchman161 Interstellar Action [World Map] (3452).mp3")
pygame.mixer.music.play (-1)

# Create a variable to store the background image
# Source: https://www.popularmechanics.com/space/solar-system/a25693/jupiter-is-a-jerk/
background = pygame.image.load ("Jupiterjerk.png")

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

# Space ship sprite
class SpaceShip (pygame.sprite.Sprite):

    def __init__ (self, c, w, h, v) :
        super ().__init__()

        # Set the parameters such as the "hitbox"
        self.image = pygame.Surface ([w+27, h])
        # White will be our transparent color
        self.image.fill (BLACK)
        self.image.set_colorkey (BLACK)

        self.width = w
        self.height = h
        self.color = c
        self.speed = v

        # Draw Space ship (cockpit with 2 thrusters)
        pygame.draw.polygon (self.image, c, [[25, 0], [25, h], [w+25, h//2]])
        pygame.draw.rect (self.image, c, [0, 0, w, 25])
        pygame.draw.rect (self.image, c, [0, 75, w, 25])

        # Create the sprite
        self.rect = self.image.get_rect ()

    # Function to move the ship
    def moveRight (self, speed) :
        self.rect.x += self.speed * speed/20

    # Function to change speed of ship
    def changeSpeed (self, speed) :
        self.speed = speed

    # Function to repaint the ship 
    def repaint (self, color) :
        self.color = color
        pygame.draw.polygon (self.image, color, [[25, 0], [25, self.height], [self.width+25, self.height//2]])
        pygame.draw.rect (self.image, color, [0, 0, self.width, 25])
        pygame.draw.rect (self.image, color, [0, 75, self.width, 25])
            
# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dank Space Jebrawlta")

# List to store sprites 
spriteList = pygame.sprite.Group ()
colorList = (GREEN, BLUE, YELLOW, PURPLE, WHITE, RED)

# Create 3 ships 
ship1 = SpaceShip (GREEN, 100, 100, 20)
ship1.rect.x = 0
ship1.rect.y = 10

ship2 = SpaceShip (RED, 100, 100, 20)
ship2.rect.x = 0
ship2.rect.y = 150

ship3 = SpaceShip (BLUE, 100, 100, 20)
ship3.rect.x = 0
ship3.rect.y = 290

# Store the sprites in the list
spriteList.add (ship1)
spriteList.add (ship2)
spriteList.add (ship3)

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn :
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE : # Press Space to end animation
                carryOn=False

        
    # --- Game logic goes here
    # There should be none for a static image
        
    # --- Draw code goes here
    # The animation to move ships to right
    for ship in spriteList :
        ship.moveRight (10)
        #resets the locations when they leave screen
        if ship.rect.x > SCREENWIDTH :
            ship.changeSpeed (random.randint (10, 30))
            ship.repaint (random.choice (colorList))
            ship.rect.y = random.randint (10, 290)
            ship.rect.x = -100
        
    # Add a background image and fill the remaining screen with correct color
    screen.fill (BLACK)
    screen.blit (background, (-190, 0))

    # Queue different shapes and lines to be drawn
    spriteList.draw (screen)

    # Update the screen with queued shapes
    pygame.display.flip ()

    # --- Limit to 60 frames per second
    clock.tick (60)

# Once the main program loop is exited, stop the game engine
pygame.quit ()
