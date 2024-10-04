from abc import ABC,abstractmethod
class shape(ABC):
  @abstractmethod
  def __init__(self,is_filled,color):
    pass
  @abstractmethod
  def area(self):
    pass
  @abstractmethod
  def perimeter(self):
    pass

class circle(shape):
  def __init__(self, is_filled, color,r):
    self.is_filled = is_filled
    self.color=color
    self.r=r
  def area(self):
    print(f"{3.14*self.r*self.r:.2f}")
  def perimeter(self):
    print(f"{3.14*self.r*2:.2f}")

class square(shape):
  def __init__(self, is_filled, color,s):
    self.is_filled = is_filled
    self.color=color
    self.s=s
  def area(self):
    print(f"{self.s*self.s:.2f}")
  def perimeter(self):
    print(f"{4*self.s}")

c1=circle(True,"Red",6.7)
s1 = square(False,"Yellow",7)
c1.area()
c1.perimeter()
s1.area()
s1.perimeter()
