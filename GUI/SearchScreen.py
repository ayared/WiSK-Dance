import pygame
import time
import random
from GUIComponents import InputBox, button, text_objects
from StyleSheet import *
from ResultsScreen import results_screen

def launch_results(text):
    #results_screen(display_width,display_height,screen,clock)

def search_screen(w,h,screen,clock):
    search = True
    input_box = InputBox(300, 300, 140, 32)

    while search:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            input_box.handle_event(event,launch_results)
            input_box.update()

        screen.fill(white)
        input_box.draw(screen)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        mediumText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects("WiSK Dance", largeText,black)
        TextRect.center = ((w/2),(100))
        screen.blit(TextSurf, TextRect)
        SearchSurf, SearchRect = text_objects("Search for a Song:",mediumText,black)
        SearchRect.center = ((w/2),250)
        screen.blit(SearchSurf,SearchRect)

        pygame.display.update()
        clock.tick(60)