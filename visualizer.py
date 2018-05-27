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

class Arrow(pygame.sprite.Sprite):
    """An arrow that will move across the screen
    Returns: arrow object
    Functions: update
    Attributes: direction, speed, image, rect, frame"""

    images = []
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.direction = direction
        self.speed = -2                 #FIX THIS TO SAY (DIFF+1)*(-2)
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
    Arrow.containers = all
    
    # Initialize clock
    clock = pygame.time.Clock()

    # Set the number of frames between new arrows
    NEW_ARROW = 120          #FIX THIS TO INCORPORATE 60/(DIFF+1)
    newarrow = NEW_ARROW

    # Create a sequence of arrows, by direction
    seq = (0, 1, 2, 3)

    i = 0
    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # create new arrow
        if newarrow:
            newarrow = newarrow - 1
        elif i < len(seq):
            Arrow(seq[i])
            newarrow = NEW_ARROW
            i = i + 1
        else:
            Arrow(random.randint(0, 3))
            newarrow = NEW_ARROW

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

#call the "main" function if running this script
if __name__ == '__main__': main()
