from modules.shape import Shape
from modules.line import Line

class Square(Shape):
  def __init__(self, width1: Line, height1: Line, width2: Line, height2: Line):
    super().__init__()
    self.width1 = width1
    self.height1 = height1
    self.width2 = width2
    self.height2 = height2
  
  @property
  def compute_area(self):
    return self.width1.compute_length() ** 2 
  
  @property
  def compute_perimeter(self):
    return 4 * self.width1.compute_length()