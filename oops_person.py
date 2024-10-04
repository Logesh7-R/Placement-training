from abc import ABC,abstractmethod
class person(ABC):
  @abstractmethod
  def calculate_age(self):
    pass

class student(person):
  def __init__(self,name,country,dob):
    self.name = name
    self.country=country
    self.dob=dob
  def calculate_age(self):
    return 2024-int(self.dob.split('-')[-1])

st1=student("logi","india","25-11-1999")
print(st1.calculate_age())
