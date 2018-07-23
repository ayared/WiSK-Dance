import pygame

pygame.init()

# Create display and set window title
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')

# Set game clock 
clock = pygame.time.Clock()

# crash defined as user closing the game window
crashed = False

# run window while user hasn't closed it
# print user interactions with the window
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)

quit()