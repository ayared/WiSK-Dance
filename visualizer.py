# visualizer.py
# The GUI file controlling WiSK Dance's visualization

# Inspiration from: https://github.com/pygame/pygame/blob/master/examples/aliens.py

try:
    import sys, pygame, os, random
    from pygame.locals import *
    from enum import Enum
except ImportError:
    print("couldn't load a module.")
    sys.exit(2)

class Direction(Enum):
    LEFT = 0
    DOWN = 1
    UP = 2
    RIGHT = 3

class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

SCREENRECT = Rect(0, 0, 1280, 720)
SCORE = 0
DIFF = Difficulty.EASY
TEMPO = 60                  # tempo in BPM, this will be passed in from Spotify
SONGLENGTH = 60             # song length in seconds, this will be passed in from Spotify
FRAMERATE = 60
SCORE = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image"
    file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)
        if surface.get_alpha() is None:
            surface.convert()
        else:
            surface = surface.convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    "loads an array of images"
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def generate_sequence():
    "generates a sequence of arrows based on the tempo and the song length"
    seq = []
    for framecount in range(0, SONGLENGTH * FRAMERATE, int(TEMPO / 60 * FRAMERATE)):     # is it okay to cast this last argument as an int?
                                                                                        # does rounding down cause slow drift in arrow timing?
        if random.randint(0,1):
            seq.append((random.randint(0,3),framecount))
    return seq

class Arrow(pygame.sprite.Sprite):
    """An arrow that will move across the screen
    Returns: arrow object
    Functions: update, check_pressed
    Attributes: direction, speed, image, rect, frame"""

    images = []
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.direction = direction
        self.speed = -6                 #FIX THIS TO SAY (DIFF+1)*(-2)
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(SCREENRECT.width*self.direction/4 + (SCREENRECT.width/4 - self.rect.width)/2, SCREENRECT.height)
        self.frame = 0

    def update(self):
        """update the location of the arrow and remove it if needed"""
        self.rect.move_ip(0, self.speed)
        self.frame = self.frame + 1
        if self.rect.bottom <= 0:
            self.kill()

    def check_pressed(self, keystate):
        """check if the user hit an arrow successfully"""
        if (self.rect.top <= 50) and (self.rect.top >= -50):
            if self.direction == 0 and keystate[pygame.K_LEFT]:
                self.kill()
                print("got a left arrow")
                return 50 - abs(self.rect.top)
            if self.direction == 1 and keystate[pygame.K_DOWN]:
                self.kill()
                print("got a down arrow")
                return 50 - abs(self.rect.top)
            if self.direction == 2 and keystate[pygame.K_UP]:
                self.kill()
                print("got an up arrow")
                return 50 - abs(self.rect.top)
            if self.direction == 3 and keystate[pygame.K_RIGHT]:
                self.kill()
                print("got a right arrow")
                return 50 - abs(self.rect.top)
        return 0

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 30)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 700)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()

    # Set the display mode
    winstyle = 0  # fullscreen
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    img = load_image('arrow.png')
    Arrow.images = [pygame.transform.rotate(img, 90), pygame.transform.rotate(img, 180), img, pygame.transform.rotate(img, -90)]
    
    #decorate the game window
    icon = pygame.transform.scale(load_image('WiSK_Logo.png'), (128, 128))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('WiSK Dance')
    pygame.mouse.set_visible(0)

    #create the background, tile the bgd image
    bgdtile = load_image('background.jpg')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0,0))
    pygame.display.flip()

    # Initialize Game Groups
    arrows = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    #assign default groups to each sprite class
    Arrow.containers = arrows, all
    Score.containers = all
    
    # Initialize clock
    clock = pygame.time.Clock()

    # Set the number of frames between new arrows (this is for random arrows in the current code)
    NEW_ARROW = 60          #FIX THIS TO INCORPORATE 60/(DIFF+1)

    global SCORE
    if pygame.font:
        all.add(Score())

    # Create a sequence of arrows, by direction, each is a tuple with the (direction of the arrow, frame count when the arrow hits top of screen)
    # seq = [(0, 60), (1, 120), (2, 180), (3, 240)]
    seq = generate_sequence()

    i = 0
    framecount = 0    #frames into
    # Event loop
    while 1:
        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:        # determine if key pressed
                keystate = pygame.key.get_pressed()
                if event.key == pygame.K_q and keystate[pygame.K_LCTRL] or keystate[pygame.K_RCTRL]:
                    return                          # quit game on ctrl + q
                for arrow in arrows:                # check all of the arrows on the screen to determine if the correct key was pressed
                    SCORE = SCORE + arrow.check_pressed(keystate)

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # create new arrows based on time into game
        if framecount > seq[i][1] - SCREENRECT.height/abs(-6):  #note that -6 is hard coded as the speed for now, this needs to be FIXED
            Arrow(seq[i][0])
            i = i + 1

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(FRAMERATE)
        framecount = framecount + 1

#call the "main" function if running this script
if __name__ == '__main__': main()
