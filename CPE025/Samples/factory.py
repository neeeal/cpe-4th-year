class ShapeFactory:
  def create_shape(self, shape_type):
    pass

class CircleFactory(ShapeFactory):
  def create_shape(self, shape_type):
    if shape_type == "circle":
      return Circle()
    else:
      raise ValueError("Invalid shape type")

class RectangleFactory(ShapeFactory):
  def create_shape(self, shape_type):
    if shape_type == "rectangle":
      return Rectangle()
    else:
      raise ValueError("Invalid shape type")

class Shape:
  def draw(self):
    pass

class Circle(Shape):
  def draw(self):
    print("Drawing a circle")

class Rectangle(Shape):
  def draw(self):
    print("Drawing a rectangle")

def main():
  circle_factory = CircleFactory()
  rectangle_factory = RectangleFactory()

  circle = circle_factory.create_shape("circle")
  rectangle = rectangle_factory.create_shape("rectangle")

  circle.draw()
  rectangle.draw()

if __name__ == "__main__":
  main()
