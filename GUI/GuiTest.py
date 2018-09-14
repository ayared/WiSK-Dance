import pygame
import time
import random
from GUIComponents import InputBox, button, text_objects
from SearchScreen import search_screen
from StyleSheet import *
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('WiSK Dance')

clock = pygame.time.Clock()
dmxImg = pygame.image.load('dmx.jpg')

def DMX(x,y):
    gameDisplay.blit(dmxImg, (x,y))

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

def launch_search():
    search_screen(display_width,display_height,gameDisplay,clock)

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
        TextSurf, TextRect = text_objects("WiSK Dance", largeText,black)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,black,gameDisplay,launch_search)
        button("Quit",550,450,100,50,red,bright_red,black,gameDisplay,game_quit)
        
        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()