import math
class Clynder:
  def __init__(self,radius,height):
    self.radius=radius
    self.height=height
  def get_height(self):
    return self.height
  def set_height(self,height):
    if height>0:
      self.height=height
  def get_radius(self):
    return self.radius
  def set_radius(self,radius):
    if radius>0:
      self.radius=radius
  def base_area(self):
    return math.pi* (self.radius**2)
  def surface_area(self):
    return 2*math.pi*self.radius*self.height
  def Area(self):
    return self.surface_area()+self.base_area()*2
  def Volume(self):
    return self.base_area()*self.height
  
silindir=Clynder(3,5)
print(silindir.base_area())
print(silindir.surface_area())
print(silindir.Area())
print(silindir.Volume())



