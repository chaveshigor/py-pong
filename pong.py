import sys, pygame
from pygame.locals import*
from lib.screen import Screen

game_screen = Screen(width=1366, height=768, color=(10, 10, 10))

def main():
  screen = pygame.display.set_mode((game_screen.width, game_screen.height))
  screen.fill(game_screen.color)
  pygame.display.flip()

  while True:
    for events in pygame.event.get():
      if events.type == QUIT:
        sys.exit(0)

main()
