# ICS3U
# Assignment 2: Logo
# Jacky Liang

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Adobe Logo")

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
    screen.fill(RED)

    # Queue different shapes and lines to be drawn
    # - Left side
    pygame.draw.line (screen, WHITE, [200, 0], [35, 270], 75)
    # - Right side
    pygame.draw.line (screen, WHITE, [200, 0], [362, 270], 75)

    # - Bottom end 
    pygame.draw.line (screen, WHITE, [70, 233], [172, 233], 75)
    pygame.draw.line (screen, WHITE, [170, 196], [210, 270], 75)

    # - Blank space 
    pygame.draw.rect (screen, WHITE, [0, 270, 400, 150])

    # - Text
    font = pygame.font.SysFont ("Adobe Text Pro Regular", 190)
    text = font.render ("Adobe", True, BLACK)
    screen.blit (text, (200 - text.get_width () // 2, 425 - text.get_height ())) 
    
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
