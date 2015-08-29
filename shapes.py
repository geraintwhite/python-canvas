class Shape(list):
  def __init__(self, radius, char='x'):
    self.char = char
    self.radius = radius
    self.diameter = 2 * radius + 1

  def __repr__(self):
    return repr(self.render())

  def __str__(self):
    return '\n'.join(''.join(row) for row in self.render())

  def set(self, shape):
    list.__init__(self, shape)

  def render(self):
    return [
      [
        (' ' + self.char)[p] for p in row
      ] for row in self
    ]


class Circle(Shape):
  def __init__(self, *args):
    super().__init__(*args)

    r = self.radius
    d = self.diameter

    self.set([
      [
        ((x-r)**2 + (y-r)**2 == r**2) for x in range(d)
      ] for y in range(d)
    ])


class Square(Shape):
  def __init__(self, *args):
    super().__init__(*args)

    r = self.radius
    d = self.diameter

    self.set([
      [
        (x in [0, d-1] or y in [0, d-1]) for x in range(d)
      ] for y in range(d)
    ])


class Diamond(Shape):
  def __init__(self, *args):
    super().__init__(*args)

    r = self.radius
    d = self.diameter

    self.set([
      [
        (x in [r+y, r-y, y-r, 3*r-y]) for x in range(d)
      ] for y in range(d)
    ])


class Grid(Shape):
  def __init__(self, *args):
    super().__init__(*args)

    r = self.radius
    d = self.diameter

    self.set([
      [
        False for x in range(d)
      ] for y in range(d)
    ])
