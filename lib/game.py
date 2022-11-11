from lib.pygame.engine import Engine
from lib.pygame.events import Events

from lib.player import Player
from lib.screen import Screen
from lib.builder import Builder

class Game:

  def __init__(self):
    self.game_windows = Screen(width=1366, height=768, color=(5, 5, 25))
    self.events = Events()
    self.engine = Engine()
    self.builder = Builder(engine=self.engine)

  def run(self):
    events = self.events
    game_elements = self.game_elements()
    builder = self.builder

    builder.build_screen(self.game_windows)
    builder.render_elements(elements_to_render=game_elements)
    builder.update_screen()

    while True:
      for event in events.get_event():
        if event.type == events.quit:
          events.exit_game()

  def game_elements(self):
    player_1 = Player(initial_position=(50, 250))

    return [player_1]
