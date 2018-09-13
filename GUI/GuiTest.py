import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('WiSK Dance')

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)

clock = pygame.time.Clock()
dmxImg = pygame.image.load('dmx.jpg')

def DMX(x,y):
    gameDisplay.blit(dmxImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_quit():
    pygame.quit()
    quit()
    
def game_loop():
    crashed = False
    x = (display_width * 0.2)
    y = (display_height * 0.3)
    x_change = 0
    y_change = 0
    car_speed = 0
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
        gameDisplay.fill(white)
        DMX(x,y)

        pygame.display.update()
        clock.tick(60)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("WiSK Dance", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,game_quit)

        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()