from lib.screen import Screen

class Wall:
  HEIGHT = 20

  def __init__(self, screen: Screen, initial_position):
    self.width = screen.width - 2*50
    self.height = Wall.HEIGHT
    self.screen_position = initial_position
    self.color = (250, 250, 250)