import sys, pygame
from pygame.locals import*

width = 1366                    #screen width
height = 768                    #screen height
screen_color = (10, 10, 10)     #screen background color
block_color = (255, 255, 255)

def main():
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    pygame.display.flip()

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

main()
