from modules.shape import Shape
from modules.line import Line

class Triangle(Shape):
  def __init__(self, side1: Line, side2: Line, side3: Line):
    super().__init__()
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

  def compute_area(self):
    ...
  
  def compute_perimeter(self):
    ...

class IsocelesTriangle(Triangle):
  def __init__(self, base: Line, height: Line, side1: Line, side2: Line):
    super().__init__(side1, side2, height)
    self.base = base
    self.height = height

  @property
  def compute_area(self):
    return (self.base.compute_length() * self.height.compute_length()) / 2
  
  @property
  def compute_perimeter(self):
    return self.base.compute_length() + (2 * self.side1.compute_length())

class EquilateralTriangle(Triangle):
  def __init__(self, side1: Line, side2: Line, side3: Line):
    super().__init__(side1, side2, side3)

  @property
  def compute_area(self):
    return (self.side1.compute_length() ** 2 * (3 ** 0.5)) / 4
  
  @property
  def compute_perimeter(self):
    return 3 * self.side1.compute_length()
  
class RectangleTriangle(Triangle):
  def __init__(self, side1: Line, side2: Line, side3: Line):
    super().__init__(side1, side2, side3)

  @property
  def compute_area(self):
    return (self.side1.compute_length() * self.side2.compute_length()) / 2
  
  @property
  def compute_perimeter(self):
    return self.side1.compute_length() + self.side2.compute_length() + self.side3.compute_length()
  
class ScaleneTriangle(Triangle):
  def __init__(self, side1: Line, side2: Line, side3: Line):
    super().__init__(side1, side2, side3)

  @property
  def compute_area(self):
    s = (self.side1.compute_length() + self.side2.compute_length() + self.side3.compute_length()) / 2
    return (s * (s - self.side1.compute_length()) * (s - self.side2.compute_length()) * (s - self.side3.compute_length())) ** 0.5
  
  @property
  def compute_perimeter(self):
    return self.side1.compute_length() + self.side2.compute_length() + self.side3.compute_length()