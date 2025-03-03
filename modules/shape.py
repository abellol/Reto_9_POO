import time

def timer(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    # ejecucion de la funcion que recibe como argumento
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time of {func}: {end_time - start_time:.4f} seconds")
    return result
  # retorna la funcion decorada sin ejecutarla
  return wrapper


class Shape:
  def __init__(self):
    pass

  def compute_area(self):
    ...
  
  def compute_perimeter(self):
    ...