from copy import deepcopy


class Screen(list):

  def __str__(self):
    return '\n'.join(''.join(row) for row in self)

  def add(self, shape, pos):
    ox, oy = pos

    for y, row in enumerate(shape):
      for x, p in enumerate(row):
        self[oy+y][ox+x] = p

  def difference(self):
    diff = []

    # TODO - get a true diff, handling deletions

    for y, row in enumerate(self):
      for x, p in enumerate(row):
        try:
          if not p == self._old_grid[y][x]:
            diff.append((x, y, p))
        except:
          diff.append((x, y, p))

    self._old_grid = deepcopy(self)
    return diff


def pos_str(x, y, s):
  return '\033[{};{}H{}'.format(y+1, x+1, s)

def diff(d):
  return ''.join(pos_str(*args) for args in d)
