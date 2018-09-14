import pygame
import time
import random
from GUIComponents import InputBox, button, text_objects
from StyleSheet import *

def results_screen(w,h,screen,clock):
    screen = True
    while screen:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)

        
        pygame.display.update()
        clock.tick(60)