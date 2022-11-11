import pygame
from pygame.locals import*

class Engine:

  def __init__(self):
    pass

  def draw_rectangle(self, screen, x_position: float, y_position: float, width: float, height: float, color: tuple):
    rectangle = pygame.Rect(x_position, y_position, width, height)
    pygame.draw.rect(screen, color, rectangle)

  def set_screen(self, width: float, height: float, color: tuple):
    self.screen = pygame.display.set_mode((width, height))
    self.screen.fill(color)

    return self.screen

  def update_screen(self):
    pygame.display.flip()
