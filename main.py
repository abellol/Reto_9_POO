from modules.point import Point
from modules.line import Line
from modules.rectangle import Rectangle

def main():
  
#* RECTANGLE
  start1 = Point(0, 0)
  end1 = Point(0, 5)
  line1 = Line(start1, end1)
  start2 = Point(0, 0)
  end2 = Point(4, 0)
  line2 = Line(start2, end2)
  start3 = Point(4, 0)
  end3 = Point(4, 5)
  line3 = Line(start3, end3)
  start4 = Point(0, 5)
  end4 = Point(4, 5)
  line4 = Line(start4, end4)
  rectangle1 = Rectangle(line1, line2, line3, line4)

  # Call as a method, with timer decorator
  print("Área del rectángulo:", rectangle1.compute_area())

  # Call as atribute, not as a method
  print("Perímetro del rectángulo:", rectangle1.compute_perimeter) 



if __name__ == "__main__":
  main()
