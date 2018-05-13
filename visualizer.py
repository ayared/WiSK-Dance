# visualizer.py
# The GUI file controlling WiSK Dance's visualization

try:
    import sys, pygame, os
    from pygame.locals import *
except ImportError:
    print("couldn't load a module.")
    sys.exit(2)

def load_png(name):
    """ Load image and return image object"""
    #fullname = os.path.join('data', name)
    fullname = name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit
    return image, image.get_rect()

class Arrow(pygame.sprite.Sprite):
    """An arrow that will move across the screen
    Returns: arrow object
    Functions: update, rot_center, remove
    Attributes: image, rect, area, difficulty, direction, speed"""

    def __init__(self, difficulty, direction, height):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('arrow.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.difficulty = difficulty                            #0 = easy, 1 = medium, 2 = hard
        self.direction = direction                              #0 = left, 1 = down, 2 = up, 3 = right
        if self.direction == 0:
            self.image = self.rot_center(90)
            self.rect = self.rect.move(0,height)
        elif self.direction == 1:
            self.image = self.rot_center(180)
            self.rect = self.rect.move(255,height)
        elif self.direction == 2:
            self.rect = self.rect.move(510,height)
        elif self.direction == 3:
            self.image = self.rot_center(-90)
            self.rect = self.rect.move(765,height)
        if self.difficulty == 0:
            self.speed = -2
        elif self.difficulty == 1:
            self.speed = -4
        elif self.difficulty == 2:
            self.speed = -6

    def update(self):
        """update the location of the arrow"""
        self.rect = self.rect.move(0,self.speed)

    def rot_center(self, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = self.rect
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    #come up with a way to delete the arrows from the screen

def main():
    # Initialise screen
    pygame.init()   
    pygame.display.set_caption('WiSK Dance')
    size = width, height = 1020, 600
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)

    # Initialize arrows
    uparrow = Arrow(0,2,height)

    # Initialize sprites
    arrowsprite = pygame.sprite.RenderPlain(uparrow)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize clock
    clock = pygame.time.Clock()

    # Event loop
    while 1:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(background, uparrow.rect, uparrow.rect)
        arrowsprite.update()
        arrowsprite.draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()
