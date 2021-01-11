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
    pass


