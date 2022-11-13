class Ball:

  SIZE = 25

  def __init__(self, initial_position):
    self.width = Ball.SIZE
    self.height = Ball.SIZE
    self.screen_position = initial_position
    self.color = (250, 250, 250)
