class HouseBuilder:
  def __init__(self):
    self.house = House()

  def build_foundation(self):
    self.house.foundation = "Concrete"

  def build_walls(self):
    self.house.walls = "Brick"

  def build_roof(self):
    self.house.roof = "Shingles"

  def build_doors(self):
    self.house.doors = 2

  def build_windows(self):
    self.house.windows = 4

  def get_house(self):
    return self.house

class House:
  def __init__(self):
    self.foundation = None
    self.walls = None
    self.roof = None
    self.doors = None
    self.windows = None

  def __str__(self):
    return f"House with {self.foundation} foundation, {self.walls} walls, {self.roof} roof, {self.doors} doors, and {self.windows} windows."

def main():
  builder = HouseBuilder()

  builder.build_foundation()
  builder.build_walls()
  builder.build_roof()
  builder.build_doors()
  builder.build_windows()

  house = builder.get_house()

  print(house)

if __name__ == "__main__":
  main()
