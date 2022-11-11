from lib.screen import Screen
from lib.pygame.engine import Engine

class Builder:

  def __init__(self, engine: Engine):
    self.engine = engine

  def update_screen(self):
    engine = self.engine
    engine.update_screen()

  def render_elements(self, elements_to_render):
    engine = self.engine

    for element in elements_to_render:
      engine.draw_rectangle(self.screen, element.screen_position[0], element.screen_position[1], element.width, element.height, element.color)

  def build_screen(self, windows: Screen):
    engine = self.engine
    self.screen = engine.set_screen(width=windows.width, height=windows.height, color=windows.color)
