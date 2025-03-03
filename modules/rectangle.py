from modules.shape import Shape, timer
from modules.line import Line

class Rectangle(Shape):
  def __init__(self, width1: Line, height1: Line, width2: Line, height2: Line):
    super().__init__()
    self.width1 = width1
    self.height1 = height1
    self.width2 = width2
    self.height2 = height2

  @timer
  def compute_area(self):
    return self.width1.compute_length * self.height1.compute_length
  
  @property
  def compute_perimeter(self):
    return (2 * self.height1.compute_length) + (2 * self.width1.compute_length)
  