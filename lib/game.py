from lib.pygame.engine import Engine
from lib.pygame.events import Events

from lib.entities.player import Player
from lib.entities.wall import Wall

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
    player_2 = Player(initial_position=(self.game_windows.width - 50 - Player.WIDTH, 250))

    top_wall = Wall(initial_position=(50, 10), screen=self.game_windows)
    bottom_wall = Wall(initial_position=(50, self.game_windows.height - 10 - Wall.HEIGHT), screen=self.game_windows)

    return [player_1, player_2, top_wall, bottom_wall]
