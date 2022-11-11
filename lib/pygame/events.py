import sys, pygame
from pygame.locals import*

class Events:

  def __init__(self):
    self.quit = QUIT

  def get_event(self):
    return pygame.event.get()

  def exit_game(self):
    sys.exit(0)
