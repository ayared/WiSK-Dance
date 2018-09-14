import pygame
import time
import random
from GUIComponents import InputBox, button, text_objects
from StyleSheet import *

def search_screen(w,h,screen,clock):
    search = True
    input_box = InputBox(300, 300, 140, 32)

    while search:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            input_box.handle_event(event)
            input_box.update()

        screen.fill(white)
        input_box.draw(screen)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("WiSK Dance", largeText,black)
        TextRect.center = ((w/2),(h/4))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)