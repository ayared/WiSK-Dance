import pygame
pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #user clicked on input box
            if self.rect.collidepoint(event.pos): #toggle active variable
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE #match color to state
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN: #reset text on enter
                    self.text = ''              #TODO, replace with call to Spotify
                elif event.key == pygame.K_BACKSPACE: #delete character
                    self.text = self.text[:-1] 
                else:
                    self.text += event.unicode #update string
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def update(self):
        #Resize box if text is too long
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    
    def draw(self, screen):
        # blit the text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # blit the rectangle
        pygame.draw.rect(screen, self.color, self.rect, 2)

def button(msg,x,y,w,h,ic,ac,tc,screen,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText,tc)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
