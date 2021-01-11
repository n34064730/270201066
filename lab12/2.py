class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def get_name(self):
    return self.name
  def set_name(self,name):
    if len(name)>0:
      self.name=name
  def get_salary(self):
    return self.salary
  def set_salary(self,salary):
    if salary>0:
      self.salary=salary
  def display(self):
    print("Name:{} \tSalary:{}".format(self.name,self.salary))
  
class Company:
  def __init__(self):
    self.employee_list=[]
  def get_employee_list(self):
    return self.employee_list
  def set_employee_list(self,employee_list):
    if type(employee_list)==list:
      self.employee_list=employee_list
  def add_employee(self,new_employee):
    if isinstance(new_employee,Employee):
      self.employee_list.append(new_employee)
  def avg_salary(self):
    toplam=0
    for emp in self.employee_list:
      toplam+= emp.get_salary()
    return toplam/len(self.employee_list)
  def display(self):
    for emp in self.employee_list:
      emp.display()



p1=Employee("Ahmet",5000)
p2=Employee("Mustafa",400)
p3=Employee("Deniz",2850)
