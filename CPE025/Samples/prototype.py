class Shape:
  def __init__(self, name, radius = 0, width =  0, height = 0):
    self.name = name
    self.radius = radius
    self.width = width
    self.height = height

  def clone(self):
    return Shape(self.name, self.radius, self.width, self.height)

  def draw(self):
    if self.radius != 0:
      print(f"Drawing a circle with radius {self.radius}")
    else:
      print(f"Drawing a rectangle with width {self.width} and height {self.height}")

class Circle(Shape):
  def __init__(self, name, radius):
    super().__init__(name)
    self.radius = radius


class Rectangle(Shape):
  def __init__(self, name, width, height):
    super().__init__(name)
    self.width = width
    self.height = height

def main():
  circle = Circle("Circle", 10)
  rectangle = Rectangle("Rectangle", 20, 30)

  circle_clone = circle.clone()
  rectangle_clone = rectangle.clone()

  circle_clone.draw()
  rectangle_clone.draw()

if __name__ == "__main__":
  main()
