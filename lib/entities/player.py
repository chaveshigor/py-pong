class Player:

  def __init__(self, initial_position):
    self.shape = 'rectangle'
    self.color = (250, 250, 250)
    self.initial_position = initial_position
    self.width = 30
    self.height = 200
    self.location = self.set_location()
    self.screen_position = (self.initial_position[0], self.initial_position[1])

  def set_location(self):
    x_initial_position = self.initial_position[0]
    y_initial_position = self.initial_position[1]

    p1 = (x_initial_position, y_initial_position)
    p2 = (x_initial_position + self.width, y_initial_position)
    p3 = (x_initial_position, y_initial_position + self.height)
    p4 = (x_initial_position + self.width, y_initial_position + self.height)

    self.location = [p1, p2, p3, p4]
