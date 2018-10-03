import pygame
import time
from GUIComponents import InputBox, button, text_objects
from StyleSheet import *
from APItest import *
pygame.init()

pygame.display.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('WiSK Dance')

clock = pygame.time.Clock()

def game_quit():
    pygame.quit()
    quit()

def launch_search():
    search_screen(display_width,display_height,gameDisplay,clock)

def launch_results(text):
    results_screen(display_width,display_height,gameDisplay,clock,text)

def launch_game(song_number):
    if(song_number.isdigit()):
        song_number = int(song_number)
        url = results['tracks']['items'][song_number]['external_urls']['spotify']
        webbrowser.open(url)
    game_screen(display_width,display_height,gameDisplay,clock)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)

        TextSurf, TextRect = text_objects("WiSK Dance", largeText,black)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",650,650,100,50,green,bright_green,black,gameDisplay,launch_search)
        button("Quit",850,650,100,50,red,bright_red,black,gameDisplay,game_quit)
        
        pygame.display.flip()
        clock.tick(15)

def search_screen(w,h,screen,clock):
    search = True
    input_box = InputBox(700, 400, 140, 32)

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
        TextSurf, TextRect = text_objects("WiSK Dance", largeText,black)
        TextRect.center = ((w/2),(100))
        screen.blit(TextSurf, TextRect)
        SearchSurf, SearchRect = text_objects("Search for a Song:",mediumText,black)
        SearchRect.center = ((w/2),250)
        screen.blit(SearchSurf,SearchRect)

        pygame.display.flip()
        clock.tick(60)

def results_screen(w,h,screen,clock,song_name):
    show = True
    spotify = Authentication()
    global results
    results = spotify.search(song_name,type='track')
    input_box = InputBox(700, 900, 140, 32)
    while show:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            input_box.handle_event(event,launch_game)
            input_box.update()
        
        screen.fill(white) 
        input_box.draw(screen)
        TextSurf=[None]*10
        TextRect=[None]*10
        for index, item in enumerate(results['tracks']['items']):
            text = 'track ' + str(index) + ': ' + str(item['name']) + ' by ' + str(item['artists'][0]['name'])
            TextSurf[index], TextRect[index] = text_objects(text, mediumText,black)
            TextRect[index].center = ((w/2),(index*50+100))
            screen.blit(TextSurf[index], TextRect[index])      

        SelectSurf, SelectRect = text_objects("Select a Song:",mediumText,black)
        SelectRect.center = ((w/2),800)
        screen.blit(SelectSurf,SelectRect)

        pygame.display.update()
        clock.tick(60)

def game_screen(w,h,screen,clock):
    ### PUT GAME HERE ###
    #Temporary filler:
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        screen.fill(white)

        pygame.display.update()
        clock.tick(60)

game_intro()
pygame.quit()
quit()