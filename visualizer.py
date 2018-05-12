import sys, pygame
pygame.init()
pygame.display.set_caption('WiSK Dance')

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

size = width, height = 1020, 600
speed = [0, -2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

arrow_up = pygame.image.load("arrow.png")

arrow_right = rot_center(arrow_up, -90)
arrow_left = rot_center(arrow_up, 90)
arrow_down = rot_center(arrow_up, 180)

#this returns the size which is the same for all arrows because they are square
arrowrect = arrow_up.get_rect()

arrowrect_up = arrowrect.move(510,height)
arrowrect_right = arrowrect.move(765,height)
arrowrect_left = arrowrect.move(0,height)
arrowrect_down = arrowrect.move(255,height)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    arrowrect_up = arrowrect_up.move(speed)
    # if arrowrect.left < 0 or arrowrect.right > width:
    #     speed[0] = -speed[0]
    # if arrowrect.top < 0 or arrowrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(arrow_up, arrowrect_up)
    pygame.display.flip()

